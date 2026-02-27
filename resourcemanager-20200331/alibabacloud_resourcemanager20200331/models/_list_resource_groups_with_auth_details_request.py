# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class ListResourceGroupsWithAuthDetailsRequest(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        include_tags: bool = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_ids: List[str] = None,
        resource_region_id: str = None,
        resource_types: List[main_models.ListResourceGroupsWithAuthDetailsRequestResourceTypes] = None,
        status: str = None,
        tag: List[main_models.ListResourceGroupsWithAuthDetailsRequestTag] = None,
    ):
        # The display name of the resource group. This parameter specifies a filter condition for the query. Fuzzy search is supported.
        # 
        # The display name can be a maximum of 50 characters in length.
        self.display_name = display_name
        # Specifies whether to return the information of tags. Valid values:
        # 
        # *   false (default)
        # *   true
        # 
        # >  If you set a tag filter condition, the tag information is returned regardless of the `IncludeTags` value.
        self.include_tags = include_tags
        # The identifier of the resource group. This parameter specifies a filter condition for the query. Fuzzy search is supported.
        # 
        # The identifier can be a maximum of 50 characters in length and can contain letters, digits, and hyphens (-).
        self.name = name
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The IDs of the resource groups that you want to query.
        self.resource_group_ids = resource_group_ids
        # The ID of the region where the resource resides.
        self.resource_region_id = resource_region_id
        # The resource types.
        self.resource_types = resource_types
        # The status of the resource group. This parameter specifies a filter condition for the query. Valid values:
        # 
        # *   Creating: The resource group is being created.
        # *   OK: The resource group is created.
        # *   PendingDelete: The resource group is waiting to be deleted.
        self.status = status
        # The tags.
        self.tag = tag

    def validate(self):
        if self.resource_types:
            for v1 in self.resource_types:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.include_tags is not None:
            result['IncludeTags'] = self.include_tags

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        result['ResourceTypes'] = []
        if self.resource_types is not None:
            for k1 in self.resource_types:
                result['ResourceTypes'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('IncludeTags') is not None:
            self.include_tags = m.get('IncludeTags')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        self.resource_types = []
        if m.get('ResourceTypes') is not None:
            for k1 in m.get('ResourceTypes'):
                temp_model = main_models.ListResourceGroupsWithAuthDetailsRequestResourceTypes()
                self.resource_types.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListResourceGroupsWithAuthDetailsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListResourceGroupsWithAuthDetailsRequestTag(DaraModel):
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

class ListResourceGroupsWithAuthDetailsRequestResourceTypes(DaraModel):
    def __init__(
        self,
        resource_type_code: str = None,
        service: str = None,
    ):
        # The resource type.
        # 
        # You can obtain the resource type from the **Resource type** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.resource_type_code = resource_type_code
        # The service code.
        # 
        # You can obtain the code from the **Service code** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_type_code is not None:
            result['ResourceTypeCode'] = self.resource_type_code

        if self.service is not None:
            result['Service'] = self.service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceTypeCode') is not None:
            self.resource_type_code = m.get('ResourceTypeCode')

        if m.get('Service') is not None:
            self.service = m.get('Service')

        return self

