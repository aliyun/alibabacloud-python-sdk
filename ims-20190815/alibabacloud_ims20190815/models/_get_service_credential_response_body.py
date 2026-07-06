# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class GetServiceCredentialResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        service_credential: main_models.GetServiceCredentialResponseBodyServiceCredential = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The service credential information.
        self.service_credential = service_credential

    def validate(self):
        if self.service_credential:
            self.service_credential.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_credential is not None:
            result['ServiceCredential'] = self.service_credential.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceCredential') is not None:
            temp_model = main_models.GetServiceCredentialResponseBodyServiceCredential()
            self.service_credential = temp_model.from_map(m.get('ServiceCredential'))

        return self

class GetServiceCredentialResponseBodyServiceCredential(DaraModel):
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
        # The creation time.
        self.create_time = create_time
        # The expiration time. This field is not returned for permanent service credentials.
        self.expiration_time = expiration_time
        # The service credential ID.
        self.service_credential_id = service_credential_id
        # The service credential name.
        self.service_credential_name = service_credential_name
        # The Alibaba Cloud service name.
        self.service_name = service_name
        # The service credential status.
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

