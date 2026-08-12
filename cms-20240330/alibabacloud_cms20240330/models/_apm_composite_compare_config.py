# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApmCompositeCompareConfig(DaraModel):
    def __init__(
        self,
        aggregate: str = None,
        operator: str = None,
        threshold: float = None,
        yoy_time_unit: str = None,
        yoy_time_value: int = None,
    ):
        # The aggregate functions used for aggregation.
        # 
        # This parameter is required.
        self.aggregate = aggregate
        # The comparison operator. GTE/LTE indicates greater than or equal to/less than or equal to. YOY_UP/YOY_DOWN indicates year-over-year increase/decrease, which requires yoyTimeUnit and yoyTimeValue to be specified.
        # 
        # This parameter is required.
        self.operator = operator
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
        if self.aggregate is not None:
            result['aggregate'] = self.aggregate

        if self.operator is not None:
            result['operator'] = self.operator

        if self.threshold is not None:
            result['threshold'] = self.threshold

        if self.yoy_time_unit is not None:
            result['yoyTimeUnit'] = self.yoy_time_unit

        if self.yoy_time_value is not None:
            result['yoyTimeValue'] = self.yoy_time_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggregate') is not None:
            self.aggregate = m.get('aggregate')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        if m.get('yoyTimeUnit') is not None:
            self.yoy_time_unit = m.get('yoyTimeUnit')

        if m.get('yoyTimeValue') is not None:
            self.yoy_time_value = m.get('yoyTimeValue')

        return self

