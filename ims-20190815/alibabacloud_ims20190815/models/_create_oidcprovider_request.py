# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOIDCProviderRequest(DaraModel):
    def __init__(
        self,
        client_ids: str = None,
        description: str = None,
        fingerprints: str = None,
        issuance_limit_time: int = None,
        issuer_url: str = None,
        oidcprovider_name: str = None,
    ):
        # The ID of the client, which is provided by the external IdP. If you want to specify multiple client IDs, separate the client IDs with commas (,).
        # 
        # The client ID can contain letters, digits, and special characters and cannot start with the special characters. The special characters are `periods (.), hyphens (-), underscores (_), colons (:), and forward slashes (/)`.``
        # 
        # The client ID can be up to 128 characters in length.
        self.client_ids = client_ids
        # The description of the OIDC IdP.
        # 
        # The description can be up to 256 characters in length.
        self.description = description
        # The fingerprint of the HTTPS CA certificate, which is provided by the external IdP. If you want to specify multiple fingerprints, separate the fingerprints with commas (,).
        # 
        # The fingerprint can contain letters and digits.
        # 
        # The fingerprint can be up to 128 characters in length.
        self.fingerprints = fingerprints
        # The earliest time when an external IdP can issue an ID token. If the value of the iat field in the ID token is later than the current time, the request is rejected. Unit: hours. Valid values: 1 to 168.
        self.issuance_limit_time = issuance_limit_time
        # The URL of the issuer, which is provided by the external IdP. The URL of the issuer must be unique within an Alibaba Cloud account.
        # 
        # The URL of the issuer must start with `https` and be in the valid URL format. The URL cannot contain query parameters that follow a question mark (`?`) or logon information that is identified by at signs (`@`). The URL cannot be a fragment URL that contains number signs (`#`).
        # 
        # The URL can be up to 255 characters in length.
        self.issuer_url = issuer_url
        # The name of the OIDC IdP.
        # 
        # The name can contain letters, digits, and special characters and cannot start or end with the special characters. The special characters are `periods, (.), hyphens (-), and underscores (_)`.``
        # 
        # The name can be up to 128 characters in length.
        self.oidcprovider_name = oidcprovider_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids

        if self.description is not None:
            result['Description'] = self.description

        if self.fingerprints is not None:
            result['Fingerprints'] = self.fingerprints

        if self.issuance_limit_time is not None:
            result['IssuanceLimitTime'] = self.issuance_limit_time

        if self.issuer_url is not None:
            result['IssuerUrl'] = self.issuer_url

        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Fingerprints') is not None:
            self.fingerprints = m.get('Fingerprints')

        if m.get('IssuanceLimitTime') is not None:
            self.issuance_limit_time = m.get('IssuanceLimitTime')

        if m.get('IssuerUrl') is not None:
            self.issuer_url = m.get('IssuerUrl')

        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')

        return self

