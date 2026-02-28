# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListVisitorChatMessagesRequest(DaraModel):
    def __init__(
        self,
        access_channel_id: str = None,
        access_token: str = None,
        end_time: str = None,
        instance_id: str = None,
        next_page_token: str = None,
        page_size: int = None,
        sort_order: str = None,
        start_time: int = None,
        visitor_id: str = None,
    ):
        self.access_channel_id = access_channel_id
        self.access_token = access_token
        self.end_time = end_time
        self.instance_id = instance_id
        self.next_page_token = next_page_token
        self.page_size = page_size
        self.sort_order = sort_order
        self.start_time = start_time
        self.visitor_id = visitor_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_channel_id is not None:
            result['AccessChannelId'] = self.access_channel_id

        if self.access_token is not None:
            result['AccessToken'] = self.access_token

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.visitor_id is not None:
            result['VisitorId'] = self.visitor_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessChannelId') is not None:
            self.access_channel_id = m.get('AccessChannelId')

        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('VisitorId') is not None:
            self.visitor_id = m.get('VisitorId')

        return self

