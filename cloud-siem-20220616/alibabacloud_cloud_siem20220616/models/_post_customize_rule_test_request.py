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
        # The ID of the rule.
        self.id = id
        # The data management center of the threat analysis feature. Specify this parameter based on the region in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id
        # The ID of the account that you switch from the management account.
        self.role_for = role_for
        # The type of the view. Valid values:
        # - 0: the current Alibaba Cloud account
        # - 1: the global account
        self.role_type = role_type
        # The simulation data for the test. This parameter is available only when TestType is set to simulate.
        self.simulated_data = simulated_data
        # The test type. Valid values:
        # 
        # *   simulate: simulation data test
        # *   business: business data test
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

