# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetResourceOAuth2TokenResponseBody(DaraModel):
    def __init__(
        self,
        access_token: str = None,
        authorization_url: str = None,
        expires_in: int = None,
        request_id: str = None,
        session_status: str = None,
        session_uri: str = None,
    ):
        self.access_token = access_token
        self.authorization_url = authorization_url
        self.expires_in = expires_in
        self.request_id = request_id
        self.session_status = session_status
        self.session_uri = session_uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token is not None:
            result['AccessToken'] = self.access_token

        if self.authorization_url is not None:
            result['AuthorizationURL'] = self.authorization_url

        if self.expires_in is not None:
            result['ExpiresIn'] = self.expires_in

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.session_status is not None:
            result['SessionStatus'] = self.session_status

        if self.session_uri is not None:
            result['SessionURI'] = self.session_uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')

        if m.get('AuthorizationURL') is not None:
            self.authorization_url = m.get('AuthorizationURL')

        if m.get('ExpiresIn') is not None:
            self.expires_in = m.get('ExpiresIn')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SessionStatus') is not None:
            self.session_status = m.get('SessionStatus')

        if m.get('SessionURI') is not None:
            self.session_uri = m.get('SessionURI')

        return self

