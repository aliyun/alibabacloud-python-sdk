# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AccessDeniedDetail(DaraModel):
    def __init__(
        self,
        auth_action: str = None,
        auth_principal_display_name: str = None,
        auth_principal_owner_id: str = None,
        auth_principal_type: str = None,
        encoded_diagnostic_info: str = None,
        no_permission_type: str = None,
        policy_type: str = None,
    ):
        # 被拒绝的 RAM action，如 agentrun:ListTemplates
        self.auth_action = auth_action
        # 鉴权主体展示名
        self.auth_principal_display_name = auth_principal_display_name
        # 鉴权主体所属账号 ID
        self.auth_principal_owner_id = auth_principal_owner_id
        # 鉴权主体类型，如 SubUser、AssumedRoleUser
        self.auth_principal_type = auth_principal_type
        # Base64 编码的诊断信息，可用于 RAM 控制台自诊断
        self.encoded_diagnostic_info = encoded_diagnostic_info
        # 无权限类型：ImplicitDeny 或 ExplicitDeny
        self.no_permission_type = no_permission_type
        # 策略类型，如 ResourceBasedPolicy、IdentityBasedPolicy
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_action is not None:
            result['authAction'] = self.auth_action

        if self.auth_principal_display_name is not None:
            result['authPrincipalDisplayName'] = self.auth_principal_display_name

        if self.auth_principal_owner_id is not None:
            result['authPrincipalOwnerId'] = self.auth_principal_owner_id

        if self.auth_principal_type is not None:
            result['authPrincipalType'] = self.auth_principal_type

        if self.encoded_diagnostic_info is not None:
            result['encodedDiagnosticInfo'] = self.encoded_diagnostic_info

        if self.no_permission_type is not None:
            result['noPermissionType'] = self.no_permission_type

        if self.policy_type is not None:
            result['policyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authAction') is not None:
            self.auth_action = m.get('authAction')

        if m.get('authPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('authPrincipalDisplayName')

        if m.get('authPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('authPrincipalOwnerId')

        if m.get('authPrincipalType') is not None:
            self.auth_principal_type = m.get('authPrincipalType')

        if m.get('encodedDiagnosticInfo') is not None:
            self.encoded_diagnostic_info = m.get('encodedDiagnosticInfo')

        if m.get('noPermissionType') is not None:
            self.no_permission_type = m.get('noPermissionType')

        if m.get('policyType') is not None:
            self.policy_type = m.get('policyType')

        return self

