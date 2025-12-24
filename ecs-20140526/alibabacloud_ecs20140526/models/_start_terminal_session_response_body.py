# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartTerminalSessionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        security_token: str = None,
        session_id: str = None,
        web_socket_url: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The security token included in the WebSocket request header. The system uses this token to authenticate the request.
        self.security_token = security_token
        # The session ID.
        self.session_id = session_id
        # The URL of the WebSocket session that is used to connect to the instance. The URL includes the session ID (`SessionId`) and the authentication token (`SecurityToken`).
        self.web_socket_url = web_socket_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.web_socket_url is not None:
            result['WebSocketUrl'] = self.web_socket_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('WebSocketUrl') is not None:
            self.web_socket_url = m.get('WebSocketUrl')

        return self

