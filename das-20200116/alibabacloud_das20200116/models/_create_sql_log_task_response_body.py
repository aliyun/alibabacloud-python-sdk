# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class CreateSqlLogTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateSqlLogTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The response code.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        # 
        # >  If the request was successful, **Successful** is returned. If the request failed, error information such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
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
            temp_model = main_models.CreateSqlLogTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateSqlLogTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        end: int = None,
        instance_id: str = None,
        name: str = None,
        start: int = None,
        status: str = None,
        task_id: str = None,
    ):
        # The time when the task was created. This value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time
        # The end of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.end = end
        # The ID of the database instance.
        self.instance_id = instance_id
        # The name of the task.
        self.name = name
        # The beginning of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start = start
        # The state of the task. Valid values:
        # 
        # *   **INIT**: The task is to be scheduled.
        # *   **RUNNING**: The task is running.
        # *   **FAILED**: The task failed.
        # *   **CANCELED**: The task is canceled.
        # *   **COMPLETED**: The task is complete.
        # 
        # >  You can view the result of a task that is in the **COMPLETED** state.
        self.status = status
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.end is not None:
            result['End'] = self.end

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.start is not None:
            result['Start'] = self.start

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

