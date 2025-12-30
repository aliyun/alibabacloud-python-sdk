# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePlayListRequest(DaraModel):
    def __init__(
        self,
        begin_ts: str = None,
        end_ts: str = None,
        order_name: str = None,
        order_type: str = None,
        page_no: int = None,
        page_size: int = None,
        play_type: str = None,
        status: str = None,
        trace_id: str = None,
    ):
        # The beginning of the time range to query. By default, the system queries data of the current day.
        # 
        # This parameter is required.
        self.begin_ts = begin_ts
        # The end of the time range to query. The time range cannot exceed 24 hours.
        # 
        # This parameter is required.
        self.end_ts = end_ts
        # The criteria by which the sorting is performed. Valid values:
        # 
        # - FirstFrameDuration
        # - PlayDuration
        # - VideoDuration
        # - StuckDuration
        self.order_name = order_name
        # The sort order. Valid values:
        # 
        # - DESC: descending order.
        # - ASC: ascending order.
        self.order_type = order_type
        # The page number. Default value: 1.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The playback type. Valid value: 
        # 
        # - vod
        self.play_type = play_type
        # The playback status. Valid values:
        # 
        # - complete
        # - playing
        # - unusual: A playback error occurs.
        self.status = status
        # The TraceId of the player.
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_ts is not None:
            result['BeginTs'] = self.begin_ts

        if self.end_ts is not None:
            result['EndTs'] = self.end_ts

        if self.order_name is not None:
            result['OrderName'] = self.order_name

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.play_type is not None:
            result['PlayType'] = self.play_type

        if self.status is not None:
            result['Status'] = self.status

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTs') is not None:
            self.begin_ts = m.get('BeginTs')

        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')

        if m.get('OrderName') is not None:
            self.order_name = m.get('OrderName')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PlayType') is not None:
            self.play_type = m.get('PlayType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

