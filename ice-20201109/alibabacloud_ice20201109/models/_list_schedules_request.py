# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSchedulesRequest(DaraModel):
    def __init__(
        self,
        channel_name: str = None,
        page_no: int = None,
        page_size: int = None,
        window_duration_seconds: int = None,
    ):
        # The name of the channel.
        # 
        # This parameter is required.
        self.channel_name = channel_name
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The time window of the program schedule.
        # 
        # This parameter is required.
        self.window_duration_seconds = window_duration_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.window_duration_seconds is not None:
            result['WindowDurationSeconds'] = self.window_duration_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('WindowDurationSeconds') is not None:
            self.window_duration_seconds = m.get('WindowDurationSeconds')

        return self

