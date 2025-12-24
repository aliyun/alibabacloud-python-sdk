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
        session_manager_config: main_models.ModifyCloudAssistantSettingsRequestSessionManagerConfig = None,
        setting_type: str = None,
        sls_delivery_config: main_models.ModifyCloudAssistantSettingsRequestSlsDeliveryConfig = None,
    ):
        # The configurations for upgrading Cloud Assistant Agent.
        self.agent_upgrade_config = agent_upgrade_config
        # The configurations for delivering records to Object Storage Service (OSS).
        self.oss_delivery_config = oss_delivery_config
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Cloud Assistant Session Manager configuration.
        self.session_manager_config = session_manager_config
        # The Cloud Assistant feature. Set SettingType to one of the following valid values:
        # 
        # *   SessionManagerDelivery: the Session Record Delivery configurations.
        # *   InvocationDelivery: the Operation Content and Result Delivery configurations.
        # *   AgentUpgradeConfig: the Cloud Assistant Agent Upgrade configurations.
        # *   SessionManagerConfig: Cloud Assistant the SessionManager configuration.
        # 
        # This parameter is required.
        self.setting_type = setting_type
        # The configurations for delivering records to Simple Log Service.
        self.sls_delivery_config = sls_delivery_config

    def validate(self):
        if self.agent_upgrade_config:
            self.agent_upgrade_config.validate()
        if self.oss_delivery_config:
            self.oss_delivery_config.validate()
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
        # Specifies whether to deliver records to Simple Log Service. Default value: false.
        self.enabled = enabled
        # The name of the Logstore.
        self.logstore_name = logstore_name
        # The name of the Simple Log Service project.
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
        # Specify whether to enable Cloud Assistant Session Manager. Valid values:
        # 
        # *   true: Enables the feature.
        # *   false: Disables the feature.
        # 
        # Notes:
        # 
        # *   The feature applies to all regions.
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
        # Specifies whether to deliver records to OSS. Default value: false.
        self.enabled = enabled
        # The OSS encryption algorithm. Valid values:
        # 
        # *   AES256
        # *   SM4
        self.encryption_algorithm = encryption_algorithm
        # The ID of the customer master key (CMK) when EncryptionType is set to KMS.
        self.encryption_key_id = encryption_key_id
        # The OSS encryption method. Valid values:
        # 
        # *   Inherit: the encryption method used by the specified bucket.
        # *   OssManaged: server-side encryption by using OSS-managed keys (SSE-OSS).
        # *   KMS: server-side encryption by using Key Management Service managed keys (SSE-KMS).
        self.encryption_type = encryption_type
        # The prefix of the OSS bucket directory. The prefix must meet the following requirements:
        # 
        # *   The prefix can be up to 254 characters in length.
        # *   The prefix cannot start with a forward slash (/) or a backslash (\\\\).
        # 
        # Note: If you do not need a directory prefix, specify a pair of double quotation marks ("") for this parameter to clear the directory prefix that you specified.
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
        enabled: bool = None,
        time_zone: str = None,
    ):
        # The time windows during which Cloud Assistant Agent can be upgraded. The time windows can be accurate to minutes. The Coordinated Universal Time (UTC) time zone is used by default.
        # 
        # Make sure that the upgrade windows specified by this parameter are not shorter than 1 hour.
        # 
        # Specify each upgrade window in the following format: \\<Start time in the HH:mm format>-\\<End time in the HH:mm format>.
        # 
        # For example, [ "02:00-03:00", "05:00-06:00" ] specifies that Cloud Assistant Agent can be upgraded from 2:00:00 to 3:00:00 and from 5:00:00 to 6:00:00 every day in the UTC time zone.
        self.allowed_upgrade_window = allowed_upgrade_window
        # Specifies whether to enable custom upgrade for Cloud Assistant Agent. If you set this parameter to false, an upgrade attempt is performed for Cloud Assistant Agent every 30 minutes.
        # 
        # Default value: false.
        self.enabled = enabled
        # The time zone of the time windows. Default value: UTC. You can specify a time zone in the following forms:
        # 
        # *   The time zone name. Examples: Asia/Shanghai and America/Los_Angeles.
        # *   The time offset from GMT. Examples: GMT+8:00 (UTC+8) and GMT-7:00 (UTC-7). You cannot add leading zeros to the hour value.
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

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedUpgradeWindow') is not None:
            self.allowed_upgrade_window = m.get('AllowedUpgradeWindow')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        return self

