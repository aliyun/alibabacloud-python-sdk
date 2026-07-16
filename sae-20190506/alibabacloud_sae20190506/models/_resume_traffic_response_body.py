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
        # The API status code or POP error code. Valid values:
        # 
        # - **2xx**: The request was successful.
        # 
        # - **3xx**: Redirection.
        # 
        # - **4xx**: A client-side error occurred.
        # 
        # - **5xx**: A server-side error occurred.
        self.code = code
        # The returned results.
        self.data = data
        # The error code.
        # 
        # - This parameter is empty if the request is successful.
        # 
        # - If the request fails, this parameter contains an error code. For more information, see the "**Error codes**" section of this topic.
        self.error_code = error_code
        # The returned message.
        # 
        # - If the request is successful, **success** is returned.
        # 
        # - If the request fails, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the traffic was resumed. **True** indicates that the traffic was resumed, and **False** indicates that the traffic was not resumed.
        self.success = success
        # The trace ID of the request. You can use this ID to troubleshoot the request.
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
        # Details about the operation\\"s result.
        self.msg = msg
        # Indicates whether the traffic was resumed.
        # 
        # - **True**: The traffic was resumed.
        # 
        # - **False**: The traffic was not resumed.
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

