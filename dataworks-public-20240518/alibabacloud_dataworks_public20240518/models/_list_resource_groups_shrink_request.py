# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListResourceGroupsShrinkRequest(DaraModel):
    def __init__(
        self,
        aliyun_resource_group_id: str = None,
        aliyun_resource_tags_shrink: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        payment_type: str = None,
        project_id: int = None,
        resource_group_types_shrink: str = None,
        sort_by: str = None,
        statuses_shrink: str = None,
    ):
        # The Alibaba Cloud resource group ID.
        self.aliyun_resource_group_id = aliyun_resource_group_id
        # The list of Alibaba Cloud tags.
        self.aliyun_resource_tags_shrink = aliyun_resource_tags_shrink
        # The name of the resource group. Fuzzy search is supported.
        self.name = name
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The billing method of the resource group. Valid values include:
        # 
        # - `PrePaid`: subscription.
        # 
        # - `PostPaid`: pay-as-you-go.
        self.payment_type = payment_type
        # The ID of the workspace.
        self.project_id = project_id
        # The types of the resource groups to query. **If this parameter is not specified, general-purpose resource groups are queried by default.**
        self.resource_group_types_shrink = resource_group_types_shrink
        # The sorting criterion for the results. The format is `FieldName SortOrder`. `SortOrder` can be `Asc` (ascending) or `Desc` (descending). If you do not specify `SortOrder`, the default is `Asc`. The following fields are supported:
        # 
        # - `Id`: Resource group ID
        # 
        # - `Name`: Resource group name
        # 
        # - `Remark`: Resource group remarks
        # 
        # - `Type`: Resource group type
        # 
        # - `Status`: Resource group status
        # 
        # - `Spec`: Resource group specifications
        # 
        # - `CreateUser`: The user who created the resource group
        # 
        # - `CreateTime`: The time when the resource group was created
        # 
        # Default value: `CreateTime Asc`
        self.sort_by = sort_by
        # The statuses of the resource groups to query.
        self.statuses_shrink = statuses_shrink

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

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.resource_group_types_shrink is not None:
            result['ResourceGroupTypes'] = self.resource_group_types_shrink

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.statuses_shrink is not None:
            result['Statuses'] = self.statuses_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunResourceGroupId') is not None:
            self.aliyun_resource_group_id = m.get('AliyunResourceGroupId')

        if m.get('AliyunResourceTags') is not None:
            self.aliyun_resource_tags_shrink = m.get('AliyunResourceTags')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ResourceGroupTypes') is not None:
            self.resource_group_types_shrink = m.get('ResourceGroupTypes')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Statuses') is not None:
            self.statuses_shrink = m.get('Statuses')

        return self

