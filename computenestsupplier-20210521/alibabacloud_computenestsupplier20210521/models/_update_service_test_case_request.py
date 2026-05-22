# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateServiceTestCaseRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        test_case_id: str = None,
        test_case_name: str = None,
        test_config: str = None,
    ):
        # Region ID.
        self.region_id = region_id
        # Service test case ID
        # 
        # This parameter is required.
        self.test_case_id = test_case_id
        # Test case name
        # 
        # This parameter is required.
        self.test_case_name = test_case_name
        # Test configuration
        # 
        # This parameter is required.
        self.test_config = test_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.test_case_id is not None:
            result['TestCaseId'] = self.test_case_id

        if self.test_case_name is not None:
            result['TestCaseName'] = self.test_case_name

        if self.test_config is not None:
            result['TestConfig'] = self.test_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TestCaseId') is not None:
            self.test_case_id = m.get('TestCaseId')

        if m.get('TestCaseName') is not None:
            self.test_case_name = m.get('TestCaseName')

        if m.get('TestConfig') is not None:
            self.test_config = m.get('TestConfig')

        return self

