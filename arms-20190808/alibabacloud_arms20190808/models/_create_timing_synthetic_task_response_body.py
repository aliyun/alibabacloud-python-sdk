# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class CreateTimingSyntheticTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.CreateTimingSyntheticTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned. The status code 200 indicates that the request was successful.
        self.code = code
        # The struct returned.
        self.data = data
        # The message returned.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: true and false.
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
            temp_model = main_models.CreateTimingSyntheticTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateTimingSyntheticTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        status: str = None,
        task_id: str = None,
    ):
        # The task status. Valid values:
        # 
        # - INIT: The task is in the initial state.
        # - RELEASE: The task is being parsed.
        # - RUNNING: The task is running.
        # - STOP: The task is suspended.
        # - SYSTEM_STOP: The task is suspended by the system.
        # - CANCEL: The task is canceled.
        # - SYSTEM_CANCEL: The task is canceled by the system.
        # - DONE: The task is complete.
        self.status = status
        # The ID of the synthetic monitoring task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

