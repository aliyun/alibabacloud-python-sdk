# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class PackageWeightSizeCheckResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.PackageWeightSizeCheckResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. 200 indicates a successful call. For other response codes, refer to the error code information.
        self.code = code
        # The asynchronous submission result data, which contains the asynchronous task ID.
        self.data = data
        # The error message. "Success" is returned for normal calls, and specific error information is returned for exceptions.
        self.message = message
        # The request ID, used to identify a unique request call.
        self.request_id = request_id
        # Whether the call was successful. true indicates success, and false indicates failure.
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
            temp_model = main_models.PackageWeightSizeCheckResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class PackageWeightSizeCheckResponseBodyData(DaraModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # The asynchronous task ID, used to query the audit result later through QueryAsyncTaskResult.
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

