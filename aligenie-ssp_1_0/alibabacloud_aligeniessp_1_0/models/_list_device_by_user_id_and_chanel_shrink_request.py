# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDeviceByUserIdAndChanelShrinkRequest(DaraModel):
    def __init__(
        self,
        channel_info_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # Activation channel, such as WeChat mini program or third-party app.
        # 
        # This parameter is required.
        self.channel_info_shrink = channel_info_shrink
        # List of User Identifier information.
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
        if self.channel_info_shrink is not None:
            result['ChannelInfo'] = self.channel_info_shrink

        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelInfo') is not None:
            self.channel_info_shrink = m.get('ChannelInfo')

        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')

        return self

