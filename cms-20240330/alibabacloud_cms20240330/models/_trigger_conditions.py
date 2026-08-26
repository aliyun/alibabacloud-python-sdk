# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TriggerConditions(DaraModel):
    def __init__(
        self,
        expression_type: str = None,
        max: float = None,
        min: float = None,
        operator: str = None,
        query_name: str = None,
        threshold: float = None,
    ):
        # The expression type, fixed as SIMPLE (used by MetricSet multi-threshold triggers).
        self.expression_type = expression_type
        # The upper bound of the range. Required when operator is IN_RANGE or OUT_OF_RANGE. Must be greater than or equal to min.
        self.max = max
        # The lower bound of the range. Required when operator is IN_RANGE or OUT_OF_RANGE.
        self.min = min
        # The comparison operator. Valid values: GT / GE / LT / LE / EQ / NE / IN_RANGE (requires both min and max) / OUT_OF_RANGE (requires both min and max) / PRESENT / NOT_PRESENT.
        self.operator = operator
        # The referenced query name, corresponding to QueryConfigUnified.queries[].name.
        self.query_name = query_name
        # The comparison threshold. Used when operator is GT, GE, LT, LE, EQ, or NE. Use min and max for IN_RANGE or OUT_OF_RANGE. Leave empty for PRESENT or NOT_PRESENT.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression_type is not None:
            result['expressionType'] = self.expression_type

        if self.max is not None:
            result['max'] = self.max

        if self.min is not None:
            result['min'] = self.min

        if self.operator is not None:
            result['operator'] = self.operator

        if self.query_name is not None:
            result['queryName'] = self.query_name

        if self.threshold is not None:
            result['threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expressionType') is not None:
            self.expression_type = m.get('expressionType')

        if m.get('max') is not None:
            self.max = m.get('max')

        if m.get('min') is not None:
            self.min = m.get('min')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('queryName') is not None:
            self.query_name = m.get('queryName')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        return self

