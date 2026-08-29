from __future__ import annotations

from pathlib import Path, PurePosixPath
import subprocess
import sys
import tarfile
import tempfile
import venv
import zipfile

from .vocabulary import ValidationError

_RUNTIME_ROOT = Path("src/schema_org")
_REQUIRED_LICENSES = {"LICENSE.txt", "LICENSE-SCHEMA-ORG.txt"}


def validate_distributions(dist_dir: Path, *, project_root: Path) -> Path:
    try:
        artifacts = sorted(path for path in dist_dir.iterdir() if path.is_file())
    except OSError as error:
        raise ValidationError("distribution directory is invalid") from error
    wheels = [path for path in artifacts if path.suffix == ".whl"]
    sdists = [path for path in artifacts if path.name.endswith(".tar.gz")]
    if len(wheels) != 1 or len(sdists) != 1 or len(artifacts) != 2:
        raise ValidationError("distribution directory must contain one wheel and one sdist")
    runtime_root = project_root / _RUNTIME_ROOT
    if not runtime_root.is_dir():
        raise ValidationError("tracked runtime package is missing")
    runtime = {
        path.relative_to(runtime_root).as_posix()
        for path in runtime_root.rglob("*")
        if path.is_file() and (path.suffix == ".py" or path.name == "py.typed")
    }
    _validate_wheel(wheels[0], runtime)
    _validate_sdist(sdists[0], runtime, project_root)
    _clean_wheel_smoke(wheels[0])
    return wheels[0]


def _validate_wheel(path: Path, runtime: set[str]) -> None:
    try:
        with zipfile.ZipFile(path) as archive:
            infos = archive.infolist()
    except (OSError, zipfile.BadZipFile) as error:
        raise ValidationError("wheel archive is invalid") from error
    names = [info.filename for info in infos]
    if len(names) != len(set(names)):
        raise ValidationError("wheel contains duplicate entries")
    if any(not _safe_archive_name(name) or name.endswith("/") for name in names):
        raise ValidationError("wheel contains unsafe or non-file entries")
    dist_roots = {name.split("/", 1)[0] for name in names if ".dist-info/" in name}
    if len(dist_roots) != 1:
        raise ValidationError("wheel must contain one dist-info root")
    dist_info = next(iter(dist_roots))
    if any(info.is_dir() or (info.external_attr >> 16) & 0o170000 not in {0, 0o100000} for info in infos):
        raise ValidationError("wheel contains non-regular entries")
    package_names = {f"schema_org/{name}" for name in runtime}
    metadata_names = {
        f"{dist_info}/METADATA",
        f"{dist_info}/WHEEL",
        f"{dist_info}/RECORD",
        *(f"{dist_info}/licenses/{name}" for name in _REQUIRED_LICENSES),
    }
    if set(names) != package_names | metadata_names:
        raise ValidationError("wheel contents do not match tracked runtime files")

def _validate_sdist(path: Path, runtime: set[str], project_root: Path) -> None:
    try:
        with tarfile.open(path) as archive:
            members = archive.getmembers()
    except (OSError, tarfile.TarError) as error:
        raise ValidationError("sdist archive is invalid") from error
    names = [member.name for member in members]
    if not names:
        raise ValidationError("sdist is empty")
    if len(names) != len(set(names)):
        raise ValidationError("sdist contains duplicate entries")
    if any(not _safe_archive_name(name) for name in names):
        raise ValidationError("sdist contains unsafe paths")
    expected_root = path.name.removesuffix(".tar.gz")
    roots = {name.split("/", 1)[0] for name in names}
    if roots != {expected_root}:
        raise ValidationError("sdist has an unexpected root")
    expected = {f"{expected_root}/src/schema_org/{name}" for name in runtime} | {
        f"{expected_root}/pyproject.toml", f"{expected_root}/README.md", f"{expected_root}/CHANGELOG.md",
        f"{expected_root}/LICENSE.txt", f"{expected_root}/LICENSE-SCHEMA-ORG.txt",
        f"{expected_root}/build_hooks.py", f"{expected_root}/PKG-INFO",
    }
    files = {member.name for member in members if member.isfile()}
    directories = {member.name.rstrip("/") for member in members if member.isdir()}
    allowed_directories = {
        name.rsplit("/", 1)[0]
        for name in expected
        if "/" in name
    }
    allowed_directories |= {
        "/".join(name.split("/")[:index])
        for name in expected
        for index in range(1, len(name.split("/")))
    }
    if any(not member.isfile() and not member.isdir() for member in members):
        raise ValidationError("sdist contains non-regular entries")
    if files != expected or not directories <= allowed_directories:
        raise ValidationError("sdist contents do not match the source contract")
    if directories - allowed_directories:
        raise ValidationError("sdist contains unexpected directories")


def _safe_archive_name(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        bool(name)
        and bool(pure.parts)
        and not pure.is_absolute()
        and "\\" not in name
        and "//" not in name
        and ".." not in pure.parts
        and "." not in pure.parts
        and ":" not in pure.parts[0]
    )

def _clean_wheel_smoke(wheel: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="schema-org-wheel-") as temporary:
        environment = Path(temporary) / "venv"
        venv.EnvBuilder(with_pip=True, clear=True).create(environment)
        python = environment / "bin/python"
        _run([str(python), "-m", "pip", "install", str(wheel)], Path(temporary))
        script = """
from schema_org import (
    Person, PostalAddress, SequentialArt, Book, VisualArtwork,
    Offer, ItemAvailability, BookFormatType, SCHEMA_VERSION,
)
assert isinstance(SCHEMA_VERSION, str) and SCHEMA_VERSION
assert issubclass(SequentialArt, Book)
assert issubclass(SequentialArt, VisualArtwork)
person = Person(name='Ada', address=PostalAddress(address_locality='London'))
assert person.to_jsonld()['address']['addressLocality'] == 'London'
offer = Offer(availability=ItemAvailability.IN_STOCK)
assert offer.to_jsonld()['availability'] == 'https://schema.org/InStock'
assert SequentialArt(book_format=BookFormatType.E_BOOK)
"""
        _run([str(python), "-c", script], Path(temporary))


def _run(command: list[str], cwd: Path) -> None:
    result = subprocess.run(command, cwd=cwd, capture_output=True, text=True)
    if result.returncode:
        detail = (result.stderr or result.stdout).strip()
        raise ValidationError(f"package smoke command failed: {detail}")


if __name__ == "__main__":
    root = Path.cwd()
    directory = Path(sys.argv[1]) if len(sys.argv) == 2 else root / "dist"
    validate_distributions(directory, project_root=root)
