# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class AddWorkspaceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        workspace: main_models.AddWorkspaceResponseBodyWorkspace = None,
    ):
        # requestId
        self.request_id = request_id
        self.workspace = workspace

    def validate(self):
        if self.workspace:
            self.workspace.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.workspace is not None:
            result['workspace'] = self.workspace.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('workspace') is not None:
            temp_model = main_models.AddWorkspaceResponseBodyWorkspace()
            self.workspace = temp_model.from_map(m.get('workspace'))

        return self

class AddWorkspaceResponseBodyWorkspace(DaraModel):
    def __init__(
        self,
        corp_id: str = None,
        cover: str = None,
        create_time: str = None,
        creator_id: str = None,
        description: str = None,
        icon: main_models.AddWorkspaceResponseBodyWorkspaceIcon = None,
        modified_time: str = None,
        modifier_id: str = None,
        name: str = None,
        permission_role: str = None,
        root_node_id: str = None,
        team_id: str = None,
        type: str = None,
        url: str = None,
        workspace_id: str = None,
    ):
        self.corp_id = corp_id
        self.cover = cover
        self.create_time = create_time
        self.creator_id = creator_id
        self.description = description
        self.icon = icon
        self.modified_time = modified_time
        self.modifier_id = modifier_id
        self.name = name
        self.permission_role = permission_role
        self.root_node_id = root_node_id
        self.team_id = team_id
        self.type = type
        self.url = url
        self.workspace_id = workspace_id

    def validate(self):
        if self.icon:
            self.icon.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id

        if self.cover is not None:
            result['Cover'] = self.cover

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.description is not None:
            result['Description'] = self.description

        if self.icon is not None:
            result['Icon'] = self.icon.to_map()

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id

        if self.name is not None:
            result['Name'] = self.name

        if self.permission_role is not None:
            result['PermissionRole'] = self.permission_role

        if self.root_node_id is not None:
            result['RootNodeId'] = self.root_node_id

        if self.team_id is not None:
            result['TeamId'] = self.team_id

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')

        if m.get('Cover') is not None:
            self.cover = m.get('Cover')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Icon') is not None:
            temp_model = main_models.AddWorkspaceResponseBodyWorkspaceIcon()
            self.icon = temp_model.from_map(m.get('Icon'))

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PermissionRole') is not None:
            self.permission_role = m.get('PermissionRole')

        if m.get('RootNodeId') is not None:
            self.root_node_id = m.get('RootNodeId')

        if m.get('TeamId') is not None:
            self.team_id = m.get('TeamId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class AddWorkspaceResponseBodyWorkspaceIcon(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

