# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReportTaskSucceededRequest(DaraModel):
    def __init__(
        self,
        output: str = None,
        task_token: str = None,
    ):
        # The output information of the task whose execution success you want to report.
        # 
        # This parameter is required.
        self.output = output
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
        if self.output is not None:
            result['Output'] = self.output

        if self.task_token is not None:
            result['TaskToken'] = self.task_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('TaskToken') is not None:
            self.task_token = m.get('TaskToken')

        return self

