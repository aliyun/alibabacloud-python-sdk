# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListResourceGroupsRequest(DaraModel):
    def __init__(
        self,
        aliyun_resource_group_id: str = None,
        aliyun_resource_tags: List[main_models.ListResourceGroupsRequestAliyunResourceTags] = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        payment_type: str = None,
        project_id: int = None,
        resource_group_types: List[str] = None,
        sort_by: str = None,
        statuses: List[str] = None,
    ):
        # The ID of the Alibaba Cloud resource group.
        self.aliyun_resource_group_id = aliyun_resource_group_id
        # The Alibaba Cloud tags.
        self.aliyun_resource_tags = aliyun_resource_tags
        # The name of the resource group for fuzzy match.
        self.name = name
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The billing method of the resource group. Valid values:
        # 
        # - PrePaid: Subscription.
        # - PostPaid: Pay-as-you-go.
        self.payment_type = payment_type
        # The ID of the workspace to which the resource group belongs.
        self.project_id = project_id
        # The types of the resource groups to query. **If this parameter is left empty, general-purpose resource groups are queried by default.**
        self.resource_group_types = resource_group_types
        # The fields by which to sort the results. You can sort the results by fields such as scheduled time and start time. The format is \\"Sort field+Sort order (Desc/Asc)\\". Asc can be omitted. Valid values for the sort field:
        # 
        # - Id (Desc/Asc): The ID of the resource group.
        # - Name (Desc/Asc): The name of the resource group.
        # - Remark (Desc/Asc): The description of the resource group.
        # - Type (Desc/Asc): The type of the resource group.
        # - Status (Desc/Asc): The status of the resource group.
        # - Spec (Desc/Asc): The specifications of the resource group.
        # - CreateUser (Desc/Asc): The creator of the resource group.
        # - CreateTime (Desc/Asc): The time when the resource group was created.
        # 
        # Default value: CreateTime Asc.
        self.sort_by = sort_by
        # The statuses of the resource groups to query.
        self.statuses = statuses

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

        if self.resource_group_types is not None:
            result['ResourceGroupTypes'] = self.resource_group_types

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.statuses is not None:
            result['Statuses'] = self.statuses

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunResourceGroupId') is not None:
            self.aliyun_resource_group_id = m.get('AliyunResourceGroupId')

        self.aliyun_resource_tags = []
        if m.get('AliyunResourceTags') is not None:
            for k1 in m.get('AliyunResourceTags'):
                temp_model = main_models.ListResourceGroupsRequestAliyunResourceTags()
                self.aliyun_resource_tags.append(temp_model.from_map(k1))

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
            self.resource_group_types = m.get('ResourceGroupTypes')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')

        return self

class ListResourceGroupsRequestAliyunResourceTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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

