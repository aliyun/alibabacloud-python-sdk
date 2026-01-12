# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEcsSpecsRequest(DaraModel):
    def __init__(
        self,
        accelerator_type: str = None,
        instance_types: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_type: str = None,
        sort_by: str = None,
    ):
        # Filter by accelerator type. Valid values:
        # 
        # *   CPU
        # *   GPU
        self.accelerator_type = accelerator_type
        # The instance types to query. Separate the types with commas (,).
        self.instance_types = instance_types
        # The sorting order. Valid values:
        # 
        # *   desc: descending order.
        # *   asc: ascending order.
        self.order = order
        # The number of the page to query. The start value is 1.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The type of the resource. Valid values:
        # 
        # *   ECS
        # *   Lingjun
        self.resource_type = resource_type
        # The field based on which the results are sorted. Valid values:
        # 
        # *   CPU
        # *   GPU
        # *   Memory
        # *   GmtCreateTime
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type

        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')

        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        return self

