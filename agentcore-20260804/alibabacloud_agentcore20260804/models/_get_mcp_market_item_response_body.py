# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetMcpMarketItemResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetMcpMarketItemResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code.
        self.code = code
        # The response data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The response message.
        self.message = message
        # The request ID, which is used to locate and troubleshoot issues.
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
            temp_model = main_models.GetMcpMarketItemResponseBodyData()
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

class GetMcpMarketItemResponseBodyData(DaraModel):
    def __init__(
        self,
        category: str = None,
        description: str = None,
        display_metadata: Dict[str, Any] = None,
        icon_url: str = None,
        install_count: int = None,
        market_item_id: str = None,
        mcp_type: str = None,
        name: str = None,
        official_tag: str = None,
        protocol: str = None,
        readme: str = None,
        schema_version: str = None,
        template_input_schema: str = None,
        template_version: str = None,
    ):
        # The category of the MCP marketplace template.
        self.category = category
        # The description of the MCP service.
        self.description = description
        # The display metadata of the template.
        self.display_metadata = display_metadata
        # The icon URL of the MCP marketplace template.
        self.icon_url = icon_url
        # The number of times the template has been installed.
        self.install_count = install_count
        # The MCP marketplace template ID.
        self.market_item_id = market_item_id
        # The MCP type.
        self.mcp_type = mcp_type
        # The name of the MCP marketplace template.
        self.name = name
        # The official usage tag.
        self.official_tag = official_tag
        # The MCP protocol.
        self.protocol = protocol
        # The usage instructions for the MCP marketplace template.
        self.readme = readme
        # The template schema version.
        self.schema_version = schema_version
        # The template input schema, represented as a JSON Schema string.
        self.template_input_schema = template_input_schema
        # The version of the MCP marketplace template.
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        if self.description is not None:
            result['description'] = self.description

        if self.display_metadata is not None:
            result['displayMetadata'] = self.display_metadata

        if self.icon_url is not None:
            result['iconUrl'] = self.icon_url

        if self.install_count is not None:
            result['installCount'] = self.install_count

        if self.market_item_id is not None:
            result['marketItemId'] = self.market_item_id

        if self.mcp_type is not None:
            result['mcpType'] = self.mcp_type

        if self.name is not None:
            result['name'] = self.name

        if self.official_tag is not None:
            result['officialTag'] = self.official_tag

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.readme is not None:
            result['readme'] = self.readme

        if self.schema_version is not None:
            result['schemaVersion'] = self.schema_version

        if self.template_input_schema is not None:
            result['templateInputSchema'] = self.template_input_schema

        if self.template_version is not None:
            result['templateVersion'] = self.template_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayMetadata') is not None:
            self.display_metadata = m.get('displayMetadata')

        if m.get('iconUrl') is not None:
            self.icon_url = m.get('iconUrl')

        if m.get('installCount') is not None:
            self.install_count = m.get('installCount')

        if m.get('marketItemId') is not None:
            self.market_item_id = m.get('marketItemId')

        if m.get('mcpType') is not None:
            self.mcp_type = m.get('mcpType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('officialTag') is not None:
            self.official_tag = m.get('officialTag')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('readme') is not None:
            self.readme = m.get('readme')

        if m.get('schemaVersion') is not None:
            self.schema_version = m.get('schemaVersion')

        if m.get('templateInputSchema') is not None:
            self.template_input_schema = m.get('templateInputSchema')

        if m.get('templateVersion') is not None:
            self.template_version = m.get('templateVersion')

        return self

