# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUserShrinkRequest(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        password_encrypted: str = None,
        role_codes_shrink: str = None,
        sso_provider: str = None,
        tenant_id: str = None,
        wn_account_id: str = None,
    ):
        # The cluster name.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The base64-encoded password ciphertext encrypted by using RSA-OAEP-SHA256 (required).
        # 
        # This parameter is required.
        self.password_encrypted = password_encrypted
        # The list of new system role codes (full replacement, must contain at least one role). Valid values: SUPER_ADMIN, SYSTEM_ADMIN, SEMANTIC_ADMIN, SKILL_ADMIN, KB_ADMIN, AGENT_ADMIN, and APPLICATION_USER.
        self.role_codes_shrink = role_codes_shrink
        # The SSO provider type. This parameter is optional if the tenant has only one external logon method. This parameter is required if the tenant has multiple external logon methods. Currently, createUser supports BUILD_IN and AGENT_ONE.
        self.sso_provider = sso_provider
        # The ID of the tenant on which the operation takes effect.
        self.tenant_id = tenant_id
        # The WINNEXO logon account (unique identifier, required).
        # 
        # This parameter is required.
        self.wn_account_id = wn_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.password_encrypted is not None:
            result['passwordEncrypted'] = self.password_encrypted

        if self.role_codes_shrink is not None:
            result['roleCodes'] = self.role_codes_shrink

        if self.sso_provider is not None:
            result['ssoProvider'] = self.sso_provider

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.wn_account_id is not None:
            result['wnAccountId'] = self.wn_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('passwordEncrypted') is not None:
            self.password_encrypted = m.get('passwordEncrypted')

        if m.get('roleCodes') is not None:
            self.role_codes_shrink = m.get('roleCodes')

        if m.get('ssoProvider') is not None:
            self.sso_provider = m.get('ssoProvider')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('wnAccountId') is not None:
            self.wn_account_id = m.get('wnAccountId')

        return self

