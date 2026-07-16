# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAPIKeyCredentialProviderRequest(DaraModel):
    def __init__(
        self,
        apikey_credential_provider_name: str = None,
        token_vault_name: str = None,
    ):
        self.apikey_credential_provider_name = apikey_credential_provider_name
        self.token_vault_name = token_vault_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apikey_credential_provider_name is not None:
            result['APIKeyCredentialProviderName'] = self.apikey_credential_provider_name

        if self.token_vault_name is not None:
            result['TokenVaultName'] = self.token_vault_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('APIKeyCredentialProviderName') is not None:
            self.apikey_credential_provider_name = m.get('APIKeyCredentialProviderName')

        if m.get('TokenVaultName') is not None:
            self.token_vault_name = m.get('TokenVaultName')

        return self

