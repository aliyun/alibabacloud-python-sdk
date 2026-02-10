# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitOperationTaskResponseBody(DaraModel):
    def __init__(
        self,
        operate_code: str = None,
        request_id: str = None,
        root_task_id: str = None,
    ):
        # The handling result code. Valid values:
        # 
        # *   Insufficient authorization: AuthorizationExhaust
        # *   Unauthorized: ActionTrialUnauthorized
        self.operate_code = operate_code
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The main task ID that is returned when the task is submitted.
        self.root_task_id = root_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operate_code is not None:
            result['OperateCode'] = self.operate_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root_task_id is not None:
            result['RootTaskId'] = self.root_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateCode') is not None:
            self.operate_code = m.get('OperateCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootTaskId') is not None:
            self.root_task_id = m.get('RootTaskId')

        return self

