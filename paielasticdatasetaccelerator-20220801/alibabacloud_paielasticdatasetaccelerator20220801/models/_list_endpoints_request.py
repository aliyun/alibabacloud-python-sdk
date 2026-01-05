# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEndpointsRequest(DaraModel):
    def __init__(
        self,
        endpoint_ids: str = None,
        instance_ids: str = None,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        slot_ids: str = None,
        sort_by: str = None,
        type: str = None,
    ):
        self.endpoint_ids = endpoint_ids
        # 所属加速实例的ID。
        self.instance_ids = instance_ids
        self.name = name
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.slot_ids = slot_ids
        self.sort_by = sort_by
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_ids is not None:
            result['EndpointIds'] = self.endpoint_ids

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.name is not None:
            result['Name'] = self.name

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.slot_ids is not None:
            result['SlotIds'] = self.slot_ids

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointIds') is not None:
            self.endpoint_ids = m.get('EndpointIds')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SlotIds') is not None:
            self.slot_ids = m.get('SlotIds')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

