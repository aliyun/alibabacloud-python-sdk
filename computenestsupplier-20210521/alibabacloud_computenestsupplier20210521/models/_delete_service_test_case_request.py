# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteServiceTestCaseRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        test_case_id: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The ID of the service test case.
        # 
        # This parameter is required.
        self.test_case_id = test_case_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TestCaseId') is not None:
            self.test_case_id = m.get('TestCaseId')

        return self

