# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRumOcuStatisticDataShrinkRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        filter_shrink: str = None,
        group_shrink: str = None,
        page: int = None,
        page_size: int = None,
        query_type: str = None,
        region_id: str = None,
        start_time: int = None,
    ):
        # The end of the time range to query. Unit: milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The filter condition. Three types of filter conditions are provided:
        # 
        # *   Application name: pid (Note that the application name is displayed, but the application ID is actually specified)
        # *   Application type: siteType
        # *   Data type: dataType
        self.filter_shrink = filter_shrink
        # The grouping fields. Valid values:
        # 
        # *   siteType: The total number of OCUs is grouped by application type.
        # *   dataType: The total number of OCUs is grouped by data type.
        # *   pid: The total number of OCUs is grouped by application ID.
        # *   appName: The total number of OCUs is grouped by application name.
        # *   startTime: The total number of OCUs is grouped by start time.
        self.group_shrink = group_shrink
        # The page number.
        # 
        # This parameter is required.
        self.page = page
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The type of the query. To query non-time series data, set the value to INSTANT. To query time series data, set the value to TIME_SERIES.
        self.query_type = query_type
        # The region ID.
        self.region_id = region_id
        # The beginning of the time range to query. Unit: milliseconds.
        # 
        # This parameter is required.
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

        if self.filter_shrink is not None:
            result['Filter'] = self.filter_shrink

        if self.group_shrink is not None:
            result['Group'] = self.group_shrink

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Filter') is not None:
            self.filter_shrink = m.get('Filter')

        if m.get('Group') is not None:
            self.group_shrink = m.get('Group')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

