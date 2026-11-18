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
        security_token: str = None,
        step_name: str = None,
        task_action: str = None,
        task_id: str = None,
    ):
        # The parameters related to the action, in JSON format.
        # If **TaskAction** is set to **modifySwitchTime**, set this parameter to `{"recoverMode": "xxx", "recoverTime": "xxx"}`.
        # * **recoverMode**: the recovery mode of the task. Valid values:
        #   * **imePoint**: executes the task at a specified point in time.
        #   * **immediate**: executes the task immediately.
        #   * **maintainTime**: executes the task during the O&M window.
        # 
        # * **recoverTime**: the specified point in time. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. This parameter is required when **recoverMode** is set to **timePoint**.
        self.action_params = action_params
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The name of the current execution step. You can call the [DescribeHistoryTasks](https://help.aliyun.com/document_detail/2400077.html) operation to query the current execution step of a specified task. A common value is **do_pause**, which indicates that the task is waiting to be executed at a preset time.
        self.step_name = step_name
        # The operation name. Valid value: **modifySwitchTime**, which indicates modifying the switchover time or recovery time.
        self.task_action = task_action
        # The task ID. Separate multiple task IDs with commas (,). A maximum of 30 task IDs are supported.
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

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

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

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')

        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

