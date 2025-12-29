# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateNamespaceVpcResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # Indicates whether the VPC information was updated. Valid values:
        # 
        # *   **true**: indicates that the information was updated.
        # *   **false**: indicates that the information could not be updated.
        self.code = code
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: indicates that the request was successful.
        # *   **3xx**: indicates that the request was redirected.
        # *   **4xx**: indicates that the request was invalid.
        # *   **5xx**: indicates that a server error occurred.
        self.error_code = error_code
        # The ID of the trace. It can be used to query the details of a request.
        self.message = message
        # The returned message.
        # 
        # *   **success** is returned when the request succeeds.
        # *   An error code is returned when the request fails.
        self.request_id = request_id
        self.success = success
        # The error code.
        # 
        # *   The **ErrorCode** parameter is not returned when the request succeeds.
        # *   The **ErrorCode** parameter is returned when the request fails. For more information, see **Error codes** in this topic.
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

