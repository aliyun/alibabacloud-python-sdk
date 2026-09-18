# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CompareList(DaraModel):
    def __init__(
        self,
        abs_deviation: float = None,
        aggregate: str = None,
        baseline_period: str = None,
        operator: str = None,
        sensitivity: str = None,
        threshold: float = None,
        yoy_time_unit: str = None,
        yoy_time_value: int = None,
    ):
        # The dynamic baseline minimum deviation or absolute deviation dead zone. This parameter takes effect only when a baseline operator is used. If |current value − boundary| < absDeviation, no alert is triggered. The unit is the same as the metric unit. The value must be greater than or equal to 0. A value of 0 indicates no restriction.
        self.abs_deviation = abs_deviation
        # The aggregation function.
        # 
        # This parameter is required.
        self.aggregate = aggregate
        # The baseline period. This parameter takes effect only when a baseline operator is used. Valid values:
        # - AUTO: Automatically identifies the period. The specific identification result cannot be displayed.
        # - DAILY: Daily period.
        # - WEEKLY: Weekly period. The backend automatically expands the historical training window to at least 14 days.
        # - NONE: No period.
        self.baseline_period = baseline_period
        # The comparison operator. Valid values:
        # - GTE: greater than or equal to.
        # - LTE: less than or equal to.
        # - YOY_UP: year-over-year increase. You must also specify yoyTimeUnit and yoyTimeValue.
        # - YOY_DOWN: year-over-year decrease. You must also specify yoyTimeUnit and yoyTimeValue.
        # - ABOVE_UPPER: dynamic baseline spike. You must specify sensitivity. When using a baseline operator, threshold is not used for evaluation. Set it to 0 as a placeholder.
        # - BELOW_LOWER: dynamic baseline drop. You must specify sensitivity. When using a baseline operator, threshold is not used for evaluation. Set it to 0 as a placeholder.
        # - OUT_OF_BAND: dynamic baseline bidirectional. You must specify sensitivity. When using a baseline operator, threshold is not used for evaluation. Set it to 0 as a placeholder.
        # 
        # This parameter is required.
        self.operator = operator
        # The dynamic baseline sensitivity. This parameter takes effect only when a baseline operator is used. Valid values:
        # - HIGH: The narrowest band and the most sensitive.
        # - MEDIUM: Medium sensitivity.
        # - LOW: The widest band and the least sensitive.
        self.sensitivity = sensitivity
        # The threshold.
        # 
        # This parameter is required.
        self.threshold = threshold
        # The year-over-year time unit. This parameter takes effect only when operator is set to YOY_UP or YOY_DOWN.
        self.yoy_time_unit = yoy_time_unit
        # The year-over-year time value. This parameter takes effect only when operator is set to YOY_UP or YOY_DOWN.
        self.yoy_time_value = yoy_time_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abs_deviation is not None:
            result['absDeviation'] = self.abs_deviation

        if self.aggregate is not None:
            result['aggregate'] = self.aggregate

        if self.baseline_period is not None:
            result['baselinePeriod'] = self.baseline_period

        if self.operator is not None:
            result['operator'] = self.operator

        if self.sensitivity is not None:
            result['sensitivity'] = self.sensitivity

        if self.threshold is not None:
            result['threshold'] = self.threshold

        if self.yoy_time_unit is not None:
            result['yoyTimeUnit'] = self.yoy_time_unit

        if self.yoy_time_value is not None:
            result['yoyTimeValue'] = self.yoy_time_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('absDeviation') is not None:
            self.abs_deviation = m.get('absDeviation')

        if m.get('aggregate') is not None:
            self.aggregate = m.get('aggregate')

        if m.get('baselinePeriod') is not None:
            self.baseline_period = m.get('baselinePeriod')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('sensitivity') is not None:
            self.sensitivity = m.get('sensitivity')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        if m.get('yoyTimeUnit') is not None:
            self.yoy_time_unit = m.get('yoyTimeUnit')

        if m.get('yoyTimeValue') is not None:
            self.yoy_time_value = m.get('yoyTimeValue')

        return self

