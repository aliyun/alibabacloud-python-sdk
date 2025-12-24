# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeFlowStatisticRequest(DaraModel):
    def __init__(
        self,
        desktop_id: str = None,
        office_site_id: str = None,
        page_number: int = None,
        page_size: int = None,
        period: int = None,
        region_id: str = None,
    ):
        # The ID of the cloud computer.
        self.desktop_id = desktop_id
        # The office network ID.
        # 
        # This parameter is required.
        self.office_site_id = office_site_id
        # The number of the page to return.\\
        # Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The statistic collection interval. Unit: seconds.
        # 
        # Valid values:
        # 
        # *   3600: 1 hour
        # *   10800: 3 hours
        # *   86400: 24 hours
        # 
        # This parameter is required.
        self.period = period
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

