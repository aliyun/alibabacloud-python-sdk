# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListStackEventsRequest(DaraModel):
    def __init__(
        self,
        logical_resource_id: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_type: List[str] = None,
        stack_id: str = None,
        status: List[str] = None,
    ):
        # The logical IDs of the resources.
        self.logical_resource_id = logical_resource_id
        # The number of the page to return.\\
        # Pages start from page 1.\\
        # Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.\\
        # Maximum value: 50.\\
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the stack. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource types.
        self.resource_type = resource_type
        # The stack ID.
        # 
        # This parameter is required.
        self.stack_id = stack_id
        # The status of the resource.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

