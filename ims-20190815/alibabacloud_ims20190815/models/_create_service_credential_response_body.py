# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class CreateServiceCredentialResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        service_credential: main_models.CreateServiceCredentialResponseBodyServiceCredential = None,
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
            temp_model = main_models.CreateServiceCredentialResponseBodyServiceCredential()
            self.service_credential = temp_model.from_map(m.get('ServiceCredential'))

        return self

class CreateServiceCredentialResponseBodyServiceCredential(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        expiration_time: str = None,
        service_credential_id: str = None,
        service_credential_name: str = None,
        service_credential_secret: str = None,
        service_name: str = None,
        status: str = None,
        user_principal_name: str = None,
    ):
        # The time when the service credential was created.
        self.create_time = create_time
        # The expiration time of the service credential.
        # This field is not returned for permanently valid service credentials.
        self.expiration_time = expiration_time
        # The service credential ID.
        self.service_credential_id = service_credential_id
        # The service credential name.
        self.service_credential_name = service_credential_name
        # The secret of the service credential.
        self.service_credential_secret = service_credential_secret
        # The Alibaba Cloud service name.
        self.service_name = service_name
        # The status of the service credential.
        self.status = status
        # The logon name of the RAM user.
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

        if self.service_credential_secret is not None:
            result['ServiceCredentialSecret'] = self.service_credential_secret

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

        if m.get('ServiceCredentialSecret') is not None:
            self.service_credential_secret = m.get('ServiceCredentialSecret')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        return self

