# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class CreateAtiRegistrantResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.CreateAtiRegistrantResponseBodyAccessDeniedDetail = None,
        create_timestamp: int = None,
        name: str = None,
        registrant_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The details of the access denial. This field is returned only when RAM authentication fails.
        self.access_denied_detail = access_denied_detail
        # The creation time (timestamp).
        self.create_timestamp = create_timestamp
        # The name of the real-name registrant.
        self.name = name
        # The ID of the real-name registrant.
        self.registrant_id = registrant_id
        # The request ID.
        self.request_id = request_id
        # The real-name verification status. Valid values:
        # 
        # - Approved.
        # - Pending review.
        # - Rejected.
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

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.name is not None:
            result['Name'] = self.name

        if self.registrant_id is not None:
            result['RegistrantId'] = self.registrant_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.CreateAtiRegistrantResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegistrantId') is not None:
            self.registrant_id = m.get('RegistrantId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class CreateAtiRegistrantResponseBodyAccessDeniedDetail(DaraModel):
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
        # The encrypted diagnostic message.
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

