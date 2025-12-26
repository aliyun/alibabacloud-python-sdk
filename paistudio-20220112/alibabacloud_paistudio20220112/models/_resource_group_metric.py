# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class ResourceGroupMetric(DaraModel):
    def __init__(
        self,
        gpu_type: str = None,
        metrics: List[main_models.Metric] = None,
        resource_group_id: str = None,
    ):
        self.gpu_type = gpu_type
        self.metrics = metrics
        self.resource_group_id = resource_group_id

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
        if self.gpu_type is not None:
            result['GpuType'] = self.gpu_type

        result['Metrics'] = []
        if self.metrics is not None:
            for k1 in self.metrics:
                result['Metrics'].append(k1.to_map() if k1 else None)

        if self.resource_group_id is not None:
            result['ResourceGroupID'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GpuType') is not None:
            self.gpu_type = m.get('GpuType')

        self.metrics = []
        if m.get('Metrics') is not None:
            for k1 in m.get('Metrics'):
                temp_model = main_models.Metric()
                self.metrics.append(temp_model.from_map(k1))

        if m.get('ResourceGroupID') is not None:
            self.resource_group_id = m.get('ResourceGroupID')

        return self

