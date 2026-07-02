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
        # The identity provider information.
        self.identity_provider_detail = identity_provider_detail
        # The request ID.
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
        endpoint_metadata: main_models.GetIdentityProviderResponseBodyIdentityProviderDetailEndpointMetadata = None,
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
        saml_config: main_models.GetIdentityProviderResponseBodyIdentityProviderDetailSamlConfig = None,
        ud_pull_config: main_models.GetIdentityProviderResponseBodyIdentityProviderDetailUdPullConfig = None,
        ud_pull_status: str = None,
        ud_push_config: main_models.GetIdentityProviderResponseBodyIdentityProviderDetailUdPushConfig = None,
        ud_push_status: str = None,
        update_time: int = None,
        we_com_config: main_models.GetIdentityProviderResponseBodyIdentityProviderDetailWeComConfig = None,
    ):
        # The advanced configuration status. Valid values:
        # 
        # - disabled: Disabled.
        # 
        # - enabled: Enabled.
        self.advanced_status = advanced_status
        # The authentication source product, such as Okta, Google, or Azure AD. Valid values:
        # 
        # - urn:alibaba:idaas:idp:alibaba:dingtalk: DingTalk.
        # 
        # - urn:alibaba:idaas:idp:unknown:ldap: LDAP.
        # 
        # - urn:alibaba:idaas:idp:alibaba:idaas: Alibaba Cloud IDaaS.
        # 
        # - urn:alibaba:idaas:idp:tencent:wecom: WeCom.
        # 
        # - urn:alibaba:idaas:idp:bytedance:lark: Lark.
        # 
        # - urn:alibaba:idaas:idp:microsoft:ad: Active Directory.
        # 
        # - urn:alibaba:idaas:idp:microsoft:aad: Azure Active Directory.
        # 
        # - urn:alibaba:idaas:idp:alibaba:sase: Alibaba Cloud SASE.
        self.authn_source_supplier = authn_source_supplier
        # The authentication method type, such as OIDC or SAML. Valid values:
        # 
        # - urn:alibaba:idaas:authntype:oidc: OIDC.
        # 
        # - urn:alibaba:idaas:authntype:saml2: SAML.
        self.authn_source_type = authn_source_type
        # Specifies whether the corresponding IdP supports authentication. Valid values:
        # 
        # - disabled: Disabled.
        # 
        # - enabled: Enabled.
        self.authn_status = authn_status
        # The creation time, in UNIX timestamp format. Unit: milliseconds.
        self.create_time = create_time
        # The description of the identity provider.
        self.description = description
        # The DingTalk basic configuration.
        self.dingtalk_app_config = dingtalk_app_config
        # The DingTalk synchronization configuration. This value is returned only for DingTalk identity providers.
        self.dingtalk_provisioning_config = dingtalk_provisioning_config
        # The endpoint metadata.
        self.endpoint_metadata = endpoint_metadata
        # The external ID of the identity provider.
        self.identity_provider_external_id = identity_provider_external_id
        # The identity provider ID.
        self.identity_provider_id = identity_provider_id
        # The name of the identity provider.
        self.identity_provider_name = identity_provider_name
        # The synchronization type of the identity provider. Valid values:
        # 
        # - urn:alibaba:idaas:idp:alibaba:dingtalk:pull: Inbound DingTalk.
        # 
        # - urn:alibaba:idaas:idp:alibaba:dingtalk:push: Outbound DingTalk.
        # 
        # - urn:alibaba:idaas:idp:tencent:wecom:pull: Inbound WeCom.
        # 
        # - urn:alibaba:idaas:idp:bytedance:lark:pull: Inbound Lark.
        # 
        # - urn:alibaba:idaas:idp:microsoft:ad:pull: Inbound AD.
        # 
        # - urn:alibaba:idaas:idp:unknown:ldap:pull: Inbound LDAP.
        # 
        # - urn:alibaba:idaas:idp:standard:oidc: Standard OIDC.
        # 
        # - urn:alibaba:idaas:idp:alibaba:sase: SASE custom OIDC.
        self.identity_provider_type = identity_provider_type
        # The instance ID.
        self.instance_id = instance_id
        # The Lark configuration.
        self.lark_config = lark_config
        # The result of the last status check.
        self.last_status_check_job_result = last_status_check_job_result
        # The AD/LDAP identity provider configuration.
        self.ldap_config = ldap_config
        # The lock reason.
        self.lock_reason = lock_reason
        # The custom logo URL of the identity provider.
        self.logo_url = logo_url
        # The network endpoint ID.
        self.network_access_endpoint_id = network_access_endpoint_id
        # The OIDC IdP configuration.
        self.oidc_config = oidc_config
        # The SAML IdP configuration.
        self.saml_config = saml_config
        # The inbound synchronization configuration.
        self.ud_pull_config = ud_pull_config
        # Specifies whether the inbound synchronization feature is supported. Valid values:
        # 
        # - disabled: Disabled.
        # 
        # - enabled: Enabled.
        self.ud_pull_status = ud_pull_status
        # The outbound synchronization configuration.
        self.ud_push_config = ud_push_config
        # Specifies whether the outbound synchronization feature is enabled. Valid values:
        # 
        # - disabled: Disabled.
        # 
        # - enabled: Enabled.
        self.ud_push_status = ud_push_status
        # The update time, in UNIX timestamp format. Unit: milliseconds.
        self.update_time = update_time
        # The WeCom configuration.
        self.we_com_config = we_com_config

    def validate(self):
        if self.dingtalk_app_config:
            self.dingtalk_app_config.validate()
        if self.dingtalk_provisioning_config:
            self.dingtalk_provisioning_config.validate()
        if self.endpoint_metadata:
            self.endpoint_metadata.validate()
        if self.lark_config:
            self.lark_config.validate()
        if self.ldap_config:
            self.ldap_config.validate()
        if self.oidc_config:
            self.oidc_config.validate()
        if self.saml_config:
            self.saml_config.validate()
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

        if self.endpoint_metadata is not None:
            result['EndpointMetadata'] = self.endpoint_metadata.to_map()

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

        if self.saml_config is not None:
            result['SamlConfig'] = self.saml_config.to_map()

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

        if m.get('EndpointMetadata') is not None:
            temp_model = main_models.GetIdentityProviderResponseBodyIdentityProviderDetailEndpointMetadata()
            self.endpoint_metadata = temp_model.from_map(m.get('EndpointMetadata'))

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

        if m.get('SamlConfig') is not None:
            temp_model = main_models.GetIdentityProviderResponseBodyIdentityProviderDetailSamlConfig()
            self.saml_config = temp_model.from_map(m.get('SamlConfig'))

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
        # The ID of the WeCom self-built application.
        self.agent_id = agent_id
        # The authorization callback domain.
        self.authorize_callback_domain = authorize_callback_domain
        # The CorpId of the WeCom self-built application.
        self.corp_id = corp_id
        # The CorpSecret of the WeCom self-built application.
        self.corp_secret = corp_secret
        # The trusted domain name.
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
        # This field is not in use. Ignore it.
        self.incremental_callback_status = incremental_callback_status
        # The list of synchronization scope configurations.
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
        # The list of synchronization source nodes.
        self.source_scopes = source_scopes
        # The synchronization target node.
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
        # Specifies whether group synchronization is enabled. Valid values:
        # 
        # - disabled: Disabled.
        # 
        # - enabled: Enabled.
        self.group_sync_status = group_sync_status
        # The incremental callback status. Specifies whether to process incremental callback data from the IdP. Valid values:
        # 
        # - disabled: Disabled.
        # 
        # - enabled: Enabled.
        self.incremental_callback_status = incremental_callback_status
        # The synchronization scope configuration.
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
        # The list of synchronization source nodes.
        self.source_scopes = source_scopes
        # The synchronization target node.
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

class GetIdentityProviderResponseBodyIdentityProviderDetailSamlConfig(DaraModel):
    def __init__(
        self,
        binding_method: str = None,
        certificates: List[main_models.GetIdentityProviderResponseBodyIdentityProviderDetailSamlConfigCertificates] = None,
        id_pentity_id: str = None,
        id_psso_url: str = None,
        max_clock_skew: int = None,
        require_request_signed: bool = None,
        want_assertions_signed: bool = None,
        want_response_signed: bool = None,
    ):
        # The binding type.
        self.binding_method = binding_method
        # The list of IdP signing certificates.
        self.certificates = certificates
        # The EntityId of the IdP.
        self.id_pentity_id = id_pentity_id
        # The logon URL of the IdP.
        self.id_psso_url = id_psso_url
        # The maximum clock skew.
        self.max_clock_skew = max_clock_skew
        # Specifies whether the request must be signed.
        self.require_request_signed = require_request_signed
        self.want_assertions_signed = want_assertions_signed
        self.want_response_signed = want_response_signed

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
        if self.binding_method is not None:
            result['BindingMethod'] = self.binding_method

        result['Certificates'] = []
        if self.certificates is not None:
            for k1 in self.certificates:
                result['Certificates'].append(k1.to_map() if k1 else None)

        if self.id_pentity_id is not None:
            result['IdPEntityId'] = self.id_pentity_id

        if self.id_psso_url is not None:
            result['IdPSsoUrl'] = self.id_psso_url

        if self.max_clock_skew is not None:
            result['MaxClockSkew'] = self.max_clock_skew

        if self.require_request_signed is not None:
            result['RequireRequestSigned'] = self.require_request_signed

        if self.want_assertions_signed is not None:
            result['WantAssertionsSigned'] = self.want_assertions_signed

        if self.want_response_signed is not None:
            result['WantResponseSigned'] = self.want_response_signed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindingMethod') is not None:
            self.binding_method = m.get('BindingMethod')

        self.certificates = []
        if m.get('Certificates') is not None:
            for k1 in m.get('Certificates'):
                temp_model = main_models.GetIdentityProviderResponseBodyIdentityProviderDetailSamlConfigCertificates()
                self.certificates.append(temp_model.from_map(k1))

        if m.get('IdPEntityId') is not None:
            self.id_pentity_id = m.get('IdPEntityId')

        if m.get('IdPSsoUrl') is not None:
            self.id_psso_url = m.get('IdPSsoUrl')

        if m.get('MaxClockSkew') is not None:
            self.max_clock_skew = m.get('MaxClockSkew')

        if m.get('RequireRequestSigned') is not None:
            self.require_request_signed = m.get('RequireRequestSigned')

        if m.get('WantAssertionsSigned') is not None:
            self.want_assertions_signed = m.get('WantAssertionsSigned')

        if m.get('WantResponseSigned') is not None:
            self.want_response_signed = m.get('WantResponseSigned')

        return self

class GetIdentityProviderResponseBodyIdentityProviderDetailSamlConfigCertificates(DaraModel):
    def __init__(
        self,
        certificate_metadata: main_models.GetIdentityProviderResponseBodyIdentityProviderDetailSamlConfigCertificatesCertificateMetadata = None,
        content: str = None,
    ):
        # The certificate metadata.
        self.certificate_metadata = certificate_metadata
        # The certificate content.
        self.content = content

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateMetadata') is not None:
            temp_model = main_models.GetIdentityProviderResponseBodyIdentityProviderDetailSamlConfigCertificatesCertificateMetadata()
            self.certificate_metadata = temp_model.from_map(m.get('CertificateMetadata'))

        if m.get('Content') is not None:
            self.content = m.get('Content')

        return self

class GetIdentityProviderResponseBodyIdentityProviderDetailSamlConfigCertificatesCertificateMetadata(DaraModel):
    def __init__(
        self,
        not_after: int = None,
        not_before: int = None,
    ):
        # The latest validity date of the certificate.
        self.not_after = not_after
        # The earliest validity date of the certificate.
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
        # The OIDC client authentication configuration.
        self.authn_param = authn_param
        # The OIDC endpoint configuration.
        self.endpoint_config = endpoint_config
        # The list of OIDC grant scopes.
        self.grant_scopes = grant_scopes
        # The OIDC grant type.
        self.grant_type = grant_type
        # The PKCE algorithm. Valid values:
        # 
        # - S256: SHA-256.
        # 
        # - plain: Plaintext.
        self.pkce_challenge_method = pkce_challenge_method
        # Specifies whether to use PKCE in the AuthorizationCode grant mode.
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
        # The OIDC authorization endpoint.
        self.authorization_endpoint = authorization_endpoint
        # The OIDC issuer information.
        self.issuer = issuer
        # The OIDC JWKS URI.
        self.jwks_uri = jwks_uri
        # The OIDC token endpoint.
        self.token_endpoint = token_endpoint
        # The OIDC user information endpoint.
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
        # The OIDC authentication method.
        self.authn_method = authn_method
        # The OIDC client ID.
        self.client_id = client_id
        # The OIDC client secret.
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
        # The AD/LDAP administrator password.
        self.administrator_password = administrator_password
        # The AD/LDAP administrator account.
        self.administrator_username = administrator_username
        # Specifies whether to verify the certificate fingerprint. Valid values:
        # 
        # - disabled: Disabled.
        # 
        # - enabled: Enabled.
        self.certificate_fingerprint_status = certificate_fingerprint_status
        # The list of certificate fingerprints.
        self.certificate_fingerprints = certificate_fingerprints
        # The communication protocol of AD/LDAP.
        self.ldap_protocol = ldap_protocol
        # The AD/LDAP server address.
        self.ldap_server_host = ldap_server_host
        # The AD/LDAP server address.
        self.ldap_server_port = ldap_server_port
        # Specifies whether StartTLS is enabled. Valid values:
        # 
        # - disabled: Disabled.
        # 
        # - enabled: Enabled.
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
        # The AppId of the Lark self-built application.
        self.app_id = app_id
        # The AppSecret of the Lark self-built application.
        self.app_secret = app_secret
        # The EncryptKey of the Lark self-built application.
        self.encrypt_key = encrypt_key
        # The Lark enterprise number.
        self.enterprise_number = enterprise_number
        # The VerificationToken of the Lark self-built application.
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

class GetIdentityProviderResponseBodyIdentityProviderDetailEndpointMetadata(DaraModel):
    def __init__(
        self,
        saml_acs_endpoint: str = None,
        saml_entity_id: str = None,
        saml_meta_endpoint: str = None,
    ):
        # The SAML Assertion Consumer Service (ACS) endpoint.
        self.saml_acs_endpoint = saml_acs_endpoint
        # The SAML EntityId.
        self.saml_entity_id = saml_entity_id
        # The SAML metadata endpoint.
        self.saml_meta_endpoint = saml_meta_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.saml_acs_endpoint is not None:
            result['SamlAcsEndpoint'] = self.saml_acs_endpoint

        if self.saml_entity_id is not None:
            result['SamlEntityId'] = self.saml_entity_id

        if self.saml_meta_endpoint is not None:
            result['SamlMetaEndpoint'] = self.saml_meta_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SamlAcsEndpoint') is not None:
            self.saml_acs_endpoint = m.get('SamlAcsEndpoint')

        if m.get('SamlEntityId') is not None:
            self.saml_entity_id = m.get('SamlEntityId')

        if m.get('SamlMetaEndpoint') is not None:
            self.saml_meta_endpoint = m.get('SamlMetaEndpoint')

        return self

class GetIdentityProviderResponseBodyIdentityProviderDetailDingtalkProvisioningConfig(DaraModel):
    def __init__(
        self,
        authed_department_ids: List[main_models.GetIdentityProviderResponseBodyIdentityProviderDetailDingtalkProvisioningConfigAuthedDepartmentIds] = None,
        authed_users: List[main_models.GetIdentityProviderResponseBodyIdentityProviderDetailDingtalkProvisioningConfigAuthedUsers] = None,
        corp_id: str = None,
        corp_name: str = None,
    ):
        # The authorized DingTalk departments.
        self.authed_department_ids = authed_department_ids
        # The list of authorized DingTalk accounts.
        self.authed_users = authed_users
        # The DingTalk enterprise CorpId.
        self.corp_id = corp_id
        # The DingTalk enterprise name.
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
        # The DingTalk username.
        self.name = name
        # The DingTalk user ID.
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
        # The DingTalk department ID.
        self.dept_id = dept_id
        # The DingTalk department name.
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
        # The AppKey of the DingTalk first-party application.
        self.app_key = app_key
        # The AppSecret of the DingTalk first-party application.
        self.app_secret = app_secret
        # The CorpId of the DingTalk first-party application.
        self.corp_id = corp_id
        # The DingTalk QR code logon version.
        self.dingtalk_login_version = dingtalk_login_version
        # The DingTalk version. Valid values:
        # 
        # - public_dingtalk: Standard DingTalk.
        # 
        # - private_dingtalk: Dedicated DingTalk.
        self.dingtalk_version = dingtalk_version
        # The EncryptKey of the DingTalk application.
        self.encrypt_key = encrypt_key
        # The VerificationToken of the DingTalk application.
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

