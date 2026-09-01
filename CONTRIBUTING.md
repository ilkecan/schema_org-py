# Contributing

## Schema.org updates

Schema.org vocabulary updates are handled by an automated workflow that maintainers can trigger; see [MAINTAINING.md](MAINTAINING.md#schema-org-updates).

## Pull request gate

The `Pull Request` workflow runs the required pull request gate. Run its checks locally in this order:

```sh
uv run python -m pytest
uv run ruff check .
uv run ty check
uv run python -m schema_org_codegen.check
uv run python -m build --outdir "$PWD/dist"
uv run python -m schema_org_codegen.package_check "$PWD/dist"
```
