# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class FetchOAuthAuthenticationTokenRequest(DaraModel):
    def __init__(
        self,
        credential_provider_identifier: str = None,
        custom_parameters: Dict[str, str] = None,
        force_authentication: bool = None,
        scope: str = None,
    ):
        # The credential provider identifier.
        # 
        # This parameter is required.
        self.credential_provider_identifier = credential_provider_identifier
        # Custom key-value pairs appended to the OAuth authorization URL to pass additional parameters supported by the OAuth provider.
        self.custom_parameters = custom_parameters
        # Specifies whether to ignore existing valid tokens and force re-authorization. Default value: false.
        self.force_authentication = force_authentication
        # The scope corresponding to the OAuth protocol.
        # 
        # > If not specified, the scope of the issued OAuth Access Token defaults to the scope configuration of the corresponding credential provider.
        # 
        # >Notice: Multiple scope values are separated by spaces.
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

        if self.custom_parameters is not None:
            result['customParameters'] = self.custom_parameters

        if self.force_authentication is not None:
            result['forceAuthentication'] = self.force_authentication

        if self.scope is not None:
            result['scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('credentialProviderIdentifier') is not None:
            self.credential_provider_identifier = m.get('credentialProviderIdentifier')

        if m.get('customParameters') is not None:
            self.custom_parameters = m.get('customParameters')

        if m.get('forceAuthentication') is not None:
            self.force_authentication = m.get('forceAuthentication')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        return self

