# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGdnInstancesRequest(DaraModel):
    def __init__(
        self,
        filter_type: str = None,
        filter_value: str = None,
        gdnid: str = None,
        page_num: str = None,
        page_size: str = None,
        region_id: str = None,
    ):
        self.filter_type = filter_type
        self.filter_value = filter_value
        # GDN ID。
        self.gdnid = gdnid
        self.page_num = page_num
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_type is not None:
            result['FilterType'] = self.filter_type

        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value

        if self.gdnid is not None:
            result['GDNId'] = self.gdnid

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterType') is not None:
            self.filter_type = m.get('FilterType')

        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')

        if m.get('GDNId') is not None:
            self.gdnid = m.get('GDNId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

