# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAutomateResponseConfigFeatureRequest(DaraModel):
    def __init__(
        self,
        auto_response_type: str = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
    ):
        # The type of automated response. Valid values:
        # 
        # - event: event
        # 
        # - alert: alert
        self.auto_response_type = auto_response_type
        # The region where the Data Management center of threat analysis is deployed. Select a region based on the location of your assets. Valid values:
        # 
        # - cn-hangzhou: Assets in the Chinese mainland and Hong Kong (China).
        # 
        # - ap-southeast-1: Assets outside China.
        self.region_id = region_id
        # The user ID of the member. An administrator can use this parameter to switch to the perspective of the member.
        self.role_for = role_for
        # The type of view. Valid values:
        # 
        # - 0: the view of the current Alibaba Cloud account.
        # 
        # - 1: the view of all accounts that are managed by the administrator account.
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_response_type is not None:
            result['AutoResponseType'] = self.auto_response_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoResponseType') is not None:
            self.auto_response_type = m.get('AutoResponseType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

