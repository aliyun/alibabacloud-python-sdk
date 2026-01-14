# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartAvatarSessionResponseBody(DaraModel):
    def __init__(
        self,
        channel_token: str = None,
        request_id: str = None,
        session_id: str = None,
        token: str = None,
        web_socket_url: str = None,
    ):
        self.channel_token = channel_token
        self.request_id = request_id
        self.session_id = session_id
        self.token = token
        self.web_socket_url = web_socket_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_token is not None:
            result['channelToken'] = self.channel_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.token is not None:
            result['token'] = self.token

        if self.web_socket_url is not None:
            result['webSocketUrl'] = self.web_socket_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelToken') is not None:
            self.channel_token = m.get('channelToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('token') is not None:
            self.token = m.get('token')

        if m.get('webSocketUrl') is not None:
            self.web_socket_url = m.get('webSocketUrl')

        return self

