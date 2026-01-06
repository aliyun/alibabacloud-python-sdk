# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyVirtualClusterRequest(DaraModel):
    def __init__(
        self,
        active_cluster_id: str = None,
        dbcluster_id: str = None,
        dbinstance_id: str = None,
        region_id: str = None,
        standby_cluster_id: str = None,
    ):
        self.active_cluster_id = active_cluster_id
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is required.
        self.region_id = region_id
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

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

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

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StandbyClusterId') is not None:
            self.standby_cluster_id = m.get('StandbyClusterId')

        return self

