# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNacosMcpServerRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        encrypt_tool_spec: bool = None,
        endpoint_specification: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        server_name: str = None,
        server_specification: str = None,
        tool_specification: str = None,
        yaml_config: str = None,
    ):
        # The language of the response. Valid values: zh (Chinese, default) and en (English).
        self.accept_language = accept_language
        # Specifies whether to encrypt the MCP tool specification. Valid values:
        # 
        # - `true`: Encrypts the specification.
        # - `false`: Does not encrypt the specification. This is the default value.
        self.encrypt_tool_spec = encrypt_tool_spec
        # The JSON string of the endpoint specification.
        self.endpoint_specification = endpoint_specification
        # The instance ID.
        self.instance_id = instance_id
        # The namespace ID.
        self.namespace_id = namespace_id
        # The service name.
        self.server_name = server_name
        # The JSON string of the server specification.
        self.server_specification = server_specification
        # The JSON string of the tool specification.
        self.tool_specification = tool_specification
        # The YAML configuration of the AI gateway. This parameter is optional.
        self.yaml_config = yaml_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.encrypt_tool_spec is not None:
            result['EncryptToolSpec'] = self.encrypt_tool_spec

        if self.endpoint_specification is not None:
            result['EndpointSpecification'] = self.endpoint_specification

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.server_name is not None:
            result['ServerName'] = self.server_name

        if self.server_specification is not None:
            result['ServerSpecification'] = self.server_specification

        if self.tool_specification is not None:
            result['ToolSpecification'] = self.tool_specification

        if self.yaml_config is not None:
            result['YamlConfig'] = self.yaml_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('EncryptToolSpec') is not None:
            self.encrypt_tool_spec = m.get('EncryptToolSpec')

        if m.get('EndpointSpecification') is not None:
            self.endpoint_specification = m.get('EndpointSpecification')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')

        if m.get('ServerSpecification') is not None:
            self.server_specification = m.get('ServerSpecification')

        if m.get('ToolSpecification') is not None:
            self.tool_specification = m.get('ToolSpecification')

        if m.get('YamlConfig') is not None:
            self.yaml_config = m.get('YamlConfig')

        return self

