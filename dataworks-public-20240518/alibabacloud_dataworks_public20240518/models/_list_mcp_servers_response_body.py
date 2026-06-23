# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListMcpServersResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListMcpServersResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The paging information.
        self.paging_info = paging_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListMcpServersResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListMcpServersResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        mcp_servers: List[main_models.ListMcpServersResponseBodyPagingInfoMcpServers] = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # The maximum number of results returned on the current page.****
        self.max_results = max_results
        # A list of MCP Server objects.
        self.mcp_servers = mcp_servers
        # The token for the next page of results. A null value indicates that all results have been returned.****
        self.next_token = next_token
        # The total count of entries that match the filter criteria.
        self.total_count = total_count

    def validate(self):
        if self.mcp_servers:
            for v1 in self.mcp_servers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        result['McpServers'] = []
        if self.mcp_servers is not None:
            for k1 in self.mcp_servers:
                result['McpServers'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        self.mcp_servers = []
        if m.get('McpServers') is not None:
            for k1 in m.get('McpServers'):
                temp_model = main_models.ListMcpServersResponseBodyPagingInfoMcpServers()
                self.mcp_servers.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListMcpServersResponseBodyPagingInfoMcpServers(DaraModel):
    def __init__(
        self,
        config: main_models.ListMcpServersResponseBodyPagingInfoMcpServersConfig = None,
        creator_id: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        modifier_id: str = None,
        name: str = None,
        visibility: str = None,
    ):
        # The connection configuration of the MCP Server.
        self.config = config
        # The creator ID.
        self.creator_id = creator_id
        # The creation time, as a millisecond timestamp.****
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.gmt_create_time = gmt_create_time
        # The last modified time, as a millisecond timestamp.****
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.gmt_modified_time = gmt_modified_time
        # The ID of the user who last modified the server.
        self.modifier_id = modifier_id
        # The name of the MCP Server.
        self.name = name
        # The visibility level.****
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
            temp_model = main_models.ListMcpServersResponseBodyPagingInfoMcpServersConfig()
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

class ListMcpServersResponseBodyPagingInfoMcpServersConfig(DaraModel):
    def __init__(
        self,
        custom_headers: Dict[str, Any] = None,
        transport: str = None,
        url: str = None,
    ):
        # The custom headers.
        self.custom_headers = custom_headers
        # The transport protocol.
        self.transport = transport
        # The service address of the MCP Server.
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

