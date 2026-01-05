# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateProjectRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        dev_environment_enabled: bool = None,
        dev_role_disabled: bool = None,
        display_name: str = None,
        id: int = None,
        pai_task_enabled: bool = None,
        status: str = None,
    ):
        # The description of the workspace.
        self.description = description
        # Specifies whether to enable the development environment. Valid values:
        # 
        # *   true: enables the development environment. In this case, the development environment is isolated from the production environment in the workspace.
        # *   false: disables the development environment. In this case, only the production environment is used in the workspace.
        self.dev_environment_enabled = dev_environment_enabled
        # Specifies whether to disable the Develop role. Valid values:
        # 
        # *   false (default)
        # *   true
        # 
        # Note: If you disable the Develop role, you cannot assume the Develop role to develop nodes in workflows and edit node code. The Develop role cannot be enabled again after it is disabled.
        self.dev_role_disabled = dev_role_disabled
        # The display name of the workspace.
        self.display_name = display_name
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://dataworks.console.aliyun.com/workspace/list) and go to the workspace management page to obtain the ID.
        # 
        # This parameter is used to determine the DataWorks workspaces used for this API call.
        # 
        # This parameter is required.
        self.id = id
        # Specifies whether to enable scheduling of Platform for AI (PAI) tasks. Valid values:
        # 
        # *   true: enables scheduling of PAI tasks. In this case, you can create a PAI node in a DataWorks workspace and configure scheduling properties for the node to implement periodic scheduling of PAI tasks.
        # *   false: disables scheduling of PAI tasks.
        self.pai_task_enabled = pai_task_enabled
        # Specifies whether to disable or enable the workspace. Valid values:
        # 
        # *   Available: enables the workspace.
        # *   Forbidden: disables the workspace.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.dev_environment_enabled is not None:
            result['DevEnvironmentEnabled'] = self.dev_environment_enabled

        if self.dev_role_disabled is not None:
            result['DevRoleDisabled'] = self.dev_role_disabled

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.id is not None:
            result['Id'] = self.id

        if self.pai_task_enabled is not None:
            result['PaiTaskEnabled'] = self.pai_task_enabled

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DevEnvironmentEnabled') is not None:
            self.dev_environment_enabled = m.get('DevEnvironmentEnabled')

        if m.get('DevRoleDisabled') is not None:
            self.dev_role_disabled = m.get('DevRoleDisabled')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PaiTaskEnabled') is not None:
            self.pai_task_enabled = m.get('PaiTaskEnabled')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

