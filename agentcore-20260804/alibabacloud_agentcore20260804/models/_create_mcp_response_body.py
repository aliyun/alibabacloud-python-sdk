# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateMcpResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateMcpResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code.
        self.code = code
        # The returned data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.CreateMcpResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class CreateMcpResponseBodyData(DaraModel):
    def __init__(
        self,
        addresses: List[str] = None,
        auth: main_models.CreateMcpResponseBodyDataAuth = None,
        description: str = None,
        mcp_server_config: str = None,
        mcp_server_id: str = None,
        name: str = None,
        protocol: str = None,
        status: str = None,
        status_reason: str = None,
        swagger_config: str = None,
        type: str = None,
    ):
        # The list of MCP service addresses.
        self.addresses = addresses
        # The backend authentication configuration. enabled indicates whether authentication is enabled. directProxy specifies custom authentication headers for direct proxy. httpToMcp specifies the OpenAPI credential list for HTTP_TO_MCP.
        self.auth = auth
        # The description.
        self.description = description
        # The MCP server configuration.
        self.mcp_server_config = mcp_server_config
        # The MCP server ID.
        self.mcp_server_id = mcp_server_id
        # The name.
        self.name = name
        # The MCP protocol.
        self.protocol = protocol
        # The status.
        self.status = status
        # The status reason.
        self.status_reason = status_reason
        # The Swagger configuration.
        self.swagger_config = swagger_config
        # The type.
        self.type = type

    def validate(self):
        if self.auth:
            self.auth.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addresses is not None:
            result['addresses'] = self.addresses

        if self.auth is not None:
            result['auth'] = self.auth.to_map()

        if self.description is not None:
            result['description'] = self.description

        if self.mcp_server_config is not None:
            result['mcpServerConfig'] = self.mcp_server_config

        if self.mcp_server_id is not None:
            result['mcpServerId'] = self.mcp_server_id

        if self.name is not None:
            result['name'] = self.name

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.status is not None:
            result['status'] = self.status

        if self.status_reason is not None:
            result['statusReason'] = self.status_reason

        if self.swagger_config is not None:
            result['swaggerConfig'] = self.swagger_config

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addresses') is not None:
            self.addresses = m.get('addresses')

        if m.get('auth') is not None:
            temp_model = main_models.CreateMcpResponseBodyDataAuth()
            self.auth = temp_model.from_map(m.get('auth'))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('mcpServerConfig') is not None:
            self.mcp_server_config = m.get('mcpServerConfig')

        if m.get('mcpServerId') is not None:
            self.mcp_server_id = m.get('mcpServerId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')

        if m.get('swaggerConfig') is not None:
            self.swagger_config = m.get('swaggerConfig')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateMcpResponseBodyDataAuth(DaraModel):
    def __init__(
        self,
        direct_proxy: main_models.CreateMcpResponseBodyDataAuthDirectProxy = None,
        enabled: bool = None,
        http_to_mcp: List[main_models.CreateMcpResponseBodyDataAuthHttpToMcp] = None,
    ):
        # The authentication configuration for direct proxy.
        self.direct_proxy = direct_proxy
        # Specifies whether to enable authentication.
        self.enabled = enabled
        # The list of HTTP_TO_MCP authentication configurations.
        self.http_to_mcp = http_to_mcp

    def validate(self):
        if self.direct_proxy:
            self.direct_proxy.validate()
        if self.http_to_mcp:
            for v1 in self.http_to_mcp:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direct_proxy is not None:
            result['directProxy'] = self.direct_proxy.to_map()

        if self.enabled is not None:
            result['enabled'] = self.enabled

        result['httpToMcp'] = []
        if self.http_to_mcp is not None:
            for k1 in self.http_to_mcp:
                result['httpToMcp'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('directProxy') is not None:
            temp_model = main_models.CreateMcpResponseBodyDataAuthDirectProxy()
            self.direct_proxy = temp_model.from_map(m.get('directProxy'))

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        self.http_to_mcp = []
        if m.get('httpToMcp') is not None:
            for k1 in m.get('httpToMcp'):
                temp_model = main_models.CreateMcpResponseBodyDataAuthHttpToMcp()
                self.http_to_mcp.append(temp_model.from_map(k1))

        return self

class CreateMcpResponseBodyDataAuthHttpToMcp(DaraModel):
    def __init__(
        self,
        credential: str = None,
        id: str = None,
        name: str = None,
        position: str = None,
        type: str = None,
    ):
        # The authentication credential.
        self.credential = credential
        # The authentication scheme ID.
        self.id = id
        # The name.
        self.name = name
        # The position of the credential.
        self.position = position
        # The type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential is not None:
            result['credential'] = self.credential

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.position is not None:
            result['position'] = self.position

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('credential') is not None:
            self.credential = m.get('credential')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('position') is not None:
            self.position = m.get('position')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateMcpResponseBodyDataAuthDirectProxy(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name.
        self.name = name
        # The authentication parameter value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

