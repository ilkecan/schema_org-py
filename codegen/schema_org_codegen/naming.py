from __future__ import annotations

import keyword
import re

_DIGIT_WORDS = {
    "0": "Zero", "1": "One", "2": "Two", "3": "Three", "4": "Four",
    "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine",
}


def _replace_leading_digits(name: str) -> str:
    match = re.match(r"^\d+", name)
    if not match:
        return name
    return "".join(_DIGIT_WORDS[digit] for digit in match.group()) + name[match.end():]


def constant_name(schema_name: str) -> str:
    name = _replace_leading_digits(str(schema_name))
    if not re.fullmatch(r"[A-Z][A-Za-z0-9_]*", name):
        raise ValueError(f"Invalid Python class name for schema term {schema_name}: {name}")
    return name


def snake_name(schema_name: str) -> str:
    name = _replace_leading_digits(str(schema_name))
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    name = re.sub(r"[^A-Za-z0-9_]", "_", name).lower()
    if not re.fullmatch(r"[a-z_][a-z0-9_]*", name):
        raise ValueError(f"Invalid Python name for schema term {schema_name}: {name}")
    return name


def module_name(schema_name: str) -> str:
    name = snake_name(schema_name)
    return f"{name}_" if keyword.iskeyword(name) else name


def property_name(schema_name: str) -> str:
    name = snake_name(schema_name)
    return f"{name}_" if keyword.iskeyword(name) else name


def enum_member_name(schema_name: str) -> str:
    name = snake_name(schema_name).upper()
    if not re.fullmatch(r"[A-Z_][A-Z0-9_]*", name):
        raise ValueError(f"Invalid Python enum member for schema term {schema_name}: {name}")
    return name
