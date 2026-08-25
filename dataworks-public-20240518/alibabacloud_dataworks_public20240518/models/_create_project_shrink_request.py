# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateProjectShrinkRequest(DaraModel):
    def __init__(
        self,
        aliyun_resource_group_id: str = None,
        aliyun_resource_tags_shrink: str = None,
        description: str = None,
        dev_environment_enabled: bool = None,
        dev_role_disabled: bool = None,
        display_name: str = None,
        name: str = None,
        pai_task_enabled: bool = None,
    ):
        # The ID of the Alibaba Cloud resource group to which the workspace belongs. You can log on to the [Resource Management console](https://resourcemanager.console.aliyun.com/resource-groups) and go to the resource group list page to obtain the ID.
        # 
        # This parameter is used to manage the DataWorks workspace that you create within the specified Alibaba Cloud resource group.
        self.aliyun_resource_group_id = aliyun_resource_group_id
        # The list of tags.
        self.aliyun_resource_tags_shrink = aliyun_resource_tags_shrink
        # The description of the workspace.
        self.description = description
        # Specifies whether to enable the development environment. Valid values:
        # 
        # - true: The development environment is enabled for the workspace, which supports isolation between the development and production environments.
        # 
        # - false: Only the production environment is used.
        self.dev_environment_enabled = dev_environment_enabled
        # Specifies whether to disable the development role. Valid values:
        # 
        # - false: The development role is enabled. This is the default value.
        # 
        # - true: The development role is disabled.
        self.dev_role_disabled = dev_role_disabled
        # The display name of the workspace.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The workspace name.
        # 
        # Constraints:
        # 
        # - The workspace name must be unique within the region.
        # 
        # - The name must start with a letter and can contain only letters, digits, and underscores (_).
        # 
        # - The name must be 3 to 28 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # Specifies whether to enable PAI task scheduling. Valid values:
        # 
        # - true: You can create Machine Learning Platform for AI (PAI) nodes in the DataWorks workspace and run them on a periodic schedule based on the node configurations.
        # 
        # - false: PAI task scheduling is disabled.
        self.pai_task_enabled = pai_task_enabled

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

        if self.description is not None:
            result['Description'] = self.description

        if self.dev_environment_enabled is not None:
            result['DevEnvironmentEnabled'] = self.dev_environment_enabled

        if self.dev_role_disabled is not None:
            result['DevRoleDisabled'] = self.dev_role_disabled

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.name is not None:
            result['Name'] = self.name

        if self.pai_task_enabled is not None:
            result['PaiTaskEnabled'] = self.pai_task_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunResourceGroupId') is not None:
            self.aliyun_resource_group_id = m.get('AliyunResourceGroupId')

        if m.get('AliyunResourceTags') is not None:
            self.aliyun_resource_tags_shrink = m.get('AliyunResourceTags')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DevEnvironmentEnabled') is not None:
            self.dev_environment_enabled = m.get('DevEnvironmentEnabled')

        if m.get('DevRoleDisabled') is not None:
            self.dev_role_disabled = m.get('DevRoleDisabled')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PaiTaskEnabled') is not None:
            self.pai_task_enabled = m.get('PaiTaskEnabled')

        return self

