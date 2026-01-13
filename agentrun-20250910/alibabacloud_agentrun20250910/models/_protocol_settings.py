# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ProtocolSettings(DaraModel):
    def __init__(
        self,
        a_2aagent_card: str = None,
        headers: str = None,
        input_body_json_schema: str = None,
        method: str = None,
        name: str = None,
        output_body_json_schema: str = None,
        path: str = None,
        path_prefix: str = None,
        request_content_type: str = None,
        response_content_type: str = None,
    ):
        # A2A Agent Card
        self.a_2aagent_card = a_2aagent_card
        # 请求头
        self.headers = headers
        # 请求体JSON模式
        self.input_body_json_schema = input_body_json_schema
        # HTTP方法
        self.method = method
        # 协议名称
        self.name = name
        # 响应体JSON模式
        self.output_body_json_schema = output_body_json_schema
        # 协议路径
        self.path = path
        # 协议路径前缀
        self.path_prefix = path_prefix
        # 请求内容类型
        self.request_content_type = request_content_type
        # 响应内容类型
        self.response_content_type = response_content_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.a_2aagent_card is not None:
            result['A2AAgentCard'] = self.a_2aagent_card

        if self.headers is not None:
            result['headers'] = self.headers

        if self.input_body_json_schema is not None:
            result['inputBodyJsonSchema'] = self.input_body_json_schema

        if self.method is not None:
            result['method'] = self.method

        if self.name is not None:
            result['name'] = self.name

        if self.output_body_json_schema is not None:
            result['outputBodyJsonSchema'] = self.output_body_json_schema

        if self.path is not None:
            result['path'] = self.path

        if self.path_prefix is not None:
            result['pathPrefix'] = self.path_prefix

        if self.request_content_type is not None:
            result['requestContentType'] = self.request_content_type

        if self.response_content_type is not None:
            result['responseContentType'] = self.response_content_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('A2AAgentCard') is not None:
            self.a_2aagent_card = m.get('A2AAgentCard')

        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('inputBodyJsonSchema') is not None:
            self.input_body_json_schema = m.get('inputBodyJsonSchema')

        if m.get('method') is not None:
            self.method = m.get('method')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('outputBodyJsonSchema') is not None:
            self.output_body_json_schema = m.get('outputBodyJsonSchema')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('pathPrefix') is not None:
            self.path_prefix = m.get('pathPrefix')

        if m.get('requestContentType') is not None:
            self.request_content_type = m.get('requestContentType')

        if m.get('responseContentType') is not None:
            self.response_content_type = m.get('responseContentType')

        return self

