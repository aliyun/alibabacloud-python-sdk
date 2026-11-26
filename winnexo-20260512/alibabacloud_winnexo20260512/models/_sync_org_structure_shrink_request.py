# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SyncOrgStructureShrinkRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        corp_id: str = None,
        departments_shrink: str = None,
        members_shrink: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        platform_type: str = None,
        sso_settings_id: str = None,
        sync_members: bool = None,
        tenant_id: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The enterprise identifier. This value must match the corpId returned by listAvailableConfigs.
        # 
        # This parameter is required.
        self.corp_id = corp_id
        # The department list. At least one root department must be included.
        # 
        # This parameter is required.
        self.departments_shrink = departments_shrink
        # The member list. This parameter is required when syncMembers is set to true.
        self.members_shrink = members_shrink
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The platform type. Valid values: saml, oauth2, or custom.
        # 
        # This parameter is required.
        self.platform_type = platform_type
        # The SSO configuration ID. For SAML/OAuth2, this parameter is optional. If not specified, the value is automatically derived based on corpId. If multiple IdPs use the same corpId, you must explicitly specify this parameter. Otherwise, an AMBIGUOUS error is returned. This parameter is not required for custom.
        self.sso_settings_id = sso_settings_id
        # Specifies whether to synchronize member relationships. In custom mode, this parameter is forced to false.
        self.sync_members = sync_members
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.corp_id is not None:
            result['corpId'] = self.corp_id

        if self.departments_shrink is not None:
            result['departments'] = self.departments_shrink

        if self.members_shrink is not None:
            result['members'] = self.members_shrink

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.platform_type is not None:
            result['platformType'] = self.platform_type

        if self.sso_settings_id is not None:
            result['ssoSettingsId'] = self.sso_settings_id

        if self.sync_members is not None:
            result['syncMembers'] = self.sync_members

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')

        if m.get('departments') is not None:
            self.departments_shrink = m.get('departments')

        if m.get('members') is not None:
            self.members_shrink = m.get('members')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('platformType') is not None:
            self.platform_type = m.get('platformType')

        if m.get('ssoSettingsId') is not None:
            self.sso_settings_id = m.get('ssoSettingsId')

        if m.get('syncMembers') is not None:
            self.sync_members = m.get('syncMembers')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

