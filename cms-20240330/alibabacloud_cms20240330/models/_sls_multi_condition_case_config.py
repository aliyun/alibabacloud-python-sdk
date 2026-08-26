# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SlsMultiConditionCaseConfig(DaraModel):
    def __init__(
        self,
        condition: str = None,
        count_condition: str = None,
        count_operator: str = None,
        count_threshold: int = None,
        match_field: str = None,
        match_operator: str = None,
        match_value: str = None,
        operator: str = None,
        raw_condition: str = None,
        severity: str = None,
    ):
        # The match expression (corresponds to V1 condition, preserved as-is without structured parsing).
        self.condition = condition
        # The count match expression (corresponds to V1 countCondition, preserved as-is without structured parsing).
        self.count_condition = count_condition
        # **[Deprecated]** The write path is disabled. Use countCondition instead.
        self.count_operator = count_operator
        # **[Deprecated]** The write path is disabled. Use countCondition instead.
        self.count_threshold = count_threshold
        # **[Deprecated]** The write path is disabled. Use condition instead.
        self.match_field = match_field
        # **[Deprecated]** The write path is disabled. Use condition instead.
        self.match_operator = match_operator
        # **[Deprecated]** The write path is disabled. Use condition instead.
        self.match_value = match_value
        # The detection operator (aligned with V1 caseList.type): HAS_DATA / HAS_DATA_COUNT / HAS_DATA_MATCH / HAS_DATA_MATCH_COUNT.
        self.operator = operator
        # **[Deprecated]** The write path is disabled. Use condition instead.
        self.raw_condition = raw_condition
        # The severity level (corresponds to V1 level).
        self.severity = severity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['condition'] = self.condition

        if self.count_condition is not None:
            result['countCondition'] = self.count_condition

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

        if self.operator is not None:
            result['operator'] = self.operator

        if self.raw_condition is not None:
            result['rawCondition'] = self.raw_condition

        if self.severity is not None:
            result['severity'] = self.severity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')

        if m.get('countCondition') is not None:
            self.count_condition = m.get('countCondition')

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

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('rawCondition') is not None:
            self.raw_condition = m.get('rawCondition')

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        return self

