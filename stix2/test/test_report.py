import stix2
import pytest
from .constants import INDICATOR_KWARGS

EXPECTED = """{
    "created": "2015-12-21T19:59:11Z",
    "created_by_ref": "identity--a463ffb3-1bd9-4d94-b02d-74e4f1658283",
    "description": "A simple report with an indicator and campaign",
    "id": "report--84e4d88f-44ea-4bcd-bbf3-b2c1c320bcb3",
    "labels": [
        "campaign"
    ],
    "modified": "2015-12-21T19:59:11Z",
    "name": "The Black Vine Cyberespionage Group",
    "object_refs": [
        "indicator--26ffb872-1dd9-446e-b6f5-d58527e5b5d2",
        "campaign--83422c77-904c-4dc1-aff5-5c38f3a2c55c",
        "relationship--f82356ae-fe6c-437c-9c24-6b64314ae68a"
    ],
    "published": "2016-01-20T17:00:00Z",
    "type": "report"
}"""


def test_report_example():
    report = stix2.Report(
        id="report--84e4d88f-44ea-4bcd-bbf3-b2c1c320bcb3",
        created_by_ref="identity--a463ffb3-1bd9-4d94-b02d-74e4f1658283",
        created="2015-12-21T19:59:11Z",
        modified="2015-12-21T19:59:11Z",
        name="The Black Vine Cyberespionage Group",
        description="A simple report with an indicator and campaign",
        published="2016-01-20T17:00:00Z",
        labels=["campaign"],
        object_refs=[
            "indicator--26ffb872-1dd9-446e-b6f5-d58527e5b5d2",
            "campaign--83422c77-904c-4dc1-aff5-5c38f3a2c55c",
            "relationship--f82356ae-fe6c-437c-9c24-6b64314ae68a"
        ],
    )

    assert str(report) == EXPECTED


def test_report_example_objects_in_object_refs():
    report = stix2.Report(
        id="report--84e4d88f-44ea-4bcd-bbf3-b2c1c320bcb3",
        created_by_ref="identity--a463ffb3-1bd9-4d94-b02d-74e4f1658283",
        created="2015-12-21T19:59:11.000Z",
        modified="2015-12-21T19:59:11.000Z",
        name="The Black Vine Cyberespionage Group",
        description="A simple report with an indicator and campaign",
        published="2016-01-20T17:00:00Z",
        labels=["campaign"],
        object_refs=[
            stix2.Indicator(id="indicator--26ffb872-1dd9-446e-b6f5-d58527e5b5d2", **INDICATOR_KWARGS),
            "campaign--83422c77-904c-4dc1-aff5-5c38f3a2c55c",
            "relationship--f82356ae-fe6c-437c-9c24-6b64314ae68a"
        ],
    )

    assert str(report) == EXPECTED


def test_report_example_objects_in_object_refs_with_bad_id():
    with pytest.raises(ValueError) as excinfo:
        stix2.Report(
            id="report--84e4d88f-44ea-4bcd-bbf3-b2c1c320bcb3",
            created_by_ref="identity--a463ffb3-1bd9-4d94-b02d-74e4f1658283",
            created="2015-12-21T19:59:11.000Z",
            modified="2015-12-21T19:59:11.000Z",
            name="The Black Vine Cyberespionage Group",
            description="A simple report with an indicator and campaign",
            published="2016-01-20T17:00:00Z",
            labels=["campaign"],
            object_refs=[
                stix2.Indicator(id="indicator--26ffb872-1dd9-446e-b6f5-d58527e5b5d2", **INDICATOR_KWARGS),
                "campaign-83422c77-904c-4dc1-aff5-5c38f3a2c55c",   # the "bad" id, missing a "-"
                "relationship--f82356ae-fe6c-437c-9c24-6b64314ae68a"
            ],
        )

    assert str(excinfo.value) == "Invalid value for Report 'object_refs': must match <object-type>--<guid>."

# TODO: Add other examples
