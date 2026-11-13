# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UploadAgentSessionFileResponseBody(DaraModel):
    def __init__(
        self,
        json_rpc_response: main_models.UploadAgentSessionFileResponseBodyJsonRpcResponse = None,
        request_id: str = None,
    ):
        self.json_rpc_response = json_rpc_response
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
            temp_model = main_models.UploadAgentSessionFileResponseBodyJsonRpcResponse()
            self.json_rpc_response = temp_model.from_map(m.get('JsonRpcResponse'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UploadAgentSessionFileResponseBodyJsonRpcResponse(DaraModel):
    def __init__(
        self,
        error: main_models.UploadAgentSessionFileResponseBodyJsonRpcResponseError = None,
        id: str = None,
        jsonrpc: str = None,
        result: main_models.UploadAgentSessionFileResponseBodyJsonRpcResponseResult = None,
        timestamp: int = None,
    ):
        self.error = error
        self.id = id
        self.jsonrpc = jsonrpc
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
            temp_model = main_models.UploadAgentSessionFileResponseBodyJsonRpcResponseError()
            self.error = temp_model.from_map(m.get('Error'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Jsonrpc') is not None:
            self.jsonrpc = m.get('Jsonrpc')

        if m.get('Result') is not None:
            temp_model = main_models.UploadAgentSessionFileResponseBodyJsonRpcResponseResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class UploadAgentSessionFileResponseBodyJsonRpcResponseResult(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        relative_path: str = None,
        signature: main_models.UploadAgentSessionFileResponseBodyJsonRpcResponseResultSignature = None,
        size: int = None,
        upload_id: str = None,
    ):
        self.id = id
        self.name = name
        self.relative_path = relative_path
        self.signature = signature
        self.size = size
        self.upload_id = upload_id

    def validate(self):
        if self.signature:
            self.signature.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.relative_path is not None:
            result['RelativePath'] = self.relative_path

        if self.signature is not None:
            result['Signature'] = self.signature.to_map()

        if self.size is not None:
            result['Size'] = self.size

        if self.upload_id is not None:
            result['UploadId'] = self.upload_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RelativePath') is not None:
            self.relative_path = m.get('RelativePath')

        if m.get('Signature') is not None:
            temp_model = main_models.UploadAgentSessionFileResponseBodyJsonRpcResponseResultSignature()
            self.signature = temp_model.from_map(m.get('Signature'))

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('UploadId') is not None:
            self.upload_id = m.get('UploadId')

        return self

class UploadAgentSessionFileResponseBodyJsonRpcResponseResultSignature(DaraModel):
    def __init__(
        self,
        expires_at: str = None,
        headers: Dict[str, str] = None,
        url: str = None,
    ):
        self.expires_at = expires_at
        self.headers = headers
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expires_at is not None:
            result['ExpiresAt'] = self.expires_at

        if self.headers is not None:
            result['Headers'] = self.headers

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiresAt') is not None:
            self.expires_at = m.get('ExpiresAt')

        if m.get('Headers') is not None:
            self.headers = m.get('Headers')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class UploadAgentSessionFileResponseBodyJsonRpcResponseError(DaraModel):
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

