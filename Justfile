#!/usr/bin/env -S just --justfile
# https://just.systems

set fallback
set quiet

[private]
default:
  just --list

outdated:
  uv tree --outdated

sync:
  uv sync --locked

test:
  uv run python -m pytest

lint:
  uv run ruff check . && uv run ty check

update:
  uv lock --upgrade
