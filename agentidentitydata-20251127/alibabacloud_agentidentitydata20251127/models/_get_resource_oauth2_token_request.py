# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from darabonba.model import DaraModel

class GetResourceOAuth2TokenRequest(DaraModel):
    def __init__(
        self,
        custom_parameters: Dict[str, Any] = None,
        custom_state: str = None,
        force_authentication: bool = None,
        oauth2_flow: str = None,
        resource_credential_provider_name: str = None,
        resource_oauth2_return_url: str = None,
        scopes: List[str] = None,
        session_uri: str = None,
        workload_access_token: str = None,
    ):
        self.custom_parameters = custom_parameters
        self.custom_state = custom_state
        self.force_authentication = force_authentication
        self.oauth2_flow = oauth2_flow
        self.resource_credential_provider_name = resource_credential_provider_name
        self.resource_oauth2_return_url = resource_oauth2_return_url
        self.scopes = scopes
        self.session_uri = session_uri
        self.workload_access_token = workload_access_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_parameters is not None:
            result['CustomParameters'] = self.custom_parameters

        if self.custom_state is not None:
            result['CustomState'] = self.custom_state

        if self.force_authentication is not None:
            result['ForceAuthentication'] = self.force_authentication

        if self.oauth2_flow is not None:
            result['OAuth2Flow'] = self.oauth2_flow

        if self.resource_credential_provider_name is not None:
            result['ResourceCredentialProviderName'] = self.resource_credential_provider_name

        if self.resource_oauth2_return_url is not None:
            result['ResourceOAuth2ReturnURL'] = self.resource_oauth2_return_url

        if self.scopes is not None:
            result['Scopes'] = self.scopes

        if self.session_uri is not None:
            result['SessionURI'] = self.session_uri

        if self.workload_access_token is not None:
            result['WorkloadAccessToken'] = self.workload_access_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomParameters') is not None:
            self.custom_parameters = m.get('CustomParameters')

        if m.get('CustomState') is not None:
            self.custom_state = m.get('CustomState')

        if m.get('ForceAuthentication') is not None:
            self.force_authentication = m.get('ForceAuthentication')

        if m.get('OAuth2Flow') is not None:
            self.oauth2_flow = m.get('OAuth2Flow')

        if m.get('ResourceCredentialProviderName') is not None:
            self.resource_credential_provider_name = m.get('ResourceCredentialProviderName')

        if m.get('ResourceOAuth2ReturnURL') is not None:
            self.resource_oauth2_return_url = m.get('ResourceOAuth2ReturnURL')

        if m.get('Scopes') is not None:
            self.scopes = m.get('Scopes')

        if m.get('SessionURI') is not None:
            self.session_uri = m.get('SessionURI')

        if m.get('WorkloadAccessToken') is not None:
            self.workload_access_token = m.get('WorkloadAccessToken')

        return self

