# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class GetRenderingProjectInstanceStateMetricsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        state_metrics: List[main_models.GetRenderingProjectInstanceStateMetricsResponseBodyStateMetrics] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.state_metrics = state_metrics

    def validate(self):
        if self.state_metrics:
            for v1 in self.state_metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StateMetrics'] = []
        if self.state_metrics is not None:
            for k1 in self.state_metrics:
                result['StateMetrics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.state_metrics = []
        if m.get('StateMetrics') is not None:
            for k1 in m.get('StateMetrics'):
                temp_model = main_models.GetRenderingProjectInstanceStateMetricsResponseBodyStateMetrics()
                self.state_metrics.append(temp_model.from_map(k1))

        return self

class GetRenderingProjectInstanceStateMetricsResponseBodyStateMetrics(DaraModel):
    def __init__(
        self,
        count: str = None,
        state: str = None,
    ):
        self.count = count
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

