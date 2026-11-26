# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class SyncOrgStructureRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        corp_id: str = None,
        departments: List[main_models.SyncOrgStructureRequestDepartments] = None,
        members: List[main_models.SyncOrgStructureRequestMembers] = None,
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
        self.departments = departments
        # The member list. This parameter is required when syncMembers is set to true.
        self.members = members
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
        if self.app_token is not None:
            result['appToken'] = self.app_token

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

class SyncOrgStructureRequestMembers(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        dept_id: str = None,
        name: str = None,
    ):
        # The user identifier. In the SAML scenario, this is an email address or UPN, which must match rbj_user_account.account_id.
        self.account_id = account_id
        # The department ID to which the member belongs. This value must correspond to a deptId in the departments list.
        self.dept_id = dept_id
        # The username for display purposes. This parameter is optional.
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
        # The department ID. This is an external identifier. The client is responsible for ensuring uniqueness.
        self.dept_id = dept_id
        # The department name.
        self.dept_name = dept_name
        # The sort order. A smaller value indicates a higher priority.
        self.order = order
        # The parent department ID. A value of null indicates a top-level department or root department.
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

