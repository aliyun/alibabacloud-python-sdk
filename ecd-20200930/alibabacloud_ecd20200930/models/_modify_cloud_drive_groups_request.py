# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyCloudDriveGroupsRequest(DaraModel):
    def __init__(
        self,
        cds_id: str = None,
        group_id: List[str] = None,
        region_id: str = None,
        status: str = None,
        total_size: int = None,
    ):
        # The ID of the cloud disk in Cloud Drive Service.
        # 
        # This parameter is required.
        self.cds_id = cds_id
        # The IDs of the teams.
        self.group_id = group_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The status of the team space. Valid values:
        # 
        # *   enabled
        # *   disabled
        # 
        # Default value: enabled.
        self.status = status
        # The total capacity of the team space.
        self.total_size = total_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cds_id is not None:
            result['CdsId'] = self.cds_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdsId') is not None:
            self.cds_id = m.get('CdsId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

