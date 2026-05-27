# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_starops20260428 import models as main_models
from darabonba.model import DaraModel

class CreateMcpServiceRequest(DaraModel):
    def __init__(
        self,
        connection: main_models.CreateMcpServiceRequestConnection = None,
        description: str = None,
        display_name: str = None,
        enable: bool = None,
        mcp_service_name: str = None,
        network: main_models.CreateMcpServiceRequestNetwork = None,
        tools: List[main_models.CreateMcpServiceRequestTools] = None,
    ):
        # This parameter is required.
        self.connection = connection
        self.description = description
        self.display_name = display_name
        # This parameter is required.
        self.enable = enable
        # This parameter is required.
        self.mcp_service_name = mcp_service_name
        # This parameter is required.
        self.network = network
        # This parameter is required.
        self.tools = tools

    def validate(self):
        if self.connection:
            self.connection.validate()
        if self.network:
            self.network.validate()
        if self.tools:
            for v1 in self.tools:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection is not None:
            result['connection'] = self.connection.to_map()

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.enable is not None:
            result['enable'] = self.enable

        if self.mcp_service_name is not None:
            result['mcpServiceName'] = self.mcp_service_name

        if self.network is not None:
            result['network'] = self.network.to_map()

        result['tools'] = []
        if self.tools is not None:
            for k1 in self.tools:
                result['tools'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('connection') is not None:
            temp_model = main_models.CreateMcpServiceRequestConnection()
            self.connection = temp_model.from_map(m.get('connection'))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('mcpServiceName') is not None:
            self.mcp_service_name = m.get('mcpServiceName')

        if m.get('network') is not None:
            temp_model = main_models.CreateMcpServiceRequestNetwork()
            self.network = temp_model.from_map(m.get('network'))

        self.tools = []
        if m.get('tools') is not None:
            for k1 in m.get('tools'):
                temp_model = main_models.CreateMcpServiceRequestTools()
                self.tools.append(temp_model.from_map(k1))

        return self

class CreateMcpServiceRequestTools(DaraModel):
    def __init__(
        self,
        annotations: Dict[str, Any] = None,
        confirm: bool = None,
        description: str = None,
        display_name: str = None,
        enable: bool = None,
        execution: Dict[str, Any] = None,
        icons: List[Dict[str, Any]] = None,
        input_schema: Dict[str, Any] = None,
        name: str = None,
        output_schema: Dict[str, Any] = None,
        title: str = None,
    ):
        self.annotations = annotations
        self.confirm = confirm
        self.description = description
        self.display_name = display_name
        self.enable = enable
        self.execution = execution
        self.icons = icons
        # This parameter is required.
        self.input_schema = input_schema
        # This parameter is required.
        self.name = name
        self.output_schema = output_schema
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotations is not None:
            result['annotations'] = self.annotations

        if self.confirm is not None:
            result['confirm'] = self.confirm

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.enable is not None:
            result['enable'] = self.enable

        if self.execution is not None:
            result['execution'] = self.execution

        if self.icons is not None:
            result['icons'] = self.icons

        if self.input_schema is not None:
            result['inputSchema'] = self.input_schema

        if self.name is not None:
            result['name'] = self.name

        if self.output_schema is not None:
            result['outputSchema'] = self.output_schema

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')

        if m.get('confirm') is not None:
            self.confirm = m.get('confirm')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('execution') is not None:
            self.execution = m.get('execution')

        if m.get('icons') is not None:
            self.icons = m.get('icons')

        if m.get('inputSchema') is not None:
            self.input_schema = m.get('inputSchema')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('outputSchema') is not None:
            self.output_schema = m.get('outputSchema')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class CreateMcpServiceRequestNetwork(DaraModel):
    def __init__(
        self,
        access_ip: str = None,
        access_port: int = None,
        gateway_id: str = None,
        mcp_server_id: str = None,
        mode: str = None,
        region: str = None,
        security_group_id: str = None,
        vpc_id: str = None,
        vsw_id: str = None,
    ):
        self.access_ip = access_ip
        self.access_port = access_port
        self.gateway_id = gateway_id
        self.mcp_server_id = mcp_server_id
        # This parameter is required.
        self.mode = mode
        self.region = region
        self.security_group_id = security_group_id
        self.vpc_id = vpc_id
        self.vsw_id = vsw_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_ip is not None:
            result['accessIp'] = self.access_ip

        if self.access_port is not None:
            result['accessPort'] = self.access_port

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.mcp_server_id is not None:
            result['mcpServerId'] = self.mcp_server_id

        if self.mode is not None:
            result['mode'] = self.mode

        if self.region is not None:
            result['region'] = self.region

        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        if self.vsw_id is not None:
            result['vswId'] = self.vsw_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessIp') is not None:
            self.access_ip = m.get('accessIp')

        if m.get('accessPort') is not None:
            self.access_port = m.get('accessPort')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('mcpServerId') is not None:
            self.mcp_server_id = m.get('mcpServerId')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        if m.get('vswId') is not None:
            self.vsw_id = m.get('vswId')

        return self

class CreateMcpServiceRequestConnection(DaraModel):
    def __init__(
        self,
        auth: main_models.CreateMcpServiceRequestConnectionAuth = None,
        endpoint: str = None,
        platform: str = None,
        timeout: int = None,
        transport: str = None,
    ):
        self.auth = auth
        # This parameter is required.
        self.endpoint = endpoint
        # This parameter is required.
        self.platform = platform
        self.timeout = timeout
        # This parameter is required.
        self.transport = transport

    def validate(self):
        if self.auth:
            self.auth.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth is not None:
            result['auth'] = self.auth.to_map()

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.platform is not None:
            result['platform'] = self.platform

        if self.timeout is not None:
            result['timeout'] = self.timeout

        if self.transport is not None:
            result['transport'] = self.transport

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth') is not None:
            temp_model = main_models.CreateMcpServiceRequestConnectionAuth()
            self.auth = temp_model.from_map(m.get('auth'))

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('platform') is not None:
            self.platform = m.get('platform')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        if m.get('transport') is not None:
            self.transport = m.get('transport')

        return self

class CreateMcpServiceRequestConnectionAuth(DaraModel):
    def __init__(
        self,
        key_info: Dict[str, str] = None,
        type: str = None,
    ):
        # key
        self.key_info = key_info
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_info is not None:
            result['keyInfo'] = self.key_info

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyInfo') is not None:
            self.key_info = m.get('keyInfo')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

