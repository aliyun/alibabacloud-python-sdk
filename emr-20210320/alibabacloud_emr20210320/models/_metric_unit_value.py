# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MetricUnitValue(DaraModel):
    def __init__(
        self,
        metric_name: str = None,
        metric_unit: str = None,
    ):
        # 指标名称。
        self.metric_name = metric_name
        # 指标单位。
        self.metric_unit = metric_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.metric_unit is not None:
            result['MetricUnit'] = self.metric_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('MetricUnit') is not None:
            self.metric_unit = m.get('MetricUnit')

        return self

