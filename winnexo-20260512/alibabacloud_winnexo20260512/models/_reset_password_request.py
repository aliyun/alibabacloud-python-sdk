# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResetPasswordRequest(DaraModel):
    def __init__(
        self,
        password_encrypted: str = None,
        tenant_id: str = None,
        wn_user_id: str = None,
    ):
        # The base64-encoded password ciphertext encrypted with RSA-OAEP-SHA256. This parameter is required and cannot be empty.
        # 
        # This parameter is required.
        self.password_encrypted = password_encrypted
        # The tenant ID.
        self.tenant_id = tenant_id
        # The ID of the target user (WINNEXO platform user ID).
        # 
        # This parameter is required.
        self.wn_user_id = wn_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.password_encrypted is not None:
            result['passwordEncrypted'] = self.password_encrypted

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.wn_user_id is not None:
            result['wnUserId'] = self.wn_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('passwordEncrypted') is not None:
            self.password_encrypted = m.get('passwordEncrypted')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('wnUserId') is not None:
            self.wn_user_id = m.get('wnUserId')

        return self

