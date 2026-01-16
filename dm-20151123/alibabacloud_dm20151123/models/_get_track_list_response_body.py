# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class GetTrackListResponseBody(DaraModel):
    def __init__(
        self,
        offset_create_time: str = None,
        offset_create_time_desc: str = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
        total_pages: int = None,
        data: main_models.GetTrackListResponseBodyData = None,
    ):
        # Used for pagination. Not set for the first query, but for subsequent queries, it should be set to the value of OffsetCreateTime from the previous response. (This field is deprecated)
        self.offset_create_time = offset_create_time
        # (This field is deprecated)
        self.offset_create_time_desc = offset_create_time_desc
        # Current page number
        self.page_no = page_no
        # Number of items per page
        self.page_size = page_size
        # Request ID
        self.request_id = request_id
        # Total number of items
        self.total = total
        self.total_pages = total_pages
        # Tracking data records
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.offset_create_time is not None:
            result['OffsetCreateTime'] = self.offset_create_time

        if self.offset_create_time_desc is not None:
            result['OffsetCreateTimeDesc'] = self.offset_create_time_desc

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        if self.data is not None:
            result['data'] = self.data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OffsetCreateTime') is not None:
            self.offset_create_time = m.get('OffsetCreateTime')

        if m.get('OffsetCreateTimeDesc') is not None:
            self.offset_create_time_desc = m.get('OffsetCreateTimeDesc')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        if m.get('data') is not None:
            temp_model = main_models.GetTrackListResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        return self

class GetTrackListResponseBodyData(DaraModel):
    def __init__(
        self,
        stat: List[main_models.GetTrackListResponseBodyDataStat] = None,
    ):
        self.stat = stat

    def validate(self):
        if self.stat:
            for v1 in self.stat:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['stat'] = []
        if self.stat is not None:
            for k1 in self.stat:
                result['stat'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stat = []
        if m.get('stat') is not None:
            for k1 in m.get('stat'):
                temp_model = main_models.GetTrackListResponseBodyDataStat()
                self.stat.append(temp_model.from_map(k1))

        return self

class GetTrackListResponseBodyDataStat(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        rcpt_click_count: str = None,
        rcpt_click_rate: str = None,
        rcpt_open_count: str = None,
        rcpt_open_rate: str = None,
        rcpt_unique_click_count: str = None,
        rcpt_unique_click_rate: str = None,
        rcpt_unique_open_count: str = None,
        rcpt_unique_open_rate: str = None,
        total_number: str = None,
    ):
        # Creation time
        self.create_time = create_time
        # Click count
        self.rcpt_click_count = rcpt_click_count
        # Click rate
        self.rcpt_click_rate = rcpt_click_rate
        # Number of Opens
        self.rcpt_open_count = rcpt_open_count
        # Open rate
        self.rcpt_open_rate = rcpt_open_rate
        # Unique click count
        self.rcpt_unique_click_count = rcpt_unique_click_count
        # Unique click rate
        self.rcpt_unique_click_rate = rcpt_unique_click_rate
        # Unique open count
        self.rcpt_unique_open_count = rcpt_unique_open_count
        # Unique open rate
        self.rcpt_unique_open_rate = rcpt_unique_open_rate
        # Total number
        self.total_number = total_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.rcpt_click_count is not None:
            result['RcptClickCount'] = self.rcpt_click_count

        if self.rcpt_click_rate is not None:
            result['RcptClickRate'] = self.rcpt_click_rate

        if self.rcpt_open_count is not None:
            result['RcptOpenCount'] = self.rcpt_open_count

        if self.rcpt_open_rate is not None:
            result['RcptOpenRate'] = self.rcpt_open_rate

        if self.rcpt_unique_click_count is not None:
            result['RcptUniqueClickCount'] = self.rcpt_unique_click_count

        if self.rcpt_unique_click_rate is not None:
            result['RcptUniqueClickRate'] = self.rcpt_unique_click_rate

        if self.rcpt_unique_open_count is not None:
            result['RcptUniqueOpenCount'] = self.rcpt_unique_open_count

        if self.rcpt_unique_open_rate is not None:
            result['RcptUniqueOpenRate'] = self.rcpt_unique_open_rate

        if self.total_number is not None:
            result['TotalNumber'] = self.total_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('RcptClickCount') is not None:
            self.rcpt_click_count = m.get('RcptClickCount')

        if m.get('RcptClickRate') is not None:
            self.rcpt_click_rate = m.get('RcptClickRate')

        if m.get('RcptOpenCount') is not None:
            self.rcpt_open_count = m.get('RcptOpenCount')

        if m.get('RcptOpenRate') is not None:
            self.rcpt_open_rate = m.get('RcptOpenRate')

        if m.get('RcptUniqueClickCount') is not None:
            self.rcpt_unique_click_count = m.get('RcptUniqueClickCount')

        if m.get('RcptUniqueClickRate') is not None:
            self.rcpt_unique_click_rate = m.get('RcptUniqueClickRate')

        if m.get('RcptUniqueOpenCount') is not None:
            self.rcpt_unique_open_count = m.get('RcptUniqueOpenCount')

        if m.get('RcptUniqueOpenRate') is not None:
            self.rcpt_unique_open_rate = m.get('RcptUniqueOpenRate')

        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')

        return self

