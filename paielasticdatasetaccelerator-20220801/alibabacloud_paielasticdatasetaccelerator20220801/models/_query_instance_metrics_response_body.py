# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paielasticdatasetaccelerator20220801 import models as main_models
from darabonba.model import DaraModel

class QueryInstanceMetricsResponseBody(DaraModel):
    def __init__(
        self,
        metrics: List[main_models.Metric] = None,
        period: str = None,
        request_id: str = None,
    ):
        self.metrics = metrics
        self.period = period
        # This parameter is required.
        self.request_id = request_id

    def validate(self):
        if self.metrics:
            for v1 in self.metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Metrics'] = []
        if self.metrics is not None:
            for k1 in self.metrics:
                result['Metrics'].append(k1.to_map() if k1 else None)

        if self.period is not None:
            result['Period'] = self.period

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metrics = []
        if m.get('Metrics') is not None:
            for k1 in m.get('Metrics'):
                temp_model = main_models.Metric()
                self.metrics.append(temp_model.from_map(k1))

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

