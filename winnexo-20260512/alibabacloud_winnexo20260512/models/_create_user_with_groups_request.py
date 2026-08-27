# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateUserWithGroupsRequest(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        password_encrypted: str = None,
        role_codes: List[str] = None,
        tenant_id: str = None,
        user_group_ids: List[str] = None,
        wn_account_id: str = None,
    ):
        # The display name of the user (unique within the tenant, required, up to 100 characters).
        # 
        # This parameter is required.
        self.display_name = display_name
        # The Base64-encoded password ciphertext encrypted by RSA-OAEP-SHA256 (required).
        # 
        # This parameter is required.
        self.password_encrypted = password_encrypted
        # The list of system role codes. Valid values: SUPER_ADMIN, SYSTEM_ADMIN, SEMANTIC_ADMIN, SKILL_ADMIN, KB_ADMIN, AGENT_ADMIN, and APPLICATION_USER. Default value: APPLICATION_USER.
        self.role_codes = role_codes
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id
        # The list of initial user group IDs. This parameter is optional. All user groups must belong to the current tenant.
        self.user_group_ids = user_group_ids
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

        if self.role_codes is not None:
            result['roleCodes'] = self.role_codes

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.user_group_ids is not None:
            result['userGroupIds'] = self.user_group_ids

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
            self.role_codes = m.get('roleCodes')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('userGroupIds') is not None:
            self.user_group_ids = m.get('userGroupIds')

        if m.get('wnAccountId') is not None:
            self.wn_account_id = m.get('wnAccountId')

        return self

