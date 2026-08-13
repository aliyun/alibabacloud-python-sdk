# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class SyncOrgStructureRequest(DaraModel):
    def __init__(
        self,
        corp_id: str = None,
        departments: List[main_models.SyncOrgStructureRequestDepartments] = None,
        members: List[main_models.SyncOrgStructureRequestMembers] = None,
        platform_type: str = None,
        sso_settings_id: str = None,
        sync_members: bool = None,
        tenant_id: str = None,
    ):
        # 企业标识（必须与 listAvailableConfigs 返回的 corpId 一致）
        # 
        # This parameter is required.
        self.corp_id = corp_id
        # 部门列表（至少包含一个根部门）
        # 
        # This parameter is required.
        self.departments = departments
        # 成员列表（syncMembers=true 时必须提供）
        self.members = members
        # 平台类型: saml / oauth2 / custom
        # 
        # This parameter is required.
        self.platform_type = platform_type
        # SSO 配置 ID（SAML/OAuth2 可选：不传时按 corpId 自动推导；若存在多个 IdP 使用相同 corpId 则必须显式传入，否则报 AMBIGUOUS 错误；custom 不需要）
        self.sso_settings_id = sso_settings_id
        # 是否同步成员关系（custom 模式强制为 false）
        self.sync_members = sync_members
        # 租户ID，公共参数，缺省时使用调用方默认租户
        self.tenant_id = tenant_id

    def validate(self):
        if self.departments:
            for v1 in self.departments:
                 if v1:
                    v1.validate()
        if self.members:
            for v1 in self.members:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corp_id is not None:
            result['corpId'] = self.corp_id

        result['departments'] = []
        if self.departments is not None:
            for k1 in self.departments:
                result['departments'].append(k1.to_map() if k1 else None)

        result['members'] = []
        if self.members is not None:
            for k1 in self.members:
                result['members'].append(k1.to_map() if k1 else None)

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
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')

        self.departments = []
        if m.get('departments') is not None:
            for k1 in m.get('departments'):
                temp_model = main_models.SyncOrgStructureRequestDepartments()
                self.departments.append(temp_model.from_map(k1))

        self.members = []
        if m.get('members') is not None:
            for k1 in m.get('members'):
                temp_model = main_models.SyncOrgStructureRequestMembers()
                self.members.append(temp_model.from_map(k1))

        if m.get('platformType') is not None:
            self.platform_type = m.get('platformType')

        if m.get('ssoSettingsId') is not None:
            self.sso_settings_id = m.get('ssoSettingsId')

        if m.get('syncMembers') is not None:
            self.sync_members = m.get('syncMembers')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

class SyncOrgStructureRequestMembers(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        dept_id: str = None,
        name: str = None,
    ):
        # 用户标识（SAML 场景为邮箱/UPN，需与 rbj_user_account.account_id 匹配）
        self.account_id = account_id
        # 所属部门 ID（必须与 departments 中的 deptId 对应）
        self.dept_id = dept_id
        # 用户姓名（展示用，可选）
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.dept_id is not None:
            result['deptId'] = self.dept_id

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('deptId') is not None:
            self.dept_id = m.get('deptId')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class SyncOrgStructureRequestDepartments(DaraModel):
    def __init__(
        self,
        dept_id: str = None,
        dept_name: str = None,
        order: int = None,
        parent_dept_id: str = None,
    ):
        # 部门 ID（外部标识，客户端自行保证唯一性）
        self.dept_id = dept_id
        # 部门名称
        self.dept_name = dept_name
        # 排序号（数值越小越靠前）
        self.order = order
        # 父部门 ID（null 表示一级部门/根部门）
        self.parent_dept_id = parent_dept_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dept_id is not None:
            result['deptId'] = self.dept_id

        if self.dept_name is not None:
            result['deptName'] = self.dept_name

        if self.order is not None:
            result['order'] = self.order

        if self.parent_dept_id is not None:
            result['parentDeptId'] = self.parent_dept_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deptId') is not None:
            self.dept_id = m.get('deptId')

        if m.get('deptName') is not None:
            self.dept_name = m.get('deptName')

        if m.get('order') is not None:
            self.order = m.get('order')

        if m.get('parentDeptId') is not None:
            self.parent_dept_id = m.get('parentDeptId')

        return self

