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
        # The description of the workspace. The description cannot exceed 80 characters in length.
        # 
        # This parameter is required.
        self.description = description
        # We recommend that you name the workspace based on its business attribute to facilitate identification of its purpose. If you do not configure this parameter, the workspace name is used by default.
        self.display_name = display_name
        # The environments included in the workspace:
        # - The simple mode contains only the production environment (prod).
        # - The standard mode contains both the development environment (dev) and the production environment (prod).
        # 
        # This parameter is required.
        self.env_types = env_types
        # The resource group ID. For information about how to obtain the resource group ID, see [View basic information of a resource group](https://help.aliyun.com/document_detail/151181.html).
        self.resource_group_id = resource_group_id
        # The name of the workspace. The format is as follows:
        # - The length is 3 to 23 characters and can contain letters, underscores (_), or digits.
        # - It must start with a letter (uppercase or lowercase).
        # - It must be unique within the current region.
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

