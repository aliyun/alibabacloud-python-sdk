# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class CreatePxfsAccessTokenResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.CreatePxfsAccessTokenResponseBodyAccessDeniedDetail = None,
        data: main_models.CreatePxfsAccessTokenResponseBodyData = None,
        request_id: str = None,
    ):
        # The details of the access denial.
        self.access_denied_detail = access_denied_detail
        # The response data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.CreatePxfsAccessTokenResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Data') is not None:
            temp_model = main_models.CreatePxfsAccessTokenResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreatePxfsAccessTokenResponseBodyData(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
        expires_at: str = None,
        identity_name: str = None,
        label: str = None,
        port: int = None,
        tenant_id: str = None,
        token: str = None,
        token_id: str = None,
    ):
        # The access endpoint.
        self.endpoint = endpoint
        # The expiration time.
        self.expires_at = expires_at
        # The name of the identity.
        self.identity_name = identity_name
        # The label of the token.
        self.label = label
        # The port.
        self.port = port
        # The tenant ID.
        self.tenant_id = tenant_id
        # The plaintext of the token.
        self.token = token
        # Token ID
        self.token_id = token_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.expires_at is not None:
            result['ExpiresAt'] = self.expires_at

        if self.identity_name is not None:
            result['IdentityName'] = self.identity_name

        if self.label is not None:
            result['Label'] = self.label

        if self.port is not None:
            result['Port'] = self.port

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.token is not None:
            result['Token'] = self.token

        if self.token_id is not None:
            result['TokenId'] = self.token_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('ExpiresAt') is not None:
            self.expires_at = m.get('ExpiresAt')

        if m.get('IdentityName') is not None:
            self.identity_name = m.get('IdentityName')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('TokenId') is not None:
            self.token_id = m.get('TokenId')

        return self

class CreatePxfsAccessTokenResponseBodyAccessDeniedDetail(DaraModel):
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
        # The authentication action.
        self.auth_action = auth_action
        # The display name of the authentication principal.
        self.auth_principal_display_name = auth_principal_display_name
        # The owner ID of the authentication principal.
        self.auth_principal_owner_id = auth_principal_owner_id
        # The type of the authentication principal.
        self.auth_principal_type = auth_principal_type
        # The diagnostic message.
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # The type of the missing permission.
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

