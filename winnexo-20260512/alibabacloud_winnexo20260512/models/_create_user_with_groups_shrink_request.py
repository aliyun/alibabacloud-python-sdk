# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUserWithGroupsShrinkRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        display_name: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        password_encrypted: str = None,
        role_codes_shrink: str = None,
        tenant_id: str = None,
        user_group_ids_shrink: str = None,
        wn_account_id: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The display name of the user. The name must be unique within the tenant and cannot exceed 100 characters in length.
        # 
        # This parameter is required.
        self.display_name = display_name
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The Base64-encoded password ciphertext encrypted by using the RSA-OAEP-SHA256 algorithm.
        # 
        # This parameter is required.
        self.password_encrypted = password_encrypted
        # The list of initial system role codes. If this parameter is not specified, the `APPLICATION_USER` role is assigned by default.
        self.role_codes_shrink = role_codes_shrink
        # The tenant ID. This is a common parameter. In winnexo-cli, pass this parameter explicitly by using `--tenant-id`.
        self.tenant_id = tenant_id
        # The list of initial user group IDs. A maximum of 100 user group IDs can be specified. All user groups must belong to the current tenant.
        self.user_group_ids_shrink = user_group_ids_shrink
        # The WINNEXO logon account. This parameter is a unique identifier and cannot be empty.
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
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.password_encrypted is not None:
            result['passwordEncrypted'] = self.password_encrypted

        if self.role_codes_shrink is not None:
            result['roleCodes'] = self.role_codes_shrink

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.user_group_ids_shrink is not None:
            result['userGroupIds'] = self.user_group_ids_shrink

        if self.wn_account_id is not None:
            result['wnAccountId'] = self.wn_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('passwordEncrypted') is not None:
            self.password_encrypted = m.get('passwordEncrypted')

        if m.get('roleCodes') is not None:
            self.role_codes_shrink = m.get('roleCodes')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('userGroupIds') is not None:
            self.user_group_ids_shrink = m.get('userGroupIds')

        if m.get('wnAccountId') is not None:
            self.wn_account_id = m.get('wnAccountId')

        return self

