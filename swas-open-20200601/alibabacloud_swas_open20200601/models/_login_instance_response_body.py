# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LoginInstanceResponseBody(DaraModel):
    def __init__(
        self,
        protocol: str = None,
        redirect_url: str = None,
        request_id: str = None,
        security_token: str = None,
        session_id: str = None,
    ):
        # The session protocol.
        self.protocol = protocol
        # The URL of the remote logon desktop.
        self.redirect_url = redirect_url
        # The request ID.
        self.request_id = request_id
        # The security token.
        self.security_token = security_token
        # The session ID.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.redirect_url is not None:
            result['RedirectUrl'] = self.redirect_url

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RedirectUrl') is not None:
            self.redirect_url = m.get('RedirectUrl')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

