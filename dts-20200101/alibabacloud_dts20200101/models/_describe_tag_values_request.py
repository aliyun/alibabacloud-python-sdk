# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTagValuesRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        key: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The type of the tag key. Valid values:
        # 
        # *   **Custom**: The tag key is created by users.
        # *   **System**: The tag key is created by the system.
        # 
        # >  By default, if the parameter is left empty, both custom tag keys and system tag keys are returned.
        self.category = category
        # The tag key.
        # 
        # >  This parameter is required.
        self.key = key
        # The page number of the start page to return for a tag key that has multiple values. The valid value ranges from 1 to the maximum value of the INTEGER data type. This parameter is often used with the PageSize parameter. Default value: 1.
        self.page_number = page_number
        # The number of tag values to return each time for a tag key that has multiple values. Default value: 20.
        self.page_size = page_size
        # The region ID of the DTS instance. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # The ID of the data migration, data synchronization, or change tracking instance. You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the instance ID.
        # 
        # >  If this parameter is left empty, the values of all tag keys of the current user are returned.
        self.resource_id = resource_id
        # The resource type. Set the value to **ALIYUN::DTS::INSTANCE**.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.key is not None:
            result['Key'] = self.key

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

