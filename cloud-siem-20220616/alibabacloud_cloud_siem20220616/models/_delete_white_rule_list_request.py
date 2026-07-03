# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteWhiteRuleListRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
    ):
        # The unique ID of the whitelist rule.
        # 
        # This parameter is required.
        self.id = id
        # The region of the data management center for threat analysis. Select a region based on the location of your assets. Valid values:
        # 
        # - cn-hangzhou: The assets are in the Chinese mainland or China (Hong Kong).
        # 
        # - ap-southeast-1: The assets are in a region outside China.
        self.region_id = region_id
        # The user ID of a member. An administrator can switch to the perspective of the member.
        self.role_for = role_for
        # The view type.
        # 
        # - 0: The view for the current Alibaba Cloud account.
        # 
        # - 1: The view for all accounts in the enterprise.
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

