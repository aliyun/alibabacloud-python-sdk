# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class GetWebshellTokenResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetWebshellTokenResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: The request was successful.
        # *   **3xx**: The request was redirected.
        # *   **4xx**: The request failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # The returned result.
        self.data = data
        # The error code returned if the call failed. Value values:
        # 
        # *   If the request was successful, **ErrorCode** is not returned.
        # *   If the request failed, the **ErrorCode** parameter is returned. For more information, see **Error codes** section in this topic.
        self.error_code = error_code
        # The returned message. Value description:
        # 
        # *   If the request was successful, a success message is returned.
        # *   An error code is returned if the request failed.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The ID of the trace.
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
            temp_model = main_models.GetWebshellTokenResponseBodyData()
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

class GetWebshellTokenResponseBodyData(DaraModel):
    def __init__(
        self,
        http_url: str = None,
        token: str = None,
        web_socket_url: str = None,
    ):
        # Webshell page address
        self.http_url = http_url
        # The information about the token.
        self.token = token
        # The WebSocket address.
        self.web_socket_url = web_socket_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.http_url is not None:
            result['HttpUrl'] = self.http_url

        if self.token is not None:
            result['Token'] = self.token

        if self.web_socket_url is not None:
            result['WebSocketUrl'] = self.web_socket_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpUrl') is not None:
            self.http_url = m.get('HttpUrl')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('WebSocketUrl') is not None:
            self.web_socket_url = m.get('WebSocketUrl')

        return self

