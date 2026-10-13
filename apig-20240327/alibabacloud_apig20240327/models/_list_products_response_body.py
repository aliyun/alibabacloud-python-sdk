# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListProductsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListProductsResponseBodyData = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The response status code.
        self.code = code
        # The response data.
        self.data = data
        # The maximum number of entries returned in this request.
        self.max_results = max_results
        # The response message.
        self.message = message
        # The cursor token for the next page.
        self.next_token = next_token
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

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.message is not None:
            result['message'] = self.message

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListProductsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListProductsResponseBodyData(DaraModel):
    def __init__(
        self,
        content: List[main_models.ListProductsResponseBodyDataContent] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of API products. The list element is named productInfo, and each element contains the information of an API product.
        self.content = content
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['content'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('content') is not None:
            for k1 in m.get('content'):
                temp_model = main_models.ListProductsResponseBodyDataContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListProductsResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        agent_config: main_models.HiMarketAgentConfig = None,
        auto_approve: bool = None,
        categories: List[main_models.HiMarketProductCategory] = None,
        description: str = None,
        document: str = None,
        feature: main_models.HiMarketProductFeature = None,
        icon: main_models.HiMarketIcon = None,
        mcp_config: main_models.HiMarketMcpConfig = None,
        model_config: main_models.HiMarketModelConfig = None,
        name: str = None,
        product_id: str = None,
        status: str = None,
        type: str = None,
    ):
        # The agent-related configurations of the API product. The agentAPIConfig member includes agentProtocols (the list of protocols supported by the agent) and routes (the list of routes).
        self.agent_config = agent_config
        # Specifies whether subscription requests for the API product are automatically approved. This is the AutoApprove property of the API product resource.
        self.auto_approve = auto_approve
        # The list of product categories to which the API product belongs. The list element is named category.
        self.categories = categories
        # The description of the API product, which is the Description property of the API product resource.
        self.description = description
        # The documentation of the API product, which is the Document property of the API product resource.
        self.document = document
        # The capability configurations of the API product. Currently, it includes only the modelFeature (model capabilities) member, which contains model, maxTokens, temperature, streaming, webSearch, enableThinking, and enableMultiModal.
        self.feature = feature
        # The icon of the API product, which is the Icon property of the API product resource. It consists of two fields: type (the icon type) and value (the icon information).
        self.icon = icon
        # The MCP-related configurations of the API product. The members include mcpServerName (the MCP server name), tools, mcpServerConfig (path and domains), and meta (protocol).
        self.mcp_config = mcp_config
        # The model API-related configurations of the API product. The modelAPIConfig member includes modelCategory (the AI model category), aiProtocols (the list of AI API protocols), and routes (the list of routes).
        self.model_config = model_config
        # The name of the API product, which is the Name property of the API product resource.
        self.name = name
        # The ID of the API product, which is the primary ID of the API product resource. You can use it to locate the product in operations such as GetProduct, UpdateProduct, DeleteProduct, PublishProduct, SetProductCategories, and ListProductPublications.
        self.product_id = product_id
        # The status of the API product, which is the Status property of the API product resource. Valid values: Pending, Ready, and Published.
        self.status = status
        # The type of the API product, which is the Type property of the API product resource. The valid values are not declared in the API definition. Refer to the types displayed in the console.
        self.type = type

    def validate(self):
        if self.agent_config:
            self.agent_config.validate()
        if self.categories:
            for v1 in self.categories:
                 if v1:
                    v1.validate()
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

        result['categories'] = []
        if self.categories is not None:
            for k1 in self.categories:
                result['categories'].append(k1.to_map() if k1 else None)

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

        self.categories = []
        if m.get('categories') is not None:
            for k1 in m.get('categories'):
                temp_model = main_models.HiMarketProductCategory()
                self.categories.append(temp_model.from_map(k1))

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

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

