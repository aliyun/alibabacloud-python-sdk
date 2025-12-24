# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListVirtualResourceRequest(DaraModel):
    def __init__(
        self,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort: str = None,
        virtual_resource_id: str = None,
        virtual_resource_name: str = None,
    ):
        self.order = order
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 100.
        self.page_size = page_size
        self.sort = sort
        # The ID of the virtual resource group.
        self.virtual_resource_id = virtual_resource_id
        # The name of the virtual resource group.
        self.virtual_resource_name = virtual_resource_name

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

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.virtual_resource_id is not None:
            result['VirtualResourceId'] = self.virtual_resource_id

        if self.virtual_resource_name is not None:
            result['VirtualResourceName'] = self.virtual_resource_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('VirtualResourceId') is not None:
            self.virtual_resource_id = m.get('VirtualResourceId')

        if m.get('VirtualResourceName') is not None:
            self.virtual_resource_name = m.get('VirtualResourceName')

        return self

