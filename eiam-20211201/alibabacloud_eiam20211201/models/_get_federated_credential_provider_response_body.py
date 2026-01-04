# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetFederatedCredentialProviderResponseBody(DaraModel):
    def __init__(
        self,
        federated_credential_provider: main_models.GetFederatedCredentialProviderResponseBodyFederatedCredentialProvider = None,
        request_id: str = None,
    ):
        self.federated_credential_provider = federated_credential_provider
        self.request_id = request_id

    def validate(self):
        if self.federated_credential_provider:
            self.federated_credential_provider.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.federated_credential_provider is not None:
            result['FederatedCredentialProvider'] = self.federated_credential_provider.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FederatedCredentialProvider') is not None:
            temp_model = main_models.GetFederatedCredentialProviderResponseBodyFederatedCredentialProvider()
            self.federated_credential_provider = temp_model.from_map(m.get('FederatedCredentialProvider'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetFederatedCredentialProviderResponseBodyFederatedCredentialProvider(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        federated_credential_provider_id: str = None,
        federated_credential_provider_name: str = None,
        federated_credential_provider_type: str = None,
        instance_id: str = None,
        network_access_endpoint_id: str = None,
        oidc_provider_config: main_models.GetFederatedCredentialProviderResponseBodyFederatedCredentialProviderOidcProviderConfig = None,
        pkcs_7provider_config: main_models.GetFederatedCredentialProviderResponseBodyFederatedCredentialProviderPkcs7ProviderConfig = None,
        private_ca_provider_config: main_models.GetFederatedCredentialProviderResponseBodyFederatedCredentialProviderPrivateCaProviderConfig = None,
        status: str = None,
        update_time: int = None,
    ):
        # 创建时间
        self.create_time = create_time
        # 描述
        self.description = description
        # Federated Credential Provider ID
        self.federated_credential_provider_id = federated_credential_provider_id
        # 联邦凭证提供方名称
        self.federated_credential_provider_name = federated_credential_provider_name
        # 联邦凭证提供方类型
        self.federated_credential_provider_type = federated_credential_provider_type
        # EIAM 实例ID
        self.instance_id = instance_id
        # 网络访问端点ID
        self.network_access_endpoint_id = network_access_endpoint_id
        # OIDC配置
        self.oidc_provider_config = oidc_provider_config
        # PKCS7配置
        self.pkcs_7provider_config = pkcs_7provider_config
        # 私有CA配置
        self.private_ca_provider_config = private_ca_provider_config
        # 状态
        self.status = status
        # 更新时间
        self.update_time = update_time

    def validate(self):
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
            temp_model = main_models.GetFederatedCredentialProviderResponseBodyFederatedCredentialProviderOidcProviderConfig()
            self.oidc_provider_config = temp_model.from_map(m.get('OidcProviderConfig'))

        if m.get('Pkcs7ProviderConfig') is not None:
            temp_model = main_models.GetFederatedCredentialProviderResponseBodyFederatedCredentialProviderPkcs7ProviderConfig()
            self.pkcs_7provider_config = temp_model.from_map(m.get('Pkcs7ProviderConfig'))

        if m.get('PrivateCaProviderConfig') is not None:
            temp_model = main_models.GetFederatedCredentialProviderResponseBodyFederatedCredentialProviderPrivateCaProviderConfig()
            self.private_ca_provider_config = temp_model.from_map(m.get('PrivateCaProviderConfig'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetFederatedCredentialProviderResponseBodyFederatedCredentialProviderPrivateCaProviderConfig(DaraModel):
    def __init__(
        self,
        certificates: List[main_models.GetFederatedCredentialProviderResponseBodyFederatedCredentialProviderPrivateCaProviderConfigCertificates] = None,
        trust_anchor_source: str = None,
        trust_condition: str = None,
    ):
        # Root证书
        self.certificates = certificates
        # Root证书获取方式
        self.trust_anchor_source = trust_anchor_source
        # Root证书的默认条件
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
                temp_model = main_models.GetFederatedCredentialProviderResponseBodyFederatedCredentialProviderPrivateCaProviderConfigCertificates()
                self.certificates.append(temp_model.from_map(k1))

        if m.get('TrustAnchorSource') is not None:
            self.trust_anchor_source = m.get('TrustAnchorSource')

        if m.get('TrustCondition') is not None:
            self.trust_condition = m.get('TrustCondition')

        return self

class GetFederatedCredentialProviderResponseBodyFederatedCredentialProviderPrivateCaProviderConfigCertificates(DaraModel):
    def __init__(
        self,
        certificate_metadata: main_models.GetFederatedCredentialProviderResponseBodyFederatedCredentialProviderPrivateCaProviderConfigCertificatesCertificateMetadata = None,
        content: str = None,
        fingerprint: str = None,
    ):
        # 证书元数据
        self.certificate_metadata = certificate_metadata
        # Root证书内容
        self.content = content
        # Root证书指纹
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
            temp_model = main_models.GetFederatedCredentialProviderResponseBodyFederatedCredentialProviderPrivateCaProviderConfigCertificatesCertificateMetadata()
            self.certificate_metadata = temp_model.from_map(m.get('CertificateMetadata'))

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')

        return self

class GetFederatedCredentialProviderResponseBodyFederatedCredentialProviderPrivateCaProviderConfigCertificatesCertificateMetadata(DaraModel):
    def __init__(
        self,
        not_after: int = None,
        not_before: int = None,
    ):
        # 证书过期时间
        self.not_after = not_after
        # 证书生效时间
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

class GetFederatedCredentialProviderResponseBodyFederatedCredentialProviderPkcs7ProviderConfig(DaraModel):
    def __init__(
        self,
        certificates: List[main_models.GetFederatedCredentialProviderResponseBodyFederatedCredentialProviderPkcs7ProviderConfigCertificates] = None,
        cms_verification_mode: str = None,
        signature_effective_time: int = None,
        signing_time_value_expression: str = None,
        trust_anchor_source: str = None,
        trust_condition: str = None,
    ):
        # pkcs7证书列表
        self.certificates = certificates
        # CMS验证模式
        self.cms_verification_mode = cms_verification_mode
        # 签名有效时间
        self.signature_effective_time = signature_effective_time
        # 签名时间
        self.signing_time_value_expression = signing_time_value_expression
        # 证书信任锚点来源
        self.trust_anchor_source = trust_anchor_source
        # 信任条件
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
                temp_model = main_models.GetFederatedCredentialProviderResponseBodyFederatedCredentialProviderPkcs7ProviderConfigCertificates()
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

class GetFederatedCredentialProviderResponseBodyFederatedCredentialProviderPkcs7ProviderConfigCertificates(DaraModel):
    def __init__(
        self,
        certificate_metadata: main_models.GetFederatedCredentialProviderResponseBodyFederatedCredentialProviderPkcs7ProviderConfigCertificatesCertificateMetadata = None,
        content: str = None,
        fingerprint: str = None,
    ):
        # 证书元数据
        self.certificate_metadata = certificate_metadata
        # Root证书内容
        self.content = content
        # Root证书指纹
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
            temp_model = main_models.GetFederatedCredentialProviderResponseBodyFederatedCredentialProviderPkcs7ProviderConfigCertificatesCertificateMetadata()
            self.certificate_metadata = temp_model.from_map(m.get('CertificateMetadata'))

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')

        return self

class GetFederatedCredentialProviderResponseBodyFederatedCredentialProviderPkcs7ProviderConfigCertificatesCertificateMetadata(DaraModel):
    def __init__(
        self,
        not_after: int = None,
        not_before: int = None,
    ):
        # 证书过期时间
        self.not_after = not_after
        # 证书生效时间
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

class GetFederatedCredentialProviderResponseBodyFederatedCredentialProviderOidcProviderConfig(DaraModel):
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
        # oidc凭证的受众列表
        self.audiences = audiences
        # 动态获取的jwks
        self.dynamic_jwks = dynamic_jwks
        # Issuer
        self.issuer = issuer
        self.jwks_last_obtained_time = jwks_last_obtained_time
        # Jwks来源
        self.jwks_source = jwks_source
        # JWKS 端点
        self.jwks_uri = jwks_uri
        # 静态获取的jwks
        self.static_jwks = static_jwks
        # 默认条件
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

