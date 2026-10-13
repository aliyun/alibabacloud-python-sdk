# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetProductResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetProductResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response status code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetProductResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetProductResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_config: main_models.HiMarketAgentConfig = None,
        auto_approve: bool = None,
        description: str = None,
        document: str = None,
        feature: main_models.HiMarketProductFeature = None,
        icon: main_models.HiMarketIcon = None,
        mcp_config: main_models.HiMarketMcpConfig = None,
        model_config: main_models.HiMarketModelConfig = None,
        name: str = None,
        product_id: str = None,
        region_id: str = None,
        status: str = None,
        type: str = None,
    ):
        # The Agent-related configurations of the API product. The agentAPIConfig member includes agentProtocols, which is a list of protocols supported by the agent, and routes, which is a list of routes.
        self.agent_config = agent_config
        # Indicates whether subscription requests for the product are automatically approved.
        self.auto_approve = auto_approve
        # The description of the API product.
        self.description = description
        # The documentation content of the API product.
        self.document = document
        # The capability configurations of the API product. Currently, this includes only the modelFeature member for model capabilities, which contains model, maxTokens, temperature, streaming, webSearch, enableThinking, and enableMultiModal.
        self.feature = feature
        # The icon configurations of the API product, which consist of two fields: type for the icon type and value for the icon information.
        self.icon = icon
        # The MCP-related configurations of the API product. The members include mcpServerName for the MCP server name, tools, mcpServerConfig for the path and domains, and meta for the protocol.
        self.mcp_config = mcp_config
        # The model API-related configurations of the API product. The modelAPIConfig member includes modelCategory for the AI model category, aiProtocols for the list of AI API protocols, and routes for the list of routes.
        self.model_config = model_config
        # The name of the API product.
        self.name = name
        # The ID of the API product, which is the primary ID of the API product resource. You can use this ID to locate the product in operations such as GetProduct, UpdateProduct, DeleteProduct, PublishProduct, SetProductCategories, and GetProductRef.
        self.product_id = product_id
        # The ID of the region to which the API product belongs.
        self.region_id = region_id
        # The status of the API product. Valid values: Pending, Ready, and Published.
        self.status = status
        # The type of the API product. The set of valid values is not declared in the API definition. Refer to the types displayed in the console.
        self.type = type

    def validate(self):
        if self.agent_config:
            self.agent_config.validate()
        if self.feature:
            self.feature.validate()
        if self.icon:
            self.icon.validate()
        if self.mcp_config:
            self.mcp_config.validate()
        if self.model_config:
            self.model_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_config is not None:
            result['agentConfig'] = self.agent_config.to_map()

        if self.auto_approve is not None:
            result['autoApprove'] = self.auto_approve

        if self.description is not None:
            result['description'] = self.description

        if self.document is not None:
            result['document'] = self.document

        if self.feature is not None:
            result['feature'] = self.feature.to_map()

        if self.icon is not None:
            result['icon'] = self.icon.to_map()

        if self.mcp_config is not None:
            result['mcpConfig'] = self.mcp_config.to_map()

        if self.model_config is not None:
            result['modelConfig'] = self.model_config.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentConfig') is not None:
            temp_model = main_models.HiMarketAgentConfig()
            self.agent_config = temp_model.from_map(m.get('agentConfig'))

        if m.get('autoApprove') is not None:
            self.auto_approve = m.get('autoApprove')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('document') is not None:
            self.document = m.get('document')

        if m.get('feature') is not None:
            temp_model = main_models.HiMarketProductFeature()
            self.feature = temp_model.from_map(m.get('feature'))

        if m.get('icon') is not None:
            temp_model = main_models.HiMarketIcon()
            self.icon = temp_model.from_map(m.get('icon'))

        if m.get('mcpConfig') is not None:
            temp_model = main_models.HiMarketMcpConfig()
            self.mcp_config = temp_model.from_map(m.get('mcpConfig'))

        if m.get('modelConfig') is not None:
            temp_model = main_models.HiMarketModelConfig()
            self.model_config = temp_model.from_map(m.get('modelConfig'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

