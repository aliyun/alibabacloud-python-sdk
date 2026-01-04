# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListIdentityProvidersResponseBody(DaraModel):
    def __init__(
        self,
        identity_providers: List[main_models.ListIdentityProvidersResponseBodyIdentityProviders] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Identity provider information array.
        self.identity_providers = identity_providers
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.identity_providers:
            for v1 in self.identity_providers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IdentityProviders'] = []
        if self.identity_providers is not None:
            for k1 in self.identity_providers:
                result['IdentityProviders'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.identity_providers = []
        if m.get('IdentityProviders') is not None:
            for k1 in m.get('IdentityProviders'):
                temp_model = main_models.ListIdentityProvidersResponseBodyIdentityProviders()
                self.identity_providers.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListIdentityProvidersResponseBodyIdentityProviders(DaraModel):
    def __init__(
        self,
        advanced_status: str = None,
        authn_source_supplier: str = None,
        authn_source_type: str = None,
        authn_status: str = None,
        create_time: int = None,
        description: str = None,
        identity_provider_external_id: str = None,
        identity_provider_id: str = None,
        identity_provider_name: str = None,
        identity_provider_type: str = None,
        incremental_callback_status: str = None,
        instance_id: str = None,
        last_status_check_job_result: str = None,
        lock_reason: str = None,
        logo_url: str = None,
        periodic_sync_status: str = None,
        ud_pull_status: str = None,
        ud_pull_target_scope: str = None,
        ud_push_status: str = None,
        update_time: int = None,
    ):
        # Advanced configuration capabilities
        self.advanced_status = advanced_status
        # Authentication source product.
        # - urn:alibaba:idaas:idp:okta:okta
        # - urn:alibaba:idaas:idp:google:account
        # - urn:alibaba:idaas:idp:microsoft:aad
        # - urn:alibaba:idaas:idp:microsoft:ad
        # - urn:alibaba:idaas:idp:bytedance:lark
        # - urn:alibaba:idaas:idp:unknown:ldap
        # - urn:alibaba:idaas:idp:alibaba:idaas
        # - urn:alibaba:idaas:idp:tencent:wecom
        # - urn:alibaba:idaas:idp:alibaba:aliyunram
        self.authn_source_supplier = authn_source_supplier
        # Authentication method type.
        # - urn:alibaba:idaas:authntype:oidc
        # - urn:alibaba:idaas:authntype:saml2
        self.authn_source_type = authn_source_type
        # Does the corresponding IdP support authentication.
        self.authn_status = authn_status
        # The time when the instance was created.
        self.create_time = create_time
        # The description of the Identity provider.
        self.description = description
        # Identity provider external ID.
        self.identity_provider_external_id = identity_provider_external_id
        # Identity provider ID.
        self.identity_provider_id = identity_provider_id
        # Identity provider name.
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
        self.identity_provider_type = identity_provider_type
        # Incremental callback status, whether to process the incremental callback data from IdP.
        self.incremental_callback_status = incremental_callback_status
        # The instance ID.
        self.instance_id = instance_id
        # Last status check result.
        self.last_status_check_job_result = last_status_check_job_result
        # The reason why write operations are locked.
        self.lock_reason = lock_reason
        # IdP logo url.
        self.logo_url = logo_url
        # Regular verification status.
        self.periodic_sync_status = periodic_sync_status
        # Whether support UD synchronization.Values:
        # - enabled
        # - disabled
        self.ud_pull_status = ud_pull_status
        # When supporting the range in the UD of ud_pullIDaaS side.
        self.ud_pull_target_scope = ud_pull_target_scope
        # Synchronize capabilities
        self.ud_push_status = ud_push_status
        # The time when the service was updated.
        self.update_time = update_time

    def validate(self):
        pass

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

        if self.identity_provider_external_id is not None:
            result['IdentityProviderExternalId'] = self.identity_provider_external_id

        if self.identity_provider_id is not None:
            result['IdentityProviderId'] = self.identity_provider_id

        if self.identity_provider_name is not None:
            result['IdentityProviderName'] = self.identity_provider_name

        if self.identity_provider_type is not None:
            result['IdentityProviderType'] = self.identity_provider_type

        if self.incremental_callback_status is not None:
            result['IncrementalCallbackStatus'] = self.incremental_callback_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.last_status_check_job_result is not None:
            result['LastStatusCheckJobResult'] = self.last_status_check_job_result

        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.logo_url is not None:
            result['LogoUrl'] = self.logo_url

        if self.periodic_sync_status is not None:
            result['PeriodicSyncStatus'] = self.periodic_sync_status

        if self.ud_pull_status is not None:
            result['UdPullStatus'] = self.ud_pull_status

        if self.ud_pull_target_scope is not None:
            result['UdPullTargetScope'] = self.ud_pull_target_scope

        if self.ud_push_status is not None:
            result['UdPushStatus'] = self.ud_push_status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

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

        if m.get('IdentityProviderExternalId') is not None:
            self.identity_provider_external_id = m.get('IdentityProviderExternalId')

        if m.get('IdentityProviderId') is not None:
            self.identity_provider_id = m.get('IdentityProviderId')

        if m.get('IdentityProviderName') is not None:
            self.identity_provider_name = m.get('IdentityProviderName')

        if m.get('IdentityProviderType') is not None:
            self.identity_provider_type = m.get('IdentityProviderType')

        if m.get('IncrementalCallbackStatus') is not None:
            self.incremental_callback_status = m.get('IncrementalCallbackStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LastStatusCheckJobResult') is not None:
            self.last_status_check_job_result = m.get('LastStatusCheckJobResult')

        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('LogoUrl') is not None:
            self.logo_url = m.get('LogoUrl')

        if m.get('PeriodicSyncStatus') is not None:
            self.periodic_sync_status = m.get('PeriodicSyncStatus')

        if m.get('UdPullStatus') is not None:
            self.ud_pull_status = m.get('UdPullStatus')

        if m.get('UdPullTargetScope') is not None:
            self.ud_pull_target_scope = m.get('UdPullTargetScope')

        if m.get('UdPushStatus') is not None:
            self.ud_push_status = m.get('UdPushStatus')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

