# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class ModifyCloudAssistantSettingsRequest(DaraModel):
    def __init__(
        self,
        agent_upgrade_config: main_models.ModifyCloudAssistantSettingsRequestAgentUpgradeConfig = None,
        oss_delivery_config: main_models.ModifyCloudAssistantSettingsRequestOssDeliveryConfig = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_usage_config: main_models.ModifyCloudAssistantSettingsRequestResourceUsageConfig = None,
        session_manager_config: main_models.ModifyCloudAssistantSettingsRequestSessionManagerConfig = None,
        setting_type: str = None,
        sls_delivery_config: main_models.ModifyCloudAssistantSettingsRequestSlsDeliveryConfig = None,
    ):
        # The Cloud Assistant Agent upgrade configuration.
        self.agent_upgrade_config = agent_upgrade_config
        # The OSS delivery configuration.
        self.oss_delivery_config = oss_delivery_config
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The Cloud Assistant resource usage configuration. This parameter takes effect only when the Cloud Assistant Agent version meets the following minimum requirements:
        # 
        # - Windows: 2.1.4.1065
        # 
        # - Linux: 2.2.4.1065
        self.resource_usage_config = resource_usage_config
        # The Cloud Assistant session feature configuration.
        self.session_manager_config = session_manager_config
        # The service configuration type. Valid values:
        # - SessionManagerDelivery: session operation log delivery.
        # - InvocationDelivery: task execution log delivery.
        # - AgentUpgradeConfig: Cloud Assistant Agent upgrade configuration.
        # - SessionManagerConfig: Cloud Assistant SessionManager configuration.
        # 
        # This parameter is required.
        self.setting_type = setting_type
        # The Simple Log Service (SLS) delivery configuration.
        self.sls_delivery_config = sls_delivery_config

    def validate(self):
        if self.agent_upgrade_config:
            self.agent_upgrade_config.validate()
        if self.oss_delivery_config:
            self.oss_delivery_config.validate()
        if self.resource_usage_config:
            self.resource_usage_config.validate()
        if self.session_manager_config:
            self.session_manager_config.validate()
        if self.sls_delivery_config:
            self.sls_delivery_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_upgrade_config is not None:
            result['AgentUpgradeConfig'] = self.agent_upgrade_config.to_map()

        if self.oss_delivery_config is not None:
            result['OssDeliveryConfig'] = self.oss_delivery_config.to_map()

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_usage_config is not None:
            result['ResourceUsageConfig'] = self.resource_usage_config.to_map()

        if self.session_manager_config is not None:
            result['SessionManagerConfig'] = self.session_manager_config.to_map()

        if self.setting_type is not None:
            result['SettingType'] = self.setting_type

        if self.sls_delivery_config is not None:
            result['SlsDeliveryConfig'] = self.sls_delivery_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentUpgradeConfig') is not None:
            temp_model = main_models.ModifyCloudAssistantSettingsRequestAgentUpgradeConfig()
            self.agent_upgrade_config = temp_model.from_map(m.get('AgentUpgradeConfig'))

        if m.get('OssDeliveryConfig') is not None:
            temp_model = main_models.ModifyCloudAssistantSettingsRequestOssDeliveryConfig()
            self.oss_delivery_config = temp_model.from_map(m.get('OssDeliveryConfig'))

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceUsageConfig') is not None:
            temp_model = main_models.ModifyCloudAssistantSettingsRequestResourceUsageConfig()
            self.resource_usage_config = temp_model.from_map(m.get('ResourceUsageConfig'))

        if m.get('SessionManagerConfig') is not None:
            temp_model = main_models.ModifyCloudAssistantSettingsRequestSessionManagerConfig()
            self.session_manager_config = temp_model.from_map(m.get('SessionManagerConfig'))

        if m.get('SettingType') is not None:
            self.setting_type = m.get('SettingType')

        if m.get('SlsDeliveryConfig') is not None:
            temp_model = main_models.ModifyCloudAssistantSettingsRequestSlsDeliveryConfig()
            self.sls_delivery_config = temp_model.from_map(m.get('SlsDeliveryConfig'))

        return self

class ModifyCloudAssistantSettingsRequestSlsDeliveryConfig(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        logstore_name: str = None,
        project_name: str = None,
    ):
        # Specifies whether to enable delivery to SLS.
        # Default value: false.
        self.enabled = enabled
        # The name of the SLS Logstore.
        self.logstore_name = logstore_name
        # The name of the SLS project.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.logstore_name is not None:
            result['LogstoreName'] = self.logstore_name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('LogstoreName') is not None:
            self.logstore_name = m.get('LogstoreName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

class ModifyCloudAssistantSettingsRequestSessionManagerConfig(DaraModel):
    def __init__(
        self,
        session_manager_enabled: bool = None,
    ):
        # Specifies whether to enable the Cloud Assistant session feature. Valid values:
        # * true: Enabled.
        # * false: Disabled.
        # 
        # Note:
        # * Enabling or disabling the session feature takes effect across all regions.
        self.session_manager_enabled = session_manager_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.session_manager_enabled is not None:
            result['SessionManagerEnabled'] = self.session_manager_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionManagerEnabled') is not None:
            self.session_manager_enabled = m.get('SessionManagerEnabled')

        return self

class ModifyCloudAssistantSettingsRequestResourceUsageConfig(DaraModel):
    def __init__(
        self,
        cpu_limit: int = None,
        keep_script_file: bool = None,
        log_file_count_limit: int = None,
        log_size_limit: str = None,
        memory_limit: str = None,
        overload_limit: int = None,
    ):
        # The maximum CPU usage allowed for the Cloud Assistant Agent main process.
        # 
        # - Unit: percentage.
        # 
        # - Valid values: 10 to 95.
        # 
        # - Default value: 20.
        self.cpu_limit = cpu_limit
        # Specifies whether to retain the script file in the Cloud Assistant directory after command execution is complete.
        # Default value: false.
        self.keep_script_file = keep_script_file
        # The maximum number of Cloud Assistant log files to retain.
        # - Default value: 30.
        # - Minimum value: 7.
        # - Maximum value: 365.
        self.log_file_count_limit = log_file_count_limit
        # The maximum size of a single Cloud Assistant log file. You must specify the unit (B|KB|MB).
        # - Default value: 100MB.
        # - Minimum value: 10MB.
        # - Maximum value: 1024MB.
        self.log_size_limit = log_size_limit
        # The maximum memory usage allowed for the Cloud Assistant Agent main process. You must specify the unit (B|KB|MB).
        # - Default value: 50MB.
        # - Minimum value: 35MB.
        # - Maximum value: 1024MB.
        self.memory_limit = memory_limit
        # The maximum number of consecutive times that CPU or memory resources usage can exceed the limit before the Cloud Assistant Agent automatically stops running.
        # - Default value: 3.
        # - Minimum value: 3.
        self.overload_limit = overload_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_limit is not None:
            result['CpuLimit'] = self.cpu_limit

        if self.keep_script_file is not None:
            result['KeepScriptFile'] = self.keep_script_file

        if self.log_file_count_limit is not None:
            result['LogFileCountLimit'] = self.log_file_count_limit

        if self.log_size_limit is not None:
            result['LogSizeLimit'] = self.log_size_limit

        if self.memory_limit is not None:
            result['MemoryLimit'] = self.memory_limit

        if self.overload_limit is not None:
            result['OverloadLimit'] = self.overload_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuLimit') is not None:
            self.cpu_limit = m.get('CpuLimit')

        if m.get('KeepScriptFile') is not None:
            self.keep_script_file = m.get('KeepScriptFile')

        if m.get('LogFileCountLimit') is not None:
            self.log_file_count_limit = m.get('LogFileCountLimit')

        if m.get('LogSizeLimit') is not None:
            self.log_size_limit = m.get('LogSizeLimit')

        if m.get('MemoryLimit') is not None:
            self.memory_limit = m.get('MemoryLimit')

        if m.get('OverloadLimit') is not None:
            self.overload_limit = m.get('OverloadLimit')

        return self

class ModifyCloudAssistantSettingsRequestOssDeliveryConfig(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        enabled: bool = None,
        encryption_algorithm: str = None,
        encryption_key_id: str = None,
        encryption_type: str = None,
        prefix: str = None,
    ):
        # The name of the OSS bucket.
        self.bucket_name = bucket_name
        # Specifies whether to enable delivery to OSS. Default value: false.
        self.enabled = enabled
        # The OSS encryption algorithm. Valid values:
        # - AES256
        # - SM4
        self.encryption_algorithm = encryption_algorithm
        # The ID of the customer master key (CMK) when the encryption method is set to KMS.
        self.encryption_key_id = encryption_key_id
        # The OSS encryption method. Valid values:
        # - Inherit: inherits the encryption method of the bucket.
        # - OssManaged: OSS-managed encryption.
        # - KMS: Key Management Service (KMS) encryption.
        self.encryption_type = encryption_type
        # The directory prefix of the OSS bucket. The following limits apply:
        # - The prefix cannot exceed 254 characters in length.
        # - The prefix cannot start with a forward slash (/) or a backslash (\\).
        # 
        # > Note: Set this parameter to an empty string ("") if no directory prefix is required. If a prefix was previously configured and is no longer needed, set this parameter to an empty string ("") to clear it.
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.encryption_algorithm is not None:
            result['EncryptionAlgorithm'] = self.encryption_algorithm

        if self.encryption_key_id is not None:
            result['EncryptionKeyId'] = self.encryption_key_id

        if self.encryption_type is not None:
            result['EncryptionType'] = self.encryption_type

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('EncryptionAlgorithm') is not None:
            self.encryption_algorithm = m.get('EncryptionAlgorithm')

        if m.get('EncryptionKeyId') is not None:
            self.encryption_key_id = m.get('EncryptionKeyId')

        if m.get('EncryptionType') is not None:
            self.encryption_type = m.get('EncryptionType')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        return self

class ModifyCloudAssistantSettingsRequestAgentUpgradeConfig(DaraModel):
    def __init__(
        self,
        allowed_upgrade_window: List[str] = None,
        bootstrap_upgrade: bool = None,
        disable_upgrade: bool = None,
        enabled: bool = None,
        time_zone: str = None,
    ):
        # The list of time windows during which upgrades are allowed. The time can be specified down to the minute. The default time zone is UTC.
        # 
        # The interval between time windows cannot be less than 1 hour.
        # 
        # Format: Start time (HH:mm)-End time (HH:mm).
        # 
        # Example: [
        # "02:00-03:00",
        # "05:00-06:00"
        # ]
        # This indicates that upgrades are allowed daily from 02:00 to 03:00 and from 05:00 to 06:00 in the UTC time zone.
        self.allowed_upgrade_window = allowed_upgrade_window
        # Specifies whether the Cloud Assistant Agent checks for updates and performs an upgrade immediately upon startup. Default value: true.
        # 
        # This parameter takes effect only when the Cloud Assistant Agent version meets the following minimum requirements:
        # 
        # - Windows: 2.1.4.1065
        # 
        # - Linux: 2.2.4.1065
        self.bootstrap_upgrade = bootstrap_upgrade
        # Specifies whether to prevent the Cloud Assistant Agent from checking for and performing updates. Default value: false.
        # 
        # This parameter takes effect only when the Cloud Assistant Agent version meets the following minimum requirements:
        # 
        # - Windows: 2.1.4.1065
        # 
        # - Linux: 2.2.4.1065
        self.disable_upgrade = disable_upgrade
        # Specifies whether to enable the custom Agent upgrade configuration. If this parameter is set to false, the system attempts to upgrade the Agent every 30 minutes by default.
        # 
        # Default value: false.
        self.enabled = enabled
        # The time zone for the allowed upgrade time windows. Default value: UTC.
        # The time zone can be specified in the following formats:
        # - Full time zone name, such as Asia/Shanghai or America/Los_Angeles.
        # - GMT offset from Greenwich Mean Time, such as GMT+8:00 or GMT-7:00. Leading zeros are not supported for the hour value.
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_upgrade_window is not None:
            result['AllowedUpgradeWindow'] = self.allowed_upgrade_window

        if self.bootstrap_upgrade is not None:
            result['BootstrapUpgrade'] = self.bootstrap_upgrade

        if self.disable_upgrade is not None:
            result['DisableUpgrade'] = self.disable_upgrade

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedUpgradeWindow') is not None:
            self.allowed_upgrade_window = m.get('AllowedUpgradeWindow')

        if m.get('BootstrapUpgrade') is not None:
            self.bootstrap_upgrade = m.get('BootstrapUpgrade')

        if m.get('DisableUpgrade') is not None:
            self.disable_upgrade = m.get('DisableUpgrade')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        return self

