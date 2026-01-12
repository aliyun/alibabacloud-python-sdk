# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AutoscalingMetricSpec(DaraModel):
    def __init__(
        self,
        metric_name: str = None,
        target_value: int = None,
    ):
        self.metric_name = metric_name
        self.target_value = target_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.target_value is not None:
            result['TargetValue'] = self.target_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')

        return self

