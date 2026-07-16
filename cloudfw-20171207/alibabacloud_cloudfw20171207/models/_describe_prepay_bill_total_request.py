# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePrepayBillTotalRequest(DaraModel):
    def __init__(
        self,
        bill_type: str = None,
        current_page: int = None,
        end_time: str = None,
        lang: str = None,
        page_size: int = None,
        start_time: str = None,
    ):
        # The billing type. Valid values:
        # - elastic_traffic: elastic traffic.
        # - sdl: sensitive data leak detection traffic.
        self.bill_type = bill_type
        # The page number for a paged query. Default value: 1.
        self.current_page = current_page
        # The end time. Specify a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The language. Valid values:
        # - zh
        # - en
        # 
        # Default value: zh.
        self.lang = lang
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The start time of the query. Specify a UNIX timestamp in seconds.
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
        if self.bill_type is not None:
            result['BillType'] = self.bill_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

