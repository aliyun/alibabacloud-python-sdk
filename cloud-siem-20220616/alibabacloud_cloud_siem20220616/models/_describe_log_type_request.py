# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLogTypeRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
    ):
        # The region of the Data Management center. Select a region based on where your assets are located. Valid values:
        # 
        # - cn-hangzhou: for assets in the Chinese mainland and China (Hong Kong)
        # 
        # - ap-southeast-1: for assets in regions outside China
        self.region_id = region_id
        # The user ID of the member. An administrator can use this parameter to switch to the perspective of a specific member.
        self.role_for = role_for
        # The type of the view. Valid values:
        # 
        # - 0: The view of the current Alibaba Cloud account.
        # 
        # - 1: The view of all accounts in an enterprise.
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

