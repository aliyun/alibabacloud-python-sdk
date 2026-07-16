# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateServiceCredentialRequest(DaraModel):
    def __init__(
        self,
        service_credential_id: str = None,
        service_credential_name: str = None,
        status: str = None,
        user_principal_name: str = None,
    ):
        # The service credential ID.
        # 
        # This parameter is required.
        self.service_credential_id = service_credential_id
        # The name of the service credential. The name must be 1 to 128 characters in length and can contain letters, digits, periods (.), hyphens (-), and underscores (_). Specify at least one of Status and ServiceCredentialName.
        self.service_credential_name = service_credential_name
        # The status of the service credential. Valid values:
        # - Active
        # - Inactive
        # 
        # Specify at least one of Status and ServiceCredentialName.
        self.status = status
        # The logon name of the Resource Access Management (RAM) user. If this parameter is not specified, the service credential of the identity that invokes this operation is modified.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_credential_id is not None:
            result['ServiceCredentialId'] = self.service_credential_id

        if self.service_credential_name is not None:
            result['ServiceCredentialName'] = self.service_credential_name

        if self.status is not None:
            result['Status'] = self.status

        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCredentialId') is not None:
            self.service_credential_id = m.get('ServiceCredentialId')

        if m.get('ServiceCredentialName') is not None:
            self.service_credential_name = m.get('ServiceCredentialName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        return self

