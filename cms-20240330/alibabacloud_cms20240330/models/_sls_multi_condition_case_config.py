# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SlsMultiConditionCaseConfig(DaraModel):
    def __init__(
        self,
        count_operator: str = None,
        count_threshold: int = None,
        match_field: str = None,
        match_operator: str = None,
        match_value: str = None,
        severity: str = None,
    ):
        # The count comparison operator. Valid values: GTE, GT, EQ, LTE, LT.
        self.count_operator = count_operator
        # The count threshold. The alert is triggered when this threshold is met.
        self.count_threshold = count_threshold
        # The log field name. Required when matchOperator is set to CONTAINS, EQUALS, or REGEX. Specify the field name when matchOperator is set to PRESENT or NOT_PRESENT.
        self.match_field = match_field
        # The log matching operator. Valid values: PRESENT (field exists), NOT_PRESENT (field does not exist), CONTAINS (contains), EQUALS (equals), REGEX (regular expression). If left empty, any data matches.
        self.match_operator = match_operator
        # The log match value. Required when matchOperator is set to CONTAINS, EQUALS, or REGEX.
        self.match_value = match_value
        # The severity level.
        self.severity = severity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count_operator is not None:
            result['countOperator'] = self.count_operator

        if self.count_threshold is not None:
            result['countThreshold'] = self.count_threshold

        if self.match_field is not None:
            result['matchField'] = self.match_field

        if self.match_operator is not None:
            result['matchOperator'] = self.match_operator

        if self.match_value is not None:
            result['matchValue'] = self.match_value

        if self.severity is not None:
            result['severity'] = self.severity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('countOperator') is not None:
            self.count_operator = m.get('countOperator')

        if m.get('countThreshold') is not None:
            self.count_threshold = m.get('countThreshold')

        if m.get('matchField') is not None:
            self.match_field = m.get('matchField')

        if m.get('matchOperator') is not None:
            self.match_operator = m.get('matchOperator')

        if m.get('matchValue') is not None:
            self.match_value = m.get('matchValue')

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        return self

