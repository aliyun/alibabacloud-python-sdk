# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateBatchTaskRequest(DaraModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        param: str = None,
        region_id: str = None,
        task_name: str = None,
        task_type: str = None,
    ):
        # This parameter is required.
        self.instance_ids = instance_ids
        self.param = param
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.task_name = task_name
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.param is not None:
            result['Param'] = self.param

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Param') is not None:
            self.param = m.get('Param')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

