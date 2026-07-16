# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetServiceCredentialRequest(DaraModel):
    def __init__(
        self,
        service_credential_id: str = None,
        user_principal_name: str = None,
    ):
        # The service credential ID.
        # 
        # This parameter is required.
        self.service_credential_id = service_credential_id
        # The logon name of the Resource Access Management (RAM) user.
        # If not specified, the service credential of the current caller identity that invokes this operation is retrieved.
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

        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCredentialId') is not None:
            self.service_credential_id = m.get('ServiceCredentialId')

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        return self

