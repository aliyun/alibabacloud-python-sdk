# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ExecIdentityProviderMetadataUrlResolutionResponseBody(DaraModel):
    def __init__(
        self,
        identity_provider_metadata: main_models.ExecIdentityProviderMetadataUrlResolutionResponseBodyIdentityProviderMetadata = None,
        request_id: str = None,
    ):
        self.identity_provider_metadata = identity_provider_metadata
        self.request_id = request_id

    def validate(self):
        if self.identity_provider_metadata:
            self.identity_provider_metadata.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identity_provider_metadata is not None:
            result['IdentityProviderMetadata'] = self.identity_provider_metadata.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentityProviderMetadata') is not None:
            temp_model = main_models.ExecIdentityProviderMetadataUrlResolutionResponseBodyIdentityProviderMetadata()
            self.identity_provider_metadata = temp_model.from_map(m.get('IdentityProviderMetadata'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ExecIdentityProviderMetadataUrlResolutionResponseBodyIdentityProviderMetadata(DaraModel):
    def __init__(
        self,
        oidc_open_id_configuration: main_models.ExecIdentityProviderMetadataUrlResolutionResponseBodyIdentityProviderMetadataOidcOpenIdConfiguration = None,
        saml_metadata_configuration: main_models.ExecIdentityProviderMetadataUrlResolutionResponseBodyIdentityProviderMetadataSamlMetadataConfiguration = None,
    ):
        # OIDC IdP的Meta信息。
        self.oidc_open_id_configuration = oidc_open_id_configuration
        self.saml_metadata_configuration = saml_metadata_configuration

    def validate(self):
        if self.oidc_open_id_configuration:
            self.oidc_open_id_configuration.validate()
        if self.saml_metadata_configuration:
            self.saml_metadata_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oidc_open_id_configuration is not None:
            result['OidcOpenIdConfiguration'] = self.oidc_open_id_configuration.to_map()

        if self.saml_metadata_configuration is not None:
            result['SamlMetadataConfiguration'] = self.saml_metadata_configuration.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OidcOpenIdConfiguration') is not None:
            temp_model = main_models.ExecIdentityProviderMetadataUrlResolutionResponseBodyIdentityProviderMetadataOidcOpenIdConfiguration()
            self.oidc_open_id_configuration = temp_model.from_map(m.get('OidcOpenIdConfiguration'))

        if m.get('SamlMetadataConfiguration') is not None:
            temp_model = main_models.ExecIdentityProviderMetadataUrlResolutionResponseBodyIdentityProviderMetadataSamlMetadataConfiguration()
            self.saml_metadata_configuration = temp_model.from_map(m.get('SamlMetadataConfiguration'))

        return self

class ExecIdentityProviderMetadataUrlResolutionResponseBodyIdentityProviderMetadataSamlMetadataConfiguration(DaraModel):
    def __init__(
        self,
        certificates: List[main_models.ExecIdentityProviderMetadataUrlResolutionResponseBodyIdentityProviderMetadataSamlMetadataConfigurationCertificates] = None,
        id_pentity_id: str = None,
        id_psso_url: str = None,
    ):
        self.certificates = certificates
        self.id_pentity_id = id_pentity_id
        self.id_psso_url = id_psso_url

    def validate(self):
        if self.certificates:
            for v1 in self.certificates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Certificates'] = []
        if self.certificates is not None:
            for k1 in self.certificates:
                result['Certificates'].append(k1.to_map() if k1 else None)

        if self.id_pentity_id is not None:
            result['IdPEntityId'] = self.id_pentity_id

        if self.id_psso_url is not None:
            result['IdPSsoUrl'] = self.id_psso_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.certificates = []
        if m.get('Certificates') is not None:
            for k1 in m.get('Certificates'):
                temp_model = main_models.ExecIdentityProviderMetadataUrlResolutionResponseBodyIdentityProviderMetadataSamlMetadataConfigurationCertificates()
                self.certificates.append(temp_model.from_map(k1))

        if m.get('IdPEntityId') is not None:
            self.id_pentity_id = m.get('IdPEntityId')

        if m.get('IdPSsoUrl') is not None:
            self.id_psso_url = m.get('IdPSsoUrl')

        return self

class ExecIdentityProviderMetadataUrlResolutionResponseBodyIdentityProviderMetadataSamlMetadataConfigurationCertificates(DaraModel):
    def __init__(
        self,
        content: str = None,
    ):
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        return self

class ExecIdentityProviderMetadataUrlResolutionResponseBodyIdentityProviderMetadataOidcOpenIdConfiguration(DaraModel):
    def __init__(
        self,
        authorization_endpoint: str = None,
        issuer: str = None,
        jwks_uri: str = None,
        token_endpoint: str = None,
        userinfo_endpoint: str = None,
    ):
        # oAuth2 授权端点。
        self.authorization_endpoint = authorization_endpoint
        # OIDC issuer信息。
        self.issuer = issuer
        # OIDC jwks地址。
        self.jwks_uri = jwks_uri
        # oAuth2 Token端点。
        self.token_endpoint = token_endpoint
        # OIDC 用户信息端点。
        self.userinfo_endpoint = userinfo_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_endpoint is not None:
            result['AuthorizationEndpoint'] = self.authorization_endpoint

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.jwks_uri is not None:
            result['JwksUri'] = self.jwks_uri

        if self.token_endpoint is not None:
            result['TokenEndpoint'] = self.token_endpoint

        if self.userinfo_endpoint is not None:
            result['UserinfoEndpoint'] = self.userinfo_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationEndpoint') is not None:
            self.authorization_endpoint = m.get('AuthorizationEndpoint')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('JwksUri') is not None:
            self.jwks_uri = m.get('JwksUri')

        if m.get('TokenEndpoint') is not None:
            self.token_endpoint = m.get('TokenEndpoint')

        if m.get('UserinfoEndpoint') is not None:
            self.userinfo_endpoint = m.get('UserinfoEndpoint')

        return self

