# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FetchOAuthAuthenticationTokenRequest(DaraModel):
    def __init__(
        self,
        credential_provider_identifier: str = None,
        scope: str = None,
    ):
        # This parameter is required.
        self.credential_provider_identifier = credential_provider_identifier
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_provider_identifier is not None:
            result['credentialProviderIdentifier'] = self.credential_provider_identifier

        if self.scope is not None:
            result['scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('credentialProviderIdentifier') is not None:
            self.credential_provider_identifier = m.get('credentialProviderIdentifier')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        return self

