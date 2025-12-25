# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetApprovalDetailRequest(DaraModel):
    def __init__(
        self,
        tid: int = None,
        workflow_instance_id: int = None,
    ):
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) operation to obtain the tenant ID.
        self.tid = tid
        # The ID of the approval process. You can call the [GetOrderBaseInfo](https://help.aliyun.com/document_detail/144642.html) operation to obtain the ID of the approval process.
        # 
        # This parameter is required.
        self.workflow_instance_id = workflow_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tid is not None:
            result['Tid'] = self.tid

        if self.workflow_instance_id is not None:
            result['WorkflowInstanceId'] = self.workflow_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('WorkflowInstanceId') is not None:
            self.workflow_instance_id = m.get('WorkflowInstanceId')

        return self

