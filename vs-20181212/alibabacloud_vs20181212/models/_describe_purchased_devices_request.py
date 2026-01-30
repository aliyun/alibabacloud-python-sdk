# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePurchasedDevicesRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        id: str = None,
        name: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        sort_by: str = None,
        sort_direction: str = None,
        sub_type: str = None,
        type: str = None,
        vendor: str = None,
    ):
        self.group_id = group_id
        self.id = id
        self.name = name
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.sort_by = sort_by
        self.sort_direction = sort_direction
        self.sub_type = sub_type
        self.type = type
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction

        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        if self.type is not None:
            result['Type'] = self.type

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

