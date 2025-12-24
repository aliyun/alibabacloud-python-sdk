# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLiveMessageGroupMessagesRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        begin_time: int = None,
        data_center: str = None,
        end_time: int = None,
        group_id: str = None,
        msg_type: int = None,
        next_page_token: int = None,
        page_size: int = None,
        sort_type: int = None,
    ):
        # The ID of the interactive messaging application to query.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds. If you leave this parameter empty, the earliest available time is used.
        self.begin_time = begin_time
        # The data center. It must be the same as the data center that was specified when you called the [CreateLiveMessageApp](https://help.aliyun.com/document_detail/2848162.html) operation to create the interactive messaging application. Valid values: cn-shanghai and ap-southeast-1 (Singapore).
        self.data_center = data_center
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds. If you leave this parameter empty, the latest available time is used.
        self.end_time = end_time
        # The ID of the group to query.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The type of messages that you want to query. If you leave this parameter empty, all types of messages are queried.
        self.msg_type = msg_type
        # The starting page number for the query. If you leave this parameter empty, the query starts from the first page.
        self.next_page_token = next_page_token
        # The number of entries per page. Valid values: **10 to 50**.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The sort order based on the time when the messages were sent. Valid values:
        # 
        # *   1: ascending order
        # *   2: descending order
        # 
        # This parameter is required.
        self.sort_type = sort_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.data_center is not None:
            result['DataCenter'] = self.data_center

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.msg_type is not None:
            result['MsgType'] = self.msg_type

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_type is not None:
            result['SortType'] = self.sort_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('MsgType') is not None:
            self.msg_type = m.get('MsgType')

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')

        return self

