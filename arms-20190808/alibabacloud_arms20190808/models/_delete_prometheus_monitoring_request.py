# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeletePrometheusMonitoringRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        monitoring_name: str = None,
        region_id: str = None,
        type: str = None,
    ):
        # The ID of the Prometheus instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The name of the monitoring configuration.
        # 
        # This parameter is required.
        self.monitoring_name = monitoring_name
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The type of the monitoring configuration. 
        # Valid values for a Prometheus instance for Container Service: serviceMonitor, podMonitor, customJob, and probe. 
        # Valid values for a Prometheus instance for ECS: customJob and probe.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.monitoring_name is not None:
            result['MonitoringName'] = self.monitoring_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('MonitoringName') is not None:
            self.monitoring_name = m.get('MonitoringName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

