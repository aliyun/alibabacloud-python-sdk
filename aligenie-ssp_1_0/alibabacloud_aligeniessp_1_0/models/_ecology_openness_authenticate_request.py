# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EcologyOpennessAuthenticateRequest(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        login_state_access_token: str = None,
    ):
        # entity key
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # entity Type
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # logon state access token
        # 
        # This parameter is required.
        self.login_state_access_token = login_state_access_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key

        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type

        if self.login_state_access_token is not None:
            result['LoginStateAccessToken'] = self.login_state_access_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')

        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')

        if m.get('LoginStateAccessToken') is not None:
            self.login_state_access_token = m.get('LoginStateAccessToken')

        return self

