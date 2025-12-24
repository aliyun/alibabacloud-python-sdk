# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateCloudDriveGroupRequest(DaraModel):
    def __init__(
        self,
        admin_user_ids: List[str] = None,
        cds_id: str = None,
        group_id: str = None,
        region_id: str = None,
        total_size: int = None,
    ):
        self.admin_user_ids = admin_user_ids
        # The ID of the cloud disk in Cloud Drive Service.
        # 
        # This parameter is required.
        self.cds_id = cds_id
        # The ID of the team.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The size of the cloud disk in Cloud Drive Service. Unit: bytes. The size is unlimited.
        # 
        # This parameter is required.
        self.total_size = total_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_user_ids is not None:
            result['AdminUserIds'] = self.admin_user_ids

        if self.cds_id is not None:
            result['CdsId'] = self.cds_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminUserIds') is not None:
            self.admin_user_ids = m.get('AdminUserIds')

        if m.get('CdsId') is not None:
            self.cds_id = m.get('CdsId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

