import subprocess
import sys
from datetime import date, datetime

import pytest
from pydantic import ValidationError

from schema_org import DayOfWeek, ItemAvailability, Observation, Offer, Person, PostalAddress
from schema_org.base import CircularReferenceError


def test_exact_typed_values_and_subclasses():
    assert Person(name="Ada").name == "Ada"
    with pytest.raises(ValidationError):
        Person(name=1)
    with pytest.raises(ValidationError):
        Person(name=type("TextSubclass", (str,), {})("Ada"))
    with pytest.raises(ValidationError):
        Person(birth_date=datetime(2020, 1, 1))


def test_enums_accept_descendants_but_not_unrelated_ranges():
    assert Offer(availability=ItemAvailability.IN_STOCK).availability is ItemAvailability.IN_STOCK
    with pytest.raises(ValidationError):
        Offer(availability=DayOfWeek.MONDAY)
    with pytest.raises(ValidationError):
        Offer(availability="InStock")


def test_input_context_is_forbidden_and_type_is_frozen():
    with pytest.raises(ValidationError):
        Person(name="Ada", **{"@context": "https://schema.org"})
    person = Person(name="Ada")
    with pytest.raises(ValidationError):
        person.schema_type = "Thing"


def test_deep_nested_models_and_structural_values():
    person = Person(children=[{"children": [{"name": "Ada"}]}])
    assert person.children[0].children[0].name == "Ada"
    with pytest.raises(ValidationError):
        Person(children=[[{"name": "Ada"}]])
    Observation(measured_property={"a": {"b": 1}})
    with pytest.raises(ValidationError):
        Observation(measured_property={"a": [1]})


def test_self_assignment_and_cycle_path():
    person = Person(name="Ada")
    with pytest.raises(ValidationError):
        person.colleague = [person, 1]
    assert person.colleague is None
    person.colleague = [person]
    with pytest.raises(CircularReferenceError, match=r"\$\.colleague\[0\]"):
        person.to_jsonld()



def test_typed_inputs_reject_subclasses_and_report_raw_cycles():
    class CustomPerson(Person):
        pass

    custom = CustomPerson.model_construct(name="Ada")
    with pytest.raises(ValidationError):
        Person(children=[custom])

    person = Person(name="Ada")
    with pytest.raises(ValidationError):
        person.children = [custom]
    child = {}
    child["children"] = [child]
    with pytest.raises(ValidationError, match=r"\$\.children\[0\]\.children\[0\]"):
        Person(children=[child])


def test_lazy_model_resolution_is_cached_and_forceable():
    from schema_org import registry
    from schema_org import Person as RootPerson
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

def test_jsonld_aliases_context_and_dates():
    result = Person(name="Ada", address=PostalAddress(address_locality="London"), birth_date=date(1990, 1, 2)).to_jsonld()
    assert result == {
        "@context": "https://schema.org",
        "@type": "Person",
        "address": {"@type": "PostalAddress", "addressLocality": "London"},
        "name": "Ada",
        "birthDate": "1990-01-02",
    }
    assert '"@context":"https://schema.org"' in Person(name="Ada").to_jsonld_json()
def test_fresh_process_direct_module_and_json_validation():
    script = (
        "from schema_org.models.person import Person\n"
        "p = Person.model_validate_json('{\"name\":\"Ada\"}')\n"
        "assert p.name == 'Ada'\n"
    )
    result = subprocess.run([sys.executable, "-c", script], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
