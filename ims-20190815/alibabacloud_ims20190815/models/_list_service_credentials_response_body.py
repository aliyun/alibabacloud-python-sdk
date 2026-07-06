# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class ListServiceCredentialsResponseBody(DaraModel):
    def __init__(
        self,
        is_truncated: bool = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        service_credentials: List[main_models.ListServiceCredentialsResponseBodyServiceCredentials] = None,
    ):
        # Indicates whether there is a next page of results.
        self.is_truncated = is_truncated
        # The maximum number of entries per page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The list of service credentials.
        self.service_credentials = service_credentials

    def validate(self):
        if self.service_credentials:
            for v1 in self.service_credentials:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ServiceCredentials'] = []
        if self.service_credentials is not None:
            for k1 in self.service_credentials:
                result['ServiceCredentials'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.service_credentials = []
        if m.get('ServiceCredentials') is not None:
            for k1 in m.get('ServiceCredentials'):
                temp_model = main_models.ListServiceCredentialsResponseBodyServiceCredentials()
                self.service_credentials.append(temp_model.from_map(k1))

        return self

class ListServiceCredentialsResponseBodyServiceCredentials(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        expiration_time: str = None,
        service_credential_id: str = None,
        service_credential_name: str = None,
        service_name: str = None,
        status: str = None,
        user_principal_name: str = None,
    ):
        # The time when the service credential was created.
        self.create_time = create_time
        # The expiration time. This field is not returned for permanent service credentials.
        self.expiration_time = expiration_time
        # The ID of the service credential.
        self.service_credential_id = service_credential_id
        # The name of the service credential.
        self.service_credential_name = service_credential_name
        # The service name of the Alibaba Cloud service.
        self.service_name = service_name
        # The status of the service credential.
        self.status = status
        # The logon name of the Resource Access Management (RAM) user.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time

        if self.service_credential_id is not None:
            result['ServiceCredentialId'] = self.service_credential_id

        if self.service_credential_name is not None:
            result['ServiceCredentialName'] = self.service_credential_name

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.status is not None:
            result['Status'] = self.status

        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')

        if m.get('ServiceCredentialId') is not None:
            self.service_credential_id = m.get('ServiceCredentialId')

        if m.get('ServiceCredentialName') is not None:
            self.service_credential_name = m.get('ServiceCredentialName')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        return self

