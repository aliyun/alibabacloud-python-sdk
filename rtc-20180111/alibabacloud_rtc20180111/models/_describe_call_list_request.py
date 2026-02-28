# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCallListRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        call_status: str = None,
        channel_id: str = None,
        end_ts: int = None,
        order_by: str = None,
        page_no: int = None,
        page_size: int = None,
        query_mode: str = None,
        start_ts: int = None,
        user_id: str = None,
    ):
        # APP ID。
        # 
        # This parameter is required.
        self.app_id = app_id
        self.call_status = call_status
        self.channel_id = channel_id
        # This parameter is required.
        self.end_ts = end_ts
        self.order_by = order_by
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        self.query_mode = query_mode
        # This parameter is required.
        self.start_ts = start_ts
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.call_status is not None:
            result['CallStatus'] = self.call_status

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.end_ts is not None:
            result['EndTs'] = self.end_ts

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_mode is not None:
            result['QueryMode'] = self.query_mode

        if self.start_ts is not None:
            result['StartTs'] = self.start_ts

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryMode') is not None:
            self.query_mode = m.get('QueryMode')

        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

