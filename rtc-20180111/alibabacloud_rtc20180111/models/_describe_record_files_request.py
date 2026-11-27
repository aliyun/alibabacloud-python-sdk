# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeRecordFilesRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        end_time: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        start_time: str = None,
        task_ids: List[str] = None,
    ):
        # The application ID. Only a single ID can be passed. You can create and query it in the console.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The channel ID. Only a single ID can be passed.
        self.channel_id = channel_id
        # The end time. Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC time).
        self.end_time = end_time
        self.owner_id = owner_id
        # The page number. By default, the first page is queried.
        self.page_num = page_num
        # The number of entries to return on each page. Default value: **10**. Maximum value: **100**.
        self.page_size = page_size
        # The start time. Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC time).
        self.start_time = start_time
        # Recording task ID.
        self.task_ids = task_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')

        return self

