# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Toolset(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        creator: str = None,
        description: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        tools: str = None,
        toolset_config: str = None,
        toolset_id: str = None,
        toolset_name: str = None,
        toolset_type: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.creator = creator
        self.description = description
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.tools = tools
        self.toolset_config = toolset_config
        self.toolset_id = toolset_id
        self.toolset_name = toolset_name
        self.toolset_type = toolset_type
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.tools is not None:
            result['Tools'] = self.tools

        if self.toolset_config is not None:
            result['ToolsetConfig'] = self.toolset_config

        if self.toolset_id is not None:
            result['ToolsetId'] = self.toolset_id

        if self.toolset_name is not None:
            result['ToolsetName'] = self.toolset_name

        if self.toolset_type is not None:
            result['ToolsetType'] = self.toolset_type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('Tools') is not None:
            self.tools = m.get('Tools')

        if m.get('ToolsetConfig') is not None:
            self.toolset_config = m.get('ToolsetConfig')

        if m.get('ToolsetId') is not None:
            self.toolset_id = m.get('ToolsetId')

        if m.get('ToolsetName') is not None:
            self.toolset_name = m.get('ToolsetName')

        if m.get('ToolsetType') is not None:
            self.toolset_type = m.get('ToolsetType')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

