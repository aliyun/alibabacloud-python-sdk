# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AuthLoginWithTaobaoUserInfoRequest(DaraModel):
    def __init__(
        self,
        encrypted_taobao_user_identifier: str = None,
        session_id: str = None,
    ):
        # Encrypted Taobao User Identifier
        # 
        # This parameter is required.
        self.encrypted_taobao_user_identifier = encrypted_taobao_user_identifier
        # Session ID
        # 
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encrypted_taobao_user_identifier is not None:
            result['EncryptedTaobaoUserIdentifier'] = self.encrypted_taobao_user_identifier

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptedTaobaoUserIdentifier') is not None:
            self.encrypted_taobao_user_identifier = m.get('EncryptedTaobaoUserIdentifier')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

