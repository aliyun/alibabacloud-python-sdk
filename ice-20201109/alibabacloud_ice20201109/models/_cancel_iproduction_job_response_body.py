# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class CancelIProductionJobResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.CancelIProductionJobResponseBodyAccessDeniedDetail = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial. This parameter is returned only if Resource Access Management (RAM) permission verification failed.
        self.access_denied_detail = access_denied_detail
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.CancelIProductionJobResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CancelIProductionJobResponseBodyAccessDeniedDetail(DaraModel):
    def __init__(
        self,
        auth_action: str = None,
        auth_principal_display_name: str = None,
        auth_principal_owner_id: str = None,
        auth_principal_type: str = None,
        encoded_diagnostic_message: str = None,
        no_permission_type: str = None,
        policy_type: str = None,
    ):
        # The operation that failed the permission check.
        self.auth_action = auth_action
        # The identity. Values:
        # 
        # *   RAM user: a UID
        # *   RAM role: RoleName:RoleSessionName
        # *   Federated user: ProviderType/ProviderName
        self.auth_principal_display_name = auth_principal_display_name
        # The account to which the principal belongs.
        self.auth_principal_owner_id = auth_principal_owner_id
        # The type of identity that made the request. Valid values:
        # 
        # *   SubUser: RAM user
        # *   AssumedRoleUser: RAM role
        # *   Federated: SSO federated user
        self.auth_principal_type = auth_principal_type
        # The encoded diagnostic message.
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # The type of policy that resulted in the denial. Valid values:
        # 
        # *   **ImplicitDeny**: The resource holder has not configured a policy for the current user. By default, unauthorized operations are denied.
        # *   **ExplicitDeny**: The RAM policy configured by the resource holder explicitly denies the current user access to the corresponding resources.
        self.no_permission_type = no_permission_type
        # The type of policy that triggered the permission failure.
        # 
        # *   **ControlPolicy**: control policy
        # *   **SessionPolicy**: an additional policy attached to a temporary token.
        # *   **AssumeRolePolicy**: the trust policy of a RAM role.
        # *   **AccountLevelIdentityBasedPolicy**: an identity-based policy at the account level (custom or system).
        # *   **ResourceGroupLevelIdentityBasedPolicy**: an identity-based policy scoped to a resource group.
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_action is not None:
            result['AuthAction'] = self.auth_action

        if self.auth_principal_display_name is not None:
            result['AuthPrincipalDisplayName'] = self.auth_principal_display_name

        if self.auth_principal_owner_id is not None:
            result['AuthPrincipalOwnerId'] = self.auth_principal_owner_id

        if self.auth_principal_type is not None:
            result['AuthPrincipalType'] = self.auth_principal_type

        if self.encoded_diagnostic_message is not None:
            result['EncodedDiagnosticMessage'] = self.encoded_diagnostic_message

        if self.no_permission_type is not None:
            result['NoPermissionType'] = self.no_permission_type

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthAction') is not None:
            self.auth_action = m.get('AuthAction')

        if m.get('AuthPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('AuthPrincipalDisplayName')

        if m.get('AuthPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('AuthPrincipalOwnerId')

        if m.get('AuthPrincipalType') is not None:
            self.auth_principal_type = m.get('AuthPrincipalType')

        if m.get('EncodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('EncodedDiagnosticMessage')

        if m.get('NoPermissionType') is not None:
            self.no_permission_type = m.get('NoPermissionType')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

