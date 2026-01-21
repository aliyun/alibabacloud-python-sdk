# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLogMonitorListRequest(DaraModel):
    def __init__(
        self,
        group_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        search_value: str = None,
    ):
        # The ID of the application group.
        self.group_id = group_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        self.region_id = region_id
        # The keyword that is used to search for log monitoring metrics. Fuzzy match is supported.
        self.search_value = search_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.search_value is not None:
            result['SearchValue'] = self.search_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')

        return self

