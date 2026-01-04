# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class UpdateIdentityProviderRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dingtalk_app_config: main_models.UpdateIdentityProviderRequestDingtalkAppConfig = None,
        identity_provider_id: str = None,
        identity_provider_name: str = None,
        instance_id: str = None,
        lark_config: main_models.UpdateIdentityProviderRequestLarkConfig = None,
        ldap_config: main_models.UpdateIdentityProviderRequestLdapConfig = None,
        logo_url: str = None,
        network_access_endpoint_id: str = None,
        oidc_config: main_models.UpdateIdentityProviderRequestOidcConfig = None,
        we_com_config: main_models.UpdateIdentityProviderRequestWeComConfig = None,
    ):
        self.client_token = client_token
        # 钉钉出基本信息
        self.dingtalk_app_config = dingtalk_app_config
        # IDaaS的身份提供方主键id
        # 
        # This parameter is required.
        self.identity_provider_id = identity_provider_id
        # 身份提供方名称
        self.identity_provider_name = identity_provider_name
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # 飞书配置
        self.lark_config = lark_config
        # AD/LDAP基本信息
        self.ldap_config = ldap_config
        self.logo_url = logo_url
        # 网络端点ID
        self.network_access_endpoint_id = network_access_endpoint_id
        # OIDC IdP配置。
        self.oidc_config = oidc_config
        # 企业微信基本信息
        self.we_com_config = we_com_config

    def validate(self):
        if self.dingtalk_app_config:
            self.dingtalk_app_config.validate()
        if self.lark_config:
            self.lark_config.validate()
        if self.ldap_config:
            self.ldap_config.validate()
        if self.oidc_config:
            self.oidc_config.validate()
        if self.we_com_config:
            self.we_com_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dingtalk_app_config is not None:
            result['DingtalkAppConfig'] = self.dingtalk_app_config.to_map()

        if self.identity_provider_id is not None:
            result['IdentityProviderId'] = self.identity_provider_id

        if self.identity_provider_name is not None:
            result['IdentityProviderName'] = self.identity_provider_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lark_config is not None:
            result['LarkConfig'] = self.lark_config.to_map()

        if self.ldap_config is not None:
            result['LdapConfig'] = self.ldap_config.to_map()

        if self.logo_url is not None:
            result['LogoUrl'] = self.logo_url

        if self.network_access_endpoint_id is not None:
            result['NetworkAccessEndpointId'] = self.network_access_endpoint_id

        if self.oidc_config is not None:
            result['OidcConfig'] = self.oidc_config.to_map()

        if self.we_com_config is not None:
            result['WeComConfig'] = self.we_com_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DingtalkAppConfig') is not None:
            temp_model = main_models.UpdateIdentityProviderRequestDingtalkAppConfig()
            self.dingtalk_app_config = temp_model.from_map(m.get('DingtalkAppConfig'))

        if m.get('IdentityProviderId') is not None:
            self.identity_provider_id = m.get('IdentityProviderId')

        if m.get('IdentityProviderName') is not None:
            self.identity_provider_name = m.get('IdentityProviderName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LarkConfig') is not None:
            temp_model = main_models.UpdateIdentityProviderRequestLarkConfig()
            self.lark_config = temp_model.from_map(m.get('LarkConfig'))

        if m.get('LdapConfig') is not None:
            temp_model = main_models.UpdateIdentityProviderRequestLdapConfig()
            self.ldap_config = temp_model.from_map(m.get('LdapConfig'))

        if m.get('LogoUrl') is not None:
            self.logo_url = m.get('LogoUrl')

        if m.get('NetworkAccessEndpointId') is not None:
            self.network_access_endpoint_id = m.get('NetworkAccessEndpointId')

        if m.get('OidcConfig') is not None:
            temp_model = main_models.UpdateIdentityProviderRequestOidcConfig()
            self.oidc_config = temp_model.from_map(m.get('OidcConfig'))

        if m.get('WeComConfig') is not None:
            temp_model = main_models.UpdateIdentityProviderRequestWeComConfig()
            self.we_com_config = temp_model.from_map(m.get('WeComConfig'))

        return self

class UpdateIdentityProviderRequestWeComConfig(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        authorize_callback_domain: str = None,
        corp_secret: str = None,
        trustable_domain: str = None,
    ):
        # 企业微信自建应用的Id
        self.agent_id = agent_id
        # 授权回调域
        self.authorize_callback_domain = authorize_callback_domain
        # 企业微信自建应用的corpSecret
        self.corp_secret = corp_secret
        # 可信域名
        self.trustable_domain = trustable_domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.authorize_callback_domain is not None:
            result['AuthorizeCallbackDomain'] = self.authorize_callback_domain

        if self.corp_secret is not None:
            result['CorpSecret'] = self.corp_secret

        if self.trustable_domain is not None:
            result['TrustableDomain'] = self.trustable_domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AuthorizeCallbackDomain') is not None:
            self.authorize_callback_domain = m.get('AuthorizeCallbackDomain')

        if m.get('CorpSecret') is not None:
            self.corp_secret = m.get('CorpSecret')

        if m.get('TrustableDomain') is not None:
            self.trustable_domain = m.get('TrustableDomain')

        return self

class UpdateIdentityProviderRequestOidcConfig(DaraModel):
    def __init__(
        self,
        authn_param: main_models.UpdateIdentityProviderRequestOidcConfigAuthnParam = None,
        endpoint_config: main_models.UpdateIdentityProviderRequestOidcConfigEndpointConfig = None,
        grant_scopes: List[str] = None,
        grant_type: str = None,
        pkce_challenge_method: str = None,
        pkce_required: bool = None,
    ):
        # OIDC客户端认证配置。
        self.authn_param = authn_param
        # OIDC 端点配置。
        self.endpoint_config = endpoint_config
        # OIDC标准参数，如profile、email等
        self.grant_scopes = grant_scopes
        # OIDC授权类型。
        self.grant_type = grant_type
        # 支持的PKCE算法类型。
        self.pkce_challenge_method = pkce_challenge_method
        # AuthorizationCode授权模式下是否使用PKCE。
        self.pkce_required = pkce_required

    def validate(self):
        if self.authn_param:
            self.authn_param.validate()
        if self.endpoint_config:
            self.endpoint_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authn_param is not None:
            result['AuthnParam'] = self.authn_param.to_map()

        if self.endpoint_config is not None:
            result['EndpointConfig'] = self.endpoint_config.to_map()

        if self.grant_scopes is not None:
            result['GrantScopes'] = self.grant_scopes

        if self.grant_type is not None:
            result['GrantType'] = self.grant_type

        if self.pkce_challenge_method is not None:
            result['PkceChallengeMethod'] = self.pkce_challenge_method

        if self.pkce_required is not None:
            result['PkceRequired'] = self.pkce_required

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthnParam') is not None:
            temp_model = main_models.UpdateIdentityProviderRequestOidcConfigAuthnParam()
            self.authn_param = temp_model.from_map(m.get('AuthnParam'))

        if m.get('EndpointConfig') is not None:
            temp_model = main_models.UpdateIdentityProviderRequestOidcConfigEndpointConfig()
            self.endpoint_config = temp_model.from_map(m.get('EndpointConfig'))

        if m.get('GrantScopes') is not None:
            self.grant_scopes = m.get('GrantScopes')

        if m.get('GrantType') is not None:
            self.grant_type = m.get('GrantType')

        if m.get('PkceChallengeMethod') is not None:
            self.pkce_challenge_method = m.get('PkceChallengeMethod')

        if m.get('PkceRequired') is not None:
            self.pkce_required = m.get('PkceRequired')

        return self

class UpdateIdentityProviderRequestOidcConfigEndpointConfig(DaraModel):
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

class UpdateIdentityProviderRequestOidcConfigAuthnParam(DaraModel):
    def __init__(
        self,
        authn_method: str = None,
        client_secret: str = None,
    ):
        # OIDC/oAuth2 认证方法。
        self.authn_method = authn_method
        # OIDC/oAuth2 客户端密钥。
        self.client_secret = client_secret

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authn_method is not None:
            result['AuthnMethod'] = self.authn_method

        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthnMethod') is not None:
            self.authn_method = m.get('AuthnMethod')

        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')

        return self

class UpdateIdentityProviderRequestLdapConfig(DaraModel):
    def __init__(
        self,
        administrator_password: str = None,
        administrator_username: str = None,
        certificate_fingerprint_status: str = None,
        certificate_fingerprints: List[str] = None,
        ldap_protocol: str = None,
        ldap_server_host: str = None,
        ldap_server_port: int = None,
        start_tls_status: str = None,
    ):
        # 管理员密码
        self.administrator_password = administrator_password
        # 管理员账号
        self.administrator_username = administrator_username
        # 是否验证指纹证书
        self.certificate_fingerprint_status = certificate_fingerprint_status
        # 证书指纹列表
        self.certificate_fingerprints = certificate_fingerprints
        # 通信协议
        self.ldap_protocol = ldap_protocol
        # ad/ldap 服务器地址
        self.ldap_server_host = ldap_server_host
        # 端口号
        self.ldap_server_port = ldap_server_port
        # startTls是否开启
        self.start_tls_status = start_tls_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.administrator_password is not None:
            result['AdministratorPassword'] = self.administrator_password

        if self.administrator_username is not None:
            result['AdministratorUsername'] = self.administrator_username

        if self.certificate_fingerprint_status is not None:
            result['CertificateFingerprintStatus'] = self.certificate_fingerprint_status

        if self.certificate_fingerprints is not None:
            result['CertificateFingerprints'] = self.certificate_fingerprints

        if self.ldap_protocol is not None:
            result['LdapProtocol'] = self.ldap_protocol

        if self.ldap_server_host is not None:
            result['LdapServerHost'] = self.ldap_server_host

        if self.ldap_server_port is not None:
            result['LdapServerPort'] = self.ldap_server_port

        if self.start_tls_status is not None:
            result['StartTlsStatus'] = self.start_tls_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdministratorPassword') is not None:
            self.administrator_password = m.get('AdministratorPassword')

        if m.get('AdministratorUsername') is not None:
            self.administrator_username = m.get('AdministratorUsername')

        if m.get('CertificateFingerprintStatus') is not None:
            self.certificate_fingerprint_status = m.get('CertificateFingerprintStatus')

        if m.get('CertificateFingerprints') is not None:
            self.certificate_fingerprints = m.get('CertificateFingerprints')

        if m.get('LdapProtocol') is not None:
            self.ldap_protocol = m.get('LdapProtocol')

        if m.get('LdapServerHost') is not None:
            self.ldap_server_host = m.get('LdapServerHost')

        if m.get('LdapServerPort') is not None:
            self.ldap_server_port = m.get('LdapServerPort')

        if m.get('StartTlsStatus') is not None:
            self.start_tls_status = m.get('StartTlsStatus')

        return self

class UpdateIdentityProviderRequestLarkConfig(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret: str = None,
        encrypt_key: str = None,
        verification_token: str = None,
    ):
        self.app_id = app_id
        self.app_secret = app_secret
        self.encrypt_key = encrypt_key
        self.verification_token = verification_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret

        if self.encrypt_key is not None:
            result['EncryptKey'] = self.encrypt_key

        if self.verification_token is not None:
            result['VerificationToken'] = self.verification_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')

        if m.get('EncryptKey') is not None:
            self.encrypt_key = m.get('EncryptKey')

        if m.get('VerificationToken') is not None:
            self.verification_token = m.get('VerificationToken')

        return self

class UpdateIdentityProviderRequestDingtalkAppConfig(DaraModel):
    def __init__(
        self,
        app_key: str = None,
        app_secret: str = None,
        dingtalk_login_version: str = None,
        encrypt_key: str = None,
        verification_token: str = None,
    ):
        # 钉钉一方应用的AppKey
        self.app_key = app_key
        # 钉钉一方应用的AppSecret
        self.app_secret = app_secret
        self.dingtalk_login_version = dingtalk_login_version
        self.encrypt_key = encrypt_key
        self.verification_token = verification_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret

        if self.dingtalk_login_version is not None:
            result['DingtalkLoginVersion'] = self.dingtalk_login_version

        if self.encrypt_key is not None:
            result['EncryptKey'] = self.encrypt_key

        if self.verification_token is not None:
            result['VerificationToken'] = self.verification_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')

        if m.get('DingtalkLoginVersion') is not None:
            self.dingtalk_login_version = m.get('DingtalkLoginVersion')

        if m.get('EncryptKey') is not None:
            self.encrypt_key = m.get('EncryptKey')

        if m.get('VerificationToken') is not None:
            self.verification_token = m.get('VerificationToken')

        return self

