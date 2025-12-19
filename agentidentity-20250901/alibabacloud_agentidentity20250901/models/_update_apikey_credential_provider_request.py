# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAPIKeyCredentialProviderRequest(DaraModel):
    def __init__(
        self,
        apikey: str = None,
        apikey_credential_provider_name: str = None,
        description: str = None,
    ):
        self.apikey = apikey
        self.apikey_credential_provider_name = apikey_credential_provider_name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apikey is not None:
            result['APIKey'] = self.apikey

        if self.apikey_credential_provider_name is not None:
            result['APIKeyCredentialProviderName'] = self.apikey_credential_provider_name

        if self.description is not None:
            result['Description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('APIKey') is not None:
            self.apikey = m.get('APIKey')

        if m.get('APIKeyCredentialProviderName') is not None:
            self.apikey_credential_provider_name = m.get('APIKeyCredentialProviderName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        return self

