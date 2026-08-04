# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MobileRecommendShrinkRequest(DaraModel):
    def __init__(
        self,
        bot_id: str = None,
        count: str = None,
        device_info_shrink: str = None,
        style: str = None,
        type: str = None,
        user_info_shrink: str = None,
    ):
        # Bot ID.
        self.bot_id = bot_id
        # Quantity of recommended Result
        self.count = count
        # Device identification information.
        # 
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # Required when the request type is STYLE.
        self.style = style
        # Request Type: Obtain daily recommendations, hot songs, or genre-based playlists.
        self.type = type
        # User information – userId
        # 
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bot_id is not None:
            result['BotId'] = self.bot_id

        if self.count is not None:
            result['Count'] = self.count

        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink

        if self.style is not None:
            result['Style'] = self.style

        if self.type is not None:
            result['Type'] = self.type

        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BotId') is not None:
            self.bot_id = m.get('BotId')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')

        if m.get('Style') is not None:
            self.style = m.get('Style')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')

        return self

