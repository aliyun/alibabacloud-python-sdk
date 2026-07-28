# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteResourceControlRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
        resource_control_name: str = None,
    ):
        # The database cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The region ID.
        self.region_id = region_id
        # The resource control name.
        # 
        # This parameter is required.
        self.resource_control_name = resource_control_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_control_name is not None:
            result['ResourceControlName'] = self.resource_control_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceControlName') is not None:
            self.resource_control_name = m.get('ResourceControlName')

        return self

