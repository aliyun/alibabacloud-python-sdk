# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class ListAtiRegistrantsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.ListAtiRegistrantsResponseBodyAccessDeniedDetail = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        registrants: main_models.ListAtiRegistrantsResponseBodyRegistrants = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        # The details of the access denial. This field is returned only when RAM authentication fails.
        self.access_denied_detail = access_denied_detail
        # The maximum number of records to return in this request.
        self.max_results = max_results
        # The token for the next query.
        self.next_token = next_token
        # The current page number. Minimum value: 1. Default value: 1.
        self.page_number = page_number
        # The number of rows per page in a paged query. Maximum value: 100. Default value: 20.
        self.page_size = page_size
        self.registrants = registrants
        # The unique request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_items = total_items
        # The total number of pages.
        self.total_pages = total_pages

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.registrants:
            self.registrants.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.registrants is not None:
            result['Registrants'] = self.registrants.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_items is not None:
            result['TotalItems'] = self.total_items

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.ListAtiRegistrantsResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Registrants') is not None:
            temp_model = main_models.ListAtiRegistrantsResponseBodyRegistrants()
            self.registrants = temp_model.from_map(m.get('Registrants'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class ListAtiRegistrantsResponseBodyRegistrants(DaraModel):
    def __init__(
        self,
        registrant: List[main_models.ListAtiRegistrantsResponseBodyRegistrantsRegistrant] = None,
    ):
        self.registrant = registrant

    def validate(self):
        if self.registrant:
            for v1 in self.registrant:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Registrant'] = []
        if self.registrant is not None:
            for k1 in self.registrant:
                result['Registrant'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.registrant = []
        if m.get('Registrant') is not None:
            for k1 in m.get('Registrant'):
                temp_model = main_models.ListAtiRegistrantsResponseBodyRegistrantsRegistrant()
                self.registrant.append(temp_model.from_map(k1))

        return self

class ListAtiRegistrantsResponseBodyRegistrantsRegistrant(DaraModel):
    def __init__(
        self,
        cc: str = None,
        city: str = None,
        create_timestamp: str = None,
        document_code: str = None,
        document_type: str = None,
        email: str = None,
        name: str = None,
        registrant_id: str = None,
        state: str = None,
        status: str = None,
        update_timestamp: str = None,
    ):
        self.cc = cc
        self.city = city
        self.create_timestamp = create_timestamp
        self.document_code = document_code
        self.document_type = document_type
        self.email = email
        self.name = name
        self.registrant_id = registrant_id
        self.state = state
        self.status = status
        self.update_timestamp = update_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.registrant_id is not None:
            result['RegistrantId'] = self.registrant_id

        if self.state is not None:
            result['State'] = self.state

        if self.status is not None:
            result['Status'] = self.status

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('RegistrantId') is not None:
            self.registrant_id = m.get('RegistrantId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        return self

class ListAtiRegistrantsResponseBodyAccessDeniedDetail(DaraModel):
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

