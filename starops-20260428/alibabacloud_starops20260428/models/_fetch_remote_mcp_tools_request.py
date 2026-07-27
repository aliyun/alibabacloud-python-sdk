# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_starops20260428 import models as main_models
from darabonba.model import DaraModel

class FetchRemoteMcpToolsRequest(DaraModel):
    def __init__(
        self,
        connection: main_models.FetchRemoteMcpToolsRequestConnection = None,
        network: main_models.FetchRemoteMcpToolsRequestNetwork = None,
    ):
        # The request body parameters.
        # 
        # This parameter is required.
        self.connection = connection
        # The request body parameters.
        self.network = network

    def validate(self):
        if self.connection:
            self.connection.validate()
        if self.network:
            self.network.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection is not None:
            result['connection'] = self.connection.to_map()

        if self.network is not None:
            result['network'] = self.network.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('connection') is not None:
            temp_model = main_models.FetchRemoteMcpToolsRequestConnection()
            self.connection = temp_model.from_map(m.get('connection'))

        if m.get('network') is not None:
            temp_model = main_models.FetchRemoteMcpToolsRequestNetwork()
            self.network = temp_model.from_map(m.get('network'))

        return self

class FetchRemoteMcpToolsRequestNetwork(DaraModel):
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
        # The IP address used to access the MCP service over the VPC network.
        self.access_ip = access_ip
        # The port used to access the MCP service over the VPC network. Valid values: 1 to 65535.
        self.access_port = access_port
        # The gateway ID.
        self.gateway_id = gateway_id
        # The MCP Server instance ID.
        self.mcp_server_id = mcp_server_id
        # The network access mode of the MCP service. Valid values: public and vpc.
        self.mode = mode
        # The region where the VPC network resides.
        self.region = region
        # The security group ID.
        self.security_group_id = security_group_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The vSwitch ID.
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

class FetchRemoteMcpToolsRequestConnection(DaraModel):
    def __init__(
        self,
        auth: main_models.FetchRemoteMcpToolsRequestConnectionAuth = None,
        endpoint: str = None,
        headers: Dict[str, str] = None,
        platform: str = None,
        timeout: int = None,
        transport: str = None,
    ):
        # The request body parameters.
        self.auth = auth
        # The access endpoint of the MCP service.
        # 
        # This parameter is required.
        self.endpoint = endpoint
        self.headers = headers
        # The MCP service platform type. Valid values: AIGateway and Custom.
        self.platform = platform
        # The timeout period for requests to the MCP service. Unit: milliseconds.
        self.timeout = timeout
        # The transport protocol of the MCP service. Valid values: http and sse.
        # 
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

        if self.headers is not None:
            result['headers'] = self.headers

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
            temp_model = main_models.FetchRemoteMcpToolsRequestConnectionAuth()
            self.auth = temp_model.from_map(m.get('auth'))

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('platform') is not None:
            self.platform = m.get('platform')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        if m.get('transport') is not None:
            self.transport = m.get('transport')

        return self

class FetchRemoteMcpToolsRequestConnectionAuth(DaraModel):
    def __init__(
        self,
        key_info: Dict[str, str] = None,
        type: str = None,
    ):
        # The request body parameters.
        self.key_info = key_info
        # The authentication type. Currently, only bearer is supported.
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

