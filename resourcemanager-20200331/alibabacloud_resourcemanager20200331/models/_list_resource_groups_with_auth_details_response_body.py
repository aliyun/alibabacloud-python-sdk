# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class ListResourceGroupsWithAuthDetailsResponseBody(DaraModel):
    def __init__(
        self,
        auth_details: List[main_models.ListResourceGroupsWithAuthDetailsResponseBodyAuthDetails] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        resource_groups: List[main_models.ListResourceGroupsWithAuthDetailsResponseBodyResourceGroups] = None,
        total_count: int = None,
    ):
        # The authorization details for resource groups.
        self.auth_details = auth_details
        # The page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The response parameters.
        self.request_id = request_id
        # The information of the resource groups.
        self.resource_groups = resource_groups
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.auth_details:
            for v1 in self.auth_details:
                 if v1:
                    v1.validate()
        if self.resource_groups:
            for v1 in self.resource_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AuthDetails'] = []
        if self.auth_details is not None:
            for k1 in self.auth_details:
                result['AuthDetails'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceGroups'] = []
        if self.resource_groups is not None:
            for k1 in self.resource_groups:
                result['ResourceGroups'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auth_details = []
        if m.get('AuthDetails') is not None:
            for k1 in m.get('AuthDetails'):
                temp_model = main_models.ListResourceGroupsWithAuthDetailsResponseBodyAuthDetails()
                self.auth_details.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_groups = []
        if m.get('ResourceGroups') is not None:
            for k1 in m.get('ResourceGroups'):
                temp_model = main_models.ListResourceGroupsWithAuthDetailsResponseBodyResourceGroups()
                self.resource_groups.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListResourceGroupsWithAuthDetailsResponseBodyResourceGroups(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        create_date: str = None,
        display_name: str = None,
        id: str = None,
        name: str = None,
        status: str = None,
        tags: List[main_models.ListResourceGroupsWithAuthDetailsResponseBodyResourceGroupsTags] = None,
    ):
        # The ID of the Alibaba Cloud account to which the resource group belongs.
        self.account_id = account_id
        # The time when the resource group was created. The time is displayed in UTC.
        self.create_date = create_date
        # The display name of the resource group.
        self.display_name = display_name
        # The ID of your Alibaba Cloud resource group.
        self.id = id
        # The unique identifier of the resource group.
        self.name = name
        # The status of the resource group. Valid values:
        # 
        # *   Creating: The resource group is being created.
        # *   OK: The resource group is created.
        # *   PendingDelete: The resource group is waiting to be deleted.
        self.status = status
        # The tags.
        self.tags = tags

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
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListResourceGroupsWithAuthDetailsResponseBodyResourceGroupsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListResourceGroupsWithAuthDetailsResponseBodyResourceGroupsTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class ListResourceGroupsWithAuthDetailsResponseBodyAuthDetails(DaraModel):
    def __init__(
        self,
        account_scope_auth: bool = None,
        auth_of_resource_groups: List[main_models.ListResourceGroupsWithAuthDetailsResponseBodyAuthDetailsAuthOfResourceGroups] = None,
        resource_type: str = None,
        service: str = None,
    ):
        # Indicates whether the user has account-level authorization for this resource type.
        self.account_scope_auth = account_scope_auth
        # The permission details for the resource groups on the specified resource types.
        self.auth_of_resource_groups = auth_of_resource_groups
        # The resource type.
        # 
        # You can obtain the resource type from the **Resource type** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.resource_type = resource_type
        # The ID of the Alibaba Cloud service.
        # 
        # You can obtain the ID from the **Service code** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.service = service

    def validate(self):
        if self.auth_of_resource_groups:
            for v1 in self.auth_of_resource_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_scope_auth is not None:
            result['AccountScopeAuth'] = self.account_scope_auth

        result['AuthOfResourceGroups'] = []
        if self.auth_of_resource_groups is not None:
            for k1 in self.auth_of_resource_groups:
                result['AuthOfResourceGroups'].append(k1.to_map() if k1 else None)

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service is not None:
            result['Service'] = self.service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountScopeAuth') is not None:
            self.account_scope_auth = m.get('AccountScopeAuth')

        self.auth_of_resource_groups = []
        if m.get('AuthOfResourceGroups') is not None:
            for k1 in m.get('AuthOfResourceGroups'):
                temp_model = main_models.ListResourceGroupsWithAuthDetailsResponseBodyAuthDetailsAuthOfResourceGroups()
                self.auth_of_resource_groups.append(temp_model.from_map(k1))

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Service') is not None:
            self.service = m.get('Service')

        return self

class ListResourceGroupsWithAuthDetailsResponseBodyAuthDetailsAuthOfResourceGroups(DaraModel):
    def __init__(
        self,
        has_permission: bool = None,
        resource_group_id: str = None,
    ):
        # Indicates whether the user has permissions on the resource group for the specified resource type.
        self.has_permission = has_permission
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_permission is not None:
            result['HasPermission'] = self.has_permission

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasPermission') is not None:
            self.has_permission = m.get('HasPermission')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

