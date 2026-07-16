# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentteams20260605 import models as main_models
from darabonba.model import DaraModel

class UpdateInstanceAsyncTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateInstanceAsyncTaskResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.UpdateInstanceAsyncTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateInstanceAsyncTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        current_step: str = None,
        modified_at: str = None,
        task_code: str = None,
        task_id: str = None,
        task_status: str = None,
        waiting_for_user_action: bool = None,
    ):
        self.created_at = created_at
        self.current_step = current_step
        self.modified_at = modified_at
        self.task_code = task_code
        self.task_id = task_id
        self.task_status = task_status
        self.waiting_for_user_action = waiting_for_user_action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.current_step is not None:
            result['CurrentStep'] = self.current_step

        if self.modified_at is not None:
            result['ModifiedAt'] = self.modified_at

        if self.task_code is not None:
            result['TaskCode'] = self.task_code

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.waiting_for_user_action is not None:
            result['WaitingForUserAction'] = self.waiting_for_user_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('CurrentStep') is not None:
            self.current_step = m.get('CurrentStep')

        if m.get('ModifiedAt') is not None:
            self.modified_at = m.get('ModifiedAt')

        if m.get('TaskCode') is not None:
            self.task_code = m.get('TaskCode')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('WaitingForUserAction') is not None:
            self.waiting_for_user_action = m.get('WaitingForUserAction')

        return self

