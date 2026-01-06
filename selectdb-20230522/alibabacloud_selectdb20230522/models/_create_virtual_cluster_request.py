# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVirtualClusterRequest(DaraModel):
    def __init__(
        self,
        active_cluster_id: str = None,
        cluster_name: str = None,
        dbinstance_id: str = None,
        region_id: str = None,
        standby_cluster_id: str = None,
    ):
        # This parameter is required.
        self.active_cluster_id = active_cluster_id
        # This parameter is required.
        self.cluster_name = cluster_name
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.standby_cluster_id = standby_cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_cluster_id is not None:
            result['ActiveClusterId'] = self.active_cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.standby_cluster_id is not None:
            result['StandbyClusterId'] = self.standby_cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveClusterId') is not None:
            self.active_cluster_id = m.get('ActiveClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StandbyClusterId') is not None:
            self.standby_cluster_id = m.get('StandbyClusterId')

        return self

