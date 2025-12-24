# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeConfigGroupRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        group_ids: List[str] = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
        region_id: str = None,
        statuses: List[str] = None,
        type: str = None,
    ):
        # The ID of the configuration group.
        self.group_id = group_id
        # The IDs of the configuration groups.
        self.group_ids = group_ids
        # The name of the configuration group.
        self.name = name
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The service type of the configuration group.
        # 
        # Valid value:
        # 
        # *   CLOUD_DESKTOP: the cloud computer service.
        self.product_type = product_type
        # The ID of the region. Set the value to `cn-shanghai`.
        self.region_id = region_id
        # The status of the configuration groups.
        self.statuses = statuses
        # The type of the configuration group.
        # 
        # Valid value:
        # 
        # *   Timer: the scheduled task type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.statuses is not None:
            result['Statuses'] = self.statuses

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

