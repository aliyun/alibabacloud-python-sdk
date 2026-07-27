# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CompareList(DaraModel):
    def __init__(
        self,
        aggregate: str = None,
        operator: str = None,
        threshold: float = None,
        yoy_time_unit: str = None,
        yoy_time_value: int = None,
    ):
        # This parameter is required.
        self.aggregate = aggregate
        # This parameter is required.
        self.operator = operator
        # This parameter is required.
        self.threshold = threshold
        self.yoy_time_unit = yoy_time_unit
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

