# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMonitorGroupInstanceAttributeRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        group_id: int = None,
        instance_ids: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        total: bool = None,
    ):
        # The abbreviation of the cloud service name.
        # 
        # For more information about how to obtain the abbreviation of a cloud service name, see `metricCategory` in the response parameter `Labels` of the [DescribeProjectMeta](https://help.aliyun.com/document_detail/2513265.html) operation.
        self.category = category
        # The ID of the application group.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The resource ID. Separate multiple resource IDs with commas (,). You can query the details about a maximum of 20 resources at a time.
        self.instance_ids = instance_ids
        # The keyword that is used to search for resources.
        self.keyword = keyword
        # The page number.
        # 
        # Valid values: 1 to 1000000000.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Valid values: 1 to 1000000000.
        # 
        # Default value: 10.
        self.page_size = page_size
        self.region_id = region_id
        # Specifies whether to return the total number of resources in the specified application group. Valid values:
        # 
        # *   true (default)
        # *   false
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

