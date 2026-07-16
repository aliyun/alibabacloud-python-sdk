# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class VisionFlowResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.VisionFlowResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. The value "success" is returned for a successful call.
        self.code = code
        # The submit status data of the asynchronous task, which contains the asynchronous task ID.
        self.data = data
        # The error message. The value "Success" is returned for a successful call.
        self.message = message
        # The request ID, which uniquely identifies the API call.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values: true and false.
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
            temp_model = main_models.VisionFlowResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class VisionFlowResponseBodyData(DaraModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # The asynchronous task ID. Use this ID to query the processing result through QueryAsyncTaskResult.
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

