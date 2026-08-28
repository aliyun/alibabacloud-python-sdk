# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateMcpRequest(DaraModel):
    def __init__(
        self,
        body: main_models.CreateMcpRequestBody = None,
        client_token: str = None,
    ):
        # The request body.
        self.body = body
        # The client idempotency token.
        self.client_token = client_token

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.CreateMcpRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class CreateMcpRequestBody(DaraModel):
    def __init__(
        self,
        addresses: List[str] = None,
        auth: main_models.CreateMcpRequestBodyAuth = None,
        description: str = None,
        name: str = None,
        protocol: str = None,
        swagger_config: str = None,
        type: str = None,
    ):
        # The list of MCP service addresses.
        # 
        # This parameter is required.
        self.addresses = addresses
        # The backend authentication configuration. When enabled is set to true: for DIRECT_PROXY, specify directProxy (name/value). For HTTP_TO_MCP, specify the httpToMcp array (each item contains id/type/credential. For apiKey, position/name are also required). Multiple authentication objects are supported, and the first one is used as the default upstream credential. HTTP_TO_MCP credentials are merged into the securitySchemes of the Swagger specification.
        self.auth = auth
        # The description.
        self.description = description
        # The MCP name.
        # 
        # This parameter is required.
        self.name = name
        # The MCP protocol.
        self.protocol = protocol
        # The Swagger configuration. Specify this field if Type is set to HTTP_TO_MCP.
        self.swagger_config = swagger_config
        # The type.
        # 
        # This parameter is required.
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

        if self.name is not None:
            result['name'] = self.name

        if self.protocol is not None:
            result['protocol'] = self.protocol

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
            temp_model = main_models.CreateMcpRequestBodyAuth()
            self.auth = temp_model.from_map(m.get('auth'))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('swaggerConfig') is not None:
            self.swagger_config = m.get('swaggerConfig')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateMcpRequestBodyAuth(DaraModel):
    def __init__(
        self,
        direct_proxy: main_models.CreateMcpRequestBodyAuthDirectProxy = None,
        enabled: bool = None,
        http_to_mcp: List[main_models.CreateMcpRequestBodyAuthHttpToMcp] = None,
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
            temp_model = main_models.CreateMcpRequestBodyAuthDirectProxy()
            self.direct_proxy = temp_model.from_map(m.get('directProxy'))

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        self.http_to_mcp = []
        if m.get('httpToMcp') is not None:
            for k1 in m.get('httpToMcp'):
                temp_model = main_models.CreateMcpRequestBodyAuthHttpToMcp()
                self.http_to_mcp.append(temp_model.from_map(k1))

        return self

class CreateMcpRequestBodyAuthHttpToMcp(DaraModel):
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

class CreateMcpRequestBodyAuthDirectProxy(DaraModel):
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

