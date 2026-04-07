# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListProjectsResponseBody(DaraModel):
    def __init__(
        self,
        page_result: main_models.ListProjectsResponseBodyPageResult = None,
        request_id: str = None,
    ):
        # The results that are returned.
        self.page_result = page_result
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageResult') is not None:
            temp_model = main_models.ListProjectsResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListProjectsResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        project_list: List[main_models.ListProjectsResponseBodyPageResultProjectList] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The DataWorks workspaces.
        self.project_list = project_list
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.project_list:
            for v1 in self.project_list:
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

        result['ProjectList'] = []
        if self.project_list is not None:
            for k1 in self.project_list:
                result['ProjectList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.project_list = []
        if m.get('ProjectList') is not None:
            for k1 in m.get('ProjectList'):
                temp_model = main_models.ListProjectsResponseBodyPageResultProjectList()
                self.project_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListProjectsResponseBodyPageResultProjectList(DaraModel):
    def __init__(
        self,
        disable_development: bool = None,
        is_default: int = None,
        project_description: str = None,
        project_id: int = None,
        project_identifier: str = None,
        project_name: str = None,
        project_owner_base_id: str = None,
        project_status: int = None,
        project_status_code: str = None,
        resource_manager_resource_group_id: str = None,
        table_privacy_mode: int = None,
        tags: List[main_models.ListProjectsResponseBodyPageResultProjectListTags] = None,
        use_proxy_odps_account: bool = None,
    ):
        # Indicates whether the Development role is disabled. Valid values:
        # 
        # *   **false**: enabled
        # *   **true**: disabled
        self.disable_development = disable_development
        # Indicates whether the workspace is a default workspace. Valid values:
        # 
        # *   **1**: The workspace is a default workspace.
        # *   **0**: The workspace is not a default workspace.
        self.is_default = is_default
        # The description of the workspace.
        self.project_description = project_description
        # The workspace ID.
        self.project_id = project_id
        # The name of the workspace.
        self.project_identifier = project_identifier
        # The display name of the workspace.
        self.project_name = project_name
        # The ID of the user used by the workspace owner.
        self.project_owner_base_id = project_owner_base_id
        # The status of the workspace. Valid values:
        # 
        # *   0: AVAILABLE, which indicates that the workspace is running as expected.
        # *   1: DELETED, which indicates that the workspace is deleted.
        # *   2: INITIALIZING, which indicates that the workspace is being initialized.
        # *   3: INIT_FAILED, which indicates that the workspace fails to be initialized.
        # *   4: FORBIDDEN, which indicates that the workspace is manually disabled.
        # *   5: DELETING, which indicates that the workspace is being deleted.
        # *   6: DEL_FAILED, which indicates that the workspace fails to be deleted.
        # *   7: FROZEN, which indicates that the workspace is frozen due to overdue payments.
        # *   8: UPDATING, which indicates that the workspace is being updated. After you associate a compute engine with the workspace, the system initializes the compute engine and updates the workspace.
        # *   9: UPDATE_FAILED, which indicates that the workspace fails to be updated.
        self.project_status = project_status
        # The status code of the workspace. Valid values:
        # 
        # *   AVAILABLE: 0, which indicates that the workspace is running as expected.
        # *   DELETED: 1, which indicates that the workspace is deleted.
        # *   INITIALIZING: 2, which indicates that the workspace is being initialized.
        # *   INIT_FAILED: 3, which indicates that the workspace fails to be initialized.
        # *   FORBIDDEN: 4, which indicates that the workspace is manually disabled.
        # *   DELETING: 5, which indicates that the workspace is being deleted.
        # *   DEL_FAILED: 6, which indicates that the workspace fails to be deleted.
        # *   FROZEN: 7, which indicates that the workspace is frozen due to overdue payments.
        # *   UPDATING: 8, which indicates that the workspace is being updated. After you associate a compute engine with the workspace, the system initializes the compute engine and updates the workspace.
        # *   UPDATE_FAILED: 9, which indicates that the workspace fails to be updated.
        self.project_status_code = project_status_code
        # The resource group ID.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # Indicates whether the MaxCompute tables in the workspace are visible to the users within a tenant. Valid values:
        # 
        # *   **0**: invisible
        # *   **1**: visible
        self.table_privacy_mode = table_privacy_mode
        # The tags added to the workspace.
        self.tags = tags
        # Indicates whether a proxy account is used to access the MaxCompute compute engine associated with the workspace. Valid values:
        # 
        # *   **false**
        # *   **true**
        self.use_proxy_odps_account = use_proxy_odps_account

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disable_development is not None:
            result['DisableDevelopment'] = self.disable_development

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.project_description is not None:
            result['ProjectDescription'] = self.project_description

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_identifier is not None:
            result['ProjectIdentifier'] = self.project_identifier

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.project_owner_base_id is not None:
            result['ProjectOwnerBaseId'] = self.project_owner_base_id

        if self.project_status is not None:
            result['ProjectStatus'] = self.project_status

        if self.project_status_code is not None:
            result['ProjectStatusCode'] = self.project_status_code

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.table_privacy_mode is not None:
            result['TablePrivacyMode'] = self.table_privacy_mode

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.use_proxy_odps_account is not None:
            result['UseProxyOdpsAccount'] = self.use_proxy_odps_account

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisableDevelopment') is not None:
            self.disable_development = m.get('DisableDevelopment')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('ProjectDescription') is not None:
            self.project_description = m.get('ProjectDescription')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectIdentifier') is not None:
            self.project_identifier = m.get('ProjectIdentifier')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('ProjectOwnerBaseId') is not None:
            self.project_owner_base_id = m.get('ProjectOwnerBaseId')

        if m.get('ProjectStatus') is not None:
            self.project_status = m.get('ProjectStatus')

        if m.get('ProjectStatusCode') is not None:
            self.project_status_code = m.get('ProjectStatusCode')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('TablePrivacyMode') is not None:
            self.table_privacy_mode = m.get('TablePrivacyMode')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListProjectsResponseBodyPageResultProjectListTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UseProxyOdpsAccount') is not None:
            self.use_proxy_odps_account = m.get('UseProxyOdpsAccount')

        return self

class ListProjectsResponseBodyPageResultProjectListTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N added to the workspace.
        self.key = key
        # The value of tag N added to the workspace.
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

