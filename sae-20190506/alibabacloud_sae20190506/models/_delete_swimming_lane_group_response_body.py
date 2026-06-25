# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSwimmingLaneGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # - **2xx**: The request was successful.
        # 
        # - **3xx**: The request was redirected.
        # 
        # - **4xx**: A request error occurred.
        # 
        # - **5xx**: A server error occurred.
        self.code = code
        # The error code. This parameter is returned only if the request fails. For more information, see the **Error codes** section of this topic.
        # 
        # - If the request is successful, the **ErrorCode** field is not returned.
        # 
        # - A failed request returns the **ErrorCode** field. For more information, see the **error code** list in this article.
        self.error_code = error_code
        # The returned message.
        # 
        # - **success** is returned for a successful request.
        # 
        # - An error code is returned for a failed request.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The swimming lane group was successfully deleted.
        # 
        # - **false**: The swimming lane group was not deleted.
        self.success = success
        # The trace ID. Use this ID to query the details of a call.
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

