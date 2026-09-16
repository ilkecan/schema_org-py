from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

import pytest
import schema_org_codegen.transaction as transaction_module
from schema_org_codegen.updater import SchemaUpdater
from schema_org_codegen.vocabulary import ValidationError

ROOT = Path(__file__).parents[1]
TTL = """@prefix schema: <https://schema.org/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
schema:Thing a rdfs:Class ; rdfs:label "Thing" .
schema:DataType a rdfs:Class ; rdfs:label "DataType" ; rdfs:subClassOf schema:Thing .
schema:Text a rdfs:Class ; rdfs:label "Text" ; rdfs:subClassOf schema:DataType .
schema:Person a rdfs:Class ; rdfs:label "Person" ; rdfs:subClassOf schema:Thing .
schema:PostalAddress a rdfs:Class ; rdfs:label "PostalAddress" ; rdfs:subClassOf schema:Thing .
schema:Book a rdfs:Class ; rdfs:label "Book" ; rdfs:subClassOf schema:Thing .
schema:VisualArtwork a rdfs:Class ; rdfs:label "VisualArtwork" ; rdfs:subClassOf schema:Thing .
schema:SequentialArt a rdfs:Class ; rdfs:label "SequentialArt" ; rdfs:subClassOf schema:Book, schema:VisualArtwork .
schema:Offer a rdfs:Class ; rdfs:label "Offer" ; rdfs:subClassOf schema:Thing .
schema:Enumeration a rdfs:Class ; rdfs:label "Enumeration" ; rdfs:subClassOf schema:Thing .
schema:ItemAvailability a rdfs:Class ; rdfs:label "ItemAvailability" ; rdfs:subClassOf schema:Enumeration .
schema:BookFormatType a rdfs:Class ; rdfs:label "BookFormatType" ; rdfs:subClassOf schema:Enumeration .
schema:InStock a schema:ItemAvailability ; rdfs:label "InStock" .
schema:EBook a schema:BookFormatType ; rdfs:label "EBook" .
schema:name a rdf:Property ; rdfs:label "name" ; schema:domainIncludes schema:Person ; schema:rangeIncludes schema:Text .
schema:address a rdf:Property ; rdfs:label "address" ; schema:domainIncludes schema:Person ; schema:rangeIncludes schema:PostalAddress .
schema:addressLocality a rdf:Property ; rdfs:label "addressLocality" ; schema:domainIncludes schema:PostalAddress ; schema:rangeIncludes schema:Text .
schema:availability a rdf:Property ; rdfs:label "availability" ; schema:domainIncludes schema:Offer ; schema:rangeIncludes schema:ItemAvailability .
schema:bookFormat a rdf:Property ; rdfs:label "bookFormat" ; schema:domainIncludes schema:Book ; schema:rangeIncludes schema:BookFormatType .
"""


def tracked_tree(tmp_path: Path) -> tuple[Path, Path, str]:
    root = tmp_path
    target = root / "codegen/data/schema.ttl"
    target.parent.mkdir(parents=True)
    target.write_text(
        "# schema_org_release: v30.0\n"
        "# schema_org_source: https://schema.org/version/30.0/schemaorg-all-https.ttl\n"
        + TTL,
        encoding="utf-8",
    )
    (root / "src/schema_org").mkdir(parents=True)
    shutil.copy(ROOT / "src/schema_org/base.py", root / "src/schema_org/base.py")
    (root / "codegen/generated_manifest.json").write_text(json.dumps({
        "schema_version": "30.0",
        "schema_source": "https://schema.org/version/30.0/schemaorg-all-https.ttl",
        "paths": [],
        "terms": {"classes": [], "datatypes": [], "enumerations": [], "enumeration_members": [], "properties": []},
    }) + "\n", encoding="utf-8")
    return root, target, hashlib.sha256(target.read_bytes()).hexdigest()


def test_same_version_is_noop(tmp_path):
    root, target, digest = tracked_tree(tmp_path)
    calls = []
    updater = SchemaUpdater(downloader=lambda url: calls.append(url), target=target, project_root=root)
    assert updater.update("v30.0") is False
    assert calls == []
    assert hashlib.sha256(target.read_bytes()).hexdigest() == digest


def test_lower_version_is_rejected_before_download(tmp_path):
    root, target, _ = tracked_tree(tmp_path)
    calls = []
    updater = SchemaUpdater(downloader=lambda url: calls.append(url), target=target, project_root=root)
    with pytest.raises(ValidationError, match="older"):
        updater.update("v29.9")
    assert calls == []


def test_incomplete_project_is_rejected(tmp_path):
    root, target, _ = tracked_tree(tmp_path)
    shutil.rmtree(root / "src/schema_org")
    with pytest.raises(ValidationError, match="incomplete"):
        SchemaUpdater(downloader=lambda url: TTL, target=target, project_root=root).update("v30.1")


def test_new_valid_release_generates_artifacts_without_project_validation(tmp_path):
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


def test_replacement_failure_rolls_back_all_files(tmp_path, monkeypatch):
    root, _target, _ = tracked_tree(tmp_path)
    existing = root / "src/schema_org/models/existing.py"
    existing.parent.mkdir(parents=True)
    existing.write_text("old", encoding="utf-8")
    manifest = root / "codegen/generated_manifest.json"
    manifest.write_text(json.dumps({
        "schema_version": "30.0",
        "schema_source": "https://schema.org/version/30.0/schemaorg-all-https.ttl",
        "paths": ["src/schema_org/models/existing.py"],
        "terms": {"classes": [], "datatypes": [], "enumerations": [], "enumeration_members": [], "properties": []},
    }), encoding="utf-8")
    before = {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}
    original = transaction_module._replace_bytes
    calls = 0
    failed = False

    def fail_after_two(path, content):
        nonlocal calls, failed
        calls += 1
        original(path, content)
        if calls == 3 and not failed:
            failed = True
            raise OSError("replace failed")

    monkeypatch.setattr(transaction_module, "_replace_bytes", fail_after_two)
    updater = SchemaUpdater(
        downloader=lambda url: TTL,
        target=Path("codegen/data/schema.ttl"),
        project_root=root,
    )
    with pytest.raises(OSError, match="replace failed"):
        updater.update("v30.1")
    after = {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}
    assert after == before


def _all_files(root: Path) -> dict[Path, bytes]:
    return {
        path.relative_to(root): path.read_bytes()
        for path in root.rglob("*")
        if path.is_file()
    }


def test_invalid_prior_manifest_preserves_every_file(tmp_path: Path):
    root, target, _ = tracked_tree(tmp_path)
    manifest = root / "codegen/generated_manifest.json"
    manifest.write_text("{not-json", encoding="utf-8")
    before = _all_files(root)
    with pytest.raises(ValidationError):
        SchemaUpdater(downloader=lambda url: TTL, target=target, project_root=root).update("v30.1")
    assert _all_files(root) == before
