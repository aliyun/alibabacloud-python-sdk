# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PostFinishCustomizeRuleTestRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
    ):
        # The ID of the custom rule.
        self.id = id
        # The region of the data management center for Threat Analysis. You must select the region of the management center based on the region where your assets are deployed. Valid values:
        # - cn-hangzhou: Assets are located in the Chinese mainland and Hong Kong (China).
        # - ap-southeast-1: Assets are located in regions outside China.
        self.region_id = region_id
        # The ID of the user whose perspective the administrator switches to.
        self.role_for = role_for
        # The view type. Valid values:
        # - 0: The view of the current Alibaba Cloud account.
        # - 1: The view of all accounts in the enterprise.
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

