# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SwitchReplicationLinkRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        owner_id: int = None,
        target_instance_name: str = None,
        target_instance_region_id: str = None,
    ):
        # The ID of the source or primary instance.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id
        # The name of the destination DR instance.
        # 
        # This parameter is required.
        self.target_instance_name = target_instance_name
        # The ID of the region in which the destination DR instance resides.
        # 
        # This parameter is required.
        self.target_instance_region_id = target_instance_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.target_instance_name is not None:
            result['TargetInstanceName'] = self.target_instance_name

        if self.target_instance_region_id is not None:
            result['TargetInstanceRegionId'] = self.target_instance_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('TargetInstanceName') is not None:
            self.target_instance_name = m.get('TargetInstanceName')

        if m.get('TargetInstanceRegionId') is not None:
            self.target_instance_region_id = m.get('TargetInstanceRegionId')

        return self

