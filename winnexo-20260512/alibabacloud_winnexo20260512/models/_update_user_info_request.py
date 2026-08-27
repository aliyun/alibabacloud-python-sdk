# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUserInfoRequest(DaraModel):
    def __init__(
        self,
        avatar: str = None,
        language_preference: str = None,
        name: str = None,
        offering: str = None,
        profile_role_info: str = None,
        self_introduction: str = None,
        tenant_id: str = None,
    ):
        # The profile picture URL.
        self.avatar = avatar
        # The language preference: zh-CN, en-US.
        self.language_preference = language_preference
        # The name.
        self.name = name
        # The user service description. Maximum length: 1000 characters.
        self.offering = offering
        # The user role description (used when profileRole is set to Others). Maximum length: 100 characters.
        self.profile_role_info = profile_role_info
        # The user self-introduction. Maximum length: 1000 characters.
        self.self_introduction = self_introduction
        # The effective tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar is not None:
            result['avatar'] = self.avatar

        if self.language_preference is not None:
            result['languagePreference'] = self.language_preference

        if self.name is not None:
            result['name'] = self.name

        if self.offering is not None:
            result['offering'] = self.offering

        if self.profile_role_info is not None:
            result['profileRoleInfo'] = self.profile_role_info

        if self.self_introduction is not None:
            result['selfIntroduction'] = self.self_introduction

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')

        if m.get('languagePreference') is not None:
            self.language_preference = m.get('languagePreference')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('offering') is not None:
            self.offering = m.get('offering')

        if m.get('profileRoleInfo') is not None:
            self.profile_role_info = m.get('profileRoleInfo')

        if m.get('selfIntroduction') is not None:
            self.self_introduction = m.get('selfIntroduction')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

