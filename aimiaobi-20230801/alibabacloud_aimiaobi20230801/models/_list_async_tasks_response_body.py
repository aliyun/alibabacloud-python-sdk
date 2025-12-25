# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class ListAsyncTasksResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        current: int = None,
        data: List[main_models.ListAsyncTasksResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        size: int = None,
        success: bool = None,
        total: int = None,
    ):
        self.code = code
        self.current = current
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.size = size
        self.success = success
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.current is not None:
            result['Current'] = self.current

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.size is not None:
            result['Size'] = self.size

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Current') is not None:
            self.current = m.get('Current')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAsyncTasksResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListAsyncTasksResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_user: str = None,
        id: int = None,
        task_code: str = None,
        task_definition: str = None,
        task_end_time: str = None,
        task_error_message: str = None,
        task_execute_time: str = None,
        task_id: str = None,
        task_inner_error_message: str = None,
        task_intermediate_result: str = None,
        task_name: str = None,
        task_param: str = None,
        task_progress_message: str = None,
        task_result: str = None,
        task_retry_count: str = None,
        task_start_time: str = None,
        task_status: int = None,
        task_type: str = None,
        update_time: str = None,
        update_user: str = None,
    ):
        self.create_time = create_time
        self.create_user = create_user
        self.id = id
        self.task_code = task_code
        self.task_definition = task_definition
        self.task_end_time = task_end_time
        self.task_error_message = task_error_message
        self.task_execute_time = task_execute_time
        self.task_id = task_id
        self.task_inner_error_message = task_inner_error_message
        self.task_intermediate_result = task_intermediate_result
        self.task_name = task_name
        self.task_param = task_param
        self.task_progress_message = task_progress_message
        self.task_result = task_result
        self.task_retry_count = task_retry_count
        self.task_start_time = task_start_time
        self.task_status = task_status
        self.task_type = task_type
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

        if self.id is not None:
            result['Id'] = self.id

        if self.task_code is not None:
            result['TaskCode'] = self.task_code

        if self.task_definition is not None:
            result['TaskDefinition'] = self.task_definition

        if self.task_end_time is not None:
            result['TaskEndTime'] = self.task_end_time

        if self.task_error_message is not None:
            result['TaskErrorMessage'] = self.task_error_message

        if self.task_execute_time is not None:
            result['TaskExecuteTime'] = self.task_execute_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_inner_error_message is not None:
            result['TaskInnerErrorMessage'] = self.task_inner_error_message

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

        if self.task_start_time is not None:
            result['TaskStartTime'] = self.task_start_time

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_type is not None:
            result['TaskType'] = self.task_type

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

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('TaskCode') is not None:
            self.task_code = m.get('TaskCode')

        if m.get('TaskDefinition') is not None:
            self.task_definition = m.get('TaskDefinition')

        if m.get('TaskEndTime') is not None:
            self.task_end_time = m.get('TaskEndTime')

        if m.get('TaskErrorMessage') is not None:
            self.task_error_message = m.get('TaskErrorMessage')

        if m.get('TaskExecuteTime') is not None:
            self.task_execute_time = m.get('TaskExecuteTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskInnerErrorMessage') is not None:
            self.task_inner_error_message = m.get('TaskInnerErrorMessage')

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

        if m.get('TaskStartTime') is not None:
            self.task_start_time = m.get('TaskStartTime')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateUser') is not None:
            self.update_user = m.get('UpdateUser')

        return self

