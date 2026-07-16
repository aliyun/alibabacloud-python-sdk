# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachTaskRequest(DaraModel):
    def __init__(
        self,
        call_string: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: int = None,
    ):
        # The calling string (callee information and parameter list). Valid values:
        # 
        # - **LIST**: Use this type when the script has no input variables. In this case, only the callee numbers need to be provided. Example: `0571****5678,0571****5679`.
        # - **JSON**: Use this type when the script includes input variables. You must provide the variable names, callee numbers, and variable values. Example: `{"ParamNames":["name","age"],"CalleeList":[{"Callee":"181****0000","Params":["Zhang San","20"]},{"Callee":"181****0001","Params":["Li Si","21"]}]}`. **ParamNames** represents the list of parameter names; **Params** represents the list of parameter values.
        # 
        # > You can view the script input variables on the [**Script Management**](https://aiccs.console.aliyun.com/patter/list) > **View** > **Input and Output Parameters** interface.
        self.call_string = call_string
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The job ID. You can obtain the job ID from the [Task Management](https://aiccs.console.aliyun.com/job/list) interface.
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
        if self.call_string is not None:
            result['CallString'] = self.call_string

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallString') is not None:
            self.call_string = m.get('CallString')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

