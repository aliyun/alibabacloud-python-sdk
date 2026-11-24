# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class ProbeMcpOriginRequest(DaraModel):
    def __init__(
        self,
        body: main_models.ProbeMcpOriginRequestBody = None,
    ):
        # The scope of the origin server configuration must not exceed that of the creation interface. The control fields for this validation only restrict the validation scope and do not extend the origin server access configuration.
        # 
        # This parameter is required.
        self.body = body

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.ProbeMcpOriginRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class ProbeMcpOriginRequestBody(DaraModel):
    def __init__(
        self,
        address: str = None,
        auth: main_models.ProbeMcpOriginRequestBodyAuth = None,
        swagger_config: str = None,
        type: str = None,
    ):
        # A single HTTP(S) URL that reuses the addresses of the origin server used during creation. Embedded credentials, batch addresses, or protected targets are not accepted.
        # 
        # This parameter is required.
        self.address = address
        # Reuses the enabled, directProxy, and httpToMcp origin server authentication fields and validations from the creation interface. When enabled is set to true, you must provide a configuration that matches the access type. codePackage or additional headers are not accepted.
        self.auth = auth
        # Applicable only to HTTP. Reuses the JSON or YAML string semantics from the creation interface. This field is required when validating the definition. Remote documents or references are not automatically fetched.
        self.swagger_config = swagger_config
        # Valid values: DIRECT_PROXY or HTTP_TO_MCP. CODE_PACKAGE is not accepted.
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
        if self.address is not None:
            result['address'] = self.address

        if self.auth is not None:
            result['auth'] = self.auth.to_map()

        if self.swagger_config is not None:
            result['swaggerConfig'] = self.swagger_config

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('auth') is not None:
            temp_model = main_models.ProbeMcpOriginRequestBodyAuth()
            self.auth = temp_model.from_map(m.get('auth'))

        if m.get('swaggerConfig') is not None:
            self.swagger_config = m.get('swaggerConfig')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ProbeMcpOriginRequestBodyAuth(DaraModel):
    def __init__(
        self,
        direct_proxy: main_models.ProbeMcpOriginRequestBodyAuthDirectProxy = None,
        enabled: bool = None,
        http_to_mcp: List[main_models.ProbeMcpOriginRequestBodyAuthHttpToMcp] = None,
    ):
        # The backend authentication configuration for the direct proxy.
        self.direct_proxy = direct_proxy
        # Specifies whether to enable the configuration.
        self.enabled = enabled
        # The list of backend authentication configurations for HTTP-to-MCP.
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
            temp_model = main_models.ProbeMcpOriginRequestBodyAuthDirectProxy()
            self.direct_proxy = temp_model.from_map(m.get('directProxy'))

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        self.http_to_mcp = []
        if m.get('httpToMcp') is not None:
            for k1 in m.get('httpToMcp'):
                temp_model = main_models.ProbeMcpOriginRequestBodyAuthHttpToMcp()
                self.http_to_mcp.append(temp_model.from_map(k1))

        return self

class ProbeMcpOriginRequestBodyAuthHttpToMcp(DaraModel):
    def __init__(
        self,
        credential: str = None,
        id: str = None,
        name: str = None,
        position: str = None,
        type: str = None,
    ):
        # The credential for the backend authentication.
        self.credential = credential
        # The ID of the backend authentication configuration.
        self.id = id
        # The name of the API key parameter.
        self.name = name
        # The location where the API key is passed.
        self.position = position
        # The type of the backend authentication.
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

class ProbeMcpOriginRequestBodyAuthDirectProxy(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the backend authentication header.
        self.name = name
        # The value of the backend authentication header.
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

