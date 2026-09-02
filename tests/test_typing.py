import shutil
import subprocess
from pathlib import Path


def test_ty_rejects_invalid_generated_property_assignment(tmp_path: Path) -> None:
    ty = shutil.which("ty")
    assert ty is not None
    source = tmp_path / "invalid_assignment.py"
    source.write_text(
        "from schema_org import Person\n\n"
        "person = Person(name='Ada')\n"
        "person.name = 1\n",
        encoding="utf-8",
    )
    root = Path(__file__).parents[1]
    result = subprocess.run(
        [
            ty,
            "check",
            str(source),
            "--extra-search-path",
            str(root / "src"),
            "--output-format",
            "concise",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode != 0
    assert "error[invalid-assignment]" in result.stdout
    assert "attribute `name`" in result.stdout
