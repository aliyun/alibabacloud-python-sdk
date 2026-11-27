# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeChannelAllUsersRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
    ):
        # Application ID. You can create and query this ID in the console. Only a single ID is supported.
        # 
        # This parameter is required.
        self.app_id = app_id
        # Channel ID to query. Only a single ID is supported.
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

