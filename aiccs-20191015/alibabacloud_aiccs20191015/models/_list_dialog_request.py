# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDialogRequest(DaraModel):
    def __init__(
        self,
        called: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: int = None,
    ):
        # The called number. You can view the called number in the [**Task Management**](https://aiccs.console.aliyun.com/job/list) > **Details** interface or retrieve it by invoking the [ListTaskDetail](https://help.aliyun.com/document_detail/2718009.html) API. The **Called** parameter in the API response is the called number.
        # 
        # This parameter is required.
        self.called = called
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The unique job ID of the robot outbound call task. You can view it in the [Task Management](https://aiccs.console.aliyun.com/job/list) interface or obtain it by invoking the [CreateTask](https://help.aliyun.com/document_detail/223556.html) API.
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
        if self.called is not None:
            result['Called'] = self.called

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
        if m.get('Called') is not None:
            self.called = m.get('Called')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

