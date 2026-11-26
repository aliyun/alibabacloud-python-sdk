# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResetPasswordRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        password_encrypted: str = None,
        tenant_id: str = None,
        wn_user_id: str = None,
    ):
        # The platform application token issued by the console. If this parameter is passed, the operation is performed as the user specified by opsUserId or opsUserCode.
        self.app_token = app_token
        # The proxy user code, which is unique within the tenant. This parameter is used only when the application credential is configured as source_uid.
        self.ops_user_code = ops_user_code
        # The proxy user ID, which is the WINNEXO platform user ID. This parameter is used only when the application credential is configured as winnexo_uid.
        self.ops_user_id = ops_user_id
        # The Base64-encoded password ciphertext encrypted by using RSA-OAEP-SHA256. This parameter is required and cannot be empty.
        # 
        # This parameter is required.
        self.password_encrypted = password_encrypted
        # The tenant ID.
        self.tenant_id = tenant_id
        # The target user ID, which is the WINNEXO platform user ID.
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
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.password_encrypted is not None:
            result['passwordEncrypted'] = self.password_encrypted

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.wn_user_id is not None:
            result['wnUserId'] = self.wn_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('passwordEncrypted') is not None:
            self.password_encrypted = m.get('passwordEncrypted')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('wnUserId') is not None:
            self.wn_user_id = m.get('wnUserId')

        return self

