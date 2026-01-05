# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProjectsShrinkRequest(DaraModel):
    def __init__(
        self,
        aliyun_resource_group_id: str = None,
        aliyun_resource_tags_shrink: str = None,
        dev_environment_enabled: bool = None,
        dev_role_disabled: bool = None,
        ids_shrink: str = None,
        names_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        pai_task_enabled: bool = None,
        status: str = None,
    ):
        # The ID of the Alibaba Cloud resource group to which the workspaces belong. You can log on to the [Resource Management console](https://resourcemanager.console.aliyun.com/resource-groups) and go to the Resource Group page to query the ID.
        # 
        # This parameter is used to query the information about workspaces that belong to a specific resource group.
        self.aliyun_resource_group_id = aliyun_resource_group_id
        # The tags.
        self.aliyun_resource_tags_shrink = aliyun_resource_tags_shrink
        # Specifies whether the development environment is enabled. Valid values:
        # 
        # *   true: The development environment is enabled. In this case, the development environment is isolated from the production environment in a workspace.
        # *   false: The development environment is disabled. In this case, only the production environment is used in a workspace.
        self.dev_environment_enabled = dev_environment_enabled
        # Specifies whether the Develop role is disabled. Valid values:
        # 
        # *   false (default)
        # *   true
        self.dev_role_disabled = dev_role_disabled
        # The IDs of the DataWorks workspaces.
        self.ids_shrink = ids_shrink
        # The names of the DataWorks workspaces.
        self.names_shrink = names_shrink
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # Specifies whether scheduling of Platform for AI (PAI) tasks is enabled. Valid values:
        # 
        # *   true: Scheduling of PAI tasks is enabled. In this case, you can create a PAI node in a DataWorks workspace and configure scheduling properties for the node to implement periodic scheduling of PAI tasks.
        # *   false: Scheduling of PAI tasks is disabled.
        self.pai_task_enabled = pai_task_enabled
        # The status of the workspaces. Valid values:
        # 
        # *   Available
        # *   Initializing
        # *   InitFailed
        # *   Forbidden
        # *   Deleting
        # *   DeleteFailed
        # *   Frozen
        # *   Updating
        # *   UpdateFailed
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_resource_group_id is not None:
            result['AliyunResourceGroupId'] = self.aliyun_resource_group_id

        if self.aliyun_resource_tags_shrink is not None:
            result['AliyunResourceTags'] = self.aliyun_resource_tags_shrink

        if self.dev_environment_enabled is not None:
            result['DevEnvironmentEnabled'] = self.dev_environment_enabled

        if self.dev_role_disabled is not None:
            result['DevRoleDisabled'] = self.dev_role_disabled

        if self.ids_shrink is not None:
            result['Ids'] = self.ids_shrink

        if self.names_shrink is not None:
            result['Names'] = self.names_shrink

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pai_task_enabled is not None:
            result['PaiTaskEnabled'] = self.pai_task_enabled

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunResourceGroupId') is not None:
            self.aliyun_resource_group_id = m.get('AliyunResourceGroupId')

        if m.get('AliyunResourceTags') is not None:
            self.aliyun_resource_tags_shrink = m.get('AliyunResourceTags')

        if m.get('DevEnvironmentEnabled') is not None:
            self.dev_environment_enabled = m.get('DevEnvironmentEnabled')

        if m.get('DevRoleDisabled') is not None:
            self.dev_role_disabled = m.get('DevRoleDisabled')

        if m.get('Ids') is not None:
            self.ids_shrink = m.get('Ids')

        if m.get('Names') is not None:
            self.names_shrink = m.get('Names')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PaiTaskEnabled') is not None:
            self.pai_task_enabled = m.get('PaiTaskEnabled')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

