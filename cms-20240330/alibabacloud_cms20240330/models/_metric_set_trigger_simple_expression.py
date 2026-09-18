# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MetricSetTriggerSimpleExpression(DaraModel):
    def __init__(
        self,
        abs_deviation: float = None,
        baseline_period: str = None,
        expression_type: str = None,
        max: float = None,
        min: float = None,
        operator: str = None,
        query_name: str = None,
        sensitivity: str = None,
        threshold: float = None,
    ):
        # The minimum deviation or absolute deviation dead zone for the dynamic baseline. Takes effect only for baseline operators. The unit is the same as the metric. The value must be greater than or equal to 0. A value of 0 indicates no restriction.
        self.abs_deviation = abs_deviation
        # The baseline period. Takes effect only for baseline operators. Valid values:
        # - AUTO: Automatically identifies the period.
        # - DAILY: Daily period.
        # - WEEKLY: Weekly period. The backend automatically expands the historical training window to at least 14 days.
        # - NONE: No period.
        self.baseline_period = baseline_period
        # The expression type. Fixed value: SIMPLE.
        self.expression_type = expression_type
        # The upper bound of the range. Required when operator is set to IN_RANGE or OUT_OF_RANGE. The value must be greater than or equal to min.
        self.max = max
        # The lower bound of the range. Required when operator is set to IN_RANGE or OUT_OF_RANGE.
        self.min = min
        # The comparison operator. Valid values:
        # - GT: Greater than.
        # - GE: Greater than or equal to.
        # - LT: Less than.
        # - LE: Less than or equal to.
        # - EQ: Equal to.
        # - NE: Not equal to.
        # - IN_RANGE: Within the range. Both min and max must be specified.
        # - OUT_OF_RANGE: Outside the range. Both min and max must be specified.
        # - PRESENT: The field exists. The threshold, min, and max parameters are not required.
        # - NOT_PRESENT: The field does not exist. The threshold, min, and max parameters are not required.
        # - ABOVE_UPPER: Dynamic baseline spike. The sensitivity parameter is required. The threshold, min, and max parameters are not required.
        # - BELOW_LOWER: Dynamic baseline drop. The sensitivity parameter is required. The threshold, min, and max parameters are not required.
        # - OUT_OF_BAND: Dynamic baseline bidirectional deviation. The sensitivity parameter is required. The threshold, min, and max parameters are not required.
        self.operator = operator
        # The referenced query name, corresponding to QueryConfigUnified.queries[].name.
        self.query_name = query_name
        # The dynamic baseline sensitivity. Takes effect only for baseline operators. Valid values:
        # - HIGH: The narrowest band and highest sensitivity.
        # - MEDIUM: Medium sensitivity.
        # - LOW: The widest band and lowest sensitivity.
        self.sensitivity = sensitivity
        # The comparison threshold. Used when operator is set to GT, GE, LT, LE, EQ, or NE. For IN_RANGE or OUT_OF_RANGE, use min and max instead. Not required for PRESENT or NOT_PRESENT.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abs_deviation is not None:
            result['absDeviation'] = self.abs_deviation

        if self.baseline_period is not None:
            result['baselinePeriod'] = self.baseline_period

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

        if self.sensitivity is not None:
            result['sensitivity'] = self.sensitivity

        if self.threshold is not None:
            result['threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('absDeviation') is not None:
            self.abs_deviation = m.get('absDeviation')

        if m.get('baselinePeriod') is not None:
            self.baseline_period = m.get('baselinePeriod')

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

        if m.get('sensitivity') is not None:
            self.sensitivity = m.get('sensitivity')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        return self

