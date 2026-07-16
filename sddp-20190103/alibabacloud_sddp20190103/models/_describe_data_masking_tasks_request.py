# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDataMaskingTasksRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        dst_type: int = None,
        end_time: int = None,
        lang: str = None,
        page_size: int = None,
        search_key: str = None,
        start_time: int = None,
    ):
        # The page number to return.
        self.current_page = current_page
        # The product that the destination data source belongs to. Valid values:
        # 
        # - **1**: MaxCompute.
        # 
        # - **2**: OSS.
        # 
        # - **3**: ADS.
        # 
        # - **4**: OTS.
        # 
        # - **5**: RDS.
        # 
        # - **6**: SELF_DB.
        self.dst_type = dst_type
        # The end time for creating the data masking task. The value is a UNIX timestamp. Unit: milliseconds.
        self.end_time = end_time
        # The language of the request and response. Default value: **zh_cn**. Valid values:
        # 
        # - **zh_cn**: Chinese.
        # 
        # - **en_us**: English.
        self.lang = lang
        # The number of entries to return on each page.
        self.page_size = page_size
        # A keyword to search for tasks. You can search by task name or task ID.
        self.search_key = search_key
        # The start time for creating the task. The value is a UNIX timestamp. Unit: milliseconds.
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

        if self.dst_type is not None:
            result['DstType'] = self.dst_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DstType') is not None:
            self.dst_type = m.get('DstType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

