# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindPrometheusGrafanaInstanceRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        grafana_instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the Prometheus instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The ID of the Grafana workspace.
        # 
        # This parameter is required.
        self.grafana_instance_id = grafana_instance_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the Prometheus instance belongs.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.grafana_instance_id is not None:
            result['GrafanaInstanceId'] = self.grafana_instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('GrafanaInstanceId') is not None:
            self.grafana_instance_id = m.get('GrafanaInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

