from __future__ import annotations

from pathlib import Path
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
    artifacts = sorted(path for path in dist_dir.iterdir() if path.is_file())
    wheels = [path for path in artifacts if path.suffix == ".whl"]
    sdists = [path for path in artifacts if path.name.endswith(".tar.gz")]
    if len(wheels) != 1 or len(sdists) != 1 or len(artifacts) != 2:
        raise ValidationError("distribution directory must contain one wheel and one sdist")
    runtime = {
        path.relative_to(project_root / _RUNTIME_ROOT).as_posix()
        for path in (project_root / _RUNTIME_ROOT).rglob("*")
        if path.is_file() and (path.suffix == ".py" or path.name == "py.typed")
    }
    _validate_wheel(wheels[0], runtime)
    _validate_sdist(sdists[0], runtime)
    _clean_wheel_smoke(wheels[0])
    return wheels[0]


def _validate_wheel(path: Path, runtime: set[str]) -> None:
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
    if len(names) != len(set(names)):
        raise ValidationError("wheel contains duplicate entries")
    package_names = {f"schema_org/{name}" for name in runtime}
    dist_info = next(name.split("/", 1)[0] for name in names if ".dist-info/" in name)
    metadata_names = {
        f"{dist_info}/METADATA",
        f"{dist_info}/WHEEL",
        f"{dist_info}/RECORD",
        *(f"{dist_info}/licenses/{name}" for name in _REQUIRED_LICENSES),
    }
    if set(names) != package_names | metadata_names:
        raise ValidationError("wheel contents do not match tracked runtime files")


def _validate_sdist(path: Path, runtime: set[str]) -> None:
    with tarfile.open(path) as archive:
        names = archive.getnames()
    if not names:
        raise ValidationError("sdist is empty")
    roots = {name.split("/", 1)[0] for name in names}
    if len(roots) != 1:
        raise ValidationError("sdist has multiple roots")
    root = next(iter(roots))
    expected = {f"{root}/src/schema_org/{name}" for name in runtime} | {
        f"{root}/pyproject.toml", f"{root}/README.md", f"{root}/CHANGELOG.md",
        f"{root}/LICENSE.txt", f"{root}/LICENSE-SCHEMA-ORG.txt", f"{root}/PKG-INFO",
    }
    if set(names) != expected:
        raise ValidationError("sdist contents do not match the source contract")


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
assert SCHEMA_VERSION == '30.0'
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
