# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_saf20190521 import models as main_models
from darabonba.model import DaraModel

class ExecuteRequestResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.ExecuteRequestResponseBodyAccessDeniedDetail = None,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The diagnostic details for access denial.
        self.access_denied_detail = access_denied_detail
        # The status code.
        self.code = code
        # The response data, which includes fields such as tags, score, and extend.
        self.data = data
        # The result message.
        self.message = message
        # The request ID.
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

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.ExecuteRequestResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self



class ExecuteRequestResponseBodyAccessDeniedDetail(DaraModel):
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
        # The specific action that the caller attempted to perform, such as s3:PutObject or ec2:DescribeInstances.
        self.auth_action = auth_action
        # The human-readable display name of the request principal, such as the username or role name.
        self.auth_principal_display_name = auth_principal_display_name
        # The UID of the Alibaba Cloud account to which the request principal belongs.
        self.auth_principal_owner_id = auth_principal_owner_id
        # The identity type of the request principal. Valid values:
        # - SubUser: RAM user created by an Alibaba Cloud account.
        # - AssumedRoleUser: Temporary identity obtained by assuming a role.
        self.auth_principal_type = auth_principal_type
        # The Base64-encoded permission diagnostic log used for troubleshooting and automated analysis.
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # The specific denial type for the access denied scenario. Valid values:
        # - ImplicitDeny: Implicit deny due to the lack of explicit authorization.
        # - ExplicitDeny: Explicit deny where the operation is explicitly denied in the policy.
        self.no_permission_type = no_permission_type
        # The scope and type of the policy in the access denied scenario. Valid values:
        # - AccountLevelIdentityBasedPolicy: Account-level identity-based policy that applies to the entire Alibaba Cloud account.
        # - ResourceGroupLevelIdentityBasedPolicy: Resource group-level identity-based policy that applies to a specific resource group.
        # - SessionPolicy: Session policy that applies to a temporary session.
        # - ControlPolicy: Control policy used for core permission control.
        # - AssumeRolePolicy: Trust policy that defines which entities can assume the role.
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

