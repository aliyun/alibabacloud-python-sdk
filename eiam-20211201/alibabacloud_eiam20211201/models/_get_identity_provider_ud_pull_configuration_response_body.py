# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetIdentityProviderUdPullConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        ud_pull_configuration: main_models.GetIdentityProviderUdPullConfigurationResponseBodyUdPullConfiguration = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Inbound Synchronization Configuration Information
        self.ud_pull_configuration = ud_pull_configuration

    def validate(self):
        if self.ud_pull_configuration:
            self.ud_pull_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.ud_pull_configuration is not None:
            result['UdPullConfiguration'] = self.ud_pull_configuration.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UdPullConfiguration') is not None:
            temp_model = main_models.GetIdentityProviderUdPullConfigurationResponseBodyUdPullConfiguration()
            self.ud_pull_configuration = temp_model.from_map(m.get('UdPullConfiguration'))

        return self

class GetIdentityProviderUdPullConfigurationResponseBodyUdPullConfiguration(DaraModel):
    def __init__(
        self,
        group_sync_status: str = None,
        identity_provider_id: str = None,
        incremental_callback_status: str = None,
        instance_id: str = None,
        ldap_ud_pull_config: main_models.GetIdentityProviderUdPullConfigurationResponseBodyUdPullConfigurationLdapUdPullConfig = None,
        periodic_sync_config: main_models.GetIdentityProviderUdPullConfigurationResponseBodyUdPullConfigurationPeriodicSyncConfig = None,
        periodic_sync_status: str = None,
        pull_protected_rule: main_models.GetIdentityProviderUdPullConfigurationResponseBodyUdPullConfigurationPullProtectedRule = None,
        ud_sync_scope_config: main_models.GetIdentityProviderUdPullConfigurationResponseBodyUdPullConfigurationUdSyncScopeConfig = None,
    ):
        # Group Synchronization Status
        # Possible values:
        # 
        # Disabled: disabled
        # 
        # Enabled: enabled
        self.group_sync_status = group_sync_status
        # Identity provider ID
        self.identity_provider_id = identity_provider_id
        # Incremental Callback Status: Whether to process incremental callback data from the IdP
        self.incremental_callback_status = incremental_callback_status
        # The ID of the instance.
        self.instance_id = instance_id
        # LDAP Synchronization Side Related Configuration Information
        self.ldap_ud_pull_config = ldap_ud_pull_config
        # Scheduled sync configuration
        self.periodic_sync_config = periodic_sync_config
        # Scheduled Validation Status: Whether to periodically validate data discrepancies between IDaaS and the Identity Provider. Possible values:
        # 
        # Disabled: disabled
        # 
        # Enabled: enabled
        self.periodic_sync_status = periodic_sync_status
        # Inbound Synchronization Protection Rule Configuration
        self.pull_protected_rule = pull_protected_rule
        # Synchronization Scope Configuration Information
        self.ud_sync_scope_config = ud_sync_scope_config

    def validate(self):
        if self.ldap_ud_pull_config:
            self.ldap_ud_pull_config.validate()
        if self.periodic_sync_config:
            self.periodic_sync_config.validate()
        if self.pull_protected_rule:
            self.pull_protected_rule.validate()
        if self.ud_sync_scope_config:
            self.ud_sync_scope_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_sync_status is not None:
            result['GroupSyncStatus'] = self.group_sync_status

        if self.identity_provider_id is not None:
            result['IdentityProviderId'] = self.identity_provider_id

        if self.incremental_callback_status is not None:
            result['IncrementalCallbackStatus'] = self.incremental_callback_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ldap_ud_pull_config is not None:
            result['LdapUdPullConfig'] = self.ldap_ud_pull_config.to_map()

        if self.periodic_sync_config is not None:
            result['PeriodicSyncConfig'] = self.periodic_sync_config.to_map()

        if self.periodic_sync_status is not None:
            result['PeriodicSyncStatus'] = self.periodic_sync_status

        if self.pull_protected_rule is not None:
            result['PullProtectedRule'] = self.pull_protected_rule.to_map()

        if self.ud_sync_scope_config is not None:
            result['UdSyncScopeConfig'] = self.ud_sync_scope_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupSyncStatus') is not None:
            self.group_sync_status = m.get('GroupSyncStatus')

        if m.get('IdentityProviderId') is not None:
            self.identity_provider_id = m.get('IdentityProviderId')

        if m.get('IncrementalCallbackStatus') is not None:
            self.incremental_callback_status = m.get('IncrementalCallbackStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LdapUdPullConfig') is not None:
            temp_model = main_models.GetIdentityProviderUdPullConfigurationResponseBodyUdPullConfigurationLdapUdPullConfig()
            self.ldap_ud_pull_config = temp_model.from_map(m.get('LdapUdPullConfig'))

        if m.get('PeriodicSyncConfig') is not None:
            temp_model = main_models.GetIdentityProviderUdPullConfigurationResponseBodyUdPullConfigurationPeriodicSyncConfig()
            self.periodic_sync_config = temp_model.from_map(m.get('PeriodicSyncConfig'))

        if m.get('PeriodicSyncStatus') is not None:
            self.periodic_sync_status = m.get('PeriodicSyncStatus')

        if m.get('PullProtectedRule') is not None:
            temp_model = main_models.GetIdentityProviderUdPullConfigurationResponseBodyUdPullConfigurationPullProtectedRule()
            self.pull_protected_rule = temp_model.from_map(m.get('PullProtectedRule'))

        if m.get('UdSyncScopeConfig') is not None:
            temp_model = main_models.GetIdentityProviderUdPullConfigurationResponseBodyUdPullConfigurationUdSyncScopeConfig()
            self.ud_sync_scope_config = temp_model.from_map(m.get('UdSyncScopeConfig'))

        return self

class GetIdentityProviderUdPullConfigurationResponseBodyUdPullConfigurationUdSyncScopeConfig(DaraModel):
    def __init__(
        self,
        source_scopes: List[str] = None,
        target_scope: str = None,
    ):
        # Synchronization Source Node
        self.source_scopes = source_scopes
        # Synchronization Target Node
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

class GetIdentityProviderUdPullConfigurationResponseBodyUdPullConfigurationPullProtectedRule(DaraModel):
    def __init__(
        self,
        group_deleted_threshold: int = None,
        organizational_unit_deleted_threshold: int = None,
        user_deleted_threshold: int = None,
    ):
        # Group Deletion Threshold: If the number of deleted groups exceeds this value, the synchronization task will be terminated.
        self.group_deleted_threshold = group_deleted_threshold
        # Organization Deletion Threshold: If the number of deleted organizations exceeds this value, the synchronization task will be terminated.
        self.organizational_unit_deleted_threshold = organizational_unit_deleted_threshold
        # Account Deletion Threshold: If the number of deleted users exceeds this value, the synchronization task will be terminated.
        self.user_deleted_threshold = user_deleted_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_deleted_threshold is not None:
            result['GroupDeletedThreshold'] = self.group_deleted_threshold

        if self.organizational_unit_deleted_threshold is not None:
            result['OrganizationalUnitDeletedThreshold'] = self.organizational_unit_deleted_threshold

        if self.user_deleted_threshold is not None:
            result['UserDeletedThreshold'] = self.user_deleted_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupDeletedThreshold') is not None:
            self.group_deleted_threshold = m.get('GroupDeletedThreshold')

        if m.get('OrganizationalUnitDeletedThreshold') is not None:
            self.organizational_unit_deleted_threshold = m.get('OrganizationalUnitDeletedThreshold')

        if m.get('UserDeletedThreshold') is not None:
            self.user_deleted_threshold = m.get('UserDeletedThreshold')

        return self

class GetIdentityProviderUdPullConfigurationResponseBodyUdPullConfigurationPeriodicSyncConfig(DaraModel):
    def __init__(
        self,
        periodic_sync_cron: str = None,
        periodic_sync_times: int = None,
        periodic_sync_type: str = None,
    ):
        # Cron expression
        self.periodic_sync_cron = periodic_sync_cron
        # Execution time slots, for example 3,5, meaning the task runs once between 03:00–04:00 and once between 05:00–06:00.
        self.periodic_sync_times = periodic_sync_times
        # type
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

class GetIdentityProviderUdPullConfigurationResponseBodyUdPullConfigurationLdapUdPullConfig(DaraModel):
    def __init__(
        self,
        group_member_attribute_name: str = None,
        group_object_class: str = None,
        group_object_class_custom_filter: str = None,
        organization_unit_object_class: str = None,
        user_object_class: str = None,
        user_object_class_custom_filter: str = None,
    ):
        # Group Member Identifier
        self.group_member_attribute_name = group_member_attribute_name
        # Group ObjectClass
        self.group_object_class = group_object_class
        # Group Custom Filter
        self.group_object_class_custom_filter = group_object_class_custom_filter
        # Organization ObjectClass
        self.organization_unit_object_class = organization_unit_object_class
        # User ObjectClass
        self.user_object_class = user_object_class
        # User ObjectClass Custom Filter
        self.user_object_class_custom_filter = user_object_class_custom_filter

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_member_attribute_name is not None:
            result['GroupMemberAttributeName'] = self.group_member_attribute_name

        if self.group_object_class is not None:
            result['GroupObjectClass'] = self.group_object_class

        if self.group_object_class_custom_filter is not None:
            result['GroupObjectClassCustomFilter'] = self.group_object_class_custom_filter

        if self.organization_unit_object_class is not None:
            result['OrganizationUnitObjectClass'] = self.organization_unit_object_class

        if self.user_object_class is not None:
            result['UserObjectClass'] = self.user_object_class

        if self.user_object_class_custom_filter is not None:
            result['UserObjectClassCustomFilter'] = self.user_object_class_custom_filter

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupMemberAttributeName') is not None:
            self.group_member_attribute_name = m.get('GroupMemberAttributeName')

        if m.get('GroupObjectClass') is not None:
            self.group_object_class = m.get('GroupObjectClass')

        if m.get('GroupObjectClassCustomFilter') is not None:
            self.group_object_class_custom_filter = m.get('GroupObjectClassCustomFilter')

        if m.get('OrganizationUnitObjectClass') is not None:
            self.organization_unit_object_class = m.get('OrganizationUnitObjectClass')

        if m.get('UserObjectClass') is not None:
            self.user_object_class = m.get('UserObjectClass')

        if m.get('UserObjectClassCustomFilter') is not None:
            self.user_object_class_custom_filter = m.get('UserObjectClassCustomFilter')

        return self

