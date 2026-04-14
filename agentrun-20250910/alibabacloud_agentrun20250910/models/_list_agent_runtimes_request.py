# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgentRuntimesRequest(DaraModel):
    def __init__(
        self,
        agent_runtime_name: str = None,
        discovery_resource_group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        search_mode: str = None,
        status: str = None,
        system_tags: str = None,
        workspace_id: str = None,
        workspace_ids: str = None,
    ):
        # 根据智能体运行时名称进行模糊匹配过滤
        self.agent_runtime_name = agent_runtime_name
        # 用于服务发现的资源组标识符
        self.discovery_resource_group_id = discovery_resource_group_id
        # 当前页码，从1开始计数
        self.page_number = page_number
        # 每页返回的记录数量
        self.page_size = page_size
        self.resource_group_id = resource_group_id
        # 查询模式，支持精确查询和模糊查询
        self.search_mode = search_mode
        # 根据状态进行过滤，多个状态用逗号分隔，支持精确匹配
        self.status = status
        # 根据系统标签进行过滤，多个标签用逗号分隔，支持精确匹配
        self.system_tags = system_tags
        # 根据工作空间ID进行过滤，用于资源隔离和权限管理
        self.workspace_id = workspace_id
        self.workspace_ids = workspace_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_runtime_name is not None:
            result['agentRuntimeName'] = self.agent_runtime_name

        if self.discovery_resource_group_id is not None:
            result['discoveryResourceGroupId'] = self.discovery_resource_group_id

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.search_mode is not None:
            result['searchMode'] = self.search_mode

        if self.status is not None:
            result['status'] = self.status

        if self.system_tags is not None:
            result['systemTags'] = self.system_tags

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        if self.workspace_ids is not None:
            result['workspaceIds'] = self.workspace_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentRuntimeName') is not None:
            self.agent_runtime_name = m.get('agentRuntimeName')

        if m.get('discoveryResourceGroupId') is not None:
            self.discovery_resource_group_id = m.get('discoveryResourceGroupId')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('searchMode') is not None:
            self.search_mode = m.get('searchMode')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('systemTags') is not None:
            self.system_tags = m.get('systemTags')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        if m.get('workspaceIds') is not None:
            self.workspace_ids = m.get('workspaceIds')

        return self

