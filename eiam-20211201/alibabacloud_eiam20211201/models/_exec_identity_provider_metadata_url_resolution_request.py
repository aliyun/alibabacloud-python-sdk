# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecIdentityProviderMetadataUrlResolutionRequest(DaraModel):
    def __init__(
        self,
        identity_provider_id: str = None,
        instance_id: str = None,
        network_access_endpoint_id: str = None,
        oidc_issuer: str = None,
        saml_metadata_url: str = None,
    ):
        self.identity_provider_id = identity_provider_id
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.network_access_endpoint_id = network_access_endpoint_id
        # OIDC Issuer地址。
        self.oidc_issuer = oidc_issuer
        self.saml_metadata_url = saml_metadata_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identity_provider_id is not None:
            result['IdentityProviderId'] = self.identity_provider_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_access_endpoint_id is not None:
            result['NetworkAccessEndpointId'] = self.network_access_endpoint_id

        if self.oidc_issuer is not None:
            result['OidcIssuer'] = self.oidc_issuer

        if self.saml_metadata_url is not None:
            result['SamlMetadataUrl'] = self.saml_metadata_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentityProviderId') is not None:
            self.identity_provider_id = m.get('IdentityProviderId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkAccessEndpointId') is not None:
            self.network_access_endpoint_id = m.get('NetworkAccessEndpointId')

        if m.get('OidcIssuer') is not None:
            self.oidc_issuer = m.get('OidcIssuer')

        if m.get('SamlMetadataUrl') is not None:
            self.saml_metadata_url = m.get('SamlMetadataUrl')

        return self

