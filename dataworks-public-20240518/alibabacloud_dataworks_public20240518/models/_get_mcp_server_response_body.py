# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetMcpServerResponseBody(DaraModel):
    def __init__(
        self,
        mcp_server: main_models.GetMcpServerResponseBodyMcpServer = None,
        request_id: str = None,
    ):
        self.mcp_server = mcp_server
        self.request_id = request_id

    def validate(self):
        if self.mcp_server:
            self.mcp_server.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mcp_server is not None:
            result['McpServer'] = self.mcp_server.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('McpServer') is not None:
            temp_model = main_models.GetMcpServerResponseBodyMcpServer()
            self.mcp_server = temp_model.from_map(m.get('McpServer'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMcpServerResponseBodyMcpServer(DaraModel):
    def __init__(
        self,
        config: main_models.GetMcpServerResponseBodyMcpServerConfig = None,
        creator_id: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        modifier_id: str = None,
        name: str = None,
        visibility: str = None,
    ):
        self.config = config
        self.creator_id = creator_id
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.gmt_create_time = gmt_create_time
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.gmt_modified_time = gmt_modified_time
        self.modifier_id = modifier_id
        self.name = name
        self.visibility = visibility

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id

        if self.name is not None:
            result['Name'] = self.name

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = main_models.GetMcpServerResponseBodyMcpServerConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        return self

class GetMcpServerResponseBodyMcpServerConfig(DaraModel):
    def __init__(
        self,
        custom_headers: Dict[str, Any] = None,
        transport: str = None,
        url: str = None,
    ):
        self.custom_headers = custom_headers
        self.transport = transport
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_headers is not None:
            result['CustomHeaders'] = self.custom_headers

        if self.transport is not None:
            result['Transport'] = self.transport

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomHeaders') is not None:
            self.custom_headers = m.get('CustomHeaders')

        if m.get('Transport') is not None:
            self.transport = m.get('Transport')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

