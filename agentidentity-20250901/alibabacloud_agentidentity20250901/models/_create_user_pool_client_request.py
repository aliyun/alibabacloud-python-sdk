# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateUserPoolClientRequest(DaraModel):
    def __init__(
        self,
        access_token_validity: str = None,
        client_name: str = None,
        enforce_pkce: bool = None,
        redirect_uris: List[str] = None,
        refresh_token_validity: str = None,
        scopes: List[str] = None,
        secret_required: bool = None,
        user_pool_name: str = None,
    ):
        # The validity period of the access token, in seconds. Valid values: 900 to 10800. Default value: 3600.
        self.access_token_validity = access_token_validity
        # The name of the client. The name must be unique within the same user pool and must be 1 to 64 characters in length.
        self.client_name = client_name
        # Specifies whether to enforce Proof Key for Code Exchange (PKCE). Valid values:
        # - true: Enforced. The code_challenge parameter is required in the authorization code flow.
        # - false: Not enforced.
        self.enforce_pkce = enforce_pkce
        # The list of OAuth redirect URIs. After authorization is complete, the user\\"s browser is redirected to one of the URIs in the list.
        self.redirect_uris = redirect_uris
        # The validity period of the refresh token, in seconds. Valid values: 7200 to 31536000 (90 days). Default value: 2592000 (30 days).
        self.refresh_token_validity = refresh_token_validity
        # The scopes granted to the application. You can specify multiple scopes.
        self.scopes = scopes
        # Specifies whether an application secret is required. Valid values:
        # - true: Required. This value applies to confidential clients such as server-side applications. You must call CreateClientSecret to create a secret.
        # - false: Not required. This value applies to public clients such as single-page applications (SPAs) and mobile applications.
        self.secret_required = secret_required
        # The name of the user pool.
        self.user_pool_name = user_pool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity

        if self.client_name is not None:
            result['ClientName'] = self.client_name

        if self.enforce_pkce is not None:
            result['EnforcePKCE'] = self.enforce_pkce

        if self.redirect_uris is not None:
            result['RedirectURIs'] = self.redirect_uris

        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity

        if self.scopes is not None:
            result['Scopes'] = self.scopes

        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required

        if self.user_pool_name is not None:
            result['UserPoolName'] = self.user_pool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTokenValidity') is not None:
            self.access_token_validity = m.get('AccessTokenValidity')

        if m.get('ClientName') is not None:
            self.client_name = m.get('ClientName')

        if m.get('EnforcePKCE') is not None:
            self.enforce_pkce = m.get('EnforcePKCE')

        if m.get('RedirectURIs') is not None:
            self.redirect_uris = m.get('RedirectURIs')

        if m.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = m.get('RefreshTokenValidity')

        if m.get('Scopes') is not None:
            self.scopes = m.get('Scopes')

        if m.get('SecretRequired') is not None:
            self.secret_required = m.get('SecretRequired')

        if m.get('UserPoolName') is not None:
            self.user_pool_name = m.get('UserPoolName')

        return self

