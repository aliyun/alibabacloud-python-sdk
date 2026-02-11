# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Workspace(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        is_default: bool = None,
        name: str = None,
        resource_group_id: str = None,
        updated_at: str = None,
        workspace_arn: str = None,
        workspace_id: str = None,
    ):
        self.created_at = created_at
        self.description = description
        self.is_default = is_default
        self.name = name
        self.resource_group_id = resource_group_id
        self.updated_at = updated_at
        self.workspace_arn = workspace_arn
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.is_default is not None:
            result['isDefault'] = self.is_default

        if self.name is not None:
            result['name'] = self.name

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.workspace_arn is not None:
            result['workspaceArn'] = self.workspace_arn

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspaceArn') is not None:
            self.workspace_arn = m.get('workspaceArn')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

