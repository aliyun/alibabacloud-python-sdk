# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveClientIdFromOIDCProviderRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        oidcprovider_name: str = None,
    ):
        # The client ID to remove.
        # 
        # Format: letters, digits, and the special characters `.-_:/` are allowed. The value cannot start with the special characters `.-_:/`.
        # 
        # Length: up to 128 characters.
        self.client_id = client_id
        # The name of an existing OIDC IdP that has the target `ClientId` attached. If you have not created or attached one, call `CreateOIDCProvider` (with `ClientIds` specified) or `AddClientIdToOIDCProvider` first.
        self.oidcprovider_name = oidcprovider_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')

        return self

