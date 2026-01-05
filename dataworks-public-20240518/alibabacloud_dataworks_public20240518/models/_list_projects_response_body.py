# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListProjectsResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListProjectsResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListProjectsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListProjectsResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        projects: List[main_models.ListProjectsResponseBodyPagingInfoProjects] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The workspaces.
        self.projects = projects
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.projects:
            for v1 in self.projects:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Projects'] = []
        if self.projects is not None:
            for k1 in self.projects:
                result['Projects'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.projects = []
        if m.get('Projects') is not None:
            for k1 in m.get('Projects'):
                temp_model = main_models.ListProjectsResponseBodyPagingInfoProjects()
                self.projects.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListProjectsResponseBodyPagingInfoProjects(DaraModel):
    def __init__(
        self,
        aliyun_resource_group_id: str = None,
        aliyun_resource_tags: List[main_models.ListProjectsResponseBodyPagingInfoProjectsAliyunResourceTags] = None,
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
        # *   true: The development environment is enabled. In this case, the development environment is isolated from the production environment in the workspace.
        # *   false: The development environment is disabled. In this case, only the production environment is used in the workspace.
        self.dev_environment_enabled = dev_environment_enabled
        # Indicates whether the Develop role is disabled. Valid values:
        # 
        # *   false (default)
        # *   true
        self.dev_role_disabled = dev_role_disabled
        # The display name of the workspace.
        self.display_name = display_name
        # The workspace ID.
        self.id = id
        # The name of the workspace.
        self.name = name
        # The ID of the Alibaba Cloud account to which the workspace belongs.
        self.owner = owner
        # Indicates whether scheduling of PAI tasks is enabled. Valid values:
        # 
        # *   true: Scheduling of PAI tasks is enabled. In this case, you can create a PAI node in a DataWorks workspace and configure scheduling properties for the node to implement periodic scheduling of PAI tasks.
        # *   false: Scheduling of PAI tasks is disabled.
        self.pai_task_enabled = pai_task_enabled
        # The status of the workspace. Valid values:
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
                temp_model = main_models.ListProjectsResponseBodyPagingInfoProjectsAliyunResourceTags()
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

class ListProjectsResponseBodyPagingInfoProjectsAliyunResourceTags(DaraModel):
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

