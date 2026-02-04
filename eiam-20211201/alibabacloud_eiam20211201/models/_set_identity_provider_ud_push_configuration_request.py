# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class SetIdentityProviderUdPushConfigurationRequest(DaraModel):
    def __init__(
        self,
        identity_provider_id: str = None,
        incremental_callback_status: str = None,
        instance_id: str = None,
        ldap_ud_push_config: main_models.SetIdentityProviderUdPushConfigurationRequestLdapUdPushConfig = None,
        periodic_sync_config: main_models.SetIdentityProviderUdPushConfigurationRequestPeriodicSyncConfig = None,
        periodic_sync_status: str = None,
        ud_sync_scope_configs: List[main_models.SetIdentityProviderUdPushConfigurationRequestUdSyncScopeConfigs] = None,
    ):
        # IDaaS的身份提供方主键id
        # 
        # This parameter is required.
        self.identity_provider_id = identity_provider_id
        # 增量回调状态，是否处理来自IdP的增量回调数据
        # 
        # This parameter is required.
        self.incremental_callback_status = incremental_callback_status
        # IDaaS EIAM的实例id
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.ldap_ud_push_config = ldap_ud_push_config
        self.periodic_sync_config = periodic_sync_config
        self.periodic_sync_status = periodic_sync_status
        # 同步出配置信息
        self.ud_sync_scope_configs = ud_sync_scope_configs

    def validate(self):
        if self.ldap_ud_push_config:
            self.ldap_ud_push_config.validate()
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
        if self.identity_provider_id is not None:
            result['IdentityProviderId'] = self.identity_provider_id

        if self.incremental_callback_status is not None:
            result['IncrementalCallbackStatus'] = self.incremental_callback_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ldap_ud_push_config is not None:
            result['LdapUdPushConfig'] = self.ldap_ud_push_config.to_map()

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
        if m.get('IdentityProviderId') is not None:
            self.identity_provider_id = m.get('IdentityProviderId')

        if m.get('IncrementalCallbackStatus') is not None:
            self.incremental_callback_status = m.get('IncrementalCallbackStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LdapUdPushConfig') is not None:
            temp_model = main_models.SetIdentityProviderUdPushConfigurationRequestLdapUdPushConfig()
            self.ldap_ud_push_config = temp_model.from_map(m.get('LdapUdPushConfig'))

        if m.get('PeriodicSyncConfig') is not None:
            temp_model = main_models.SetIdentityProviderUdPushConfigurationRequestPeriodicSyncConfig()
            self.periodic_sync_config = temp_model.from_map(m.get('PeriodicSyncConfig'))

        if m.get('PeriodicSyncStatus') is not None:
            self.periodic_sync_status = m.get('PeriodicSyncStatus')

        self.ud_sync_scope_configs = []
        if m.get('UdSyncScopeConfigs') is not None:
            for k1 in m.get('UdSyncScopeConfigs'):
                temp_model = main_models.SetIdentityProviderUdPushConfigurationRequestUdSyncScopeConfigs()
                self.ud_sync_scope_configs.append(temp_model.from_map(k1))

        return self

class SetIdentityProviderUdPushConfigurationRequestUdSyncScopeConfigs(DaraModel):
    def __init__(
        self,
        source_scopes: List[str] = None,
        target_scope: str = None,
    ):
        # 同步来源节点
        self.source_scopes = source_scopes
        # 同步目标节点
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

class SetIdentityProviderUdPushConfigurationRequestPeriodicSyncConfig(DaraModel):
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

class SetIdentityProviderUdPushConfigurationRequestLdapUdPushConfig(DaraModel):
    def __init__(
        self,
        organization_unit_object_class: str = None,
        organizational_unit_rdn: str = None,
        password_sync_status: str = None,
        user_object_class: str = None,
        user_rdn: str = None,
    ):
        self.organization_unit_object_class = organization_unit_object_class
        self.organizational_unit_rdn = organizational_unit_rdn
        self.password_sync_status = password_sync_status
        self.user_object_class = user_object_class
        self.user_rdn = user_rdn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.organization_unit_object_class is not None:
            result['OrganizationUnitObjectClass'] = self.organization_unit_object_class

        if self.organizational_unit_rdn is not None:
            result['OrganizationalUnitRdn'] = self.organizational_unit_rdn

        if self.password_sync_status is not None:
            result['PasswordSyncStatus'] = self.password_sync_status

        if self.user_object_class is not None:
            result['UserObjectClass'] = self.user_object_class

        if self.user_rdn is not None:
            result['UserRdn'] = self.user_rdn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationUnitObjectClass') is not None:
            self.organization_unit_object_class = m.get('OrganizationUnitObjectClass')

        if m.get('OrganizationalUnitRdn') is not None:
            self.organizational_unit_rdn = m.get('OrganizationalUnitRdn')

        if m.get('PasswordSyncStatus') is not None:
            self.password_sync_status = m.get('PasswordSyncStatus')

        if m.get('UserObjectClass') is not None:
            self.user_object_class = m.get('UserObjectClass')

        if m.get('UserRdn') is not None:
            self.user_rdn = m.get('UserRdn')

        return self

