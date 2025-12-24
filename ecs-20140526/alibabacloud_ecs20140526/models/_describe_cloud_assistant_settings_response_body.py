# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudAssistantSettingsResponseBody(DaraModel):
    def __init__(
        self,
        agent_upgrade_config: main_models.DescribeCloudAssistantSettingsResponseBodyAgentUpgradeConfig = None,
        oss_delivery_configs: main_models.DescribeCloudAssistantSettingsResponseBodyOssDeliveryConfigs = None,
        request_id: str = None,
        session_manager_config: main_models.DescribeCloudAssistantSettingsResponseBodySessionManagerConfig = None,
        sls_delivery_configs: main_models.DescribeCloudAssistantSettingsResponseBodySlsDeliveryConfigs = None,
    ):
        # The configurations for upgrading Cloud Assistant Agent.
        self.agent_upgrade_config = agent_upgrade_config
        # The configurations for delivering items to Object Storage Service (OSS).
        self.oss_delivery_configs = oss_delivery_configs
        # The request ID.
        self.request_id = request_id
        # Cloud Assistant Session Manager configuration.
        self.session_manager_config = session_manager_config
        # The configurations for delivering items to Simple Log Service.
        self.sls_delivery_configs = sls_delivery_configs

    def validate(self):
        if self.agent_upgrade_config:
            self.agent_upgrade_config.validate()
        if self.oss_delivery_configs:
            self.oss_delivery_configs.validate()
        if self.session_manager_config:
            self.session_manager_config.validate()
        if self.sls_delivery_configs:
            self.sls_delivery_configs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_upgrade_config is not None:
            result['AgentUpgradeConfig'] = self.agent_upgrade_config.to_map()

        if self.oss_delivery_configs is not None:
            result['OssDeliveryConfigs'] = self.oss_delivery_configs.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.session_manager_config is not None:
            result['SessionManagerConfig'] = self.session_manager_config.to_map()

        if self.sls_delivery_configs is not None:
            result['SlsDeliveryConfigs'] = self.sls_delivery_configs.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentUpgradeConfig') is not None:
            temp_model = main_models.DescribeCloudAssistantSettingsResponseBodyAgentUpgradeConfig()
            self.agent_upgrade_config = temp_model.from_map(m.get('AgentUpgradeConfig'))

        if m.get('OssDeliveryConfigs') is not None:
            temp_model = main_models.DescribeCloudAssistantSettingsResponseBodyOssDeliveryConfigs()
            self.oss_delivery_configs = temp_model.from_map(m.get('OssDeliveryConfigs'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SessionManagerConfig') is not None:
            temp_model = main_models.DescribeCloudAssistantSettingsResponseBodySessionManagerConfig()
            self.session_manager_config = temp_model.from_map(m.get('SessionManagerConfig'))

        if m.get('SlsDeliveryConfigs') is not None:
            temp_model = main_models.DescribeCloudAssistantSettingsResponseBodySlsDeliveryConfigs()
            self.sls_delivery_configs = temp_model.from_map(m.get('SlsDeliveryConfigs'))

        return self

class DescribeCloudAssistantSettingsResponseBodySlsDeliveryConfigs(DaraModel):
    def __init__(
        self,
        sls_delivery_config: List[main_models.DescribeCloudAssistantSettingsResponseBodySlsDeliveryConfigsSlsDeliveryConfig] = None,
    ):
        self.sls_delivery_config = sls_delivery_config

    def validate(self):
        if self.sls_delivery_config:
            for v1 in self.sls_delivery_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SlsDeliveryConfig'] = []
        if self.sls_delivery_config is not None:
            for k1 in self.sls_delivery_config:
                result['SlsDeliveryConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sls_delivery_config = []
        if m.get('SlsDeliveryConfig') is not None:
            for k1 in m.get('SlsDeliveryConfig'):
                temp_model = main_models.DescribeCloudAssistantSettingsResponseBodySlsDeliveryConfigsSlsDeliveryConfig()
                self.sls_delivery_config.append(temp_model.from_map(k1))

        return self

class DescribeCloudAssistantSettingsResponseBodySlsDeliveryConfigsSlsDeliveryConfig(DaraModel):
    def __init__(
        self,
        delivery_type: str = None,
        enabled: bool = None,
        logstore_name: str = None,
        project_name: str = None,
    ):
        # The type of items to be delivered. Valid values:
        # 
        # *   SessionManager: session records.
        # *   Invocation: task execution records.
        self.delivery_type = delivery_type
        # Indicates whether to deliver the specified items to Simple Log Service.
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
        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.logstore_name is not None:
            result['LogstoreName'] = self.logstore_name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('LogstoreName') is not None:
            self.logstore_name = m.get('LogstoreName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

class DescribeCloudAssistantSettingsResponseBodySessionManagerConfig(DaraModel):
    def __init__(
        self,
        session_manager_enabled: bool = None,
    ):
        # Specify whether to enable Cloud Assistant Session Manager. Valid values:
        # 
        # *   true: Enables the feature.
        # *   false: Disables the feature.
        # 
        # Note:
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

class DescribeCloudAssistantSettingsResponseBodyOssDeliveryConfigs(DaraModel):
    def __init__(
        self,
        oss_delivery_config: List[main_models.DescribeCloudAssistantSettingsResponseBodyOssDeliveryConfigsOssDeliveryConfig] = None,
    ):
        self.oss_delivery_config = oss_delivery_config

    def validate(self):
        if self.oss_delivery_config:
            for v1 in self.oss_delivery_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OssDeliveryConfig'] = []
        if self.oss_delivery_config is not None:
            for k1 in self.oss_delivery_config:
                result['OssDeliveryConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.oss_delivery_config = []
        if m.get('OssDeliveryConfig') is not None:
            for k1 in m.get('OssDeliveryConfig'):
                temp_model = main_models.DescribeCloudAssistantSettingsResponseBodyOssDeliveryConfigsOssDeliveryConfig()
                self.oss_delivery_config.append(temp_model.from_map(k1))

        return self

class DescribeCloudAssistantSettingsResponseBodyOssDeliveryConfigsOssDeliveryConfig(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        delivery_type: str = None,
        enabled: bool = None,
        encryption_algorithm: str = None,
        encryption_key_id: str = None,
        encryption_type: str = None,
        prefix: str = None,
    ):
        # The name of the OSS bucket.
        self.bucket_name = bucket_name
        # The type of items to be delivered. Valid values:
        # 
        # *   SessionManager: session records.
        # *   Invocation: task execution records.
        self.delivery_type = delivery_type
        # Indicates whether to deliver the specified items to OSS.
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
        # *   KMS: server-side encryption with Key Management Service (SSE-KMS).
        self.encryption_type = encryption_type
        # The prefix of the OSS bucket directory.
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

        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type

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

        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')

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

class DescribeCloudAssistantSettingsResponseBodyAgentUpgradeConfig(DaraModel):
    def __init__(
        self,
        allowed_upgrade_windows: main_models.DescribeCloudAssistantSettingsResponseBodyAgentUpgradeConfigAllowedUpgradeWindows = None,
        enabled: bool = None,
        time_zone: str = None,
    ):
        # The time windows during which Cloud Assistant Agent can be upgraded.
        self.allowed_upgrade_windows = allowed_upgrade_windows
        # Indicates whether custom upgrade is enabled for Cloud Assistant Agent. If the value is false or empty, an upgrade attempt is performed for Cloud Assistant Agent every 30 minutes.
        self.enabled = enabled
        # The time zone of the time windows.
        self.time_zone = time_zone

    def validate(self):
        if self.allowed_upgrade_windows:
            self.allowed_upgrade_windows.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_upgrade_windows is not None:
            result['AllowedUpgradeWindows'] = self.allowed_upgrade_windows.to_map()

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedUpgradeWindows') is not None:
            temp_model = main_models.DescribeCloudAssistantSettingsResponseBodyAgentUpgradeConfigAllowedUpgradeWindows()
            self.allowed_upgrade_windows = temp_model.from_map(m.get('AllowedUpgradeWindows'))

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        return self

class DescribeCloudAssistantSettingsResponseBodyAgentUpgradeConfigAllowedUpgradeWindows(DaraModel):
    def __init__(
        self,
        allowed_upgrade_window: List[str] = None,
    ):
        self.allowed_upgrade_window = allowed_upgrade_window

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_upgrade_window is not None:
            result['AllowedUpgradeWindow'] = self.allowed_upgrade_window

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedUpgradeWindow') is not None:
            self.allowed_upgrade_window = m.get('AllowedUpgradeWindow')

        return self

