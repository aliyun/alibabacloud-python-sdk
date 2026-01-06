# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SparkOperatorInfo(DaraModel):
    def __init__(
        self,
        metric_value: int = None,
        operator_name: bytes = None,
    ):
        self.metric_value = metric_value
        self.operator_name = operator_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_value is not None:
            result['MetricValue'] = self.metric_value

        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricValue') is not None:
            self.metric_value = m.get('MetricValue')

        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')

        return self

