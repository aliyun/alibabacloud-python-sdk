# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyTaskInfoRequest(DaraModel):
    def __init__(
        self,
        action_params: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        step_name: str = None,
        task_action: str = None,
        task_id: str = None,
    ):
        # A action-related parameter. This parameter can be extended based on your business requirements. This parameter value varies with the value of the TaskAction parameter.
        self.action_params = action_params
        # The region ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the step visible to the user.
        # 
        # This parameter is required.
        self.step_name = step_name
        # The action name that corresponds to the state described in the actionInfo parameter of the [DescribeHistoryTasks](https://help.aliyun.com/document_detail/2639186.html) operation.
        # 
        # This parameter is required.
        self.task_action = task_action
        # The task ID. Separate multiple IDs with commas (,). You can specify up to 10 task IDs.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_params is not None:
            result['ActionParams'] = self.action_params

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.step_name is not None:
            result['StepName'] = self.step_name

        if self.task_action is not None:
            result['TaskAction'] = self.task_action

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionParams') is not None:
            self.action_params = m.get('ActionParams')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')

        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

