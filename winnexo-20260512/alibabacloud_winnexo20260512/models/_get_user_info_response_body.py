# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class GetUserInfoResponseBody(DaraModel):
    def __init__(
        self,
        avatar: str = None,
        code: str = None,
        crm_type: str = None,
        is_admin: bool = None,
        is_system_tenant: bool = None,
        language_preference: str = None,
        message: str = None,
        name: str = None,
        offering: str = None,
        parsed_offering: str = None,
        profile_role: str = None,
        profile_role_info: str = None,
        request_id: str = None,
        self_introduction: str = None,
        tenant_id: int = None,
        tenant_list: List[main_models.GetUserInfoResponseBodyTenantList] = None,
        tenant_name: str = None,
        tenant_type: str = None,
        user_code: str = None,
        user_id: int = None,
    ):
        # The profile picture URL.
        self.avatar = avatar
        # The error code.
        self.code = code
        # The CRM type.
        self.crm_type = crm_type
        # Indicates whether the user is an enterprise administrator.
        self.is_admin = is_admin
        # Indicates whether the current logon tenant is the system tenant (tenantId=10000).
        self.is_system_tenant = is_system_tenant
        # The language preference.
        self.language_preference = language_preference
        # The status code description.
        self.message = message
        # The username.
        self.name = name
        # The user service description. Maximum length: 1000 characters.
        self.offering = offering
        # The parsed result of the user service (JSON format).
        self.parsed_offering = parsed_offering
        # The user role.
        self.profile_role = profile_role
        # The personal profile.
        self.profile_role_info = profile_role_info
        # The request ID.
        self.request_id = request_id
        # The user self-introduction. Maximum length: 1000 characters.
        self.self_introduction = self_introduction
        # The effective tenant ID.
        self.tenant_id = tenant_id
        # The tenant list.
        self.tenant_list = tenant_list
        # The current tenant name.
        self.tenant_name = tenant_name
        # The tenant type. Valid values:
        # - user: individual.
        # - org: enterprise.
        # - group: group.
        self.tenant_type = tenant_type
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

        if self.code is not None:
            result['code'] = self.code

        if self.crm_type is not None:
            result['crmType'] = self.crm_type

        if self.is_admin is not None:
            result['isAdmin'] = self.is_admin

        if self.is_system_tenant is not None:
            result['isSystemTenant'] = self.is_system_tenant

        if self.language_preference is not None:
            result['languagePreference'] = self.language_preference

        if self.message is not None:
            result['message'] = self.message

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

        if self.request_id is not None:
            result['requestId'] = self.request_id

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

        if self.tenant_type is not None:
            result['tenantType'] = self.tenant_type

        if self.user_code is not None:
            result['userCode'] = self.user_code

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('crmType') is not None:
            self.crm_type = m.get('crmType')

        if m.get('isAdmin') is not None:
            self.is_admin = m.get('isAdmin')

        if m.get('isSystemTenant') is not None:
            self.is_system_tenant = m.get('isSystemTenant')

        if m.get('languagePreference') is not None:
            self.language_preference = m.get('languagePreference')

        if m.get('message') is not None:
            self.message = m.get('message')

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

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('selfIntroduction') is not None:
            self.self_introduction = m.get('selfIntroduction')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        self.tenant_list = []
        if m.get('tenantList') is not None:
            for k1 in m.get('tenantList'):
                temp_model = main_models.GetUserInfoResponseBodyTenantList()
                self.tenant_list.append(temp_model.from_map(k1))

        if m.get('tenantName') is not None:
            self.tenant_name = m.get('tenantName')

        if m.get('tenantType') is not None:
            self.tenant_type = m.get('tenantType')

        if m.get('userCode') is not None:
            self.user_code = m.get('userCode')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class GetUserInfoResponseBodyTenantList(DaraModel):
    def __init__(
        self,
        crm_type: str = None,
        tenant_id: int = None,
        tenant_name: str = None,
        tenant_type: str = None,
    ):
        # The CRM type.
        self.crm_type = crm_type
        # The ID of the tenant to which the task belongs.
        self.tenant_id = tenant_id
        # The tenant name.
        self.tenant_name = tenant_name
        # The tenant type. Valid values:
        # - user: individual.
        # - org: enterprise.
        # - group: group.
        self.tenant_type = tenant_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.crm_type is not None:
            result['crmType'] = self.crm_type

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.tenant_name is not None:
            result['tenantName'] = self.tenant_name

        if self.tenant_type is not None:
            result['tenantType'] = self.tenant_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('crmType') is not None:
            self.crm_type = m.get('crmType')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('tenantName') is not None:
            self.tenant_name = m.get('tenantName')

        if m.get('tenantType') is not None:
            self.tenant_type = m.get('tenantType')

        return self

