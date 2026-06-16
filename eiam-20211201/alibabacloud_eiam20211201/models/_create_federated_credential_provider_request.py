# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class CreateFederatedCredentialProviderRequest(DaraModel):
    def __init__(
        self,
        cloud_id_pprovider_config: main_models.CreateFederatedCredentialProviderRequestCloudIdPProviderConfig = None,
        description: str = None,
        federated_credential_provider_name: str = None,
        federated_credential_provider_type: str = None,
        instance_id: str = None,
        network_access_endpoint_id: str = None,
        oidc_provider_config: main_models.CreateFederatedCredentialProviderRequestOidcProviderConfig = None,
        pkcs_7provider_config: main_models.CreateFederatedCredentialProviderRequestPkcs7ProviderConfig = None,
        private_ca_provider_config: main_models.CreateFederatedCredentialProviderRequestPrivateCaProviderConfig = None,
    ):
        self.cloud_id_pprovider_config = cloud_id_pprovider_config
        # The description of the federated credential provider.
        self.description = description
        # The name of the federated credential provider.
        # 
        # This parameter is required.
        self.federated_credential_provider_name = federated_credential_provider_name
        # The type of the federated credential provider.
        # 
        # This parameter is required.
        self.federated_credential_provider_type = federated_credential_provider_type
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The network access endpoint ID.
        self.network_access_endpoint_id = network_access_endpoint_id
        # The configuration for an OIDC-based provider.
        self.oidc_provider_config = oidc_provider_config
        # The configuration for a PKCS7-based provider.
        self.pkcs_7provider_config = pkcs_7provider_config
        # The configuration for a private CA-based provider.
        self.private_ca_provider_config = private_ca_provider_config

    def validate(self):
        if self.cloud_id_pprovider_config:
            self.cloud_id_pprovider_config.validate()
        if self.oidc_provider_config:
            self.oidc_provider_config.validate()
        if self.pkcs_7provider_config:
            self.pkcs_7provider_config.validate()
        if self.private_ca_provider_config:
            self.private_ca_provider_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_id_pprovider_config is not None:
            result['CloudIdPProviderConfig'] = self.cloud_id_pprovider_config.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.federated_credential_provider_name is not None:
            result['FederatedCredentialProviderName'] = self.federated_credential_provider_name

        if self.federated_credential_provider_type is not None:
            result['FederatedCredentialProviderType'] = self.federated_credential_provider_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_access_endpoint_id is not None:
            result['NetworkAccessEndpointId'] = self.network_access_endpoint_id

        if self.oidc_provider_config is not None:
            result['OidcProviderConfig'] = self.oidc_provider_config.to_map()

        if self.pkcs_7provider_config is not None:
            result['Pkcs7ProviderConfig'] = self.pkcs_7provider_config.to_map()

        if self.private_ca_provider_config is not None:
            result['PrivateCaProviderConfig'] = self.private_ca_provider_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudIdPProviderConfig') is not None:
            temp_model = main_models.CreateFederatedCredentialProviderRequestCloudIdPProviderConfig()
            self.cloud_id_pprovider_config = temp_model.from_map(m.get('CloudIdPProviderConfig'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FederatedCredentialProviderName') is not None:
            self.federated_credential_provider_name = m.get('FederatedCredentialProviderName')

        if m.get('FederatedCredentialProviderType') is not None:
            self.federated_credential_provider_type = m.get('FederatedCredentialProviderType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkAccessEndpointId') is not None:
            self.network_access_endpoint_id = m.get('NetworkAccessEndpointId')

        if m.get('OidcProviderConfig') is not None:
            temp_model = main_models.CreateFederatedCredentialProviderRequestOidcProviderConfig()
            self.oidc_provider_config = temp_model.from_map(m.get('OidcProviderConfig'))

        if m.get('Pkcs7ProviderConfig') is not None:
            temp_model = main_models.CreateFederatedCredentialProviderRequestPkcs7ProviderConfig()
            self.pkcs_7provider_config = temp_model.from_map(m.get('Pkcs7ProviderConfig'))

        if m.get('PrivateCaProviderConfig') is not None:
            temp_model = main_models.CreateFederatedCredentialProviderRequestPrivateCaProviderConfig()
            self.private_ca_provider_config = temp_model.from_map(m.get('PrivateCaProviderConfig'))

        return self

class CreateFederatedCredentialProviderRequestPrivateCaProviderConfig(DaraModel):
    def __init__(
        self,
        certificates: List[main_models.CreateFederatedCredentialProviderRequestPrivateCaProviderConfigCertificates] = None,
        trust_anchor_source: str = None,
        trust_condition: str = None,
    ):
        # The root certificates that form the trust anchor.
        self.certificates = certificates
        # The source of the trust anchor.
        self.trust_anchor_source = trust_anchor_source
        # The condition for trusting the root certificate.
        self.trust_condition = trust_condition

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

        if self.trust_anchor_source is not None:
            result['TrustAnchorSource'] = self.trust_anchor_source

        if self.trust_condition is not None:
            result['TrustCondition'] = self.trust_condition

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.certificates = []
        if m.get('Certificates') is not None:
            for k1 in m.get('Certificates'):
                temp_model = main_models.CreateFederatedCredentialProviderRequestPrivateCaProviderConfigCertificates()
                self.certificates.append(temp_model.from_map(k1))

        if m.get('TrustAnchorSource') is not None:
            self.trust_anchor_source = m.get('TrustAnchorSource')

        if m.get('TrustCondition') is not None:
            self.trust_condition = m.get('TrustCondition')

        return self

class CreateFederatedCredentialProviderRequestPrivateCaProviderConfigCertificates(DaraModel):
    def __init__(
        self,
        content: str = None,
    ):
        # The content of the PEM-encoded certificate.
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

class CreateFederatedCredentialProviderRequestPkcs7ProviderConfig(DaraModel):
    def __init__(
        self,
        certificates: List[main_models.CreateFederatedCredentialProviderRequestPkcs7ProviderConfigCertificates] = None,
        cms_verification_mode: str = None,
        signature_effective_time: int = None,
        signing_time_value_expression: str = None,
        trust_anchor_source: str = None,
        trust_condition: str = None,
    ):
        # The certificates for verifying the PKCS7 signature.
        self.certificates = certificates
        # The Cryptographic Message Syntax (CMS) verification mode.
        self.cms_verification_mode = cms_verification_mode
        # The validity period of the signature, in seconds.
        self.signature_effective_time = signature_effective_time
        # The expression to extract the signing time from the signature.
        self.signing_time_value_expression = signing_time_value_expression
        # The source of the trust anchor.
        self.trust_anchor_source = trust_anchor_source
        # The condition that the signature data must meet to be trusted.
        self.trust_condition = trust_condition

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

        if self.cms_verification_mode is not None:
            result['CmsVerificationMode'] = self.cms_verification_mode

        if self.signature_effective_time is not None:
            result['SignatureEffectiveTime'] = self.signature_effective_time

        if self.signing_time_value_expression is not None:
            result['SigningTimeValueExpression'] = self.signing_time_value_expression

        if self.trust_anchor_source is not None:
            result['TrustAnchorSource'] = self.trust_anchor_source

        if self.trust_condition is not None:
            result['TrustCondition'] = self.trust_condition

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.certificates = []
        if m.get('Certificates') is not None:
            for k1 in m.get('Certificates'):
                temp_model = main_models.CreateFederatedCredentialProviderRequestPkcs7ProviderConfigCertificates()
                self.certificates.append(temp_model.from_map(k1))

        if m.get('CmsVerificationMode') is not None:
            self.cms_verification_mode = m.get('CmsVerificationMode')

        if m.get('SignatureEffectiveTime') is not None:
            self.signature_effective_time = m.get('SignatureEffectiveTime')

        if m.get('SigningTimeValueExpression') is not None:
            self.signing_time_value_expression = m.get('SigningTimeValueExpression')

        if m.get('TrustAnchorSource') is not None:
            self.trust_anchor_source = m.get('TrustAnchorSource')

        if m.get('TrustCondition') is not None:
            self.trust_condition = m.get('TrustCondition')

        return self

class CreateFederatedCredentialProviderRequestPkcs7ProviderConfigCertificates(DaraModel):
    def __init__(
        self,
        content: str = None,
    ):
        # The content of the PEM-encoded certificate.
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

class CreateFederatedCredentialProviderRequestOidcProviderConfig(DaraModel):
    def __init__(
        self,
        audiences: List[str] = None,
        issuer: str = None,
        jwks_source: str = None,
        jwks_uri: str = None,
        static_jwks: str = None,
        trust_condition: str = None,
    ):
        # A list of audiences. The `aud` claim in the OIDC token must match a value from this list.
        self.audiences = audiences
        # The issuer identifier for the OIDC provider. This value must match the `iss` claim in the token.
        self.issuer = issuer
        # The source of the JSON Web Key Set (JWKS).
        self.jwks_source = jwks_source
        # The URI of the JWKS endpoint.
        self.jwks_uri = jwks_uri
        # The static JWKS content in JSON format.
        self.static_jwks = static_jwks
        # The condition the OIDC token must meet to be trusted.
        self.trust_condition = trust_condition

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audiences is not None:
            result['Audiences'] = self.audiences

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.jwks_source is not None:
            result['JwksSource'] = self.jwks_source

        if self.jwks_uri is not None:
            result['JwksUri'] = self.jwks_uri

        if self.static_jwks is not None:
            result['StaticJwks'] = self.static_jwks

        if self.trust_condition is not None:
            result['TrustCondition'] = self.trust_condition

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audiences') is not None:
            self.audiences = m.get('Audiences')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('JwksSource') is not None:
            self.jwks_source = m.get('JwksSource')

        if m.get('JwksUri') is not None:
            self.jwks_uri = m.get('JwksUri')

        if m.get('StaticJwks') is not None:
            self.static_jwks = m.get('StaticJwks')

        if m.get('TrustCondition') is not None:
            self.trust_condition = m.get('TrustCondition')

        return self

class CreateFederatedCredentialProviderRequestCloudIdPProviderConfig(DaraModel):
    def __init__(
        self,
        identity_provider_id: str = None,
    ):
        self.identity_provider_id = identity_provider_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identity_provider_id is not None:
            result['IdentityProviderId'] = self.identity_provider_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentityProviderId') is not None:
            self.identity_provider_id = m.get('IdentityProviderId')

        return self

