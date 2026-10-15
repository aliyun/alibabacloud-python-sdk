# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class EcomVideoRecreationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.EcomVideoRecreationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The result code. A value of `success` indicates success. If the call fails, the corresponding error code is returned.
        self.code = code
        # The submission result of the asynchronous task.
        self.data = data
        # The return message. If the call fails, an error description is returned.
        self.message = message
        # The request ID, which is used to identify a unique call.
        self.request_id = request_id
        # Indicates whether the submission is successful.
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
            temp_model = main_models.EcomVideoRecreationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class EcomVideoRecreationResponseBodyData(DaraModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # The ID of the asynchronous task, which is used to query the task result by calling QueryAsyncTaskResult.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

