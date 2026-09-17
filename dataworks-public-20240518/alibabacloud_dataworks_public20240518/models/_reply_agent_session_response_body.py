# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ReplyAgentSessionResponseBody(DaraModel):
    def __init__(
        self,
        json_rpc_response: main_models.ReplyAgentSessionResponseBodyJsonRpcResponse = None,
        request_id: str = None,
    ):
        # The JSON-RPC response. Returns Result on success or Error on protocol errors.
        self.json_rpc_response = json_rpc_response
        # The request ID for this call, which can be used for troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.json_rpc_response:
            self.json_rpc_response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.json_rpc_response is not None:
            result['JsonRpcResponse'] = self.json_rpc_response.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JsonRpcResponse') is not None:
            temp_model = main_models.ReplyAgentSessionResponseBodyJsonRpcResponse()
            self.json_rpc_response = temp_model.from_map(m.get('JsonRpcResponse'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ReplyAgentSessionResponseBodyJsonRpcResponse(DaraModel):
    def __init__(
        self,
        error: main_models.ReplyAgentSessionResponseBodyJsonRpcResponseError = None,
        id: str = None,
        jsonrpc: str = None,
        result: main_models.ReplyAgentSessionResponseBodyJsonRpcResponseResult = None,
        timestamp: int = None,
    ):
        # The JSON-RPC fault information. For example, DAEMON_PERMISSION_UNAVAILABLE is returned when the daemon reply feature is not enabled.
        self.error = error
        # The JSON-RPC correlation ID for this reply request.
        self.id = id
        # The JSON-RPC protocol version.
        self.jsonrpc = jsonrpc
        # The reply processing result. This only indicates whether the reply was accepted, not whether the original task has completed.
        self.result = result
        # The response time. This is a UNIX timestamp, in milliseconds.
        self.timestamp = timestamp

    def validate(self):
        if self.error:
            self.error.validate()
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error is not None:
            result['Error'] = self.error.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.jsonrpc is not None:
            result['Jsonrpc'] = self.jsonrpc

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Error') is not None:
            temp_model = main_models.ReplyAgentSessionResponseBodyJsonRpcResponseError()
            self.error = temp_model.from_map(m.get('Error'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Jsonrpc') is not None:
            self.jsonrpc = m.get('Jsonrpc')

        if m.get('Result') is not None:
            temp_model = main_models.ReplyAgentSessionResponseBodyJsonRpcResponseResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class ReplyAgentSessionResponseBodyJsonRpcResponseResult(DaraModel):
    def __init__(
        self,
        accepted: bool = None,
    ):
        # Indicates whether the daemon accepted the reply. A value of true indicates that the daemon accepted the reply. A value of false indicates that the reply was not accepted. Possible reasons include an unknown request, an already processed request, an expired request, or a nonexistent session. You cannot determine the specific reason from this value.
        self.accepted = accepted

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accepted is not None:
            result['Accepted'] = self.accepted

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accepted') is not None:
            self.accepted = m.get('Accepted')

        return self

class ReplyAgentSessionResponseBodyJsonRpcResponseError(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: Any = None,
        error_code: str = None,
        message: str = None,
    ):
        # The JSON-RPC error code.
        self.code = code
        # The optional additional error information. The content depends on the error type.
        self.data = data
        # The business error code.
        self.error_code = error_code
        # The error message.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

