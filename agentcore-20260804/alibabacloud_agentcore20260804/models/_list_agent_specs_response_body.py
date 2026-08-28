# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class ListAgentSpecsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListAgentSpecsResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
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
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ListAgentSpecsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListAgentSpecsResponseBodyData(DaraModel):
    def __init__(
        self,
        page_items: List[main_models.ListAgentSpecsResponseBodyDataPageItems] = None,
        page_number: int = None,
        pages_available: int = None,
        total_count: int = None,
    ):
        # The data on the current page.
        self.page_items = page_items
        # The current page number.
        self.page_number = page_number
        # The total number of pages.
        self.pages_available = pages_available
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.page_items:
            for v1 in self.page_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['pageItems'] = []
        if self.page_items is not None:
            for k1 in self.page_items:
                result['pageItems'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.pages_available is not None:
            result['pagesAvailable'] = self.pages_available

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_items = []
        if m.get('pageItems') is not None:
            for k1 in m.get('pageItems'):
                temp_model = main_models.ListAgentSpecsResponseBodyDataPageItems()
                self.page_items.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pagesAvailable') is not None:
            self.pages_available = m.get('pagesAvailable')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListAgentSpecsResponseBodyDataPageItems(DaraModel):
    def __init__(
        self,
        biz_tags: str = None,
        description: str = None,
        download_count: int = None,
        editing_version: str = None,
        enable: bool = None,
        from_: str = None,
        labels: Dict[str, str] = None,
        mcp_servers: List[main_models.ListAgentSpecsResponseBodyDataPageItemsMcpServers] = None,
        name: str = None,
        online_cnt: int = None,
        reviewing_version: str = None,
        scope: str = None,
        skills: List[main_models.ListAgentSpecsResponseBodyDataPageItemsSkills] = None,
        update_time: int = None,
    ):
        # The business tags.
        self.biz_tags = biz_tags
        # The description.
        self.description = description
        # The download count.
        self.download_count = download_count
        # The version currently being edited.
        self.editing_version = editing_version
        # Indicates whether the AgentSpec is enabled.
        self.enable = enable
        # The source.
        self.from_ = from_
        # The version labels.
        self.labels = labels
        # The list of MCP server references.
        self.mcp_servers = mcp_servers
        # The name.
        self.name = name
        # The number of online versions.
        self.online_cnt = online_cnt
        # The version currently under review.
        self.reviewing_version = reviewing_version
        # The visibility scope.
        self.scope = scope
        # The list of Skill references.
        self.skills = skills
        # The update time. This value is a UNIX timestamp in milliseconds.
        self.update_time = update_time

    def validate(self):
        if self.mcp_servers:
            for v1 in self.mcp_servers:
                 if v1:
                    v1.validate()
        if self.skills:
            for v1 in self.skills:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_tags is not None:
            result['bizTags'] = self.biz_tags

        if self.description is not None:
            result['description'] = self.description

        if self.download_count is not None:
            result['downloadCount'] = self.download_count

        if self.editing_version is not None:
            result['editingVersion'] = self.editing_version

        if self.enable is not None:
            result['enable'] = self.enable

        if self.from_ is not None:
            result['from'] = self.from_

        if self.labels is not None:
            result['labels'] = self.labels

        result['mcpServers'] = []
        if self.mcp_servers is not None:
            for k1 in self.mcp_servers:
                result['mcpServers'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.online_cnt is not None:
            result['onlineCnt'] = self.online_cnt

        if self.reviewing_version is not None:
            result['reviewingVersion'] = self.reviewing_version

        if self.scope is not None:
            result['scope'] = self.scope

        result['skills'] = []
        if self.skills is not None:
            for k1 in self.skills:
                result['skills'].append(k1.to_map() if k1 else None)

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizTags') is not None:
            self.biz_tags = m.get('bizTags')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('downloadCount') is not None:
            self.download_count = m.get('downloadCount')

        if m.get('editingVersion') is not None:
            self.editing_version = m.get('editingVersion')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('from') is not None:
            self.from_ = m.get('from')

        if m.get('labels') is not None:
            self.labels = m.get('labels')

        self.mcp_servers = []
        if m.get('mcpServers') is not None:
            for k1 in m.get('mcpServers'):
                temp_model = main_models.ListAgentSpecsResponseBodyDataPageItemsMcpServers()
                self.mcp_servers.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('onlineCnt') is not None:
            self.online_cnt = m.get('onlineCnt')

        if m.get('reviewingVersion') is not None:
            self.reviewing_version = m.get('reviewingVersion')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        self.skills = []
        if m.get('skills') is not None:
            for k1 in m.get('skills'):
                temp_model = main_models.ListAgentSpecsResponseBodyDataPageItemsSkills()
                self.skills.append(temp_model.from_map(k1))

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

class ListAgentSpecsResponseBodyDataPageItemsSkills(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class ListAgentSpecsResponseBodyDataPageItemsMcpServers(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        return self

