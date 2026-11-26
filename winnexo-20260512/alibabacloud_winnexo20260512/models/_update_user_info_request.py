# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUserInfoRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        avatar: str = None,
        language_preference: str = None,
        name: str = None,
        offering: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        profile_role_info: str = None,
        self_introduction: str = None,
        tenant_id: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The profile picture URL.
        self.avatar = avatar
        # The language preference: zh-CN or en-US.
        self.language_preference = language_preference
        # The name.
        self.name = name
        # The user service description. Maximum length: 1000 characters.
        self.offering = offering
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The user role description. This parameter is used when profileRole is set to Others. Maximum length: 100 characters.
        self.profile_role_info = profile_role_info
        # The user self-introduction. Maximum length: 1000 characters.
        self.self_introduction = self_introduction
        # The ID of the effective tenant.
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

        if self.avatar is not None:
            result['avatar'] = self.avatar

        if self.language_preference is not None:
            result['languagePreference'] = self.language_preference

        if self.name is not None:
            result['name'] = self.name

        if self.offering is not None:
            result['offering'] = self.offering

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.profile_role_info is not None:
            result['profileRoleInfo'] = self.profile_role_info

        if self.self_introduction is not None:
            result['selfIntroduction'] = self.self_introduction

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')

        if m.get('languagePreference') is not None:
            self.language_preference = m.get('languagePreference')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('offering') is not None:
            self.offering = m.get('offering')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('profileRoleInfo') is not None:
            self.profile_role_info = m.get('profileRoleInfo')

        if m.get('selfIntroduction') is not None:
            self.self_introduction = m.get('selfIntroduction')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

