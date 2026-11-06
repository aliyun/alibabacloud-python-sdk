# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ArchiveAgentSessionResponseBody(DaraModel):
    def __init__(
        self,
        json_rpc_response: main_models.ArchiveAgentSessionResponseBodyJsonRpcResponse = None,
        request_id: str = None,
    ):
        # The JSON-RPC response. Result is returned if the call is successful, and Error is returned if a protocol error occurs.
        self.json_rpc_response = json_rpc_response
        # The OpenAPI request ID, which can be used to troubleshoot call failures.
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
            temp_model = main_models.ArchiveAgentSessionResponseBodyJsonRpcResponse()
            self.json_rpc_response = temp_model.from_map(m.get('JsonRpcResponse'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ArchiveAgentSessionResponseBodyJsonRpcResponse(DaraModel):
    def __init__(
        self,
        error: main_models.ArchiveAgentSessionResponseBodyJsonRpcResponseError = None,
        id: str = None,
        jsonrpc: str = None,
        result: main_models.ArchiveAgentSessionResponseBodyJsonRpcResponseResult = None,
        timestamp: int = None,
    ):
        # The JSON-RPC fault message. This field is not returned if the call is successful.
        self.error = error
        # The JSON-RPC correlation identifier of the current request, which is passed by the caller and returned as-is.
        self.id = id
        # The JSON-RPC protocol version.
        self.jsonrpc = jsonrpc
        # The session archive status.
        self.result = result
        # The response time, which is a UNIX timestamp in milliseconds.
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
            temp_model = main_models.ArchiveAgentSessionResponseBodyJsonRpcResponseError()
            self.error = temp_model.from_map(m.get('Error'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Jsonrpc') is not None:
            self.jsonrpc = m.get('Jsonrpc')

        if m.get('Result') is not None:
            temp_model = main_models.ArchiveAgentSessionResponseBodyJsonRpcResponseResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class ArchiveAgentSessionResponseBodyJsonRpcResponseResult(DaraModel):
    def __init__(
        self,
        archived: bool = None,
        session_id: str = None,
    ):
        # The archive status after the operation is completed. A value of true indicates that the session is archived, and a value of false indicates that the session is unarchived.
        self.archived = archived
        # The ID of the session for which the archive status is set.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.archived is not None:
            result['Archived'] = self.archived

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Archived') is not None:
            self.archived = m.get('Archived')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

class ArchiveAgentSessionResponseBodyJsonRpcResponseError(DaraModel):
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

