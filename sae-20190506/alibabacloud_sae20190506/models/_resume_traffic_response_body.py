# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ResumeTrafficResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ResumeTrafficResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: The request was successful.
        # *   **3xx**: The request was redirected.
        # *   **4xx**: The request failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # The returned results.
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The message returned for the operation. Valid values:
        # 
        # *   If the request is successful, **success** is returned.
        # *   If the request fails, a specific error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **True**: The traffic was resumed.
        # *   **False**: The traffic failed to be resumed.
        self.success = success
        # The trace ID.
        self.trace_id = trace_id

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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ResumeTrafficResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class ResumeTrafficResponseBodyData(DaraModel):
    def __init__(
        self,
        msg: str = None,
        success: bool = None,
    ):
        # The description of the returned code.
        self.msg = msg
        # Indicates whether the traffic was removed. Valid values:
        # *   **true**: The traffic was removed.
        # *   **false**: The traffic failed to be removed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.msg is not None:
            result['msg'] = self.msg

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('msg') is not None:
            self.msg = m.get('msg')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

