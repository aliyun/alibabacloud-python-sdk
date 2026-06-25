# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteApplicationScalingRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The status of the API call or a POP error code. Valid values:
        # 
        # - **2xx**: success.
        # 
        # - **3xx**: redirection.
        # 
        # - **4xx**: request error.
        # 
        # - **5xx**: server error.
        self.code = code
        # The error code. The following rules apply:
        # 
        # - This parameter is not returned if the request is successful.
        # 
        # - This parameter is returned if the request fails. For more information, see the list of **error codes** in this topic.
        self.error_code = error_code
        # Additional information. The following values may be returned:
        # 
        # - **success** is returned if the request is normal.
        # 
        # - A specific error code is returned if the request is abnormal.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the Auto Scaling policy was successfully deleted. Valid values:
        # 
        # - **true**: The deletion was successful.
        # 
        # - **false**: The deletion failed.
        self.success = success
        # The trace ID. You can use this ID to query the details of a call.
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

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

