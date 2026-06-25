# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateNamespaceSlsConfigsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        message: str = None,
        success: bool = None,
        trace_id: str = None,
        request_id: str = None,
    ):
        # The API status code or POP error code. Valid values: 2xx (success), 3xx (redirect), 4xx (client error), 5xx (server error).
        self.code = code
        # The error code. Valid values:
        # 
        # - If the request is successful, the response does not include the `ErrorCode` parameter.
        # 
        # - If the request fails, the response includes the `ErrorCode` parameter. For more information, see the **Error codes** section of this topic.
        self.error_code = error_code
        # Additional information.
        self.message = message
        # Indicates whether the namespace\\"s SLS configuration was successfully updated. A value of `true` indicates success, while `false` indicates failure.
        self.success = success
        # The trace ID for the request. You can use this ID to query the details of the request.
        self.trace_id = trace_id
        # The request ID.
        self.request_id = request_id

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

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

