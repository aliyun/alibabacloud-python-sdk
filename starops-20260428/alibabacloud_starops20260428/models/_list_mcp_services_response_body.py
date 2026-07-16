# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_starops20260428 import models as main_models
from darabonba.model import DaraModel

class ListMcpServicesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        mcp_services: main_models.ListMcpServicesResponseBodyMcpServices = None,
        next_token: str = None,
        request_id: str = None,
        total: int = None,
    ):
        self.max_results = max_results
        self.mcp_services = mcp_services
        self.next_token = next_token
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.mcp_services:
            self.mcp_services.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.mcp_services is not None:
            result['mcpServices'] = self.mcp_services.to_map()

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('mcpServices') is not None:
            temp_model = main_models.ListMcpServicesResponseBodyMcpServices()
            self.mcp_services = temp_model.from_map(m.get('mcpServices'))

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListMcpServicesResponseBodyMcpServices(DaraModel):
    def __init__(
        self,
        mcp_service_list: List[main_models.ListMcpServicesResponseBodyMcpServicesMcpServiceList] = None,
    ):
        self.mcp_service_list = mcp_service_list

    def validate(self):
        if self.mcp_service_list:
            for v1 in self.mcp_service_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['mcpServiceList'] = []
        if self.mcp_service_list is not None:
            for k1 in self.mcp_service_list:
                result['mcpServiceList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mcp_service_list = []
        if m.get('mcpServiceList') is not None:
            for k1 in m.get('mcpServiceList'):
                temp_model = main_models.ListMcpServicesResponseBodyMcpServicesMcpServiceList()
                self.mcp_service_list.append(temp_model.from_map(k1))

        return self

class ListMcpServicesResponseBodyMcpServicesMcpServiceList(DaraModel):
    def __init__(
        self,
        connection: main_models.ListMcpServicesResponseBodyMcpServicesMcpServiceListConnection = None,
        description: str = None,
        display_name: str = None,
        enable: bool = None,
        mcp_service_name: str = None,
        network: main_models.ListMcpServicesResponseBodyMcpServicesMcpServiceListNetwork = None,
        tools: List[main_models.ListMcpServicesResponseBodyMcpServicesMcpServiceListTools] = None,
    ):
        self.connection = connection
        self.description = description
        self.display_name = display_name
        self.enable = enable
        self.mcp_service_name = mcp_service_name
        self.network = network
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
            temp_model = main_models.ListMcpServicesResponseBodyMcpServicesMcpServiceListConnection()
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
            temp_model = main_models.ListMcpServicesResponseBodyMcpServicesMcpServiceListNetwork()
            self.network = temp_model.from_map(m.get('network'))

        self.tools = []
        if m.get('tools') is not None:
            for k1 in m.get('tools'):
                temp_model = main_models.ListMcpServicesResponseBodyMcpServicesMcpServiceListTools()
                self.tools.append(temp_model.from_map(k1))

        return self

class ListMcpServicesResponseBodyMcpServicesMcpServiceListTools(DaraModel):
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
        self.input_schema = input_schema
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

class ListMcpServicesResponseBodyMcpServicesMcpServiceListNetwork(DaraModel):
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

class ListMcpServicesResponseBodyMcpServicesMcpServiceListConnection(DaraModel):
    def __init__(
        self,
        auth: main_models.ListMcpServicesResponseBodyMcpServicesMcpServiceListConnectionAuth = None,
        endpoint: str = None,
        platform: str = None,
        timeout: int = None,
        transport: str = None,
    ):
        self.auth = auth
        self.endpoint = endpoint
        self.platform = platform
        self.timeout = timeout
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
            temp_model = main_models.ListMcpServicesResponseBodyMcpServicesMcpServiceListConnectionAuth()
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

class ListMcpServicesResponseBodyMcpServicesMcpServiceListConnectionAuth(DaraModel):
    def __init__(
        self,
        key_info: Dict[str, str] = None,
        type: str = None,
    ):
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

