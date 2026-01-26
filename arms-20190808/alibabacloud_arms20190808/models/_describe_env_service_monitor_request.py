# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEnvServiceMonitorRequest(DaraModel):
    def __init__(
        self,
        environment_id: str = None,
        namespace: str = None,
        region_id: str = None,
        service_monitor_name: str = None,
    ):
        # The ID of the environment instance.
        # 
        # This parameter is required.
        self.environment_id = environment_id
        # The namespace where the ServiceMonitor resides.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the ServiceMonitor.
        # 
        # This parameter is required.
        self.service_monitor_name = service_monitor_name

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_monitor_name is not None:
            result['ServiceMonitorName'] = self.service_monitor_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceMonitorName') is not None:
            self.service_monitor_name = m.get('ServiceMonitorName')

        return self

