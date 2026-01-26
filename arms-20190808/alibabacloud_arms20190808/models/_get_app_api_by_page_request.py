# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAppApiByPageRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_time: int = None,
        interval_mills: int = None,
        pid: str = None,
        page_size: int = None,
        region_id: str = None,
        start_time: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # The end of the time range to query. Unit: milliseconds.
        self.end_time = end_time
        # The time interval between the data shards to be queried. Unit: milliseconds. Minimum value: 60000. Maximum value: 2147483647.
        self.interval_mills = interval_mills
        # The process identifier (PID) of the application. For information about how to obtain a PID, see [Obtain the PID of an application](https://www.alibabacloud.com/help/zh/doc-detail/186100.htm?spm=a2cdw.13409063.0.0.7a72281f0bkTfx#title-imy-7gj-qhr).
        # 
        # This parameter is required.
        self.pid = pid
        # The number of entries to return on each page. This parameter is no longer supported. The number of entries to return on each page. Default value: 10.
        self.page_size = page_size
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The beginning of the time range to query. Unit: milliseconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.interval_mills is not None:
            result['IntervalMills'] = self.interval_mills

        if self.pid is not None:
            result['PId'] = self.pid

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IntervalMills') is not None:
            self.interval_mills = m.get('IntervalMills')

        if m.get('PId') is not None:
            self.pid = m.get('PId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

