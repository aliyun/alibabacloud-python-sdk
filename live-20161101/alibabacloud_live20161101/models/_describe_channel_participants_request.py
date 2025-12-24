# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeChannelParticipantsRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        order: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # The ID of the application. You can specify only one application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the channel. You can specify only one channel ID.
        # 
        # This parameter is required.
        self.channel_id = channel_id
        # The sort order. Valid values:
        # 
        # *   **asc**: ascending order.
        # *   **desc**: descending order. This is the default value.
        self.order = order
        # The number of the page to return. Default value: 1.
        self.page_num = page_num
        # The number of entries to return on each page. Default value: 10.
        self.page_size = page_size

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

        if self.order is not None:
            result['Order'] = self.order

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

