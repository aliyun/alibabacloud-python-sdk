# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAPIKeyCredentialProviderRequest(DaraModel):
    def __init__(
        self,
        apikey_credential_provider_name: str = None,
    ):
        self.apikey_credential_provider_name = apikey_credential_provider_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apikey_credential_provider_name is not None:
            result['APIKeyCredentialProviderName'] = self.apikey_credential_provider_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('APIKeyCredentialProviderName') is not None:
            self.apikey_credential_provider_name = m.get('APIKeyCredentialProviderName')

        return self

