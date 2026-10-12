# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class CreateProductRefRequest(DaraModel):
    def __init__(
        self,
        apig_ref_config: main_models.CreateProductRefRequestApigRefConfig = None,
        gateway_id: str = None,
    ):
        # The API configuration associated with the API product.
        self.apig_ref_config = apig_ref_config
        # The ID of the gateway.
        self.gateway_id = gateway_id

    def validate(self):
        if self.apig_ref_config:
            self.apig_ref_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apig_ref_config is not None:
            result['apigRefConfig'] = self.apig_ref_config.to_map()

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apigRefConfig') is not None:
            temp_model = main_models.CreateProductRefRequestApigRefConfig()
            self.apig_ref_config = temp_model.from_map(m.get('apigRefConfig'))

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        return self

class CreateProductRefRequestApigRefConfig(DaraModel):
    def __init__(
        self,
        agent_api_id: str = None,
        agent_api_name: str = None,
        api_id: str = None,
        api_name: str = None,
        mcp_route_id: str = None,
        mcp_server_id: str = None,
        mcp_server_name: str = None,
        model_api_id: str = None,
        model_api_name: str = None,
    ):
        # The ID of the associated agent API.
        self.agent_api_id = agent_api_id
        # The name of the associated agent API.
        self.agent_api_name = agent_api_name
        # The ID of the associated API.
        self.api_id = api_id
        # The name of the associated API.
        self.api_name = api_name
        # The ID of the associated MCP route.
        self.mcp_route_id = mcp_route_id
        # The ID of the associated MCP server.
        self.mcp_server_id = mcp_server_id
        # The name of the associated MCP server.
        self.mcp_server_name = mcp_server_name
        # The ID of the associated model API.
        self.model_api_id = model_api_id
        # The name of the associated model API.
        self.model_api_name = model_api_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_api_id is not None:
            result['agentApiId'] = self.agent_api_id

        if self.agent_api_name is not None:
            result['agentApiName'] = self.agent_api_name

        if self.api_id is not None:
            result['apiId'] = self.api_id

        if self.api_name is not None:
            result['apiName'] = self.api_name

        if self.mcp_route_id is not None:
            result['mcpRouteId'] = self.mcp_route_id

        if self.mcp_server_id is not None:
            result['mcpServerId'] = self.mcp_server_id

        if self.mcp_server_name is not None:
            result['mcpServerName'] = self.mcp_server_name

        if self.model_api_id is not None:
            result['modelApiId'] = self.model_api_id

        if self.model_api_name is not None:
            result['modelApiName'] = self.model_api_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentApiId') is not None:
            self.agent_api_id = m.get('agentApiId')

        if m.get('agentApiName') is not None:
            self.agent_api_name = m.get('agentApiName')

        if m.get('apiId') is not None:
            self.api_id = m.get('apiId')

        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')

        if m.get('mcpRouteId') is not None:
            self.mcp_route_id = m.get('mcpRouteId')

        if m.get('mcpServerId') is not None:
            self.mcp_server_id = m.get('mcpServerId')

        if m.get('mcpServerName') is not None:
            self.mcp_server_name = m.get('mcpServerName')

        if m.get('modelApiId') is not None:
            self.model_api_id = m.get('modelApiId')

        if m.get('modelApiName') is not None:
            self.model_api_name = m.get('modelApiName')

        return self

