# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RevokeTokenRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
        token: str = None,
        token_type_hint: str = None,
    ):
        # The client ID.
        self.client_id = client_id
        # The client secret.
        self.client_secret = client_secret
        # The token to be revoked.
        # 
        # This parameter is required.
        self.token = token
        # The type of the token. Valid values: access_token refresh_token
        self.token_type_hint = token_type_hint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['client_id'] = self.client_id

        if self.client_secret is not None:
            result['client_secret'] = self.client_secret

        if self.token is not None:
            result['token'] = self.token

        if self.token_type_hint is not None:
            result['token_type_hint'] = self.token_type_hint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('client_id') is not None:
            self.client_id = m.get('client_id')

        if m.get('client_secret') is not None:
            self.client_secret = m.get('client_secret')

        if m.get('token') is not None:
            self.token = m.get('token')

        if m.get('token_type_hint') is not None:
            self.token_type_hint = m.get('token_type_hint')

        return self

