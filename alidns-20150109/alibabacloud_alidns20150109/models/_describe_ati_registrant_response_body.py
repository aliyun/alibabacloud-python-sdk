# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeAtiRegistrantResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.DescribeAtiRegistrantResponseBodyAccessDeniedDetail = None,
        cc: str = None,
        city: str = None,
        create_timestamp: str = None,
        document_code: str = None,
        document_type: str = None,
        email: str = None,
        name: str = None,
        phone: str = None,
        registrant_id: str = None,
        reject_reason: str = None,
        request_id: str = None,
        state: str = None,
        status: str = None,
        street: str = None,
        update_timestamp: str = None,
    ):
        # The details of the access denial. This field is returned only when RAM authentication fails.
        self.access_denied_detail = access_denied_detail
        # The country.
        self.cc = cc
        # The city. Default value: Hangzhou.
        self.city = city
        # The creation time (UNIX timestamp).
        self.create_timestamp = create_timestamp
        # The document number of the registrant. The number can be up to 50 characters in length.
        self.document_code = document_code
        # The document type of the registrant. For more information, see the appendix on document types.
        self.document_type = document_type
        # The email address. The address can be up to 300 characters in length.
        self.email = email
        # The name of the registrant. The name can be up to 255 characters in length.
        self.name = name
        # The phone number of the registrant. The number can be up to 128 characters in length. If the country is China and the number is not a mobile phone number, the area code must match the city.
        self.phone = phone
        # The ID of the real-name verified registrant.
        self.registrant_id = registrant_id
        # The reason why the real-name verification was rejected.
        self.reject_reason = reject_reason
        # The unique request ID.
        self.request_id = request_id
        # The state or province.
        self.state = state
        # The real-name verification status. Valid values:
        # 
        # - Approved.
        # - Under review.
        # - Rejected.
        self.status = status
        # The street address.
        self.street = street
        # The update time (UNIX timestamp).
        self.update_timestamp = update_timestamp

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

        if self.cc is not None:
            result['Cc'] = self.cc

        if self.city is not None:
            result['City'] = self.city

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.document_code is not None:
            result['DocumentCode'] = self.document_code

        if self.document_type is not None:
            result['DocumentType'] = self.document_type

        if self.email is not None:
            result['Email'] = self.email

        if self.name is not None:
            result['Name'] = self.name

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.registrant_id is not None:
            result['RegistrantId'] = self.registrant_id

        if self.reject_reason is not None:
            result['RejectReason'] = self.reject_reason

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.state is not None:
            result['State'] = self.state

        if self.status is not None:
            result['Status'] = self.status

        if self.street is not None:
            result['Street'] = self.street

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.DescribeAtiRegistrantResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Cc') is not None:
            self.cc = m.get('Cc')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('DocumentCode') is not None:
            self.document_code = m.get('DocumentCode')

        if m.get('DocumentType') is not None:
            self.document_type = m.get('DocumentType')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('RegistrantId') is not None:
            self.registrant_id = m.get('RegistrantId')

        if m.get('RejectReason') is not None:
            self.reject_reason = m.get('RejectReason')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Street') is not None:
            self.street = m.get('Street')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        return self

class DescribeAtiRegistrantResponseBodyAccessDeniedDetail(DaraModel):
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

