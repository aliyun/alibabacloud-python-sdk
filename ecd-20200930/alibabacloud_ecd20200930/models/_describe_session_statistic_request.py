# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSessionStatisticRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        office_site_id: str = None,
        period: int = None,
        region_id: str = None,
        search_region_id: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query.
        self.end_time = end_time
        # The workspace ID.
        self.office_site_id = office_site_id
        # The query interval. Unit: seconds. Valid values:
        # 
        # *   60
        # *   120
        self.period = period
        # The region ID.
        self.region_id = region_id
        # Specifies to search for session information by region ID. This parameter is used to filter desktop information of a specific region.
        self.search_region_id = search_region_id
        # The beginning of the time range to query.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.search_region_id is not None:
            result['SearchRegionId'] = self.search_region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SearchRegionId') is not None:
            self.search_region_id = m.get('SearchRegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

