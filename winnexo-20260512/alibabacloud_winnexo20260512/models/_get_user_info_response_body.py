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
        # 用户头像URL
        self.avatar = avatar
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # CRM 类型
        self.crm_type = crm_type
        # 是否为超级管理员
        self.is_admin = is_admin
        # 当前登录租户是否为系统租户（tenantId=10000）
        self.is_system_tenant = is_system_tenant
        # 用户语言偏好
        self.language_preference = language_preference
        # 错误描述，成功时为空
        self.message = message
        # 文件名
        self.name = name
        # 用户服务描述
        self.offering = offering
        # 用户服务解析结果（JSON格式）
        self.parsed_offering = parsed_offering
        # 用户角色
        self.profile_role = profile_role
        # 用户角色描述（当profileRole为Others时使用）
        self.profile_role_info = profile_role_info
        # 请求追踪 ID
        self.request_id = request_id
        # 用户自我介绍
        self.self_introduction = self_introduction
        # 当前租户ID
        self.tenant_id = tenant_id
        self.tenant_list = tenant_list
        # 当前租户名称
        self.tenant_name = tenant_name
        # 租户类型
        self.tenant_type = tenant_type
        # 用户代码
        self.user_code = user_code
        # 用户ID
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
        # CRM 类型
        self.crm_type = crm_type
        # 租户ID
        self.tenant_id = tenant_id
        # 租户名称
        self.tenant_name = tenant_name
        # 租户类型
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

