# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateAgentSessionResponseBody(DaraModel):
    def __init__(
        self,
        json_rpc_response: main_models.CreateAgentSessionResponseBodyJsonRpcResponse = None,
        request_id: str = None,
    ):
        # The JSON-RPC response.
        self.json_rpc_response = json_rpc_response
        # Id of the request
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
            temp_model = main_models.CreateAgentSessionResponseBodyJsonRpcResponse()
            self.json_rpc_response = temp_model.from_map(m.get('JsonRpcResponse'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateAgentSessionResponseBodyJsonRpcResponse(DaraModel):
    def __init__(
        self,
        error: main_models.CreateAgentSessionResponseBodyJsonRpcResponseError = None,
        id: str = None,
        jsonrpc: str = None,
        result: main_models.CreateAgentSessionResponseBodyJsonRpcResponseResult = None,
        timestamp: int = None,
    ):
        self.error = error
        # The request ID passed by the caller. The value is returned as-is.
        self.id = id
        # The JSON-RPC version. Fixed value: 2.0.
        self.jsonrpc = jsonrpc
        # The business data. The value is null if an error occurs.
        self.result = result
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
            temp_model = main_models.CreateAgentSessionResponseBodyJsonRpcResponseError()
            self.error = temp_model.from_map(m.get('Error'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Jsonrpc') is not None:
            self.jsonrpc = m.get('Jsonrpc')

        if m.get('Result') is not None:
            temp_model = main_models.CreateAgentSessionResponseBodyJsonRpcResponseResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class CreateAgentSessionResponseBodyJsonRpcResponseResult(DaraModel):
    def __init__(
        self,
        session_id: str = None,
    ):
        # The ID of the created session.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

class CreateAgentSessionResponseBodyJsonRpcResponseError(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: Any = None,
        error_code: str = None,
        message: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
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

