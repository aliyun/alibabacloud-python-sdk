# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSessionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        server_sn: str = None,
        session_id: str = None,
        session_token: str = None,
        wss_endpoint: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The node ID.
        self.server_sn = server_sn
        # The session ID.
        self.session_id = session_id
        # The session credential.
        self.session_token = session_token
        # The WebSocket address.
        self.wss_endpoint = wss_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.server_sn is not None:
            result['ServerSn'] = self.server_sn

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.session_token is not None:
            result['SessionToken'] = self.session_token

        if self.wss_endpoint is not None:
            result['WssEndpoint'] = self.wss_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServerSn') is not None:
            self.server_sn = m.get('ServerSn')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('SessionToken') is not None:
            self.session_token = m.get('SessionToken')

        if m.get('WssEndpoint') is not None:
            self.wss_endpoint = m.get('WssEndpoint')

        return self

