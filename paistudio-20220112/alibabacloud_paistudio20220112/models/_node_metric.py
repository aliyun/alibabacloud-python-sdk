# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class NodeMetric(DaraModel):
    def __init__(
        self,
        gputype: str = None,
        metrics: List[main_models.Metric] = None,
        node_id: str = None,
    ):
        self.gputype = gputype
        self.metrics = metrics
        self.node_id = node_id

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
        if self.gputype is not None:
            result['GPUType'] = self.gputype

        result['Metrics'] = []
        if self.metrics is not None:
            for k1 in self.metrics:
                result['Metrics'].append(k1.to_map() if k1 else None)

        if self.node_id is not None:
            result['NodeID'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')

        self.metrics = []
        if m.get('Metrics') is not None:
            for k1 in m.get('Metrics'):
                temp_model = main_models.Metric()
                self.metrics.append(temp_model.from_map(k1))

        if m.get('NodeID') is not None:
            self.node_id = m.get('NodeID')

        return self

