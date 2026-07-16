# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBatchTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        application_type: str = None,
        instance_ids_shrink: str = None,
        param: str = None,
        region_id: str = None,
        task_name: str = None,
        task_type: str = None,
    ):
        self.application_type = application_type
        # The instance IDs.
        # 
        # This parameter is required.
        self.instance_ids_shrink = instance_ids_shrink
        # The task parameters.
        self.param = param
        # The region ID.
        # 
        # > Call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query the regions of all clusters in your account.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the batch task.
        # 
        # This parameter is required.
        self.task_name = task_name
        # The task type.
        # 
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink

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
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')

        if m.get('Param') is not None:
            self.param = m.get('Param')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

