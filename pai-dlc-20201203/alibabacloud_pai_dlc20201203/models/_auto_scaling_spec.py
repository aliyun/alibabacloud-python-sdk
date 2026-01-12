# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class AutoScalingSpec(DaraModel):
    def __init__(
        self,
        autoscaling_metric_spec: main_models.AutoscalingMetricSpec = None,
        max_replicas: int = None,
        min_replicas: int = None,
        pods_to_delete: List[str] = None,
        scaling_strategy: str = None,
    ):
        self.autoscaling_metric_spec = autoscaling_metric_spec
        self.max_replicas = max_replicas
        self.min_replicas = min_replicas
        self.pods_to_delete = pods_to_delete
        self.scaling_strategy = scaling_strategy

    def validate(self):
        if self.autoscaling_metric_spec:
            self.autoscaling_metric_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.autoscaling_metric_spec is not None:
            result['AutoscalingMetricSpec'] = self.autoscaling_metric_spec.to_map()

        if self.max_replicas is not None:
            result['MaxReplicas'] = self.max_replicas

        if self.min_replicas is not None:
            result['MinReplicas'] = self.min_replicas

        if self.pods_to_delete is not None:
            result['PodsToDelete'] = self.pods_to_delete

        if self.scaling_strategy is not None:
            result['ScalingStrategy'] = self.scaling_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoscalingMetricSpec') is not None:
            temp_model = main_models.AutoscalingMetricSpec()
            self.autoscaling_metric_spec = temp_model.from_map(m.get('AutoscalingMetricSpec'))

        if m.get('MaxReplicas') is not None:
            self.max_replicas = m.get('MaxReplicas')

        if m.get('MinReplicas') is not None:
            self.min_replicas = m.get('MinReplicas')

        if m.get('PodsToDelete') is not None:
            self.pods_to_delete = m.get('PodsToDelete')

        if m.get('ScalingStrategy') is not None:
            self.scaling_strategy = m.get('ScalingStrategy')

        return self

