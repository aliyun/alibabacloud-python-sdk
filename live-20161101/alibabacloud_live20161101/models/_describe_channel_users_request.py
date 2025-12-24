# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeChannelUsersRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
    ):
        # The application ID. You can specify only one application ID in a request.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The channel ID. You can specify only one channel ID in a request.
        # 
        # This parameter is required.
        self.channel_id = channel_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        return self

