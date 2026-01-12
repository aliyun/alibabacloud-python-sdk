# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class JobReplicaStatus(DaraModel):
    def __init__(
        self,
        active: int = None,
        dequeued: int = None,
        estimated_auto_scaling_spec: main_models.AutoScalingSpec = None,
        estimated_pod_count: int = None,
        estimated_resource_config: main_models.ResourceConfig = None,
        queuing: int = None,
        type: str = None,
    ):
        self.active = active
        self.dequeued = dequeued
        self.estimated_auto_scaling_spec = estimated_auto_scaling_spec
        self.estimated_pod_count = estimated_pod_count
        self.estimated_resource_config = estimated_resource_config
        self.queuing = queuing
        self.type = type

    def validate(self):
        if self.estimated_auto_scaling_spec:
            self.estimated_auto_scaling_spec.validate()
        if self.estimated_resource_config:
            self.estimated_resource_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.dequeued is not None:
            result['Dequeued'] = self.dequeued

        if self.estimated_auto_scaling_spec is not None:
            result['EstimatedAutoScalingSpec'] = self.estimated_auto_scaling_spec.to_map()

        if self.estimated_pod_count is not None:
            result['EstimatedPodCount'] = self.estimated_pod_count

        if self.estimated_resource_config is not None:
            result['EstimatedResourceConfig'] = self.estimated_resource_config.to_map()

        if self.queuing is not None:
            result['Queuing'] = self.queuing

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('Dequeued') is not None:
            self.dequeued = m.get('Dequeued')

        if m.get('EstimatedAutoScalingSpec') is not None:
            temp_model = main_models.AutoScalingSpec()
            self.estimated_auto_scaling_spec = temp_model.from_map(m.get('EstimatedAutoScalingSpec'))

        if m.get('EstimatedPodCount') is not None:
            self.estimated_pod_count = m.get('EstimatedPodCount')

        if m.get('EstimatedResourceConfig') is not None:
            temp_model = main_models.ResourceConfig()
            self.estimated_resource_config = temp_model.from_map(m.get('EstimatedResourceConfig'))

        if m.get('Queuing') is not None:
            self.queuing = m.get('Queuing')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

