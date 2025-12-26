# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class GetNodeMetricsResponseBody(DaraModel):
    def __init__(
        self,
        metric_type: str = None,
        nodes_metrics: List[main_models.NodeMetric] = None,
        resource_group_id: str = None,
    ):
        self.metric_type = metric_type
        self.nodes_metrics = nodes_metrics
        self.resource_group_id = resource_group_id

    def validate(self):
        if self.nodes_metrics:
            for v1 in self.nodes_metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        result['NodesMetrics'] = []
        if self.nodes_metrics is not None:
            for k1 in self.nodes_metrics:
                result['NodesMetrics'].append(k1.to_map() if k1 else None)

        if self.resource_group_id is not None:
            result['ResourceGroupID'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        self.nodes_metrics = []
        if m.get('NodesMetrics') is not None:
            for k1 in m.get('NodesMetrics'):
                temp_model = main_models.NodeMetric()
                self.nodes_metrics.append(temp_model.from_map(k1))

        if m.get('ResourceGroupID') is not None:
            self.resource_group_id = m.get('ResourceGroupID')

        return self

