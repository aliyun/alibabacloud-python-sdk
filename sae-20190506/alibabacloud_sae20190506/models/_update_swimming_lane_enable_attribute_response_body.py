# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSwimmingLaneEnableAttributeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The interface status or POP error code. Valid values:
        # 
        # *   **2xx**: The request was successful.
        # *   **3xx**: Redirection.
        # *   **4xx**: Request error.
        # *   **5xx**: A server error occurred.
        self.code = code
        # Error code. Valid values:
        # 
        # *   If the request is successful, no **ErrorCode** fields are returned.
        # *   Request failed: **ErrorCode** fields are returned. For more information, see **Error codes**.
        self.error_code = error_code
        # Additional information. Valid values:
        # 
        # *   The error message returned because the request is normal and **success** is returned.
        # *   If the request is abnormal, the specific exception error code is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Whether the data is successful. Valid values:
        # 
        # *   **true**: The policy was deleted.
        # *   **false**: The policy failed to be deleted.
        self.success = success
        # The ID of the trace. This parameter is used to query the exact call information.
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

