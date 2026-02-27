# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class ListResourceGroupsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        resource_groups: main_models.ListResourceGroupsResponseBodyResourceGroups = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        self.resource_groups = resource_groups
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.resource_groups:
            self.resource_groups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_groups is not None:
            result['ResourceGroups'] = self.resource_groups.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroups') is not None:
            temp_model = main_models.ListResourceGroupsResponseBodyResourceGroups()
            self.resource_groups = temp_model.from_map(m.get('ResourceGroups'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListResourceGroupsResponseBodyResourceGroups(DaraModel):
    def __init__(
        self,
        resource_group: List[main_models.ListResourceGroupsResponseBodyResourceGroupsResourceGroup] = None,
    ):
        self.resource_group = resource_group

    def validate(self):
        if self.resource_group:
            for v1 in self.resource_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ResourceGroup'] = []
        if self.resource_group is not None:
            for k1 in self.resource_group:
                result['ResourceGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_group = []
        if m.get('ResourceGroup') is not None:
            for k1 in m.get('ResourceGroup'):
                temp_model = main_models.ListResourceGroupsResponseBodyResourceGroupsResourceGroup()
                self.resource_group.append(temp_model.from_map(k1))

        return self

class ListResourceGroupsResponseBodyResourceGroupsResourceGroup(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        create_date: str = None,
        display_name: str = None,
        id: str = None,
        name: str = None,
        status: str = None,
        tags: main_models.ListResourceGroupsResponseBodyResourceGroupsResourceGroupTags = None,
    ):
        self.account_id = account_id
        self.create_date = create_date
        self.display_name = display_name
        self.id = id
        self.name = name
        self.status = status
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

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

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

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

        if m.get('Tags') is not None:
            temp_model = main_models.ListResourceGroupsResponseBodyResourceGroupsResourceGroupTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class ListResourceGroupsResponseBodyResourceGroupsResourceGroupTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.ListResourceGroupsResponseBodyResourceGroupsResourceGroupTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListResourceGroupsResponseBodyResourceGroupsResourceGroupTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListResourceGroupsResponseBodyResourceGroupsResourceGroupTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
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

