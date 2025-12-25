# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class NotifyChannel(DaraModel):
    def __init__(
        self,
        channel_type: str = None,
        enabled_sub_channels: List[str] = None,
        receivers: List[str] = None,
    ):
        self.channel_type = channel_type
        self.enabled_sub_channels = enabled_sub_channels
        self.receivers = receivers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_type is not None:
            result['channelType'] = self.channel_type

        if self.enabled_sub_channels is not None:
            result['enabledSubChannels'] = self.enabled_sub_channels

        if self.receivers is not None:
            result['receivers'] = self.receivers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelType') is not None:
            self.channel_type = m.get('channelType')

        if m.get('enabledSubChannels') is not None:
            self.enabled_sub_channels = m.get('enabledSubChannels')

        if m.get('receivers') is not None:
            self.receivers = m.get('receivers')

        return self

