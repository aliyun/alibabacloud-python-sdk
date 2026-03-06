# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_openapiexplorer20241130 import models as main_models
from darabonba.model import DaraModel

class CreateApiMcpServerResponseBody(DaraModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
        urls: main_models.CreateApiMcpServerResponseBodyUrls = None,
    ):
        # The ID of the successfully created API MCP service.
        self.id = id
        # The request ID.
        self.request_id = request_id
        # The connection information for the API MCP service.
        self.urls = urls

    def validate(self):
        if self.urls:
            self.urls.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.urls is not None:
            result['urls'] = self.urls.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('urls') is not None:
            temp_model = main_models.CreateApiMcpServerResponseBodyUrls()
            self.urls = temp_model.from_map(m.get('urls'))

        return self

class CreateApiMcpServerResponseBodyUrls(DaraModel):
    def __init__(
        self,
        mcp: str = None,
        sse: str = None,
        vpc_mcp: str = None,
        vpc_sse: str = None,
    ):
        # The connection information for the streamable HTTP protocol. This is the recommended protocol.
        self.mcp = mcp
        # The connection information for the Server-Sent Events (SSE) protocol.
        self.sse = sse
        # The endpoint of the streamable HTTP protocol in a VPC.
        self.vpc_mcp = vpc_mcp
        # The endpoint of the SSE protocol in a VPC.
        self.vpc_sse = vpc_sse

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mcp is not None:
            result['mcp'] = self.mcp

        if self.sse is not None:
            result['sse'] = self.sse

        if self.vpc_mcp is not None:
            result['vpcMcp'] = self.vpc_mcp

        if self.vpc_sse is not None:
            result['vpcSse'] = self.vpc_sse

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mcp') is not None:
            self.mcp = m.get('mcp')

        if m.get('sse') is not None:
            self.sse = m.get('sse')

        if m.get('vpcMcp') is not None:
            self.vpc_mcp = m.get('vpcMcp')

        if m.get('vpcSse') is not None:
            self.vpc_sse = m.get('vpcSse')

        return self

