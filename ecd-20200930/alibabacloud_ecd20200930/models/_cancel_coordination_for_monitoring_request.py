# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CancelCoordinationForMonitoringRequest(DaraModel):
    def __init__(
        self,
        co_ids: List[str] = None,
        end_user_id: str = None,
        region_id: str = None,
        user_type: str = None,
    ):
        # The IDs of stream collaboration tasks.
        # 
        # This parameter is required.
        self.co_ids = co_ids
        # The ID of the end user that initiates stream collaboration. If the initiator is the administrator, skip this parameter.
        self.end_user_id = end_user_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/436773.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The type of the user.
        # 
        # Valid value:
        # 
        # * TENANT_ADMIN: administrator.
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.co_ids is not None:
            result['CoIds'] = self.co_ids

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoIds') is not None:
            self.co_ids = m.get('CoIds')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

