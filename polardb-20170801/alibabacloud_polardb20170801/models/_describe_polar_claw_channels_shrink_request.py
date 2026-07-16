# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePolarClawChannelsShrinkRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        channel_list_shrink: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The channel IDs to query. Leave this parameter empty to return all channels.
        self.channel_list_shrink = channel_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.channel_list_shrink is not None:
            result['ChannelList'] = self.channel_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ChannelList') is not None:
            self.channel_list_shrink = m.get('ChannelList')

        return self

