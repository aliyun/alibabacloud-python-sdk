# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class SubmitAtiAgentRegisterInfoResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.SubmitAtiAgentRegisterInfoResponseBodyAccessDeniedDetail = None,
        request_id: str = None,
        status: bool = None,
    ):
        # The access denied details. This field is returned only when RAM authentication fails.
        self.access_denied_detail = access_denied_detail
        # The unique request ID.
        self.request_id = request_id
        # The Agent status. Valid values:
        # 
        # - Draft: The Agent registration form is being filled in and has not been formally submitted. In the Draft state, only modification and detail viewing operations are supported. Other operations are not supported.
        # - Private CA Pending Issuance: The Agent registration has been formally submitted. Alibaba Cloud has completed the ACME DNS-01 pre-check and submitted the registration information and generated DNS records to CNNIC. The system is waiting for CNNIC to approve and issue the Private CA and complete TL sealing.
        # - DNS Pending Verification: CNNIC has approved the request, issued the Private CA certificate, and completed TL sealing, but the DNS records of the user have not been verified. The user needs to add the corresponding DNS records in domain name resolution and complete verification.
        # - Active: All processes are complete. The Private CA certificate has been issued, TL has been sealed, and DNS records have been verified. The Agent is activated and can be discovered and trusted across the network.
        # - Expired: The Agent identity certificate has expired, and the user did not complete certificate renewal within the validity period.
        # - Revoked: The Agent certificate has been revoked, DNS records have been cleaned up, and the Agent cannot be discovered or trusted. It cannot be restored to the Active state.
        self.status = status

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.SubmitAtiAgentRegisterInfoResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class SubmitAtiAgentRegisterInfoResponseBodyAccessDeniedDetail(DaraModel):
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
        # The unauthorized operation that was attempted.
        self.auth_action = auth_action
        # The display name of the authorization principal.
        self.auth_principal_display_name = auth_principal_display_name
        # The owner ID of the authorization principal.
        self.auth_principal_owner_id = auth_principal_owner_id
        # The identity type.
        self.auth_principal_type = auth_principal_type
        # The encrypted complete diagnostic message.
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # The reason for the authentication failure. Valid values:
        # - ExplicitDeny: explicit deny.
        # - ImplicitDeny: implicit deny.
        self.no_permission_type = no_permission_type
        # The policy type.
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

