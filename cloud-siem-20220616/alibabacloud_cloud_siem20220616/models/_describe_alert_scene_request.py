# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAlertSceneRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
    ):
        # The region where the data management center of Threat Analysis is deployed. You must select the region where your assets are located. Valid values:
        # 
        # - cn-hangzhou: your assets are in the Chinese mainland or China (Hong Kong).
        # 
        # - ap-southeast-1: your assets are outside China.
        self.region_id = region_id
        # The user ID of the member. An administrator can use this ID to switch to the member\\"s perspective.
        self.role_for = role_for
        # The type of the view.
        # 
        # - 0: the view of the current Alibaba Cloud account.
        # 
        # - 1: the view of all accounts within the enterprise.
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

