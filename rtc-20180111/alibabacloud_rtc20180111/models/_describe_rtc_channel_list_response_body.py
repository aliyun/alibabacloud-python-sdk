# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeRtcChannelListResponseBody(DaraModel):
    def __init__(
        self,
        channel_list: main_models.DescribeRtcChannelListResponseBodyChannelList = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_cnt: int = None,
    ):
        self.channel_list = channel_list
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total_cnt = total_cnt

    def validate(self):
        if self.channel_list:
            self.channel_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_list is not None:
            result['ChannelList'] = self.channel_list.to_map()

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_cnt is not None:
            result['TotalCnt'] = self.total_cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelList') is not None:
            temp_model = main_models.DescribeRtcChannelListResponseBodyChannelList()
            self.channel_list = temp_model.from_map(m.get('ChannelList'))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCnt') is not None:
            self.total_cnt = m.get('TotalCnt')

        return self

class DescribeRtcChannelListResponseBodyChannelList(DaraModel):
    def __init__(
        self,
        channel_list: List[main_models.DescribeRtcChannelListResponseBodyChannelListChannelList] = None,
    ):
        self.channel_list = channel_list

    def validate(self):
        if self.channel_list:
            for v1 in self.channel_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ChannelList'] = []
        if self.channel_list is not None:
            for k1 in self.channel_list:
                result['ChannelList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.channel_list = []
        if m.get('ChannelList') is not None:
            for k1 in m.get('ChannelList'):
                temp_model = main_models.DescribeRtcChannelListResponseBodyChannelListChannelList()
                self.channel_list.append(temp_model.from_map(k1))

        return self

class DescribeRtcChannelListResponseBodyChannelListChannelList(DaraModel):
    def __init__(
        self,
        call_area: main_models.DescribeRtcChannelListResponseBodyChannelListChannelListCallArea = None,
        channel_id: str = None,
        end_time: str = None,
        start_time: str = None,
        total_user_cnt: int = None,
    ):
        self.call_area = call_area
        self.channel_id = channel_id
        self.end_time = end_time
        self.start_time = start_time
        self.total_user_cnt = total_user_cnt

    def validate(self):
        if self.call_area:
            self.call_area.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_area is not None:
            result['CallArea'] = self.call_area.to_map()

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.total_user_cnt is not None:
            result['TotalUserCnt'] = self.total_user_cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallArea') is not None:
            temp_model = main_models.DescribeRtcChannelListResponseBodyChannelListChannelListCallArea()
            self.call_area = temp_model.from_map(m.get('CallArea'))

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TotalUserCnt') is not None:
            self.total_user_cnt = m.get('TotalUserCnt')

        return self

class DescribeRtcChannelListResponseBodyChannelListChannelListCallArea(DaraModel):
    def __init__(
        self,
        call_area: List[str] = None,
    ):
        self.call_area = call_area

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_area is not None:
            result['CallArea'] = self.call_area

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallArea') is not None:
            self.call_area = m.get('CallArea')

        return self

