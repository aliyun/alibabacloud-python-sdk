# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteChannelRequest(DaraModel):
    def __init__(
        self,
        channel_name: str = None,
    ):
        # The name of the channel.
        # 
        # This parameter is required.
        self.channel_name = channel_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')

        return self

