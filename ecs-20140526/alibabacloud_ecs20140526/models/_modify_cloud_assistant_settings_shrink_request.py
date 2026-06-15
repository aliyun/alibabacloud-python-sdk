# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCloudAssistantSettingsShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_upgrade_config_shrink: str = None,
        oss_delivery_config_shrink: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_usage_config_shrink: str = None,
        session_manager_config_shrink: str = None,
        setting_type: str = None,
        sls_delivery_config_shrink: str = None,
    ):
        # The configurations of upgrading the Cloud Assistant agent.
        self.agent_upgrade_config_shrink = agent_upgrade_config_shrink
        # The configurations of delivering records to OSS.
        self.oss_delivery_config_shrink = oss_delivery_config_shrink
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
        self.resource_usage_config_shrink = resource_usage_config_shrink
        # The configurations of the Session Manager feature.
        self.session_manager_config_shrink = session_manager_config_shrink
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
        self.sls_delivery_config_shrink = sls_delivery_config_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_upgrade_config_shrink is not None:
            result['AgentUpgradeConfig'] = self.agent_upgrade_config_shrink

        if self.oss_delivery_config_shrink is not None:
            result['OssDeliveryConfig'] = self.oss_delivery_config_shrink

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

        if self.resource_usage_config_shrink is not None:
            result['ResourceUsageConfig'] = self.resource_usage_config_shrink

        if self.session_manager_config_shrink is not None:
            result['SessionManagerConfig'] = self.session_manager_config_shrink

        if self.setting_type is not None:
            result['SettingType'] = self.setting_type

        if self.sls_delivery_config_shrink is not None:
            result['SlsDeliveryConfig'] = self.sls_delivery_config_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentUpgradeConfig') is not None:
            self.agent_upgrade_config_shrink = m.get('AgentUpgradeConfig')

        if m.get('OssDeliveryConfig') is not None:
            self.oss_delivery_config_shrink = m.get('OssDeliveryConfig')

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
            self.resource_usage_config_shrink = m.get('ResourceUsageConfig')

        if m.get('SessionManagerConfig') is not None:
            self.session_manager_config_shrink = m.get('SessionManagerConfig')

        if m.get('SettingType') is not None:
            self.setting_type = m.get('SettingType')

        if m.get('SlsDeliveryConfig') is not None:
            self.sls_delivery_config_shrink = m.get('SlsDeliveryConfig')

        return self

