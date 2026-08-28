from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

import schema_org_codegen.updater as updater_module
from schema_org_codegen.updater import SchemaUpdater
from schema_org_codegen.vocabulary import ValidationError


TTL = """@prefix schema: <https://schema.org/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
schema:Thing a rdfs:Class ; rdfs:label "Thing" .
schema:name a rdf:Property ; rdfs:label "name" ; schema:domainIncludes schema:Thing ; schema:rangeIncludes schema:Text .
schema:Text a rdfs:Class ; rdfs:label "Text" .
"""


def tracked_tree(tmp_path: Path) -> tuple[Path, Path, str]:
    root = tmp_path
    target = root / "codegen/data/schema.ttl"
    target.parent.mkdir(parents=True)
    target.write_text("# schema_org_release: v30.0\n# schema_org_source: https://schema.org/version/30.0/schemaorg-all-https.ttl\n" + TTL, encoding="utf-8")
    (root / "src/schema_org").mkdir(parents=True)
    (root / "codegen/generated_manifest.json").write_text('{"paths": []}\n', encoding="utf-8")
    return root, target, hashlib.sha256(target.read_bytes()).hexdigest()


def test_same_version_is_noop(tmp_path):
    root, target, digest = tracked_tree(tmp_path)
    updater = SchemaUpdater(downloader=lambda url: "unused", target=target, project_root=root)
    assert updater.update("v30.0") is False
    assert hashlib.sha256(target.read_bytes()).hexdigest() == digest


def test_new_valid_release_replaces_source_and_artifacts(tmp_path):
    root, target, _ = tracked_tree(tmp_path)
    updater = SchemaUpdater(downloader=lambda url: TTL, target=target, project_root=root)
    assert updater.update("v30.1") is True
    assert "schema_org_release: v30.1" in target.read_text(encoding="utf-8")
    assert (root / "src/schema_org/schema_version.py").exists()


def test_bad_download_preserves_source(tmp_path):
    root, target, digest = tracked_tree(tmp_path)
    updater = SchemaUpdater(downloader=lambda url: "not turtle", target=target, project_root=root)
    with pytest.raises(ValidationError):
        updater.update("v30.1")
    assert hashlib.sha256(target.read_bytes()).hexdigest() == digest


def test_latest_version_requires_release_marker():
    updater = SchemaUpdater(downloader=lambda url: "<html>latest</html>")
    with pytest.raises(ValidationError, match="could not parse"):
        updater.latest_version()


def test_http_failure_preserves_target(tmp_path):
    root, target, digest = tracked_tree(tmp_path)

    def download(url):
        class Response:
            status = 503
            body = b"unavailable"
        return Response()

    with pytest.raises(ValidationError, match="503"):
        SchemaUpdater(downloader=download, target=target, project_root=root).update("v30.1")
    assert hashlib.sha256(target.read_bytes()).hexdigest() == digest


def test_validator_failure_preserves_every_tracked_artifact(tmp_path):
    root, target, _ = tracked_tree(tmp_path)
    existing = root / "src/schema_org/existing.py"
    existing.write_text("old", encoding="utf-8")
    manifest = root / "codegen/generated_manifest.json"
    manifest.write_text(json.dumps({"paths": ["src/schema_org/existing.py"]}), encoding="utf-8")
    before = {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}

    def reject(_root):
        raise RuntimeError("validator failed")

    updater = SchemaUpdater(downloader=lambda url: TTL, target=target, project_root=root, validator=reject)
    with pytest.raises(RuntimeError, match="validator failed"):
        updater.update("v30.1")
    after = {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}
    assert after == before


def test_replacement_failure_rolls_back_all_files(tmp_path, monkeypatch):
    root, target, _ = tracked_tree(tmp_path)
    existing = root / "src/schema_org/existing.py"
    existing.write_text("old", encoding="utf-8")
    manifest = root / "codegen/generated_manifest.json"
    manifest.write_text(json.dumps({"paths": ["src/schema_org/existing.py"]}), encoding="utf-8")
    before = {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}
    original = updater_module._atomic_write_bytes
    calls = 0

    def fail_after_two(path, content):
        nonlocal calls
        calls += 1
        if calls == 3:
            raise OSError("replace failed")
        return original(path, content)

    monkeypatch.setattr(updater_module, "_atomic_write_bytes", fail_after_two)
    updater = SchemaUpdater(downloader=lambda url: TTL, target=target, project_root=root)
    with pytest.raises(OSError, match="replace failed"):
        updater.update("v30.1")
    after = {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}
    assert after == before
