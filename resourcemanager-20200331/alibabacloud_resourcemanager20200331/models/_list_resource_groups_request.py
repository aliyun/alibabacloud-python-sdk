# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class ListResourceGroupsRequest(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        include_tags: bool = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        resource_group_ids: List[str] = None,
        status: str = None,
        tag: List[main_models.ListResourceGroupsRequestTag] = None,
    ):
        # The display name of the resource group. This parameter is used as a filter condition. Fuzzy match is supported.
        # 
        # The value cannot exceed 50 characters in length.
        self.display_name = display_name
        # Specifies whether to return tag information. Valid values:
        # 
        # - false (default): Tag information is not returned.
        # 
        # - true: Tag information is returned.
        # > If you specify tag-based filter conditions, tag information is always returned regardless of the value of IncludeTags.
        self.include_tags = include_tags
        # The unique identifier of the resource group. This parameter is used as a filter condition. Fuzzy match is supported.
        # 
        # The value cannot exceed 50 characters in length and can contain letters, digits, and hyphens (-).
        self.name = name
        # The page number.
        # 
        # Minimum value: 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The resource group ID. This parameter is used as a filter condition.
        # 
        # The value cannot exceed 18 characters in length and must start with `rg-`.
        # 
        # > This parameter has been incorporated into the ResourceGroupIds parameter. If you set both ResourceGroupId and ResourceGroupIds, the value of ResourceGroupIds takes precedence.
        self.resource_group_id = resource_group_id
        # The list of resource group IDs. This parameter is used as a filter condition.
        # 
        # You can specify up to 100 resource group IDs.
        # 
        # > If you set both ResourceGroupId and ResourceGroupIds, the value of ResourceGroupIds takes precedence.
        self.resource_group_ids = resource_group_ids
        # The resource group status. This parameter is used as a filter condition. Valid values:
        # 
        # - Creating: The resource group is being created.
        # - OK: The resource group is created.
        # - PendingDelete: The resource group is pending deletion.
        self.status = status
        # The tags. This parameter is used as a filter condition.
        # 
        # You can specify up to 20 tags.
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

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids

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

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListResourceGroupsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListResourceGroupsRequestTag(DaraModel):
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

