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
        # The configurations of upgrading the Cloud Assistant agent.
        self.agent_upgrade_config = agent_upgrade_config
        # The configurations of delivering records to OSS.
        self.oss_delivery_config = oss_delivery_config
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The configurations of resource usage for Cloud Assistant. This setting takes effect only when the version of the Cloud Assistant agent is not earlier than the following versions:
        # 
        # - Windows: 2.1.4.1065
        # 
        # - Linux: 2.2.4.1065
        self.resource_usage_config = resource_usage_config
        # The configurations of the Session Manager feature.
        self.session_manager_config = session_manager_config
        # The type of the service configurations. Valid values:
        # 
        # - `SessionManagerDelivery`: the configurations of delivering session records.
        # 
        # - `InvocationDelivery`: the configurations of delivering command execution records.
        # 
        # - `AgentUpgradeConfig`: the configurations of upgrading the Cloud Assistant agent.
        # 
        # - `SessionManagerConfig`: the configurations of Cloud Assistant Session Manager.
        # 
        # This parameter is required.
        self.setting_type = setting_type
        # The configurations of delivering records to SLS.
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
        # Specifies whether to enable the feature of delivering records to SLS.
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
        # The switch for the Session Manager feature. Valid values:
        # 
        # - true: enables the feature.
        # 
        # - false: disables the feature.
        # 
        # Note:
        # 
        # - After you enable or disable the Session Manager feature, the setting takes effect for all regions.
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
        # The maximum CPU usage that is allowed for the main process of the Cloud Assistant agent.
        # 
        # - Unit: %.
        # 
        # - Valid values: 10 to 95.
        # 
        # - Default value: 20.
        self.cpu_limit = cpu_limit
        # Specifies whether to retain the script file of a command in the Cloud Assistant directory after the command execution is complete.
        # Default value: false.
        self.keep_script_file = keep_script_file
        # The maximum number of Cloud Assistant log files that can be retained.
        # 
        # - Default value: 30.
        # 
        # - Minimum value: 7.
        # 
        # - Maximum value: 365.
        self.log_file_count_limit = log_file_count_limit
        # The maximum size of a single Cloud Assistant log file. You must specify a unit (B, KB, or MB).
        # 
        # - Default value: 100 MB.
        # 
        # - Minimum value: 10 MB.
        # 
        # - Maximum value: 1024 MB.
        self.log_size_limit = log_size_limit
        # The maximum memory usage that is allowed for the main process of the Cloud Assistant agent. You must specify a unit (B, KB, or MB).
        # 
        # - Default value: 50 MB.
        # 
        # - Minimum value: 35 MB.
        # 
        # - Maximum value: 1024 MB.
        self.memory_limit = memory_limit
        # The maximum number of consecutive times that CPU or memory usage can exceed the specified limits. If the limits are consecutively exceeded for the specified number of times, the Cloud Assistant agent is automatically stopped.
        # 
        # - Default value: 3.
        # 
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
        # Specifies whether to enable the feature of delivering records to OSS. Default value: false.
        self.enabled = enabled
        # The OSS encryption algorithm. Valid values:
        # 
        # - AES256
        # 
        # - SM4
        self.encryption_algorithm = encryption_algorithm
        # The ID of the customer master key (CMK) when KMS encryption is used.
        self.encryption_key_id = encryption_key_id
        # The OSS encryption mode. Valid values:
        # 
        # - Inherit: inherits the bucket encryption.
        # 
        # - OssManaged: uses OSS-managed server-side encryption.
        # 
        # - KMS: uses KMS encryption.
        self.encryption_type = encryption_type
        # The prefix of the directory in the OSS bucket. The following limits apply:
        # 
        # - The prefix can be up to 254 characters in length.
        # 
        # - The prefix cannot start with a forward slash (/) or a backslash ().
        # 
        # Note: If you want to deliver records to the root directory of the bucket, enter "". To clear the prefix that is previously set, enter "".
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
        # A list of time windows during which the agent is allowed to be upgraded. The time windows are accurate to minutes and are in UTC by default.
        # 
        # The interval between two consecutive time windows must be at least 1 hour.
        # 
        # Format: StartTime(HH:mm)-EndTime(HH:mm).
        # 
        # For example, [
        # "02:00-03:00",
        # "05:00-06:00"
        # ]
        # indicates that the agent can be upgraded from 2:00 to 3:00 and from 5:00 to 6:00 every day in UTC.
        self.allowed_upgrade_window = allowed_upgrade_window
        # Specifies whether to immediately check the version and perform an update when the Cloud Assistant agent is started. Default value: true.
        # 
        # This setting takes effect only when the version of the Cloud Assistant agent is not earlier than the following versions:
        # 
        # - Windows: 2.1.4.1065
        # 
        # - Linux: 2.2.4.1065
        self.bootstrap_upgrade = bootstrap_upgrade
        # Specifies whether to disallow the Cloud Assistant agent to check for or perform updates. Default value: false.
        # 
        # This setting takes effect only when the version of the Cloud Assistant agent is not earlier than the following versions:
        # 
        # - Windows: 2.1.4.1065
        # 
        # - Linux: 2.2.4.1065
        self.disable_upgrade = disable_upgrade
        # Specifies whether to enable custom upgrade configurations for the agent. If you set this parameter to false, the agent attempts to upgrade every 30 minutes by default.
        # 
        # Default value: false.
        self.enabled = enabled
        # The time zone of the time windows for agent upgrade. Default value: UTC.
        # The following formats are supported for the time zone:
        # 
        # - Time zone name: for example, Asia/Shanghai (China/Shanghai time) and America/Los_Angeles (US/Los Angeles time).
        # 
        # - Offset from Greenwich Mean Time (GMT): for example, GMT+8:00 (UTC+8) and GMT-7:00 (UTC-7). The hour part cannot have a leading zero.
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

