# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListMcpProductToolsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListMcpProductToolsResponseBodyData = None,
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
            temp_model = main_models.ListMcpProductToolsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListMcpProductToolsResponseBodyData(DaraModel):
    def __init__(
        self,
        tools: List[main_models.ListMcpProductToolsResponseBodyDataTools] = None,
    ):
        # The list of MCP tools. Each element in the list represents an MCP tool.
        self.tools = tools

    def validate(self):
        if self.tools:
            for v1 in self.tools:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['tools'] = []
        if self.tools is not None:
            for k1 in self.tools:
                result['tools'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tools = []
        if m.get('tools') is not None:
            for k1 in m.get('tools'):
                temp_model = main_models.ListMcpProductToolsResponseBodyDataTools()
                self.tools.append(temp_model.from_map(k1))

        return self

class ListMcpProductToolsResponseBodyDataTools(DaraModel):
    def __init__(
        self,
        annotations: Dict[str, Any] = None,
        description: str = None,
        input_schema: Dict[str, Any] = None,
        meta: Dict[str, Any] = None,
        name: str = None,
        output_schema: Dict[str, Any] = None,
        title: str = None,
    ):
        # The annotation information of the tool, which is a map structure. The API definition declares it only as map<any> without specifying its members or purposes.
        self.annotations = annotations
        # The description of the tool.
        self.description = description
        # The input parameter structure definition of the tool, which is a map structure. The API definition declares it only as map<any> without specifying its members or constraints.
        self.input_schema = input_schema
        # The metadata information of the tool, which is a map structure. The API definition declares it only as map<any> without specifying its members or purposes.
        self.meta = meta
        # The name of the tool.
        self.name = name
        # The output result structure definition of the tool, which is a map structure. The API definition declares it only as map<any> without specifying its members or constraints.
        self.output_schema = output_schema
        # The title of the tool.
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

        if self.description is not None:
            result['description'] = self.description

        if self.input_schema is not None:
            result['inputSchema'] = self.input_schema

        if self.meta is not None:
            result['meta'] = self.meta

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

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('inputSchema') is not None:
            self.input_schema = m.get('inputSchema')

        if m.get('meta') is not None:
            self.meta = m.get('meta')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('outputSchema') is not None:
            self.output_schema = m.get('outputSchema')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

