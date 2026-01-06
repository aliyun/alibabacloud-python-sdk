# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDBClusterBindingRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbcluster_id_bak: str = None,
        dbinstance_id: str = None,
        region_id: str = None,
    ):
        # The ID of Cluster 1.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The ID of Cluster 2.
        # 
        # This parameter is required.
        self.dbcluster_id_bak = dbcluster_id_bak
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbcluster_id_bak is not None:
            result['DBClusterIdBak'] = self.dbcluster_id_bak

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBClusterIdBak') is not None:
            self.dbcluster_id_bak = m.get('DBClusterIdBak')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

