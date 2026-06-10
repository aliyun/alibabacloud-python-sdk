# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteCloudDriveUsersRequest(DaraModel):
    def __init__(
        self,
        cds_id: str = None,
        end_user_id: List[str] = None,
        region_id: str = None,
    ):
        # WUYING Workspace ID.
        # 
        # This parameter is required.
        self.cds_id = cds_id
        # List of end user IDs.
        self.end_user_id = end_user_id
        # Region ID. You can invoke [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to obtain the list of regions supported by WUYING Workspace.
        # 
        # This parameter is required.
        self.region_id = region_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdsId') is not None:
            self.cds_id = m.get('CdsId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

