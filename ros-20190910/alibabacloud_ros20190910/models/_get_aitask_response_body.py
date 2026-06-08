# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetAITaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        status_reason: str = None,
        success: str = None,
        task_id: str = None,
        task_output: Dict[str, Any] = None,
        task_type: str = None,
    ):
        # The error code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The state of the AI task.
        # 
        # *   PENDING
        # *   WAITING
        # *   RUNNING
        # *   SUCCESS
        # *   FAILURE
        self.status = status
        # The reason why the AI task is in the state.
        self.status_reason = status_reason
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The ID of the AI task.
        self.task_id = task_id
        # The outputs of the AI task. The outputs include the template.
        # 
        # *
        self.task_output = task_output
        # The type of the AI task.
        # 
        # *   GenerateTemplate: The AI task is used to generate a template.
        # *   FixTemplate: The AI task is used to fix a template.
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
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason

        if self.success is not None:
            result['Success'] = self.success

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_output is not None:
            result['TaskOutput'] = self.task_output

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskOutput') is not None:
            self.task_output = m.get('TaskOutput')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

