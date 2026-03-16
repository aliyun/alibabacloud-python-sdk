# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReportTaskFailedRequest(DaraModel):
    def __init__(
        self,
        cause: str = None,
        error: str = None,
        task_token: str = None,
    ):
        # The cause of the failure. The value must be 1 to 4,096 characters in length.
        self.cause = cause
        # The error code for the failed task. The error code must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.error = error
        # The token of the task whose execution you want to report. The task token is passed to the called service, such as Message Service (MNS) or Function Compute. For MNS, the value of this parameter can be obtained from a message. For Function Compute, the value of this parameter can be obtained from an event. For more information, see [Service integration modes](https://help.aliyun.com/document_detail/2592915.html).
        # 
        # This parameter is required.
        self.task_token = task_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cause is not None:
            result['Cause'] = self.cause

        if self.error is not None:
            result['Error'] = self.error

        if self.task_token is not None:
            result['TaskToken'] = self.task_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cause') is not None:
            self.cause = m.get('Cause')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('TaskToken') is not None:
            self.task_token = m.get('TaskToken')

        return self

