# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class UpdateUserInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        user: main_models.UpdateUserInfoResponseBodyUser = None,
    ):
        # The error code.
        self.code = code
        # The status code description.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The user information.
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.user is not None:
            result['user'] = self.user.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('user') is not None:
            temp_model = main_models.UpdateUserInfoResponseBodyUser()
            self.user = temp_model.from_map(m.get('user'))

        return self

class UpdateUserInfoResponseBodyUser(DaraModel):
    def __init__(
        self,
        avatar: str = None,
        is_admin: bool = None,
        is_system_tenant: bool = None,
        language_preference: str = None,
        name: str = None,
        offering: str = None,
        parsed_offering: str = None,
        profile_role: str = None,
        profile_role_info: str = None,
        self_introduction: str = None,
        tenant_id: int = None,
        tenant_list: List[main_models.UpdateUserInfoResponseBodyUserTenantList] = None,
        tenant_name: str = None,
        user_code: str = None,
        user_id: int = None,
    ):
        # The user profile picture URL.
        self.avatar = avatar
        # Indicates whether the user is a super administrator.
        self.is_admin = is_admin
        # Indicates whether the current logged-in tenant is a system tenant.
        self.is_system_tenant = is_system_tenant
        # The user language preference.
        self.language_preference = language_preference
        # The username.
        self.name = name
        # The user service description.
        self.offering = offering
        # The parsed user service result in JSON format.
        self.parsed_offering = parsed_offering
        # The user role.
        self.profile_role = profile_role
        # The user role description.
        self.profile_role_info = profile_role_info
        # The user self-introduction.
        self.self_introduction = self_introduction
        # The current tenant ID.
        self.tenant_id = tenant_id
        # The list of tenants to which the user belongs.
        self.tenant_list = tenant_list
        # The current tenant name.
        self.tenant_name = tenant_name
        # The user code.
        self.user_code = user_code
        # The user ID.
        self.user_id = user_id

    def validate(self):
        if self.tenant_list:
            for v1 in self.tenant_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar is not None:
            result['avatar'] = self.avatar

        if self.is_admin is not None:
            result['isAdmin'] = self.is_admin

        if self.is_system_tenant is not None:
            result['isSystemTenant'] = self.is_system_tenant

        if self.language_preference is not None:
            result['languagePreference'] = self.language_preference

        if self.name is not None:
            result['name'] = self.name

        if self.offering is not None:
            result['offering'] = self.offering

        if self.parsed_offering is not None:
            result['parsedOffering'] = self.parsed_offering

        if self.profile_role is not None:
            result['profileRole'] = self.profile_role

        if self.profile_role_info is not None:
            result['profileRoleInfo'] = self.profile_role_info

        if self.self_introduction is not None:
            result['selfIntroduction'] = self.self_introduction

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        result['tenantList'] = []
        if self.tenant_list is not None:
            for k1 in self.tenant_list:
                result['tenantList'].append(k1.to_map() if k1 else None)

        if self.tenant_name is not None:
            result['tenantName'] = self.tenant_name

        if self.user_code is not None:
            result['userCode'] = self.user_code

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')

        if m.get('isAdmin') is not None:
            self.is_admin = m.get('isAdmin')

        if m.get('isSystemTenant') is not None:
            self.is_system_tenant = m.get('isSystemTenant')

        if m.get('languagePreference') is not None:
            self.language_preference = m.get('languagePreference')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('offering') is not None:
            self.offering = m.get('offering')

        if m.get('parsedOffering') is not None:
            self.parsed_offering = m.get('parsedOffering')

        if m.get('profileRole') is not None:
            self.profile_role = m.get('profileRole')

        if m.get('profileRoleInfo') is not None:
            self.profile_role_info = m.get('profileRoleInfo')

        if m.get('selfIntroduction') is not None:
            self.self_introduction = m.get('selfIntroduction')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        self.tenant_list = []
        if m.get('tenantList') is not None:
            for k1 in m.get('tenantList'):
                temp_model = main_models.UpdateUserInfoResponseBodyUserTenantList()
                self.tenant_list.append(temp_model.from_map(k1))

        if m.get('tenantName') is not None:
            self.tenant_name = m.get('tenantName')

        if m.get('userCode') is not None:
            self.user_code = m.get('userCode')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class UpdateUserInfoResponseBodyUserTenantList(DaraModel):
    def __init__(
        self,
        tenant_id: int = None,
        tenant_name: str = None,
    ):
        # The tenant ID.
        self.tenant_id = tenant_id
        # The tenant name.
        self.tenant_name = tenant_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.tenant_name is not None:
            result['tenantName'] = self.tenant_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('tenantName') is not None:
            self.tenant_name = m.get('tenantName')

        return self

