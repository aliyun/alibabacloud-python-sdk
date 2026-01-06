# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateWorkspaceRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        env_types: List[str] = None,
        resource_group_id: str = None,
        workspace_name: str = None,
    ):
        # The description of the workspace. The description can be up to 80 characters in length.
        # 
        # This parameter is required.
        self.description = description
        # The display name of the workspace. You can set it based on the purpose of the workspace. If left empty, the name of the workspace is used.
        self.display_name = display_name
        # The environment of the workspace.
        # 
        # *   Workspaces in basic mode can run only in the production environment (prod).
        # *   Workspaces in standard mode can run in both the development and production environments (dev and prod).
        # 
        # This parameter is required.
        self.env_types = env_types
        self.resource_group_id = resource_group_id
        # The name of the workspace. Format:
        # 
        # *   The name must be 3 to 23 characters in length, and can contain letters, underscores (_), and digits.
        # *   The name must start with a letter.
        # *   It must be unique in the current region.
        # 
        # This parameter is required.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.env_types is not None:
            result['EnvTypes'] = self.env_types

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('EnvTypes') is not None:
            self.env_types = m.get('EnvTypes')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

