# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class UpdateSyncQualityCheckDataResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateSyncQualityCheckDataResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The Result code. A value of 200 indicates Succeeded. Any other value indicates failed. The API caller can determine the cause of failure based on this field.
        self.code = code
        # The complete response Content.
        self.data = data
        # Details of the error when an error occurs; "successful" when the operation succeeded.
        self.message = message
        # The request ID, which is the UUID of the request.
        self.request_id = request_id
        # Indicates whether the Request succeeded. The API caller can use this field to determine whether the Request succeeded: true indicates success; false or null indicates failure.
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
            temp_model = main_models.UpdateSyncQualityCheckDataResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateSyncQualityCheckDataResponseBodyData(DaraModel):
    def __init__(
        self,
        task_id: str = None,
        tid: str = None,
    ):
        # The Job ID.
        self.task_id = task_id
        # The UUID of the call.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

