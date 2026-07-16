# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PostCustomizeRuleTestRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
        simulated_data: str = None,
        test_type: str = None,
    ):
        # The ID of the custom rule.
        self.id = id
        # The region where the Data Management center of threat analysis is located. Select the region based on the region where your assets are located. Valid values:
        # 
        # - cn-hangzhou: Your assets are in the Chinese mainland or China (Hong Kong).
        # 
        # - ap-southeast-1: Your assets are in regions outside China.
        self.region_id = region_id
        # The user ID of the member that the administrator wants to impersonate to view data.
        self.role_for = role_for
        # The view type.
        # 
        # - 0: the view of the current Alibaba Cloud account.
        # 
        # - 1: the view of all accounts in the enterprise.
        self.role_type = role_type
        # The simulated data for the test. This parameter is required only when TestType is set to simulate.
        self.simulated_data = simulated_data
        # The test type. Valid values:
        # 
        # - simulate: tests the rule with simulated data
        # 
        # - business: tests the rule with business data
        self.test_type = test_type

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

        if self.simulated_data is not None:
            result['SimulatedData'] = self.simulated_data

        if self.test_type is not None:
            result['TestType'] = self.test_type

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

        if m.get('SimulatedData') is not None:
            self.simulated_data = m.get('SimulatedData')

        if m.get('TestType') is not None:
            self.test_type = m.get('TestType')

        return self

