# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetStorageRequest(DaraModel):
    def __init__(
        self,
        region: str = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
        ttl: int = None,
    ):
        # The log storage region.
        # 
        # If the Data Management center is in cn-hangzhou, the default value of Region is **cn-shanghai**. If the Data Management center is in **ap-southeast-1**, the default value of **Region** is **ap-southeast-1**.
        # 
        # The log storage region cannot be changed. To change the region, contact the Threat Analysis operations team.
        self.region = region
        # The region of the Data Management center for Threat Analysis. Select the region for the Data Management center based on the region of your assets. Valid values:
        # 
        # - cn-hangzhou: Select this value if your assets are in the Chinese mainland or China (Hong Kong).
        # 
        # - ap-southeast-1: Select this value if your assets are in a region outside the Chinese mainland.
        self.region_id = region_id
        # The user ID of the member. An administrator can use this parameter to switch to the view of a specific member.
        self.role_for = role_for
        # The type of the view.
        # 
        # - 0: The view of the current Alibaba Cloud account.
        # 
        # - 1: The view of all accounts in your enterprise.
        self.role_type = role_type
        # The log storage duration in days. The default value is 180. The minimum value is 30 and the maximum value is 3000.
        # 
        # This parameter is required.
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region is not None:
            result['Region'] = self.region

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

