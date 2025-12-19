# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOAuth2CredentialProviderRequest(DaraModel):
    def __init__(
        self,
        oauth2_credential_provider_name: str = None,
    ):
        self.oauth2_credential_provider_name = oauth2_credential_provider_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oauth2_credential_provider_name is not None:
            result['OAuth2CredentialProviderName'] = self.oauth2_credential_provider_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OAuth2CredentialProviderName') is not None:
            self.oauth2_credential_provider_name = m.get('OAuth2CredentialProviderName')

        return self

