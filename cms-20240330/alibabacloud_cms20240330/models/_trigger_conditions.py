# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TriggerConditions(DaraModel):
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
        # The minimum deviation or absolute deviation dead zone for dynamic baselines, which takes effect only for baseline operators. No alert is triggered if the absolute difference between the current value and the boundary is less than the absDeviation value. The unit is the same as the metric unit. The value must be greater than or equal to 0. A value of 0 indicates no limit.
        self.abs_deviation = abs_deviation
        # The baseline period, which takes effect only for baseline operators. Valid values: AUTO for automatic identification, DAILY for daily, WEEKLY for weekly, and NONE for no period. If you set this parameter to WEEKLY, the backend automatically extends the historical training window to at least 14 days.
        self.baseline_period = baseline_period
        # The expression type. The value is fixed as SIMPLE, which is used for MetricSet multi-threshold triggers.
        self.expression_type = expression_type
        # The upper bound of the range. This parameter is required when the operator is IN_RANGE or OUT_OF_RANGE, and the value must be greater than or equal to the min value.
        self.max = max
        # The lower bound of the range. This parameter is required when the operator is IN_RANGE or OUT_OF_RANGE.
        self.min = min
        # The comparison operator. Valid values: GT, GE, LT, LE, EQ, NE, IN_RANGE (requires both min and max), OUT_OF_RANGE (requires both min and max), PRESENT, and NOT_PRESENT.
        self.operator = operator
        # The referenced query name, which corresponds to QueryConfigUnified.queries[].name.
        self.query_name = query_name
        # The dynamic baseline sensitivity, which takes effect only when the operator is ABOVE_UPPER, BELOW_LOWER, or OUT_OF_BAND. Valid values: HIGH for the narrowest and most sensitive band, MEDIUM for medium sensitivity, and LOW for the widest and least sensitive band. You can configure different sensitivities for multiple subconditions.
        self.sensitivity = sensitivity
        # The comparison threshold. This parameter is used when the operator is GT, GE, LT, LE, EQ, or NE. For IN_RANGE or OUT_OF_RANGE, use the min and max parameters. For PRESENT or NOT_PRESENT, leave this parameter empty.
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

