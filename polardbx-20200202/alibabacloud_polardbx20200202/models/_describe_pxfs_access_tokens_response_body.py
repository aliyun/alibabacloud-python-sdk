# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribePxfsAccessTokensResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.DescribePxfsAccessTokensResponseBodyAccessDeniedDetail = None,
        data: main_models.DescribePxfsAccessTokensResponseBodyData = None,
        request_id: str = None,
    ):
        # The detailed reason why access was denied.
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
            temp_model = main_models.DescribePxfsAccessTokensResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Data') is not None:
            temp_model = main_models.DescribePxfsAccessTokensResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePxfsAccessTokensResponseBodyData(DaraModel):
    def __init__(
        self,
        access_tokens: List[main_models.DescribePxfsAccessTokensResponseBodyDataAccessTokens] = None,
    ):
        # The list of access tokens.
        self.access_tokens = access_tokens

    def validate(self):
        if self.access_tokens:
            for v1 in self.access_tokens:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccessTokens'] = []
        if self.access_tokens is not None:
            for k1 in self.access_tokens:
                result['AccessTokens'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_tokens = []
        if m.get('AccessTokens') is not None:
            for k1 in m.get('AccessTokens'):
                temp_model = main_models.DescribePxfsAccessTokensResponseBodyDataAccessTokens()
                self.access_tokens.append(temp_model.from_map(k1))

        return self

class DescribePxfsAccessTokensResponseBodyDataAccessTokens(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        expires_at: str = None,
        identity_name: str = None,
        label: str = None,
        status: str = None,
        token_id: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The expiration time.
        self.expires_at = expires_at
        # The identity name.
        self.identity_name = identity_name
        # The token label.
        self.label = label
        # The status.
        self.status = status
        # Token ID
        self.token_id = token_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.expires_at is not None:
            result['ExpiresAt'] = self.expires_at

        if self.identity_name is not None:
            result['IdentityName'] = self.identity_name

        if self.label is not None:
            result['Label'] = self.label

        if self.status is not None:
            result['Status'] = self.status

        if self.token_id is not None:
            result['TokenId'] = self.token_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExpiresAt') is not None:
            self.expires_at = m.get('ExpiresAt')

        if m.get('IdentityName') is not None:
            self.identity_name = m.get('IdentityName')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TokenId') is not None:
            self.token_id = m.get('TokenId')

        return self

class DescribePxfsAccessTokensResponseBodyAccessDeniedDetail(DaraModel):
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
        # The authorization action.
        self.auth_action = auth_action
        # The identity used for authorization in the request.
        self.auth_principal_display_name = auth_principal_display_name
        # The owner ID of the authorization principal.
        self.auth_principal_owner_id = auth_principal_owner_id
        # The type of the authorization principal.
        self.auth_principal_type = auth_principal_type
        # The diagnostic information.
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # NoPermissionType
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

