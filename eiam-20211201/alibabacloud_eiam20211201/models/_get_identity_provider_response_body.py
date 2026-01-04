# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetIdentityProviderResponseBody(DaraModel):
    def __init__(
        self,
        identity_provider_detail: main_models.GetIdentityProviderResponseBodyIdentityProviderDetail = None,
        request_id: str = None,
    ):
        # Identity provider Information.
        self.identity_provider_detail = identity_provider_detail
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.identity_provider_detail:
            self.identity_provider_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identity_provider_detail is not None:
            result['IdentityProviderDetail'] = self.identity_provider_detail.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentityProviderDetail') is not None:
            temp_model = main_models.GetIdentityProviderResponseBodyIdentityProviderDetail()
            self.identity_provider_detail = temp_model.from_map(m.get('IdentityProviderDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetIdentityProviderResponseBodyIdentityProviderDetail(DaraModel):
    def __init__(
        self,
        advanced_status: str = None,
        authn_source_supplier: str = None,
        authn_source_type: str = None,
        authn_status: str = None,
        create_time: int = None,
        description: str = None,
        dingtalk_app_config: main_models.GetIdentityProviderResponseBodyIdentityProviderDetailDingtalkAppConfig = None,
        dingtalk_provisioning_config: main_models.GetIdentityProviderResponseBodyIdentityProviderDetailDingtalkProvisioningConfig = None,
        identity_provider_external_id: str = None,
        identity_provider_id: str = None,
        identity_provider_name: str = None,
        identity_provider_type: str = None,
        instance_id: str = None,
        lark_config: main_models.GetIdentityProviderResponseBodyIdentityProviderDetailLarkConfig = None,
        last_status_check_job_result: str = None,
        ldap_config: main_models.GetIdentityProviderResponseBodyIdentityProviderDetailLdapConfig = None,
        lock_reason: str = None,
        logo_url: str = None,
        network_access_endpoint_id: str = None,
        oidc_config: main_models.GetIdentityProviderResponseBodyIdentityProviderDetailOidcConfig = None,
        ud_pull_config: main_models.GetIdentityProviderResponseBodyIdentityProviderDetailUdPullConfig = None,
        ud_pull_status: str = None,
        ud_push_config: main_models.GetIdentityProviderResponseBodyIdentityProviderDetailUdPushConfig = None,
        ud_push_status: str = None,
        update_time: int = None,
        we_com_config: main_models.GetIdentityProviderResponseBodyIdentityProviderDetailWeComConfig = None,
    ):
        # Advanced configuration capability. 
        # Value range:  
        # Disabled: disabled  
        # Enable: enabled
        self.advanced_status = advanced_status
        # The corresponding identity provider product, e.g., Okta, Google, or Azure AD. Possible values:
        # 
        # DingTalk: urn:alibaba:idaas:idp:alibaba:dingtalk
        # 
        # LDAP: urn:alibaba:idaas:idp:unknown:ldap
        # 
        # Alibaba Cloud IDaaS: urn:alibaba:idaas:idp:alibaba:idaas
        # 
        # WeCom (Enterprise WeChat): urn:alibaba:idaas:idp:tencent:wecom
        # 
        # Lark (Feishu): urn:alibaba:idaas:idp:bytedance:lark
        # 
        # Active Directory: urn:alibaba:idaas:idp:microsoft:ad
        # 
        # Azure Active Directory: urn:alibaba:idaas:idp:microsoft:aad
        # 
        # Alibaba Cloud SASE: urn:alibaba:idaas:idp:alibaba:sase
        self.authn_source_supplier = authn_source_supplier
        # Authentication type — OIDC or SAML. Possible values:
        # 
        # OIDC: urn:alibaba:idaas:authntype:oidc
        # 
        # SAML: urn:alibaba:idaas:authntype:saml2
        self.authn_source_type = authn_source_type
        # Whether the corresponding IdP supports authentication. Value range: 
        # Disabled: disabled  
        # Enabled: enabled
        self.authn_status = authn_status
        # The time when the version was created.
        self.create_time = create_time
        # Identity provider description.
        self.description = description
        # DingTalk Basic Configuration
        self.dingtalk_app_config = dingtalk_app_config
        # DingTalk synchronous configuration.
        self.dingtalk_provisioning_config = dingtalk_provisioning_config
        # Identity provider external ID.
        self.identity_provider_external_id = identity_provider_external_id
        # Identity provider ID.
        self.identity_provider_id = identity_provider_id
        # Identity provider name.
        self.identity_provider_name = identity_provider_name
        # Identity provider type.
        self.identity_provider_type = identity_provider_type
        # Instance ID.
        self.instance_id = instance_id
        # Lark configuration.
        self.lark_config = lark_config
        # Last status check result.
        self.last_status_check_job_result = last_status_check_job_result
        # AD/LDAP Identity provider information.
        self.ldap_config = ldap_config
        # The reason why write operations on the instance are locked.
        self.lock_reason = lock_reason
        # The URL of the application logo.
        self.logo_url = logo_url
        # The unique identifier of the network access endpoint.
        self.network_access_endpoint_id = network_access_endpoint_id
        # OIDC IdP configuration.
        self.oidc_config = oidc_config
        # Sync in configuration.
        self.ud_pull_config = ud_pull_config
        # Indicates whether the IDaaS EIAM system supports UD (User Directory) synchronization.
        self.ud_pull_status = ud_pull_status
        # Outbound synchronization configuration.
        self.ud_push_config = ud_push_config
        # Outbound synchronization capability.
        self.ud_push_status = ud_push_status
        # The time when the serviceInstance  was last updated.
        self.update_time = update_time
        # WeCom configuration.
        self.we_com_config = we_com_config

    def validate(self):
        if self.dingtalk_app_config:
            self.dingtalk_app_config.validate()
        if self.dingtalk_provisioning_config:
            self.dingtalk_provisioning_config.validate()
        if self.lark_config:
            self.lark_config.validate()
        if self.ldap_config:
            self.ldap_config.validate()
        if self.oidc_config:
            self.oidc_config.validate()
        if self.ud_pull_config:
            self.ud_pull_config.validate()
        if self.ud_push_config:
            self.ud_push_config.validate()
        if self.we_com_config:
            self.we_com_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_status is not None:
            result['AdvancedStatus'] = self.advanced_status

        if self.authn_source_supplier is not None:
            result['AuthnSourceSupplier'] = self.authn_source_supplier

        if self.authn_source_type is not None:
            result['AuthnSourceType'] = self.authn_source_type

        if self.authn_status is not None:
            result['AuthnStatus'] = self.authn_status

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.dingtalk_app_config is not None:
            result['DingtalkAppConfig'] = self.dingtalk_app_config.to_map()

        if self.dingtalk_provisioning_config is not None:
            result['DingtalkProvisioningConfig'] = self.dingtalk_provisioning_config.to_map()

        if self.identity_provider_external_id is not None:
            result['IdentityProviderExternalId'] = self.identity_provider_external_id

        if self.identity_provider_id is not None:
            result['IdentityProviderId'] = self.identity_provider_id

        if self.identity_provider_name is not None:
            result['IdentityProviderName'] = self.identity_provider_name

        if self.identity_provider_type is not None:
            result['IdentityProviderType'] = self.identity_provider_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lark_config is not None:
            result['LarkConfig'] = self.lark_config.to_map()

        if self.last_status_check_job_result is not None:
            result['LastStatusCheckJobResult'] = self.last_status_check_job_result

        if self.ldap_config is not None:
            result['LdapConfig'] = self.ldap_config.to_map()

        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.logo_url is not None:
            result['LogoUrl'] = self.logo_url

        if self.network_access_endpoint_id is not None:
            result['NetworkAccessEndpointId'] = self.network_access_endpoint_id

        if self.oidc_config is not None:
            result['OidcConfig'] = self.oidc_config.to_map()

        if self.ud_pull_config is not None:
            result['UdPullConfig'] = self.ud_pull_config.to_map()

        if self.ud_pull_status is not None:
            result['UdPullStatus'] = self.ud_pull_status

        if self.ud_push_config is not None:
            result['UdPushConfig'] = self.ud_push_config.to_map()

        if self.ud_push_status is not None:
            result['UdPushStatus'] = self.ud_push_status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.we_com_config is not None:
            result['WeComConfig'] = self.we_com_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedStatus') is not None:
            self.advanced_status = m.get('AdvancedStatus')

        if m.get('AuthnSourceSupplier') is not None:
            self.authn_source_supplier = m.get('AuthnSourceSupplier')

        if m.get('AuthnSourceType') is not None:
            self.authn_source_type = m.get('AuthnSourceType')

        if m.get('AuthnStatus') is not None:
            self.authn_status = m.get('AuthnStatus')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DingtalkAppConfig') is not None:
            temp_model = main_models.GetIdentityProviderResponseBodyIdentityProviderDetailDingtalkAppConfig()
            self.dingtalk_app_config = temp_model.from_map(m.get('DingtalkAppConfig'))

        if m.get('DingtalkProvisioningConfig') is not None:
            temp_model = main_models.GetIdentityProviderResponseBodyIdentityProviderDetailDingtalkProvisioningConfig()
            self.dingtalk_provisioning_config = temp_model.from_map(m.get('DingtalkProvisioningConfig'))

        if m.get('IdentityProviderExternalId') is not None:
            self.identity_provider_external_id = m.get('IdentityProviderExternalId')

        if m.get('IdentityProviderId') is not None:
            self.identity_provider_id = m.get('IdentityProviderId')

        if m.get('IdentityProviderName') is not None:
            self.identity_provider_name = m.get('IdentityProviderName')

        if m.get('IdentityProviderType') is not None:
            self.identity_provider_type = m.get('IdentityProviderType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LarkConfig') is not None:
            temp_model = main_models.GetIdentityProviderResponseBodyIdentityProviderDetailLarkConfig()
            self.lark_config = temp_model.from_map(m.get('LarkConfig'))

        if m.get('LastStatusCheckJobResult') is not None:
            self.last_status_check_job_result = m.get('LastStatusCheckJobResult')

        if m.get('LdapConfig') is not None:
            temp_model = main_models.GetIdentityProviderResponseBodyIdentityProviderDetailLdapConfig()
            self.ldap_config = temp_model.from_map(m.get('LdapConfig'))

        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('LogoUrl') is not None:
            self.logo_url = m.get('LogoUrl')

        if m.get('NetworkAccessEndpointId') is not None:
            self.network_access_endpoint_id = m.get('NetworkAccessEndpointId')

        if m.get('OidcConfig') is not None:
            temp_model = main_models.GetIdentityProviderResponseBodyIdentityProviderDetailOidcConfig()
            self.oidc_config = temp_model.from_map(m.get('OidcConfig'))

        if m.get('UdPullConfig') is not None:
            temp_model = main_models.GetIdentityProviderResponseBodyIdentityProviderDetailUdPullConfig()
            self.ud_pull_config = temp_model.from_map(m.get('UdPullConfig'))

        if m.get('UdPullStatus') is not None:
            self.ud_pull_status = m.get('UdPullStatus')

        if m.get('UdPushConfig') is not None:
            temp_model = main_models.GetIdentityProviderResponseBodyIdentityProviderDetailUdPushConfig()
            self.ud_push_config = temp_model.from_map(m.get('UdPushConfig'))

        if m.get('UdPushStatus') is not None:
            self.ud_push_status = m.get('UdPushStatus')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('WeComConfig') is not None:
            temp_model = main_models.GetIdentityProviderResponseBodyIdentityProviderDetailWeComConfig()
            self.we_com_config = temp_model.from_map(m.get('WeComConfig'))

        return self

class GetIdentityProviderResponseBodyIdentityProviderDetailWeComConfig(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        authorize_callback_domain: str = None,
        corp_id: str = None,
        corp_secret: str = None,
        trustable_domain: str = None,
    ):
        # The ID of the load generator. This parameter is disabled.
        self.agent_id = agent_id
        # Authorization callback domain.
        self.authorize_callback_domain = authorize_callback_domain
        # CorpId.
        self.corp_id = corp_id
        # Corp secret.
        self.corp_secret = corp_secret
        # Trusted domain.
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

        if self.corp_id is not None:
            result['CorpId'] = self.corp_id

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

        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')

        if m.get('CorpSecret') is not None:
            self.corp_secret = m.get('CorpSecret')

        if m.get('TrustableDomain') is not None:
            self.trustable_domain = m.get('TrustableDomain')

        return self

class GetIdentityProviderResponseBodyIdentityProviderDetailUdPushConfig(DaraModel):
    def __init__(
        self,
        incremental_callback_status: str = None,
        ud_sync_scope_configs: List[main_models.GetIdentityProviderResponseBodyIdentityProviderDetailUdPushConfigUdSyncScopeConfigs] = None,
    ):
        # Incremental callback status: Whether to process incremental callback data from the IdP.
        self.incremental_callback_status = incremental_callback_status
        # Outbound synchronization configuration Information.
        self.ud_sync_scope_configs = ud_sync_scope_configs

    def validate(self):
        if self.ud_sync_scope_configs:
            for v1 in self.ud_sync_scope_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.incremental_callback_status is not None:
            result['IncrementalCallbackStatus'] = self.incremental_callback_status

        result['UdSyncScopeConfigs'] = []
        if self.ud_sync_scope_configs is not None:
            for k1 in self.ud_sync_scope_configs:
                result['UdSyncScopeConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncrementalCallbackStatus') is not None:
            self.incremental_callback_status = m.get('IncrementalCallbackStatus')

        self.ud_sync_scope_configs = []
        if m.get('UdSyncScopeConfigs') is not None:
            for k1 in m.get('UdSyncScopeConfigs'):
                temp_model = main_models.GetIdentityProviderResponseBodyIdentityProviderDetailUdPushConfigUdSyncScopeConfigs()
                self.ud_sync_scope_configs.append(temp_model.from_map(k1))

        return self

class GetIdentityProviderResponseBodyIdentityProviderDetailUdPushConfigUdSyncScopeConfigs(DaraModel):
    def __init__(
        self,
        source_scopes: List[str] = None,
        target_scope: str = None,
    ):
        # Synchronization source node.
        self.source_scopes = source_scopes
        # Synchronization target node.
        self.target_scope = target_scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_scopes is not None:
            result['SourceScopes'] = self.source_scopes

        if self.target_scope is not None:
            result['TargetScope'] = self.target_scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceScopes') is not None:
            self.source_scopes = m.get('SourceScopes')

        if m.get('TargetScope') is not None:
            self.target_scope = m.get('TargetScope')

        return self

class GetIdentityProviderResponseBodyIdentityProviderDetailUdPullConfig(DaraModel):
    def __init__(
        self,
        group_sync_status: str = None,
        incremental_callback_status: str = None,
        ud_sync_scope_config: main_models.GetIdentityProviderResponseBodyIdentityProviderDetailUdPullConfigUdSyncScopeConfig = None,
    ):
        # Whether to enable group synchronization. Possible values:
        # 
        # Disabled: disabled
        # 
        # Enabled: enabled
        self.group_sync_status = group_sync_status
        # Incremental callback status: Whether to process incremental callback data from the IdP.
        self.incremental_callback_status = incremental_callback_status
        # Inbound synchronization configuration Information.
        self.ud_sync_scope_config = ud_sync_scope_config

    def validate(self):
        if self.ud_sync_scope_config:
            self.ud_sync_scope_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_sync_status is not None:
            result['GroupSyncStatus'] = self.group_sync_status

        if self.incremental_callback_status is not None:
            result['IncrementalCallbackStatus'] = self.incremental_callback_status

        if self.ud_sync_scope_config is not None:
            result['UdSyncScopeConfig'] = self.ud_sync_scope_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupSyncStatus') is not None:
            self.group_sync_status = m.get('GroupSyncStatus')

        if m.get('IncrementalCallbackStatus') is not None:
            self.incremental_callback_status = m.get('IncrementalCallbackStatus')

        if m.get('UdSyncScopeConfig') is not None:
            temp_model = main_models.GetIdentityProviderResponseBodyIdentityProviderDetailUdPullConfigUdSyncScopeConfig()
            self.ud_sync_scope_config = temp_model.from_map(m.get('UdSyncScopeConfig'))

        return self

class GetIdentityProviderResponseBodyIdentityProviderDetailUdPullConfigUdSyncScopeConfig(DaraModel):
    def __init__(
        self,
        source_scopes: List[str] = None,
        target_scope: str = None,
    ):
        # Synchronization source node.
        self.source_scopes = source_scopes
        # Synchronization target node.
        self.target_scope = target_scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_scopes is not None:
            result['SourceScopes'] = self.source_scopes

        if self.target_scope is not None:
            result['TargetScope'] = self.target_scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceScopes') is not None:
            self.source_scopes = m.get('SourceScopes')

        if m.get('TargetScope') is not None:
            self.target_scope = m.get('TargetScope')

        return self

class GetIdentityProviderResponseBodyIdentityProviderDetailOidcConfig(DaraModel):
    def __init__(
        self,
        authn_param: main_models.GetIdentityProviderResponseBodyIdentityProviderDetailOidcConfigAuthnParam = None,
        endpoint_config: main_models.GetIdentityProviderResponseBodyIdentityProviderDetailOidcConfigEndpointConfig = None,
        grant_scopes: List[str] = None,
        grant_type: str = None,
        pkce_challenge_method: str = None,
        pkce_required: bool = None,
    ):
        # OIDC client authentication configuration.
        self.authn_param = authn_param
        # OIDC endpoint configuration.
        self.endpoint_config = endpoint_config
        # OIDC authorization scope list.
        self.grant_scopes = grant_scopes
        # OIDC authorization grant type.
        self.grant_type = grant_type
        # Supported PKCE code challenge methods.
        self.pkce_challenge_method = pkce_challenge_method
        # Whether to use PKCE in authorization code grant flow.
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
            temp_model = main_models.GetIdentityProviderResponseBodyIdentityProviderDetailOidcConfigAuthnParam()
            self.authn_param = temp_model.from_map(m.get('AuthnParam'))

        if m.get('EndpointConfig') is not None:
            temp_model = main_models.GetIdentityProviderResponseBodyIdentityProviderDetailOidcConfigEndpointConfig()
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

class GetIdentityProviderResponseBodyIdentityProviderDetailOidcConfigEndpointConfig(DaraModel):
    def __init__(
        self,
        authorization_endpoint: str = None,
        issuer: str = None,
        jwks_uri: str = None,
        token_endpoint: str = None,
        userinfo_endpoint: str = None,
    ):
        # OAuth2 authorization endpoint.
        self.authorization_endpoint = authorization_endpoint
        # The CA that issued the certificate.
        self.issuer = issuer
        # Jwks uri.
        self.jwks_uri = jwks_uri
        # Token endpoint.
        self.token_endpoint = token_endpoint
        # OIDC user info endpoint.
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

class GetIdentityProviderResponseBodyIdentityProviderDetailOidcConfigAuthnParam(DaraModel):
    def __init__(
        self,
        authn_method: str = None,
        client_id: str = None,
        client_secret: str = None,
    ):
        # OIDC/OAuth2 authentication method.
        self.authn_method = authn_method
        # The client ID of the device whose access credential you want to query.
        self.client_id = client_id
        # The application secret registered with the OIDC authentication service.
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

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthnMethod') is not None:
            self.authn_method = m.get('AuthnMethod')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')

        return self

class GetIdentityProviderResponseBodyIdentityProviderDetailLdapConfig(DaraModel):
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
        # Administrator password.
        self.administrator_password = administrator_password
        # Administrator username.
        self.administrator_username = administrator_username
        # Whether to verify the fingerprint certificate.
        self.certificate_fingerprint_status = certificate_fingerprint_status
        # Certificate fingerprint list.
        self.certificate_fingerprints = certificate_fingerprints
        # Ldap protocol.
        self.ldap_protocol = ldap_protocol
        # ldap server host.
        self.ldap_server_host = ldap_server_host
        # ldap server port.
        self.ldap_server_port = ldap_server_port
        # StartTls status.
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

class GetIdentityProviderResponseBodyIdentityProviderDetailLarkConfig(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret: str = None,
        encrypt_key: str = None,
        enterprise_number: str = None,
        verification_token: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The creation time.
        self.app_secret = app_secret
        # Feishu encryptKey.
        self.encrypt_key = encrypt_key
        # Feishu enterprise code.
        self.enterprise_number = enterprise_number
        # Feishu verificationToken.
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

        if self.enterprise_number is not None:
            result['EnterpriseNumber'] = self.enterprise_number

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

        if m.get('EnterpriseNumber') is not None:
            self.enterprise_number = m.get('EnterpriseNumber')

        if m.get('VerificationToken') is not None:
            self.verification_token = m.get('VerificationToken')

        return self

class GetIdentityProviderResponseBodyIdentityProviderDetailDingtalkProvisioningConfig(DaraModel):
    def __init__(
        self,
        authed_department_ids: List[main_models.GetIdentityProviderResponseBodyIdentityProviderDetailDingtalkProvisioningConfigAuthedDepartmentIds] = None,
        authed_users: List[main_models.GetIdentityProviderResponseBodyIdentityProviderDetailDingtalkProvisioningConfigAuthedUsers] = None,
        corp_id: str = None,
        corp_name: str = None,
    ):
        # List of authorized DingTalk departments.
        self.authed_department_ids = authed_department_ids
        # Authorized DingTalk account list.
        self.authed_users = authed_users
        # DingTalk enterprise corpId.
        self.corp_id = corp_id
        # The name of the company.
        self.corp_name = corp_name

    def validate(self):
        if self.authed_department_ids:
            for v1 in self.authed_department_ids:
                 if v1:
                    v1.validate()
        if self.authed_users:
            for v1 in self.authed_users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AuthedDepartmentIds'] = []
        if self.authed_department_ids is not None:
            for k1 in self.authed_department_ids:
                result['AuthedDepartmentIds'].append(k1.to_map() if k1 else None)

        result['AuthedUsers'] = []
        if self.authed_users is not None:
            for k1 in self.authed_users:
                result['AuthedUsers'].append(k1.to_map() if k1 else None)

        if self.corp_id is not None:
            result['CorpId'] = self.corp_id

        if self.corp_name is not None:
            result['CorpName'] = self.corp_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authed_department_ids = []
        if m.get('AuthedDepartmentIds') is not None:
            for k1 in m.get('AuthedDepartmentIds'):
                temp_model = main_models.GetIdentityProviderResponseBodyIdentityProviderDetailDingtalkProvisioningConfigAuthedDepartmentIds()
                self.authed_department_ids.append(temp_model.from_map(k1))

        self.authed_users = []
        if m.get('AuthedUsers') is not None:
            for k1 in m.get('AuthedUsers'):
                temp_model = main_models.GetIdentityProviderResponseBodyIdentityProviderDetailDingtalkProvisioningConfigAuthedUsers()
                self.authed_users.append(temp_model.from_map(k1))

        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')

        if m.get('CorpName') is not None:
            self.corp_name = m.get('CorpName')

        return self

class GetIdentityProviderResponseBodyIdentityProviderDetailDingtalkProvisioningConfigAuthedUsers(DaraModel):
    def __init__(
        self,
        name: str = None,
        user_id: str = None,
    ):
        # DingTalk user name.
        self.name = name
        # DingTalk user id.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetIdentityProviderResponseBodyIdentityProviderDetailDingtalkProvisioningConfigAuthedDepartmentIds(DaraModel):
    def __init__(
        self,
        dept_id: str = None,
        dept_name: str = None,
    ):
        # Department ID.
        self.dept_id = dept_id
        # Department name.
        self.dept_name = dept_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dept_id is not None:
            result['DeptId'] = self.dept_id

        if self.dept_name is not None:
            result['DeptName'] = self.dept_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeptId') is not None:
            self.dept_id = m.get('DeptId')

        if m.get('DeptName') is not None:
            self.dept_name = m.get('DeptName')

        return self

class GetIdentityProviderResponseBodyIdentityProviderDetailDingtalkAppConfig(DaraModel):
    def __init__(
        self,
        app_key: str = None,
        app_secret: str = None,
        corp_id: str = None,
        dingtalk_login_version: str = None,
        dingtalk_version: str = None,
        encrypt_key: str = None,
        verification_token: str = None,
    ):
        # The AppKey for the application.
        self.app_key = app_key
        # The details of the application secret.
        self.app_secret = app_secret
        # DingTalk corpId.
        self.corp_id = corp_id
        # IDaaS EIAM 钉钉扫码登录版本
        self.dingtalk_login_version = dingtalk_login_version
        # DingTalk Version.
        self.dingtalk_version = dingtalk_version
        # DingTalk  encrypt key.
        self.encrypt_key = encrypt_key
        # DingTalk  verification token.
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

        if self.corp_id is not None:
            result['CorpId'] = self.corp_id

        if self.dingtalk_login_version is not None:
            result['DingtalkLoginVersion'] = self.dingtalk_login_version

        if self.dingtalk_version is not None:
            result['DingtalkVersion'] = self.dingtalk_version

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

        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')

        if m.get('DingtalkLoginVersion') is not None:
            self.dingtalk_login_version = m.get('DingtalkLoginVersion')

        if m.get('DingtalkVersion') is not None:
            self.dingtalk_version = m.get('DingtalkVersion')

        if m.get('EncryptKey') is not None:
            self.encrypt_key = m.get('EncryptKey')

        if m.get('VerificationToken') is not None:
            self.verification_token = m.get('VerificationToken')

        return self

