# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetProjectResponseBody(DaraModel):
    def __init__(
        self,
        project: main_models.GetProjectResponseBodyProject = None,
        request_id: str = None,
    ):
        # The details of the workspace.
        self.project = project
        # The request ID, which is used to locate logs and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project is not None:
            result['Project'] = self.project.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            temp_model = main_models.GetProjectResponseBodyProject()
            self.project = temp_model.from_map(m.get('Project'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetProjectResponseBodyProject(DaraModel):
    def __init__(
        self,
        aliyun_resource_group_id: str = None,
        aliyun_resource_tags: List[main_models.GetProjectResponseBodyProjectAliyunResourceTags] = None,
        description: str = None,
        dev_environment_enabled: bool = None,
        dev_role_disabled: bool = None,
        display_name: str = None,
        id: int = None,
        name: str = None,
        owner: str = None,
        pai_task_enabled: bool = None,
        status: str = None,
    ):
        # The ID of the Alibaba Cloud resource group to which the workspace belongs.
        self.aliyun_resource_group_id = aliyun_resource_group_id
        # The tags.
        self.aliyun_resource_tags = aliyun_resource_tags
        # The description of the workspace.
        self.description = description
        # Indicates whether the development environment is enabled. Valid values:
        # 
        # - true: The development environment is enabled for the workspace, which supports isolation between the development and production environments.
        # 
        # - false: Only the production environment is used.
        self.dev_environment_enabled = dev_environment_enabled
        # Indicates whether the development role is disabled. Valid values:
        # 
        # - false: The development role is enabled.
        # 
        # - true: The development role is disabled.
        self.dev_role_disabled = dev_role_disabled
        # The display name of the workspace.
        self.display_name = display_name
        # The workspace ID.
        self.id = id
        # The workspace name.
        self.name = name
        # The user ID of the workspace owner, which is the Alibaba Cloud account ID.
        self.owner = owner
        # Indicates whether PAI task scheduling is enabled. Valid values:
        # 
        # - true: You can create Machine Learning Platform for AI (PAI) nodes in the DataWorks workspace and run them on a periodic schedule based on the node configurations.
        # 
        # - false: PAI task scheduling is disabled.
        self.pai_task_enabled = pai_task_enabled
        # The workspace status. Valid values:
        # 
        # - Available: The workspace is running normally.
        # - Initializing: The workspace is being initialized.
        # - InitFailed: The workspace failed to be initialized.
        # - Forbidden: The workspace is manually disabled.
        # - Deleting: The workspace is being deleted.
        # - DeleteFailed: The workspace failed to be deleted.
        # - Frozen: The workspace is frozen due to overdue payment.
        # - Updating: The workspace is being updated.
        # - UpdateFailed: The workspace failed to be updated.
        self.status = status

    def validate(self):
        if self.aliyun_resource_tags:
            for v1 in self.aliyun_resource_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_resource_group_id is not None:
            result['AliyunResourceGroupId'] = self.aliyun_resource_group_id

        result['AliyunResourceTags'] = []
        if self.aliyun_resource_tags is not None:
            for k1 in self.aliyun_resource_tags:
                result['AliyunResourceTags'].append(k1.to_map() if k1 else None)

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

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.pai_task_enabled is not None:
            result['PaiTaskEnabled'] = self.pai_task_enabled

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunResourceGroupId') is not None:
            self.aliyun_resource_group_id = m.get('AliyunResourceGroupId')

        self.aliyun_resource_tags = []
        if m.get('AliyunResourceTags') is not None:
            for k1 in m.get('AliyunResourceTags'):
                temp_model = main_models.GetProjectResponseBodyProjectAliyunResourceTags()
                self.aliyun_resource_tags.append(temp_model.from_map(k1))

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

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PaiTaskEnabled') is not None:
            self.pai_task_enabled = m.get('PaiTaskEnabled')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetProjectResponseBodyProjectAliyunResourceTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

