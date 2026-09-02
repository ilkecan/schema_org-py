import json
import subprocess
import sys
from datetime import date, datetime, time
from typing import Any, cast

import pytest
from pydantic import ValidationError

import schema_org
from schema_org import (
    DayOfWeek,
    Event,
    ItemAvailability,
    Observation,
    Offer,
    Person,
    PostalAddress,
)
from schema_org.base import CircularReferenceError, SchemaEnum


def test_exact_typed_values_and_subclasses():
    assert Person(name="Ada").name == "Ada"
    with pytest.raises(ValidationError):
        Person(name=cast(Any, 1))
    with pytest.raises(ValidationError):
        Person(name=cast(Any, type("TextSubclass", (str,), {})("Ada")))
    with pytest.raises(ValidationError):
        Person(birth_date=cast(Any, datetime(2020, 1, 1)))


def test_enums_accept_descendants_but_not_unrelated_ranges():
    assert Offer(availability=ItemAvailability.IN_STOCK).availability is ItemAvailability.IN_STOCK
    with pytest.raises(ValidationError):
        cast(Any, Offer)(availability=cast(Any, DayOfWeek.MONDAY))
    with pytest.raises(ValidationError):
        cast(Any, Offer)(availability=cast(Any, "InStock"))


def test_input_context_is_forbidden_and_type_is_frozen():
    with pytest.raises(ValidationError):
        cast(Any, Person).model_validate({"name": "Ada", "@context": "https://schema.org"})
    person = Person(name="Ada")
    with pytest.raises(ValidationError):
        cast(Any, person).schema_type = "Thing"


def test_structural_values_cover_the_complete_shape_contract():
    model = Person(name="Ada")
    values = (
        "text",
        True,
        1,
        1.5,
        ItemAvailability.IN_STOCK,
        model,
        {"outer": {"inner": model}},
        ["text", True, 1, 1.5, ItemAvailability.IN_STOCK, model, {"inner": 1}],
    )
    for value in values:
        assert cast(Any, Observation)(measured_property=cast(Any, value)).measured_property is not None

    invalid_values = (
        [["nested"]],
        {"nested": ["list"]},
        {1: "bad"},
        ("tuple",),
        date(2020, 1, 1),
        type("TextSubclass", (str,), {})("text"),
        type("IntegerSubclass", (int,), {})(1),
        type("FloatSubclass", (float,), {})(1.5),
    )
    for value in invalid_values:
        with pytest.raises(ValidationError):
            Observation(measured_property=cast(Any, value))

    class ConsumerEnum(SchemaEnum):
        VALUE = "https://example.test/value"

    with pytest.raises(ValidationError):
        Observation(measured_property=cast(Any, ConsumerEnum.VALUE))


def test_typed_recursive_models_reject_nested_lists():
    person = cast(Any, Person)(children=cast(Any, [{"children": [{"name": "Ada"}]}]))
    assert person.children[0].children[0].name == "Ada"
    with pytest.raises(ValidationError):
        cast(Any, Person)(children=cast(Any, [[{"name": "Ada"}]]))


def test_self_assignment_is_rejected_without_mutation():
    person = Person(name="Ada")
    with pytest.raises(ValidationError):
        person.colleague = [person]
    assert person.colleague is None


def test_bypassed_cycles_report_exact_paths():
    object_cycle = Person(name="Ada")
    object.__setattr__(object_cycle, "colleague", [object_cycle])

    constructed_cycle = Person.model_construct(colleague=[])
    assert constructed_cycle.colleague is not None
    cast(Any, constructed_cycle.colleague).append(constructed_cycle)

    mutated_list_cycle = Person(colleague=[])
    assert mutated_list_cycle.colleague is not None
    cast(Any, mutated_list_cycle.colleague).append(mutated_list_cycle)

    mutated_map_cycle = Observation(measured_property={})
    measured = cast(dict[str, Any], mutated_map_cycle.measured_property)
    measured["loop"] = measured

    for value, path in (
        (object_cycle, r"\$\.colleague\[0\]"),
        (constructed_cycle, r"\$\.colleague\[0\]"),
        (mutated_list_cycle, r"\$\.colleague\[0\]"),
        (mutated_map_cycle, r"\$\.measuredProperty\['loop'\]"),
    ):
        with pytest.raises(CircularReferenceError, match=path):
            value.to_jsonld()


def test_raw_input_cycles_report_exact_paths():
    raw_list: list[Any] = []
    raw_list.append(raw_list)
    with pytest.raises(ValidationError, match=r"\$\.measuredProperty\[0\]"):
        Observation(measured_property=cast(Any, raw_list))

    raw_map: dict[str, Any] = {}
    raw_map["loop"] = raw_map
    with pytest.raises(ValidationError, match=r"\$\.measuredProperty\['loop'\]"):
        Observation(measured_property=cast(Any, raw_map))

    raw_model = Person.model_construct(colleague=[])
    assert raw_model.colleague is not None
    cast(Any, raw_model.colleague).append(raw_model)
    with pytest.raises(ValidationError, match=r"\$\.measuredProperty\.colleague\[0\]"):
        cast(Any, Observation)(measured_property=raw_model)



def test_typed_inputs_reject_model_subclasses():
    class CustomPerson(Person):
        pass

    custom = CustomPerson.model_construct(name="Ada")
    with pytest.raises(ValidationError):
        Person(children=cast(Any, [custom]))

    person = Person(name="Ada")
    with pytest.raises(ValidationError):
        person.children = cast(Any, [custom])


def test_shared_model_list_and_mapping_branches_serialize():
    shared_model = Person(name="Grace")
    shared_list = [shared_model]
    person = Person.model_construct(children=shared_list, colleague=shared_list)
    assert person.children is person.colleague
    output = person.to_jsonld()
    assert output["children"] == [{"@type": "Person", "name": "Grace"}]
    assert output["colleague"] == [{"@type": "Person", "name": "Grace"}]

    shared_mapping = {"value": shared_model}
    observation = Observation.model_construct(
        measured_property=[shared_mapping, shared_mapping]
    )
    assert observation.to_jsonld()["measuredProperty"] == [
        {"value": {"@type": "Person", "name": "Grace"}},
        {"value": {"@type": "Person", "name": "Grace"}},
    ]


def test_lazy_model_resolution_is_cached_and_forceable():
    from schema_org import Person as RootPerson
    from schema_org import registry
    from schema_org.models import Person as ModelsPerson

    registry._MODEL_CACHE.clear()
    first = registry.get_model("Person")
    assert first is RootPerson is ModelsPerson
    assert registry._MODEL_CACHE["Person"] is first
    assert registry.get_model("Person") is first
    first.model_rebuild()
    assert registry._MODEL_CACHE["Person"] is first
    assert first.model_rebuild(force=True) is True
    assert registry._MODEL_CACHE["Person"] is first

def test_root_exports_are_complete_without_eager_model_exports():
    from schema_org_codegen.naming import constant_name

    from schema_org import Person as RootPerson
    from schema_org import registry

    runtime_exports = {
        "SCHEMA_VERSION",
        "CircularReferenceError",
        "ClassMetadata",
        "EnumerationMemberMetadata",
        "JsonValue",
        "PropertyMetadata",
        "SchemaEnum",
        "SchemaMap",
        "SchemaModel",
        "SchemaScalar",
        "SchemaValue",
    }
    enum_exports = {constant_name(name) for name in registry.ENUM_BY_SCHEMA}
    model_exports = set(registry._MODEL_CLASSES.values())
    assert set(schema_org.__all__) == runtime_exports | enum_exports
    assert not set(schema_org.__all__) & model_exports
    assert "Person" in dir(schema_org)
    assert RootPerson is schema_org.Person


def test_jsonld_aliases_ids_context_dates_and_json_layout():
    result = Person(
        schema_id="urn:person:ada",
        name="Ada",
        address=PostalAddress(address_locality="London"),
        birth_date=date(1990, 1, 2),
    ).to_jsonld()
    assert result == {
        "@context": "https://schema.org",
        "@type": "Person",
        "@id": "urn:person:ada",
        "address": {"@type": "PostalAddress", "addressLocality": "London"},
        "name": "Ada",
        "birthDate": "1990-01-02",
    }
    person = Event(
        name="Ada",
        start_date=date(1990, 1, 2),
        door_time=time(3, 4, 5),
    )
    compact = person.to_jsonld_json()
    indented = person.to_jsonld_json(indent=2)
    assert compact == json.dumps(
        person.to_jsonld(), ensure_ascii=False, separators=(",", ":")
    )
    assert indented == json.dumps(person.to_jsonld(), ensure_ascii=False, indent=2)
    assert indented.count('"@context"') == 1
    assert '"doorTime": "03:04:05"' in indented

def test_fresh_process_direct_module_and_json_validation():
    script = (
        "from schema_org.models.person import Person\n"
        "p = Person.model_validate_json('{\"name\":\"Ada\"}')\n"
        "assert p.name == 'Ada'\n"
    )
    result = subprocess.run([sys.executable, "-c", script], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
