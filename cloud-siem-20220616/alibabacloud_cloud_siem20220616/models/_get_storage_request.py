# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetStorageRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
    ):
        # The region where the Data Management hub for threat analysis is located. Select a region for the management hub based on the region of your assets. Valid values:
        # 
        # - cn-hangzhou: Select this value if your assets are in the Chinese mainland or the China (Hong Kong) region.
        # 
        # - ap-southeast-1: Select this value if your assets are in a region outside China.
        self.region_id = region_id
        # The user ID of the member. This parameter is used by an administrator to switch to the perspective of a member.
        self.role_for = role_for
        # The type of the view. Valid values:
        # 
        # - 0: The view of the current Alibaba Cloud account.
        # 
        # - 1: The view of all accounts that belong to the enterprise.
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

