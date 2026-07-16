# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEventResultListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        begin_time: int = None,
        current_page: int = None,
        end_time: int = None,
        page_size: int = None,
        reg_id: str = None,
    ):
        # The language of the request and response. Default value: **zh**. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # The start time, in milliseconds (ms).
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The current page number.
        self.current_page = current_page
        # The end time, in milliseconds (ms).
        # 
        # This parameter is required.
        self.end_time = end_time
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The region code.
        self.reg_id = reg_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.begin_time is not None:
            result['beginTime'] = self.begin_time

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        return self

