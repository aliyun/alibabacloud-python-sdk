# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateUserPoolClientRequest(DaraModel):
    def __init__(
        self,
        access_token_validity: str = None,
        client_name: str = None,
        enforce_pkce: bool = None,
        redirect_uris: List[str] = None,
        refresh_token_validity: str = None,
        secret_required: bool = None,
        user_pool_name: str = None,
    ):
        self.access_token_validity = access_token_validity
        self.client_name = client_name
        self.enforce_pkce = enforce_pkce
        self.redirect_uris = redirect_uris
        self.refresh_token_validity = refresh_token_validity
        self.secret_required = secret_required
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

        if m.get('SecretRequired') is not None:
            self.secret_required = m.get('SecretRequired')

        if m.get('UserPoolName') is not None:
            self.user_pool_name = m.get('UserPoolName')

        return self

