# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateServiceTestTaskRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        task_name: str = None,
        task_region_id: str = None,
        test_case_ids: List[str] = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The name of the task.
        # 
        # This parameter is required.
        self.task_name = task_name
        # The Task Execution Region
        self.task_region_id = task_region_id
        # The service test case ids.
        # 
        # This parameter is required.
        self.test_case_ids = test_case_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_region_id is not None:
            result['TaskRegionId'] = self.task_region_id

        if self.test_case_ids is not None:
            result['TestCaseIds'] = self.test_case_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskRegionId') is not None:
            self.task_region_id = m.get('TaskRegionId')

        if m.get('TestCaseIds') is not None:
            self.test_case_ids = m.get('TestCaseIds')

        return self

