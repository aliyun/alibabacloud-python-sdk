# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class QueryAsyncTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryAsyncTaskResponseBodyData = None,
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
            temp_model = main_models.QueryAsyncTaskResponseBodyData()
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

class QueryAsyncTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_user: str = None,
        task_code: str = None,
        task_error_message: str = None,
        task_id: str = None,
        task_intermediate_result: str = None,
        task_name: str = None,
        task_param: str = None,
        task_progress_message: str = None,
        task_result: str = None,
        task_retry_count: str = None,
        task_status: int = None,
        update_time: str = None,
        update_user: str = None,
    ):
        self.create_time = create_time
        self.create_user = create_user
        self.task_code = task_code
        self.task_error_message = task_error_message
        self.task_id = task_id
        self.task_intermediate_result = task_intermediate_result
        self.task_name = task_name
        self.task_param = task_param
        self.task_progress_message = task_progress_message
        self.task_result = task_result
        self.task_retry_count = task_retry_count
        self.task_status = task_status
        self.update_time = update_time
        self.update_user = update_user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.task_code is not None:
            result['TaskCode'] = self.task_code

        if self.task_error_message is not None:
            result['TaskErrorMessage'] = self.task_error_message

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_intermediate_result is not None:
            result['TaskIntermediateResult'] = self.task_intermediate_result

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_param is not None:
            result['TaskParam'] = self.task_param

        if self.task_progress_message is not None:
            result['TaskProgressMessage'] = self.task_progress_message

        if self.task_result is not None:
            result['TaskResult'] = self.task_result

        if self.task_retry_count is not None:
            result['TaskRetryCount'] = self.task_retry_count

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_user is not None:
            result['UpdateUser'] = self.update_user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('TaskCode') is not None:
            self.task_code = m.get('TaskCode')

        if m.get('TaskErrorMessage') is not None:
            self.task_error_message = m.get('TaskErrorMessage')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskIntermediateResult') is not None:
            self.task_intermediate_result = m.get('TaskIntermediateResult')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskParam') is not None:
            self.task_param = m.get('TaskParam')

        if m.get('TaskProgressMessage') is not None:
            self.task_progress_message = m.get('TaskProgressMessage')

        if m.get('TaskResult') is not None:
            self.task_result = m.get('TaskResult')

        if m.get('TaskRetryCount') is not None:
            self.task_retry_count = m.get('TaskRetryCount')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateUser') is not None:
            self.update_user = m.get('UpdateUser')

        return self

