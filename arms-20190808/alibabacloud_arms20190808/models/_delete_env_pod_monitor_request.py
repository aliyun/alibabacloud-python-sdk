# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteEnvPodMonitorRequest(DaraModel):
    def __init__(
        self,
        environment_id: str = None,
        namespace: str = None,
        pod_monitor_name: str = None,
        region_id: str = None,
    ):
        # The ID of the environment instance.
        # 
        # This parameter is required.
        self.environment_id = environment_id
        # The namespace where the PodMonitor is located.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The name of the PodMonitor.
        # 
        # This parameter is required.
        self.pod_monitor_name = pod_monitor_name
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.pod_monitor_name is not None:
            result['PodMonitorName'] = self.pod_monitor_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('PodMonitorName') is not None:
            self.pod_monitor_name = m.get('PodMonitorName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

