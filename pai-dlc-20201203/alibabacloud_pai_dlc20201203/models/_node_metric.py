# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class NodeMetric(DaraModel):
    def __init__(
        self,
        metrics: List[main_models.Metric] = None,
        node_name: str = None,
    ):
        self.metrics = metrics
        self.node_name = node_name

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

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metrics = []
        if m.get('Metrics') is not None:
            for k1 in m.get('Metrics'):
                temp_model = main_models.Metric()
                self.metrics.append(temp_model.from_map(k1))

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        return self

