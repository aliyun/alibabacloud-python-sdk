# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class ListMcpToolsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        items: List[main_models.ListMcpToolsResponseBodyItems] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The business status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The list data.
        self.items = items
        # The maximum number of results per page.
        self.max_results = max_results
        # The response message.
        self.message = message
        # The token for the next page.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.message is not None:
            result['message'] = self.message

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListMcpToolsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListMcpToolsResponseBodyItems(DaraModel):
    def __init__(
        self,
        input_schema: str = None,
        output_schema: str = None,
        tool_description: str = None,
        tool_name: str = None,
    ):
        # The input parameter schema of the tool.
        self.input_schema = input_schema
        # The output parameter schema of the tool.
        self.output_schema = output_schema
        # The MCP tool description.
        self.tool_description = tool_description
        # The MCP tool name.
        self.tool_name = tool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_schema is not None:
            result['inputSchema'] = self.input_schema

        if self.output_schema is not None:
            result['outputSchema'] = self.output_schema

        if self.tool_description is not None:
            result['toolDescription'] = self.tool_description

        if self.tool_name is not None:
            result['toolName'] = self.tool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputSchema') is not None:
            self.input_schema = m.get('inputSchema')

        if m.get('outputSchema') is not None:
            self.output_schema = m.get('outputSchema')

        if m.get('toolDescription') is not None:
            self.tool_description = m.get('toolDescription')

        if m.get('toolName') is not None:
            self.tool_name = m.get('toolName')

        return self

