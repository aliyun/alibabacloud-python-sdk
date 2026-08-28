# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetAgentSpecLatestResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetAgentSpecLatestResponseBodyData = None,
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
            temp_model = main_models.GetAgentSpecLatestResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetAgentSpecLatestResponseBodyData(DaraModel):
    def __init__(
        self,
        biz_tags: str = None,
        content: str = None,
        description: str = None,
        download_count: int = None,
        enable: bool = None,
        mcp_servers: List[main_models.GetAgentSpecLatestResponseBodyDataMcpServers] = None,
        name: str = None,
        resource: Dict[str, main_models.DataResourceValue] = None,
        scope: str = None,
        skills: List[main_models.GetAgentSpecLatestResponseBodyDataSkills] = None,
        update_time: int = None,
    ):
        # The business tags.
        self.biz_tags = biz_tags
        # The content.
        self.content = content
        # The description.
        self.description = description
        # The download count.
        self.download_count = download_count
        # Indicates whether the AgentSpec is enabled.
        self.enable = enable
        # The list of MCP server references.
        self.mcp_servers = mcp_servers
        # The name.
        self.name = name
        # The resource file mapping.
        self.resource = resource
        # The visibility scope.
        self.scope = scope
        # The list of skill references.
        self.skills = skills
        # The update time. This value is a UNIX timestamp in milliseconds.
        self.update_time = update_time

    def validate(self):
        if self.mcp_servers:
            for v1 in self.mcp_servers:
                 if v1:
                    v1.validate()
        if self.resource:
            for v1 in self.resource.values():
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

        if self.content is not None:
            result['content'] = self.content

        if self.description is not None:
            result['description'] = self.description

        if self.download_count is not None:
            result['downloadCount'] = self.download_count

        if self.enable is not None:
            result['enable'] = self.enable

        result['mcpServers'] = []
        if self.mcp_servers is not None:
            for k1 in self.mcp_servers:
                result['mcpServers'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        result['resource'] = {}
        if self.resource is not None:
            for k1, v1 in self.resource.items():
                result['resource'][k1] = v1.to_map() if v1 else None

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

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('downloadCount') is not None:
            self.download_count = m.get('downloadCount')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        self.mcp_servers = []
        if m.get('mcpServers') is not None:
            for k1 in m.get('mcpServers'):
                temp_model = main_models.GetAgentSpecLatestResponseBodyDataMcpServers()
                self.mcp_servers.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        self.resource = {}
        if m.get('resource') is not None:
            for k1, v1 in m.get('resource').items():
                temp_model = main_models.DataResourceValue()
                self.resource[k1] = temp_model.from_map(v1)

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        self.skills = []
        if m.get('skills') is not None:
            for k1 in m.get('skills'):
                temp_model = main_models.GetAgentSpecLatestResponseBodyDataSkills()
                self.skills.append(temp_model.from_map(k1))

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

class GetAgentSpecLatestResponseBodyDataSkills(DaraModel):
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

class GetAgentSpecLatestResponseBodyDataMcpServers(DaraModel):
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

