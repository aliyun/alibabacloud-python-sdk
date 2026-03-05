# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryUnionContentInfoRequest(DaraModel):
    def __init__(
        self,
        channel_id: str = None,
        content_id: str = None,
        proxy_user_id: int = None,
    ):
        # This parameter is required.
        self.channel_id = channel_id
        # This parameter is required.
        self.content_id = content_id
        # This parameter is required.
        self.proxy_user_id = proxy_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.content_id is not None:
            result['ContentId'] = self.content_id

        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('ContentId') is not None:
            self.content_id = m.get('ContentId')

        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')

        return self

