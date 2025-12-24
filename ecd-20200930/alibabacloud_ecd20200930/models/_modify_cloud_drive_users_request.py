# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyCloudDriveUsersRequest(DaraModel):
    def __init__(
        self,
        cds_id: str = None,
        end_user_id: List[str] = None,
        region_id: str = None,
        status: str = None,
        user_max_size: int = None,
    ):
        # This parameter is required.
        self.cds_id = cds_id
        # This parameter is required.
        self.end_user_id = end_user_id
        # This parameter is required.
        self.region_id = region_id
        # The status of Cloud Drive Service users.
        # 
        # Valid values:
        # 
        # *   disabled
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     unavailable
        # 
        #     <!-- -->
        # 
        # *   enabled
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     available
        # 
        #     <!-- -->
        self.status = status
        # The maximum storage space of a user. Unit: bytes.
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

        if self.status is not None:
            result['Status'] = self.status

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserMaxSize') is not None:
            self.user_max_size = m.get('UserMaxSize')

        return self

