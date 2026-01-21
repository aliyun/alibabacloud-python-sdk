# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHybridMonitorSLSGroupRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        slsgroup_name: str = None,
    ):
        # The keyword that is used to search for Logstore groups.
        self.keyword = keyword
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Minimum value: 1. Default value: 10.
        self.page_size = page_size
        self.region_id = region_id
        # The name of the Logstore group.
        self.slsgroup_name = slsgroup_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.slsgroup_name is not None:
            result['SLSGroupName'] = self.slsgroup_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SLSGroupName') is not None:
            self.slsgroup_name = m.get('SLSGroupName')

        return self

