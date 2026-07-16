# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListFederatedCredentialProvidersResponseBody(DaraModel):
    def __init__(
        self,
        federated_credential_providers: List[main_models.ListFederatedCredentialProvidersResponseBodyFederatedCredentialProviders] = None,
        max_results: int = None,
        next_token: str = None,
        previous_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of federated trust sources.
        self.federated_credential_providers = federated_credential_providers
        # The maximum number of entries per page for a paged query.
        self.max_results = max_results
        # The pagination token returned by this call.
        self.next_token = next_token
        # The pagination token returned by this call.
        self.previous_token = previous_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries in the list.
        self.total_count = total_count

    def validate(self):
        if self.federated_credential_providers:
            for v1 in self.federated_credential_providers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FederatedCredentialProviders'] = []
        if self.federated_credential_providers is not None:
            for k1 in self.federated_credential_providers:
                result['FederatedCredentialProviders'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.previous_token is not None:
            result['PreviousToken'] = self.previous_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.federated_credential_providers = []
        if m.get('FederatedCredentialProviders') is not None:
            for k1 in m.get('FederatedCredentialProviders'):
                temp_model = main_models.ListFederatedCredentialProvidersResponseBodyFederatedCredentialProviders()
                self.federated_credential_providers.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PreviousToken') is not None:
            self.previous_token = m.get('PreviousToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListFederatedCredentialProvidersResponseBodyFederatedCredentialProviders(DaraModel):
    def __init__(
        self,
        cloud_id_pprovider_config: main_models.ListFederatedCredentialProvidersResponseBodyFederatedCredentialProvidersCloudIdPProviderConfig = None,
        create_time: int = None,
        description: str = None,
        federated_credential_provider_id: str = None,
        federated_credential_provider_name: str = None,
        federated_credential_provider_type: str = None,
        instance_id: str = None,
        network_access_endpoint_id: str = None,
        oidc_provider_config: main_models.ListFederatedCredentialProvidersResponseBodyFederatedCredentialProvidersOidcProviderConfig = None,
        pkcs_7provider_config: main_models.ListFederatedCredentialProvidersResponseBodyFederatedCredentialProvidersPkcs7ProviderConfig = None,
        private_ca_provider_config: main_models.ListFederatedCredentialProvidersResponseBodyFederatedCredentialProvidersPrivateCaProviderConfig = None,
        status: str = None,
        update_time: int = None,
    ):
        self.cloud_id_pprovider_config = cloud_id_pprovider_config
        # The creation time.
        self.create_time = create_time
        # The description.
        self.description = description
        # The federated trust source ID.
        self.federated_credential_provider_id = federated_credential_provider_id
        # The name of the federated trust source.
        self.federated_credential_provider_name = federated_credential_provider_name
        # The type of the federated trust source.
        self.federated_credential_provider_type = federated_credential_provider_type
        # The instance ID.
        self.instance_id = instance_id
        # The network access endpoint ID.
        self.network_access_endpoint_id = network_access_endpoint_id
        # The OIDC configuration.
        self.oidc_provider_config = oidc_provider_config
        # The PKCS7 configuration.
        self.pkcs_7provider_config = pkcs_7provider_config
        # The private CA configuration.
        self.private_ca_provider_config = private_ca_provider_config
        # The status.
        self.status = status
        # The update time.
        self.update_time = update_time

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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.federated_credential_provider_id is not None:
            result['FederatedCredentialProviderId'] = self.federated_credential_provider_id

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

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudIdPProviderConfig') is not None:
            temp_model = main_models.ListFederatedCredentialProvidersResponseBodyFederatedCredentialProvidersCloudIdPProviderConfig()
            self.cloud_id_pprovider_config = temp_model.from_map(m.get('CloudIdPProviderConfig'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FederatedCredentialProviderId') is not None:
            self.federated_credential_provider_id = m.get('FederatedCredentialProviderId')

        if m.get('FederatedCredentialProviderName') is not None:
            self.federated_credential_provider_name = m.get('FederatedCredentialProviderName')

        if m.get('FederatedCredentialProviderType') is not None:
            self.federated_credential_provider_type = m.get('FederatedCredentialProviderType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkAccessEndpointId') is not None:
            self.network_access_endpoint_id = m.get('NetworkAccessEndpointId')

        if m.get('OidcProviderConfig') is not None:
            temp_model = main_models.ListFederatedCredentialProvidersResponseBodyFederatedCredentialProvidersOidcProviderConfig()
            self.oidc_provider_config = temp_model.from_map(m.get('OidcProviderConfig'))

        if m.get('Pkcs7ProviderConfig') is not None:
            temp_model = main_models.ListFederatedCredentialProvidersResponseBodyFederatedCredentialProvidersPkcs7ProviderConfig()
            self.pkcs_7provider_config = temp_model.from_map(m.get('Pkcs7ProviderConfig'))

        if m.get('PrivateCaProviderConfig') is not None:
            temp_model = main_models.ListFederatedCredentialProvidersResponseBodyFederatedCredentialProvidersPrivateCaProviderConfig()
            self.private_ca_provider_config = temp_model.from_map(m.get('PrivateCaProviderConfig'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListFederatedCredentialProvidersResponseBodyFederatedCredentialProvidersPrivateCaProviderConfig(DaraModel):
    def __init__(
        self,
        certificates: List[main_models.ListFederatedCredentialProvidersResponseBodyFederatedCredentialProvidersPrivateCaProviderConfigCertificates] = None,
        trust_anchor_source: str = None,
        trust_condition: str = None,
    ):
        # The root certificates.
        self.certificates = certificates
        # The method used to retrieve the root certificate.
        self.trust_anchor_source = trust_anchor_source
        # The trust condition.
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
                temp_model = main_models.ListFederatedCredentialProvidersResponseBodyFederatedCredentialProvidersPrivateCaProviderConfigCertificates()
                self.certificates.append(temp_model.from_map(k1))

        if m.get('TrustAnchorSource') is not None:
            self.trust_anchor_source = m.get('TrustAnchorSource')

        if m.get('TrustCondition') is not None:
            self.trust_condition = m.get('TrustCondition')

        return self

class ListFederatedCredentialProvidersResponseBodyFederatedCredentialProvidersPrivateCaProviderConfigCertificates(DaraModel):
    def __init__(
        self,
        certificate_metadata: main_models.ListFederatedCredentialProvidersResponseBodyFederatedCredentialProvidersPrivateCaProviderConfigCertificatesCertificateMetadata = None,
        content: str = None,
        fingerprint: str = None,
    ):
        # The certificate metadata.
        self.certificate_metadata = certificate_metadata
        # The root certificate content.
        self.content = content
        # The root certificate fingerprint.
        self.fingerprint = fingerprint

    def validate(self):
        if self.certificate_metadata:
            self.certificate_metadata.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate_metadata is not None:
            result['CertificateMetadata'] = self.certificate_metadata.to_map()

        if self.content is not None:
            result['Content'] = self.content

        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateMetadata') is not None:
            temp_model = main_models.ListFederatedCredentialProvidersResponseBodyFederatedCredentialProvidersPrivateCaProviderConfigCertificatesCertificateMetadata()
            self.certificate_metadata = temp_model.from_map(m.get('CertificateMetadata'))

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')

        return self

class ListFederatedCredentialProvidersResponseBodyFederatedCredentialProvidersPrivateCaProviderConfigCertificatesCertificateMetadata(DaraModel):
    def __init__(
        self,
        not_after: int = None,
        not_before: int = None,
    ):
        # The time when the certificate expires.
        self.not_after = not_after
        # The effective period of the certificate.
        self.not_before = not_before

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.not_after is not None:
            result['NotAfter'] = self.not_after

        if self.not_before is not None:
            result['NotBefore'] = self.not_before

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')

        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')

        return self

class ListFederatedCredentialProvidersResponseBodyFederatedCredentialProvidersPkcs7ProviderConfig(DaraModel):
    def __init__(
        self,
        certificates: List[main_models.ListFederatedCredentialProvidersResponseBodyFederatedCredentialProvidersPkcs7ProviderConfigCertificates] = None,
        cms_verification_mode: str = None,
        signature_effective_time: int = None,
        signing_time_value_expression: str = None,
        trust_anchor_source: str = None,
        trust_condition: str = None,
    ):
        # The list of PKCS7 certificates.
        self.certificates = certificates
        # The CMS verification mode.
        self.cms_verification_mode = cms_verification_mode
        # The signature effective time.
        self.signature_effective_time = signature_effective_time
        # The expression used to retrieve the signing time.
        self.signing_time_value_expression = signing_time_value_expression
        # The certificate trust anchor source.
        self.trust_anchor_source = trust_anchor_source
        # The trust condition.
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
                temp_model = main_models.ListFederatedCredentialProvidersResponseBodyFederatedCredentialProvidersPkcs7ProviderConfigCertificates()
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

class ListFederatedCredentialProvidersResponseBodyFederatedCredentialProvidersPkcs7ProviderConfigCertificates(DaraModel):
    def __init__(
        self,
        certificate_metadata: main_models.ListFederatedCredentialProvidersResponseBodyFederatedCredentialProvidersPkcs7ProviderConfigCertificatesCertificateMetadata = None,
        content: str = None,
        fingerprint: str = None,
    ):
        # The certificate metadata.
        self.certificate_metadata = certificate_metadata
        # The certificate content.
        self.content = content
        # The certificate fingerprint.
        self.fingerprint = fingerprint

    def validate(self):
        if self.certificate_metadata:
            self.certificate_metadata.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate_metadata is not None:
            result['CertificateMetadata'] = self.certificate_metadata.to_map()

        if self.content is not None:
            result['Content'] = self.content

        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateMetadata') is not None:
            temp_model = main_models.ListFederatedCredentialProvidersResponseBodyFederatedCredentialProvidersPkcs7ProviderConfigCertificatesCertificateMetadata()
            self.certificate_metadata = temp_model.from_map(m.get('CertificateMetadata'))

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')

        return self

class ListFederatedCredentialProvidersResponseBodyFederatedCredentialProvidersPkcs7ProviderConfigCertificatesCertificateMetadata(DaraModel):
    def __init__(
        self,
        not_after: int = None,
        not_before: int = None,
    ):
        # The time when the certificate expires.
        self.not_after = not_after
        # The effective period of the certificate.
        self.not_before = not_before

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.not_after is not None:
            result['NotAfter'] = self.not_after

        if self.not_before is not None:
            result['NotBefore'] = self.not_before

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')

        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')

        return self

class ListFederatedCredentialProvidersResponseBodyFederatedCredentialProvidersOidcProviderConfig(DaraModel):
    def __init__(
        self,
        audiences: List[str] = None,
        dynamic_jwks: str = None,
        issuer: str = None,
        jwks_last_obtained_time: int = None,
        jwks_source: str = None,
        jwks_uri: str = None,
        static_jwks: str = None,
        trust_condition: str = None,
    ):
        # The list of audiences for the OIDC credential.
        self.audiences = audiences
        # The dynamically obtained JWKS.
        self.dynamic_jwks = dynamic_jwks
        # Issuer
        self.issuer = issuer
        # The time when the JWKS was last obtained.
        self.jwks_last_obtained_time = jwks_last_obtained_time
        # The JWKS source.
        self.jwks_source = jwks_source
        # The JWKS endpoint.
        self.jwks_uri = jwks_uri
        # The statically obtained JWKS.
        self.static_jwks = static_jwks
        # The trust condition.
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

        if self.dynamic_jwks is not None:
            result['DynamicJwks'] = self.dynamic_jwks

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.jwks_last_obtained_time is not None:
            result['JwksLastObtainedTime'] = self.jwks_last_obtained_time

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

        if m.get('DynamicJwks') is not None:
            self.dynamic_jwks = m.get('DynamicJwks')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('JwksLastObtainedTime') is not None:
            self.jwks_last_obtained_time = m.get('JwksLastObtainedTime')

        if m.get('JwksSource') is not None:
            self.jwks_source = m.get('JwksSource')

        if m.get('JwksUri') is not None:
            self.jwks_uri = m.get('JwksUri')

        if m.get('StaticJwks') is not None:
            self.static_jwks = m.get('StaticJwks')

        if m.get('TrustCondition') is not None:
            self.trust_condition = m.get('TrustCondition')

        return self

class ListFederatedCredentialProvidersResponseBodyFederatedCredentialProvidersCloudIdPProviderConfig(DaraModel):
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

