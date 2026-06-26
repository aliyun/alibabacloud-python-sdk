# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class ListUserPoolClientsResponseBody(DaraModel):
    def __init__(
        self,
        clients: List[main_models.ListUserPoolClientsResponseBodyClients] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.clients = clients
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.clients:
            for v1 in self.clients:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Clients'] = []
        if self.clients is not None:
            for k1 in self.clients:
                result['Clients'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clients = []
        if m.get('Clients') is not None:
            for k1 in m.get('Clients'):
                temp_model = main_models.ListUserPoolClientsResponseBodyClients()
                self.clients.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListUserPoolClientsResponseBodyClients(DaraModel):
    def __init__(
        self,
        access_token_validity: str = None,
        client_id: str = None,
        client_name: str = None,
        client_scopes: List[main_models.ListUserPoolClientsResponseBodyClientsClientScopes] = None,
        client_type: str = None,
        create_time: str = None,
        enforce_pkce: bool = None,
        redirect_uris: List[str] = None,
        refresh_token_validity: str = None,
        secret_required: bool = None,
        update_time: str = None,
        user_pool_name: str = None,
    ):
        self.access_token_validity = access_token_validity
        self.client_id = client_id
        self.client_name = client_name
        self.client_scopes = client_scopes
        self.client_type = client_type
        self.create_time = create_time
        self.enforce_pkce = enforce_pkce
        self.redirect_uris = redirect_uris
        self.refresh_token_validity = refresh_token_validity
        self.secret_required = secret_required
        self.update_time = update_time
        self.user_pool_name = user_pool_name

    def validate(self):
        if self.client_scopes:
            for v1 in self.client_scopes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_name is not None:
            result['ClientName'] = self.client_name

        result['ClientScopes'] = []
        if self.client_scopes is not None:
            for k1 in self.client_scopes:
                result['ClientScopes'].append(k1.to_map() if k1 else None)

        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.enforce_pkce is not None:
            result['EnforcePKCE'] = self.enforce_pkce

        if self.redirect_uris is not None:
            result['RedirectURIs'] = self.redirect_uris

        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity

        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_pool_name is not None:
            result['UserPoolName'] = self.user_pool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTokenValidity') is not None:
            self.access_token_validity = m.get('AccessTokenValidity')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientName') is not None:
            self.client_name = m.get('ClientName')

        self.client_scopes = []
        if m.get('ClientScopes') is not None:
            for k1 in m.get('ClientScopes'):
                temp_model = main_models.ListUserPoolClientsResponseBodyClientsClientScopes()
                self.client_scopes.append(temp_model.from_map(k1))

        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EnforcePKCE') is not None:
            self.enforce_pkce = m.get('EnforcePKCE')

        if m.get('RedirectURIs') is not None:
            self.redirect_uris = m.get('RedirectURIs')

        if m.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = m.get('RefreshTokenValidity')

        if m.get('SecretRequired') is not None:
            self.secret_required = m.get('SecretRequired')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserPoolName') is not None:
            self.user_pool_name = m.get('UserPoolName')

        return self

class ListUserPoolClientsResponseBodyClientsClientScopes(DaraModel):
    def __init__(
        self,
        description: str = None,
        scope_name: str = None,
    ):
        self.description = description
        self.scope_name = scope_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.scope_name is not None:
            result['ScopeName'] = self.scope_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ScopeName') is not None:
            self.scope_name = m.get('ScopeName')

        return self

