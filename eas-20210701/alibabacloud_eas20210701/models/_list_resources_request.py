# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListResourcesRequest(DaraModel):
    def __init__(
        self,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_status: str = None,
        resource_type: str = None,
        sort: str = None,
    ):
        # The sorting order. Valid values:
        # 
        # *   Desc
        # *   Asc
        self.order = order
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 100.
        self.page_size = page_size
        # The ID of the resource group. You can call the [CreateResource](https://help.aliyun.com/document_detail/412111.html) operation to query the ID of the resource group.
        self.resource_id = resource_id
        # The name of the resource group. You can call the [CreateResource](https://help.aliyun.com/document_detail/412111.html) operation to query the name of the resource group.
        self.resource_name = resource_name
        # The resource group status.
        self.resource_status = resource_status
        # The type of the resource group. Valid values:
        # 
        # *   Dedicated: the dedicated resource group.
        # *   SelfManaged: the self-managed resource group.
        self.resource_type = resource_type
        # The condition by which the results are sorted. By default, the query results are sorted by the timestamp type in descending order.
        # 
        # Valid values:
        # 
        # *   PrePaidInstanceCount
        # *   CpuCount
        # *   Memory
        # *   CreateTime
        # *   PostPaidInstanceCount
        # *   MemoryUsed
        # *   GpuCount
        # *   GpuUsed
        # *   CpuUsed
        # *   ServiceCount
        self.sort = sort

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.sort is not None:
            result['Sort'] = self.sort

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        return self

