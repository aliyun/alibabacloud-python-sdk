# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplyForStreamAccessTokenResponseBody(DaraModel):
    def __init__(
        self,
        access_token: str = None,
        channel_id: str = None,
        request_id: str = None,
        stream_secret: str = None,
    ):
        self.access_token = access_token
        self.channel_id = channel_id
        # Id of the request
        self.request_id = request_id
        self.stream_secret = stream_secret

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token is not None:
            result['AccessToken'] = self.access_token

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stream_secret is not None:
            result['StreamSecret'] = self.stream_secret

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StreamSecret') is not None:
            self.stream_secret = m.get('StreamSecret')

        return self

