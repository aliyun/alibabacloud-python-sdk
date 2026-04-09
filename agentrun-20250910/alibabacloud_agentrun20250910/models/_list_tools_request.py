# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListToolsRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        tool_name: str = None,
        tool_type: str = None,
        workspace_id: str = None,
        workspace_ids: str = None,
    ):
        # 当前页码，从 1 开始
        self.page_number = page_number
        # 每页返回的工具数量，用于分页查询
        self.page_size = page_size
        self.tool_name = tool_name
        # 按工具类型过滤，可选值：MCP、FUNCTIONCALL、SKILL
        self.tool_type = tool_type
        # 按工作空间ID过滤，查询指定工作空间下的工具
        self.workspace_id = workspace_id
        self.workspace_ids = workspace_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.tool_name is not None:
            result['toolName'] = self.tool_name

        if self.tool_type is not None:
            result['toolType'] = self.tool_type

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        if self.workspace_ids is not None:
            result['workspaceIds'] = self.workspace_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('toolName') is not None:
            self.tool_name = m.get('toolName')

        if m.get('toolType') is not None:
            self.tool_type = m.get('toolType')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        if m.get('workspaceIds') is not None:
            self.workspace_ids = m.get('workspaceIds')

        return self

