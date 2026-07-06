# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateServiceCredentialRequest(DaraModel):
    def __init__(
        self,
        credential_age_days: int = None,
        service_credential_name: str = None,
        service_name: str = None,
        user_principal_name: str = None,
    ):
        # The expiration time of the service credential, in days.
        # Valid values: 1 to 36600.
        # If this parameter is not specified, the service credential is permanently valid.
        self.credential_age_days = credential_age_days
        # The service credential name.
        # The name must be 1 to 128 characters in length and can contain letters, digits, periods (.), hyphens (-), and underscores (_).
        # 
        # This parameter is required.
        self.service_credential_name = service_credential_name
        # The Alibaba Cloud service name.
        # 
        # This parameter is required.
        self.service_name = service_name
        # The logon name of the RAM user.
        # If this parameter is left empty, a service credential is created for the current user by default.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_age_days is not None:
            result['CredentialAgeDays'] = self.credential_age_days

        if self.service_credential_name is not None:
            result['ServiceCredentialName'] = self.service_credential_name

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialAgeDays') is not None:
            self.credential_age_days = m.get('CredentialAgeDays')

        if m.get('ServiceCredentialName') is not None:
            self.service_credential_name = m.get('ServiceCredentialName')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        return self

