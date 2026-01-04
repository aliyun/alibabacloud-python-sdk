# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class CreateIdentityProviderRequest(DaraModel):
    def __init__(
        self,
        authn_config: main_models.CreateIdentityProviderRequestAuthnConfig = None,
        auto_create_user_config: main_models.CreateIdentityProviderRequestAutoCreateUserConfig = None,
        auto_update_user_config: main_models.CreateIdentityProviderRequestAutoUpdateUserConfig = None,
        binding_config: main_models.CreateIdentityProviderRequestBindingConfig = None,
        client_token: str = None,
        dingtalk_app_config: main_models.CreateIdentityProviderRequestDingtalkAppConfig = None,
        identity_provider_name: str = None,
        identity_provider_type: str = None,
        instance_id: str = None,
        lark_config: main_models.CreateIdentityProviderRequestLarkConfig = None,
        ldap_config: main_models.CreateIdentityProviderRequestLdapConfig = None,
        logo_url: str = None,
        network_access_endpoint_id: str = None,
        oidc_config: main_models.CreateIdentityProviderRequestOidcConfig = None,
        ud_pull_config: main_models.CreateIdentityProviderRequestUdPullConfig = None,
        ud_push_config: main_models.CreateIdentityProviderRequestUdPushConfig = None,
        we_com_config: main_models.CreateIdentityProviderRequestWeComConfig = None,
    ):
        # Authentication configuration information.
        self.authn_config = authn_config
        # Auto-create account rule configuration.
        self.auto_create_user_config = auto_create_user_config
        # Auto-update account rule configuration.
        self.auto_update_user_config = auto_update_user_config
        # OIDC identity provider account binding rule configuration.
        self.binding_config = binding_config
        # Idp client token.
        self.client_token = client_token
        # DingTalk configuration information.
        self.dingtalk_app_config = dingtalk_app_config
        # Identity provider name.
        # 
        # This parameter is required.
        self.identity_provider_name = identity_provider_name
        # Identity provider synchronization type.
        # 
        # - Inbound to DingTalk: urn:alibaba:idaas:idp:alibaba:dingtalk:pull
        # 
        # - Outbound to DingTalk: urn:alibaba:idaas:idp:alibaba:dingtalk:push
        # 
        # - Inbound to WeCom: urn:alibaba:idaas:idp:tencent:wecom:pull
        # 
        # - Inbound to Lark: urn:alibaba:idaas:idp:bytedance:lark:pull
        # 
        # - Inbound to AD: urn:alibaba:idaas:idp:microsoft:ad:pull
        # 
        # - Inbound to LDAP: urn:alibaba:idaas:idp:unknown:ldap:pull
        # 
        # - Standard OIDC: urn:alibaba:idaas:idp:standard:oidc
        # 
        # - SASE Custom OIDC: urn:alibaba:idaas:idp:alibaba:sase
        # 
        # This parameter is required.
        self.identity_provider_type = identity_provider_type
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Lark (Feishu) configuration information.
        self.lark_config = lark_config
        # AD/LDAP configuration information.
        self.ldap_config = ldap_config
        # IdP logo url.
        self.logo_url = logo_url
        # The unique identifier of the network access endpoint.
        self.network_access_endpoint_id = network_access_endpoint_id
        # OIDC IdP configuration.
        self.oidc_config = oidc_config
        # Inbound synchronization configuration information.
        self.ud_pull_config = ud_pull_config
        # Outbound synchronization configuration information.
        self.ud_push_config = ud_push_config
        # WeCom configuration information.
        self.we_com_config = we_com_config

    def validate(self):
        if self.authn_config:
            self.authn_config.validate()
        if self.auto_create_user_config:
            self.auto_create_user_config.validate()
        if self.auto_update_user_config:
            self.auto_update_user_config.validate()
        if self.binding_config:
            self.binding_config.validate()
        if self.dingtalk_app_config:
            self.dingtalk_app_config.validate()
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
        if self.authn_config is not None:
            result['AuthnConfig'] = self.authn_config.to_map()

        if self.auto_create_user_config is not None:
            result['AutoCreateUserConfig'] = self.auto_create_user_config.to_map()

        if self.auto_update_user_config is not None:
            result['AutoUpdateUserConfig'] = self.auto_update_user_config.to_map()

        if self.binding_config is not None:
            result['BindingConfig'] = self.binding_config.to_map()

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dingtalk_app_config is not None:
            result['DingtalkAppConfig'] = self.dingtalk_app_config.to_map()

        if self.identity_provider_name is not None:
            result['IdentityProviderName'] = self.identity_provider_name

        if self.identity_provider_type is not None:
            result['IdentityProviderType'] = self.identity_provider_type

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

        if self.ud_pull_config is not None:
            result['UdPullConfig'] = self.ud_pull_config.to_map()

        if self.ud_push_config is not None:
            result['UdPushConfig'] = self.ud_push_config.to_map()

        if self.we_com_config is not None:
            result['WeComConfig'] = self.we_com_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthnConfig') is not None:
            temp_model = main_models.CreateIdentityProviderRequestAuthnConfig()
            self.authn_config = temp_model.from_map(m.get('AuthnConfig'))

        if m.get('AutoCreateUserConfig') is not None:
            temp_model = main_models.CreateIdentityProviderRequestAutoCreateUserConfig()
            self.auto_create_user_config = temp_model.from_map(m.get('AutoCreateUserConfig'))

        if m.get('AutoUpdateUserConfig') is not None:
            temp_model = main_models.CreateIdentityProviderRequestAutoUpdateUserConfig()
            self.auto_update_user_config = temp_model.from_map(m.get('AutoUpdateUserConfig'))

        if m.get('BindingConfig') is not None:
            temp_model = main_models.CreateIdentityProviderRequestBindingConfig()
            self.binding_config = temp_model.from_map(m.get('BindingConfig'))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DingtalkAppConfig') is not None:
            temp_model = main_models.CreateIdentityProviderRequestDingtalkAppConfig()
            self.dingtalk_app_config = temp_model.from_map(m.get('DingtalkAppConfig'))

        if m.get('IdentityProviderName') is not None:
            self.identity_provider_name = m.get('IdentityProviderName')

        if m.get('IdentityProviderType') is not None:
            self.identity_provider_type = m.get('IdentityProviderType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LarkConfig') is not None:
            temp_model = main_models.CreateIdentityProviderRequestLarkConfig()
            self.lark_config = temp_model.from_map(m.get('LarkConfig'))

        if m.get('LdapConfig') is not None:
            temp_model = main_models.CreateIdentityProviderRequestLdapConfig()
            self.ldap_config = temp_model.from_map(m.get('LdapConfig'))

        if m.get('LogoUrl') is not None:
            self.logo_url = m.get('LogoUrl')

        if m.get('NetworkAccessEndpointId') is not None:
            self.network_access_endpoint_id = m.get('NetworkAccessEndpointId')

        if m.get('OidcConfig') is not None:
            temp_model = main_models.CreateIdentityProviderRequestOidcConfig()
            self.oidc_config = temp_model.from_map(m.get('OidcConfig'))

        if m.get('UdPullConfig') is not None:
            temp_model = main_models.CreateIdentityProviderRequestUdPullConfig()
            self.ud_pull_config = temp_model.from_map(m.get('UdPullConfig'))

        if m.get('UdPushConfig') is not None:
            temp_model = main_models.CreateIdentityProviderRequestUdPushConfig()
            self.ud_push_config = temp_model.from_map(m.get('UdPushConfig'))

        if m.get('WeComConfig') is not None:
            temp_model = main_models.CreateIdentityProviderRequestWeComConfig()
            self.we_com_config = temp_model.from_map(m.get('WeComConfig'))

        return self

class CreateIdentityProviderRequestWeComConfig(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        authorize_callback_domain: str = None,
        corp_id: str = None,
        corp_secret: str = None,
        trustable_domain: str = None,
    ):
        # Agent ID of the self-built WeCom application.
        self.agent_id = agent_id
        # Authorization callback domain.
        self.authorize_callback_domain = authorize_callback_domain
        # Corp ID of the self-built WeCom application.
        self.corp_id = corp_id
        # Corp Secret of the self-built WeCom application.
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

class CreateIdentityProviderRequestUdPushConfig(DaraModel):
    def __init__(
        self,
        incremental_callback_status: str = None,
        periodic_sync_config: main_models.CreateIdentityProviderRequestUdPushConfigPeriodicSyncConfig = None,
        periodic_sync_status: str = None,
        ud_sync_scope_configs: List[main_models.CreateIdentityProviderRequestUdPushConfigUdSyncScopeConfigs] = None,
    ):
        # Incremental callback status. This field is reserved and currently not in use; please ignore it.
        self.incremental_callback_status = incremental_callback_status
        self.periodic_sync_config = periodic_sync_config
        # Periodic check status. This field is currently not in use, please ignore it.
        self.periodic_sync_status = periodic_sync_status
        # Outbound synchronization configuration information.
        self.ud_sync_scope_configs = ud_sync_scope_configs

    def validate(self):
        if self.periodic_sync_config:
            self.periodic_sync_config.validate()
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

        if self.periodic_sync_config is not None:
            result['PeriodicSyncConfig'] = self.periodic_sync_config.to_map()

        if self.periodic_sync_status is not None:
            result['PeriodicSyncStatus'] = self.periodic_sync_status

        result['UdSyncScopeConfigs'] = []
        if self.ud_sync_scope_configs is not None:
            for k1 in self.ud_sync_scope_configs:
                result['UdSyncScopeConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncrementalCallbackStatus') is not None:
            self.incremental_callback_status = m.get('IncrementalCallbackStatus')

        if m.get('PeriodicSyncConfig') is not None:
            temp_model = main_models.CreateIdentityProviderRequestUdPushConfigPeriodicSyncConfig()
            self.periodic_sync_config = temp_model.from_map(m.get('PeriodicSyncConfig'))

        if m.get('PeriodicSyncStatus') is not None:
            self.periodic_sync_status = m.get('PeriodicSyncStatus')

        self.ud_sync_scope_configs = []
        if m.get('UdSyncScopeConfigs') is not None:
            for k1 in m.get('UdSyncScopeConfigs'):
                temp_model = main_models.CreateIdentityProviderRequestUdPushConfigUdSyncScopeConfigs()
                self.ud_sync_scope_configs.append(temp_model.from_map(k1))

        return self

class CreateIdentityProviderRequestUdPushConfigUdSyncScopeConfigs(DaraModel):
    def __init__(
        self,
        source_scopes: List[str] = None,
        target_scope: str = None,
    ):
        # List of source nodes for synchronization.
        self.source_scopes = source_scopes
        # Target node for synchronization.
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

class CreateIdentityProviderRequestUdPushConfigPeriodicSyncConfig(DaraModel):
    def __init__(
        self,
        periodic_sync_cron: str = None,
        periodic_sync_times: List[int] = None,
        periodic_sync_type: str = None,
    ):
        self.periodic_sync_cron = periodic_sync_cron
        self.periodic_sync_times = periodic_sync_times
        self.periodic_sync_type = periodic_sync_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.periodic_sync_cron is not None:
            result['PeriodicSyncCron'] = self.periodic_sync_cron

        if self.periodic_sync_times is not None:
            result['PeriodicSyncTimes'] = self.periodic_sync_times

        if self.periodic_sync_type is not None:
            result['PeriodicSyncType'] = self.periodic_sync_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeriodicSyncCron') is not None:
            self.periodic_sync_cron = m.get('PeriodicSyncCron')

        if m.get('PeriodicSyncTimes') is not None:
            self.periodic_sync_times = m.get('PeriodicSyncTimes')

        if m.get('PeriodicSyncType') is not None:
            self.periodic_sync_type = m.get('PeriodicSyncType')

        return self

class CreateIdentityProviderRequestUdPullConfig(DaraModel):
    def __init__(
        self,
        group_sync_status: str = None,
        incremental_callback_status: str = None,
        periodic_sync_config: main_models.CreateIdentityProviderRequestUdPullConfigPeriodicSyncConfig = None,
        periodic_sync_status: str = None,
        ud_sync_scope_config: main_models.CreateIdentityProviderRequestUdPullConfigUdSyncScopeConfig = None,
    ):
        # Whether group synchronization is supported. The default value is disabled. Possible values:
        # 
        # - Disabled: disabled
        # 
        # - Enabled: enabled
        self.group_sync_status = group_sync_status
        # Incremental callback status, indicating whether to process incremental callback data from the IdP. Possible values:
        # 
        # - Disabled: disabled
        # 
        # - Enabled: enabled
        self.incremental_callback_status = incremental_callback_status
        # Scheduled configuration verification.
        self.periodic_sync_config = periodic_sync_config
        # Periodic check status, indicating whether to periodically check the data differences between EIAM and the identity provider. Possible values:
        # - Disabled: disabled
        # 
        # - Enabled: enabled
        self.periodic_sync_status = periodic_sync_status
        # Synchronization scope configuration information.
        self.ud_sync_scope_config = ud_sync_scope_config

    def validate(self):
        if self.periodic_sync_config:
            self.periodic_sync_config.validate()
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

        if self.periodic_sync_config is not None:
            result['PeriodicSyncConfig'] = self.periodic_sync_config.to_map()

        if self.periodic_sync_status is not None:
            result['PeriodicSyncStatus'] = self.periodic_sync_status

        if self.ud_sync_scope_config is not None:
            result['UdSyncScopeConfig'] = self.ud_sync_scope_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupSyncStatus') is not None:
            self.group_sync_status = m.get('GroupSyncStatus')

        if m.get('IncrementalCallbackStatus') is not None:
            self.incremental_callback_status = m.get('IncrementalCallbackStatus')

        if m.get('PeriodicSyncConfig') is not None:
            temp_model = main_models.CreateIdentityProviderRequestUdPullConfigPeriodicSyncConfig()
            self.periodic_sync_config = temp_model.from_map(m.get('PeriodicSyncConfig'))

        if m.get('PeriodicSyncStatus') is not None:
            self.periodic_sync_status = m.get('PeriodicSyncStatus')

        if m.get('UdSyncScopeConfig') is not None:
            temp_model = main_models.CreateIdentityProviderRequestUdPullConfigUdSyncScopeConfig()
            self.ud_sync_scope_config = temp_model.from_map(m.get('UdSyncScopeConfig'))

        return self

class CreateIdentityProviderRequestUdPullConfigUdSyncScopeConfig(DaraModel):
    def __init__(
        self,
        source_scopes: List[str] = None,
        target_scope: str = None,
    ):
        # List of source nodes for synchronization.
        self.source_scopes = source_scopes
        # Synchronize target node, and fill in the IDaaS organization ID.
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

class CreateIdentityProviderRequestUdPullConfigPeriodicSyncConfig(DaraModel):
    def __init__(
        self,
        periodic_sync_cron: str = None,
        periodic_sync_times: List[int] = None,
        periodic_sync_type: str = None,
    ):
        # cron expression.
        self.periodic_sync_cron = periodic_sync_cron
        # Collection of time points.
        self.periodic_sync_times = periodic_sync_times
        # type.
        self.periodic_sync_type = periodic_sync_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.periodic_sync_cron is not None:
            result['PeriodicSyncCron'] = self.periodic_sync_cron

        if self.periodic_sync_times is not None:
            result['PeriodicSyncTimes'] = self.periodic_sync_times

        if self.periodic_sync_type is not None:
            result['PeriodicSyncType'] = self.periodic_sync_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeriodicSyncCron') is not None:
            self.periodic_sync_cron = m.get('PeriodicSyncCron')

        if m.get('PeriodicSyncTimes') is not None:
            self.periodic_sync_times = m.get('PeriodicSyncTimes')

        if m.get('PeriodicSyncType') is not None:
            self.periodic_sync_type = m.get('PeriodicSyncType')

        return self

class CreateIdentityProviderRequestOidcConfig(DaraModel):
    def __init__(
        self,
        authn_param: main_models.CreateIdentityProviderRequestOidcConfigAuthnParam = None,
        endpoint_config: main_models.CreateIdentityProviderRequestOidcConfigEndpointConfig = None,
        grant_scopes: List[str] = None,
        grant_type: str = None,
        pkce_challenge_method: str = None,
        pkce_required: bool = None,
    ):
        # OIDC client authentication configuration.
        self.authn_param = authn_param
        # OIDC endpoint configuration.
        self.endpoint_config = endpoint_config
        # OIDC grant scopes collection.
        self.grant_scopes = grant_scopes
        # OIDC grant type.
        self.grant_type = grant_type
        # PKCE algorithm. Possible values:
        # 
        # - SHA256: S256
        # 
        # - Plain text: plain
        self.pkce_challenge_method = pkce_challenge_method
        # Whether to use PKCE in the AuthorizationCode grant mode.
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
            temp_model = main_models.CreateIdentityProviderRequestOidcConfigAuthnParam()
            self.authn_param = temp_model.from_map(m.get('AuthnParam'))

        if m.get('EndpointConfig') is not None:
            temp_model = main_models.CreateIdentityProviderRequestOidcConfigEndpointConfig()
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

class CreateIdentityProviderRequestOidcConfigEndpointConfig(DaraModel):
    def __init__(
        self,
        authorization_endpoint: str = None,
        issuer: str = None,
        jwks_uri: str = None,
        token_endpoint: str = None,
        userinfo_endpoint: str = None,
    ):
        # OIDC authorization endpoint.
        self.authorization_endpoint = authorization_endpoint
        # OIDC issuer information.
        self.issuer = issuer
        # OIDC jwks uri.
        self.jwks_uri = jwks_uri
        # OIDC token endpoint.
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

class CreateIdentityProviderRequestOidcConfigAuthnParam(DaraModel):
    def __init__(
        self,
        authn_method: str = None,
        client_id: str = None,
        client_secret: str = None,
    ):
        # OIDC authentication method. Value range:
        # 
        # - client_secret_basic
        # 
        # - client_secret_post
        self.authn_method = authn_method
        # The ID of the client.
        self.client_id = client_id
        # The  secret of the client.
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

class CreateIdentityProviderRequestLdapConfig(DaraModel):
    def __init__(
        self,
        administrator_password: str = None,
        administrator_username: str = None,
        certificate_fingerprint_status: str = None,
        certificate_fingerprints: List[str] = None,
        group_member_attribute_name: str = None,
        group_object_class: str = None,
        group_object_class_custom_filter: str = None,
        ldap_protocol: str = None,
        ldap_server_host: str = None,
        ldap_server_port: int = None,
        organization_unit_object_class: str = None,
        organizational_unit_rdn: str = None,
        password_sync_status: str = None,
        start_tls_status: str = None,
        user_login_identifier: str = None,
        user_object_class: str = None,
        user_object_class_custom_filter: str = None,
        user_rdn: str = None,
    ):
        # Administrator password.
        self.administrator_password = administrator_password
        # Administrator username.
        self.administrator_username = administrator_username
        # Whether to verify the certificate fingerprint. Value range:
        # 
        # - Disabled: disabled
        # 
        # - Enabled: enabled
        self.certificate_fingerprint_status = certificate_fingerprint_status
        # List of certificate fingerprints.
        self.certificate_fingerprints = certificate_fingerprints
        # Group member attribute name.
        self.group_member_attribute_name = group_member_attribute_name
        # Group ObjectClass.
        self.group_object_class = group_object_class
        # Custom filter for Group ObjectClass.
        self.group_object_class_custom_filter = group_object_class_custom_filter
        # Communication protocol.
        self.ldap_protocol = ldap_protocol
        # AD/LDAP server address.
        self.ldap_server_host = ldap_server_host
        # AD/LDAP port number.
        self.ldap_server_port = ldap_server_port
        # Organization Unit ObjectClass.
        self.organization_unit_object_class = organization_unit_object_class
        self.organizational_unit_rdn = organizational_unit_rdn
        self.password_sync_status = password_sync_status
        # Whether startTLS is enabled. Value range:
        # - Disabled: disabled
        # 
        # - Enabled: enabled
        self.start_tls_status = start_tls_status
        # User login identifier.
        self.user_login_identifier = user_login_identifier
        # User ObjectClass.
        self.user_object_class = user_object_class
        # Custom filter for User ObjectClass.
        self.user_object_class_custom_filter = user_object_class_custom_filter
        self.user_rdn = user_rdn

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

        if self.group_member_attribute_name is not None:
            result['GroupMemberAttributeName'] = self.group_member_attribute_name

        if self.group_object_class is not None:
            result['GroupObjectClass'] = self.group_object_class

        if self.group_object_class_custom_filter is not None:
            result['GroupObjectClassCustomFilter'] = self.group_object_class_custom_filter

        if self.ldap_protocol is not None:
            result['LdapProtocol'] = self.ldap_protocol

        if self.ldap_server_host is not None:
            result['LdapServerHost'] = self.ldap_server_host

        if self.ldap_server_port is not None:
            result['LdapServerPort'] = self.ldap_server_port

        if self.organization_unit_object_class is not None:
            result['OrganizationUnitObjectClass'] = self.organization_unit_object_class

        if self.organizational_unit_rdn is not None:
            result['OrganizationalUnitRdn'] = self.organizational_unit_rdn

        if self.password_sync_status is not None:
            result['PasswordSyncStatus'] = self.password_sync_status

        if self.start_tls_status is not None:
            result['StartTlsStatus'] = self.start_tls_status

        if self.user_login_identifier is not None:
            result['UserLoginIdentifier'] = self.user_login_identifier

        if self.user_object_class is not None:
            result['UserObjectClass'] = self.user_object_class

        if self.user_object_class_custom_filter is not None:
            result['UserObjectClassCustomFilter'] = self.user_object_class_custom_filter

        if self.user_rdn is not None:
            result['UserRdn'] = self.user_rdn

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

        if m.get('GroupMemberAttributeName') is not None:
            self.group_member_attribute_name = m.get('GroupMemberAttributeName')

        if m.get('GroupObjectClass') is not None:
            self.group_object_class = m.get('GroupObjectClass')

        if m.get('GroupObjectClassCustomFilter') is not None:
            self.group_object_class_custom_filter = m.get('GroupObjectClassCustomFilter')

        if m.get('LdapProtocol') is not None:
            self.ldap_protocol = m.get('LdapProtocol')

        if m.get('LdapServerHost') is not None:
            self.ldap_server_host = m.get('LdapServerHost')

        if m.get('LdapServerPort') is not None:
            self.ldap_server_port = m.get('LdapServerPort')

        if m.get('OrganizationUnitObjectClass') is not None:
            self.organization_unit_object_class = m.get('OrganizationUnitObjectClass')

        if m.get('OrganizationalUnitRdn') is not None:
            self.organizational_unit_rdn = m.get('OrganizationalUnitRdn')

        if m.get('PasswordSyncStatus') is not None:
            self.password_sync_status = m.get('PasswordSyncStatus')

        if m.get('StartTlsStatus') is not None:
            self.start_tls_status = m.get('StartTlsStatus')

        if m.get('UserLoginIdentifier') is not None:
            self.user_login_identifier = m.get('UserLoginIdentifier')

        if m.get('UserObjectClass') is not None:
            self.user_object_class = m.get('UserObjectClass')

        if m.get('UserObjectClassCustomFilter') is not None:
            self.user_object_class_custom_filter = m.get('UserObjectClassCustomFilter')

        if m.get('UserRdn') is not None:
            self.user_rdn = m.get('UserRdn')

        return self

class CreateIdentityProviderRequestLarkConfig(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret: str = None,
        encrypt_key: str = None,
        enterprise_number: str = None,
        verification_token: str = None,
    ):
        # Lark (Feishu) app appId.
        self.app_id = app_id
        # Lark (Feishu) app secret.
        self.app_secret = app_secret
        # Lark (Feishu) encrypt key.
        self.encrypt_key = encrypt_key
        # Lark (Feishu) enterprise number.
        self.enterprise_number = enterprise_number
        # Lark (Feishu)  verification token.
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

class CreateIdentityProviderRequestDingtalkAppConfig(DaraModel):
    def __init__(
        self,
        app_key: str = None,
        app_secret: str = None,
        corp_id: str = None,
        dingtalk_version: str = None,
        encrypt_key: str = None,
        verification_token: str = None,
    ):
        # AppKey of the DingTalk application.
        self.app_key = app_key
        # AppSecret of the DingTalk application.
        self.app_secret = app_secret
        # CorpId of the DingTalk application.
        self.corp_id = corp_id
        # DingTalk edition. Valid values:
        # 
        # public_dingtalk – Standard DingTalk.
        # 
        # private_dingtalk – Dedicated DingTalk.
        self.dingtalk_version = dingtalk_version
        # DingTalk encrypt key.
        self.encrypt_key = encrypt_key
        # DingTalk verification token.
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

        if m.get('DingtalkVersion') is not None:
            self.dingtalk_version = m.get('DingtalkVersion')

        if m.get('EncryptKey') is not None:
            self.encrypt_key = m.get('EncryptKey')

        if m.get('VerificationToken') is not None:
            self.verification_token = m.get('VerificationToken')

        return self

class CreateIdentityProviderRequestBindingConfig(DaraModel):
    def __init__(
        self,
        auto_match_user_profile_expressions: List[main_models.CreateIdentityProviderRequestBindingConfigAutoMatchUserProfileExpressions] = None,
        auto_match_user_status: str = None,
        mapping_binding_status: str = None,
    ):
        # List of rules for automatically matching accounts.
        self.auto_match_user_profile_expressions = auto_match_user_profile_expressions
        # Whether automatic account matching is enabled. Value range:
        # 
        # - Disabled: disabled
        # 
        # - Enabled: enabled
        self.auto_match_user_status = auto_match_user_status
        # Whether the user manual account binding function is enabled. Value range:
        # - Disabled: disabled
        # 
        # - Enabled: enabled
        self.mapping_binding_status = mapping_binding_status

    def validate(self):
        if self.auto_match_user_profile_expressions:
            for v1 in self.auto_match_user_profile_expressions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AutoMatchUserProfileExpressions'] = []
        if self.auto_match_user_profile_expressions is not None:
            for k1 in self.auto_match_user_profile_expressions:
                result['AutoMatchUserProfileExpressions'].append(k1.to_map() if k1 else None)

        if self.auto_match_user_status is not None:
            result['AutoMatchUserStatus'] = self.auto_match_user_status

        if self.mapping_binding_status is not None:
            result['MappingBindingStatus'] = self.mapping_binding_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_match_user_profile_expressions = []
        if m.get('AutoMatchUserProfileExpressions') is not None:
            for k1 in m.get('AutoMatchUserProfileExpressions'):
                temp_model = main_models.CreateIdentityProviderRequestBindingConfigAutoMatchUserProfileExpressions()
                self.auto_match_user_profile_expressions.append(temp_model.from_map(k1))

        if m.get('AutoMatchUserStatus') is not None:
            self.auto_match_user_status = m.get('AutoMatchUserStatus')

        if m.get('MappingBindingStatus') is not None:
            self.mapping_binding_status = m.get('MappingBindingStatus')

        return self

class CreateIdentityProviderRequestBindingConfigAutoMatchUserProfileExpressions(DaraModel):
    def __init__(
        self,
        expression_mapping_type: str = None,
        source_value_expression: str = None,
        target_field: str = None,
        target_field_description: str = None,
    ):
        # Type of the expression. Value range:
        # 
        # - Field: filed
        # 
        # - Expression: expression
        self.expression_mapping_type = expression_mapping_type
        # Expression for the mapped attribute value.
        self.source_value_expression = source_value_expression
        # Name of the target attribute.
        self.target_field = target_field
        # Description of the target attribute.
        self.target_field_description = target_field_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression_mapping_type is not None:
            result['ExpressionMappingType'] = self.expression_mapping_type

        if self.source_value_expression is not None:
            result['SourceValueExpression'] = self.source_value_expression

        if self.target_field is not None:
            result['TargetField'] = self.target_field

        if self.target_field_description is not None:
            result['TargetFieldDescription'] = self.target_field_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpressionMappingType') is not None:
            self.expression_mapping_type = m.get('ExpressionMappingType')

        if m.get('SourceValueExpression') is not None:
            self.source_value_expression = m.get('SourceValueExpression')

        if m.get('TargetField') is not None:
            self.target_field = m.get('TargetField')

        if m.get('TargetFieldDescription') is not None:
            self.target_field_description = m.get('TargetFieldDescription')

        return self

class CreateIdentityProviderRequestAutoUpdateUserConfig(DaraModel):
    def __init__(
        self,
        auto_update_user_status: str = None,
    ):
        # Whether auto-updating of accounts is enabled. Possible values:
        # - Disabled: disabled
        # 
        # - Enabled: enabled
        self.auto_update_user_status = auto_update_user_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_update_user_status is not None:
            result['AutoUpdateUserStatus'] = self.auto_update_user_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoUpdateUserStatus') is not None:
            self.auto_update_user_status = m.get('AutoUpdateUserStatus')

        return self

class CreateIdentityProviderRequestAutoCreateUserConfig(DaraModel):
    def __init__(
        self,
        auto_create_user_status: str = None,
        target_organizational_unit_ids: List[str] = None,
    ):
        # Whether auto-creation of accounts is enabled. Possible values:
        # - Disabled: disabled
        # 
        # - Enabled: enabled
        self.auto_create_user_status = auto_create_user_status
        # Target organizational unit IDs collection.
        self.target_organizational_unit_ids = target_organizational_unit_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_create_user_status is not None:
            result['AutoCreateUserStatus'] = self.auto_create_user_status

        if self.target_organizational_unit_ids is not None:
            result['TargetOrganizationalUnitIds'] = self.target_organizational_unit_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreateUserStatus') is not None:
            self.auto_create_user_status = m.get('AutoCreateUserStatus')

        if m.get('TargetOrganizationalUnitIds') is not None:
            self.target_organizational_unit_ids = m.get('TargetOrganizationalUnitIds')

        return self

class CreateIdentityProviderRequestAuthnConfig(DaraModel):
    def __init__(
        self,
        authn_status: str = None,
        auto_update_password_status: str = None,
    ):
        # Whether the corresponding IdP supports authentication. Value range:
        # - Disabled: disabled
        # 
        # - Enabled: enabled
        self.authn_status = authn_status
        # Whether automatic password update is supported. Value range:
        # - Disabled: disabled
        # 
        # - Enabled: enabled
        self.auto_update_password_status = auto_update_password_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authn_status is not None:
            result['AuthnStatus'] = self.authn_status

        if self.auto_update_password_status is not None:
            result['AutoUpdatePasswordStatus'] = self.auto_update_password_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthnStatus') is not None:
            self.authn_status = m.get('AuthnStatus')

        if m.get('AutoUpdatePasswordStatus') is not None:
            self.auto_update_password_status = m.get('AutoUpdatePasswordStatus')

        return self

