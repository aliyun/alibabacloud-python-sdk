# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePostpayBillRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_time: str = None,
        interval: int = None,
        lang: str = None,
        page_size: int = None,
        start_time: str = None,
    ):
        # The page number of the current page in a paged query.
        self.current_page = current_page
        # The end time of the query, expressed as a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The time interval for querying data. This is an enumeration value. Valid values:
        # 
        # - 3600: queries data at the hourly level.
        # - 86400: queries data at the daily level.
        self.interval = interval
        # The language. This is an enumeration value.
        # Default value: zh.
        # Valid values: en.
        self.lang = lang
        # The maximum number of entries per page in a paged query. Default value: 10.
        self.page_size = page_size
        # The start time of the query, expressed as a UNIX timestamp in seconds.
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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

