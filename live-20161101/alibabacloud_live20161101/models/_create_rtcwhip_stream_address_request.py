# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRTCWhipStreamAddressRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        client_token: str = None,
        display_name: str = None,
        expire_time: int = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.channel_id = channel_id
        self.client_token = client_token
        # This parameter is required.
        self.display_name = display_name
        self.expire_time = expire_time
        # This parameter is required.
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

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

