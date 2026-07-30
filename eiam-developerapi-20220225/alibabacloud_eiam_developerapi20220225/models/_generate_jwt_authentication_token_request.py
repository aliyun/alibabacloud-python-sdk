# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class GenerateJwtAuthenticationTokenRequest(DaraModel):
    def __init__(
        self,
        audiences: List[str] = None,
        credential_provider_identifier: str = None,
        custom_claims: Dict[str, Any] = None,
        expiration: int = None,
        include_derived_short_token: bool = None,
        issuer: str = None,
        subject: str = None,
    ):
        # The \\`aud\\` field of the JWT.
        # 
        # This parameter is required.
        self.audiences = audiences
        # Credential provider identity.
        # 
        # This parameter is required.
        self.credential_provider_identifier = credential_provider_identifier
        # Custom claims.
        # 
        # >Notice: 
        # 
        # Key-value pairs. Keys must be strings.
        self.custom_claims = custom_claims
        # The validity period of the JWT, in seconds.
        self.expiration = expiration
        # Whether the generated JWT needs to include a "derived short token".
        self.include_derived_short_token = include_derived_short_token
        # The \\`iss\\` field of the JWT.
        self.issuer = issuer
        # The \\`sub\\` field of the JWT.
        # 
        # This parameter is required.
        self.subject = subject

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audiences is not None:
            result['audiences'] = self.audiences

        if self.credential_provider_identifier is not None:
            result['credentialProviderIdentifier'] = self.credential_provider_identifier

        if self.custom_claims is not None:
            result['customClaims'] = self.custom_claims

        if self.expiration is not None:
            result['expiration'] = self.expiration

        if self.include_derived_short_token is not None:
            result['includeDerivedShortToken'] = self.include_derived_short_token

        if self.issuer is not None:
            result['issuer'] = self.issuer

        if self.subject is not None:
            result['subject'] = self.subject

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audiences') is not None:
            self.audiences = m.get('audiences')

        if m.get('credentialProviderIdentifier') is not None:
            self.credential_provider_identifier = m.get('credentialProviderIdentifier')

        if m.get('customClaims') is not None:
            self.custom_claims = m.get('customClaims')

        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')

        if m.get('includeDerivedShortToken') is not None:
            self.include_derived_short_token = m.get('includeDerivedShortToken')

        if m.get('issuer') is not None:
            self.issuer = m.get('issuer')

        if m.get('subject') is not None:
            self.subject = m.get('subject')

        return self

