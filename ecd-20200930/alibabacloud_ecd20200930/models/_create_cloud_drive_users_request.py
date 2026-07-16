# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateCloudDriveUsersRequest(DaraModel):
    def __init__(
        self,
        cds_id: str = None,
        end_user_id: List[str] = None,
        region_id: str = None,
        user_max_size: int = None,
    ):
        # Enterprise cloud drive ID.
        # 
        # This parameter is required.
        self.cds_id = cds_id
        # List of end user IDs.
        # 
        # This parameter is required.
        self.end_user_id = end_user_id
        # The ID of the region. You can call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to obtain a list of regions supported by WUYING Workspace.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Maximum storage size for a user\\"s personal cloud drive. This value must not exceed the remaining available capacity in the enterprise cloud drive. Unit: byte.
        # 
        # This parameter is required.
        self.user_max_size = user_max_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cds_id is not None:
            result['CdsId'] = self.cds_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_max_size is not None:
            result['UserMaxSize'] = self.user_max_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdsId') is not None:
            self.cds_id = m.get('CdsId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserMaxSize') is not None:
            self.user_max_size = m.get('UserMaxSize')

        return self

