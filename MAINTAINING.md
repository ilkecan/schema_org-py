# Maintaining

## Schema.org updates

Schema.org updates are generated through the `Update Schema.org` workflow. Dispatch it manually from `main` with a `version` input in exact `v<major>.<minor>` form. The workflow downloads the requested immutable Schema.org release, regenerates the artifacts, checks the generated scope, and opens a pull request containing only the schema snapshot and generated outputs. The pull request runs the pull request gate.

The workflow uses the repository's `GITHUB_TOKEN`. Enable **Allow GitHub Actions to create and approve pull requests** under **Settings -> Actions -> General -> Workflow permissions**. No GitHub App or long-lived token is required.

Pull request workflows triggered by a pull request created with `GITHUB_TOKEN` may start in an approval-required state. A maintainer with write access must approve the workflow run before the pull request gate starts.

Run the same update locally with:

```sh
uv sync --locked
uv run python -c 'from schema_org_codegen.updater import SchemaUpdater; print(SchemaUpdater().update("v31.0"))'
```

The generated pull request may change only `codegen/data/schema.ttl`, `codegen/generated_manifest.json`, `src/schema_org/__init__.py`, `src/schema_org/datatypes.py`, `src/schema_org/enums.py`, `src/schema_org/registry.py`, `src/schema_org/schema_version.py`, `src/schema_org/py.typed`, `src/schema_org/models/__init__.py`, and files under `src/schema_org/models/`.

## Releases

The package version is defined by `project.version` in `pyproject.toml`. Update that value and the matching `CHANGELOG.md` entry in a pull request. The package version and Schema.org vocabulary version are separate.

Before releasing, configure:

- GitHub environment: `pypi`
- Required reviewers and a `main` deployment branch restriction on that environment
- PyPI trusted publisher for `schema_org-py`
- Repository: `ilkecan/schema_org-py`
- Workflow: `release.yml`

Environment protection rules are configured in repository settings. The workflow attaches the publish job to the `pypi` environment, but required reviewers cannot be declared in workflow YAML.

After the version and changelog changes pass the pull request gate and reach `main`, dispatch the `Release` workflow from `main`. It derives the package version with `uv version --short`, verifies Python 3.10 through 3.14, checks the current `main` commit, validates the package, creates the matching annotated tag, publishes the verified artifacts with trusted publishing, and creates or repairs the matching GitHub release.

The package contains generated Python files, `LICENSE.txt`, `LICENSE-SCHEMA-ORG.txt`, `README.md`, and `CHANGELOG.md`. It does not contain the maintainer input `codegen/data/schema.ttl`. No long-lived PyPI API token is used.
