# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class CreateFederatedCredentialProviderRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        federated_credential_provider_name: str = None,
        federated_credential_provider_type: str = None,
        instance_id: str = None,
        network_access_endpoint_id: str = None,
        oidc_provider_config: main_models.CreateFederatedCredentialProviderRequestOidcProviderConfig = None,
        pkcs_7provider_config: main_models.CreateFederatedCredentialProviderRequestPkcs7ProviderConfig = None,
        private_ca_provider_config: main_models.CreateFederatedCredentialProviderRequestPrivateCaProviderConfig = None,
    ):
        # 联邦凭证提供方描述
        self.description = description
        # 联邦凭证提供方名称
        # 
        # This parameter is required.
        self.federated_credential_provider_name = federated_credential_provider_name
        # 联邦凭证提供方类型
        # 
        # This parameter is required.
        self.federated_credential_provider_type = federated_credential_provider_type
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # 网络端点ID
        self.network_access_endpoint_id = network_access_endpoint_id
        # OIDC配置
        self.oidc_provider_config = oidc_provider_config
        # PKCS7配置
        self.pkcs_7provider_config = pkcs_7provider_config
        # 私有CA配置
        self.private_ca_provider_config = private_ca_provider_config

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
        # Root证书列表
        self.certificates = certificates
        # Root证书获取方式
        self.trust_anchor_source = trust_anchor_source
        # Root证书的信任条件
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
        # Root证书内容
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
        # pkcs7证书列表
        self.certificates = certificates
        # CMS验证模式
        self.cms_verification_mode = cms_verification_mode
        # 签名有效期, 单位秒，1200
        self.signature_effective_time = signature_effective_time
        # 获取签名时间的表达式
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
        # Root证书内容
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
        self.audiences = audiences
        # Issuer
        self.issuer = issuer
        # Jwks来源
        self.jwks_source = jwks_source
        # JWKS 端点
        self.jwks_uri = jwks_uri
        # 静态获取的jwks
        self.static_jwks = static_jwks
        # 信任条件
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

