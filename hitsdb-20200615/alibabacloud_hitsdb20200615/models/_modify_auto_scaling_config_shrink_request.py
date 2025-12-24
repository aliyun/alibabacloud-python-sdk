# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAutoScalingConfigShrinkRequest(DaraModel):
    def __init__(
        self,
        config_id: str = None,
        config_name: str = None,
        effective_time_end: str = None,
        effective_time_start: str = None,
        enabled: bool = None,
        engine: str = None,
        instance_id: str = None,
        nodes_max: int = None,
        nodes_min: int = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scale_rule_list_shrink: str = None,
        scale_type: str = None,
        security_token: str = None,
        spec_id: str = None,
        storage_capacity_max: int = None,
    ):
        # This parameter is required.
        self.config_id = config_id
        self.config_name = config_name
        self.effective_time_end = effective_time_end
        self.effective_time_start = effective_time_start
        self.enabled = enabled
        self.engine = engine
        # This parameter is required.
        self.instance_id = instance_id
        self.nodes_max = nodes_max
        self.nodes_min = nodes_min
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scale_rule_list_shrink = scale_rule_list_shrink
        self.scale_type = scale_type
        self.security_token = security_token
        self.spec_id = spec_id
        self.storage_capacity_max = storage_capacity_max

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.config_name is not None:
            result['ConfigName'] = self.config_name

        if self.effective_time_end is not None:
            result['EffectiveTimeEnd'] = self.effective_time_end

        if self.effective_time_start is not None:
            result['EffectiveTimeStart'] = self.effective_time_start

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.nodes_max is not None:
            result['NodesMax'] = self.nodes_max

        if self.nodes_min is not None:
            result['NodesMin'] = self.nodes_min

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scale_rule_list_shrink is not None:
            result['ScaleRuleList'] = self.scale_rule_list_shrink

        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.spec_id is not None:
            result['SpecId'] = self.spec_id

        if self.storage_capacity_max is not None:
            result['StorageCapacityMax'] = self.storage_capacity_max

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')

        if m.get('EffectiveTimeEnd') is not None:
            self.effective_time_end = m.get('EffectiveTimeEnd')

        if m.get('EffectiveTimeStart') is not None:
            self.effective_time_start = m.get('EffectiveTimeStart')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodesMax') is not None:
            self.nodes_max = m.get('NodesMax')

        if m.get('NodesMin') is not None:
            self.nodes_min = m.get('NodesMin')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ScaleRuleList') is not None:
            self.scale_rule_list_shrink = m.get('ScaleRuleList')

        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')

        if m.get('StorageCapacityMax') is not None:
            self.storage_capacity_max = m.get('StorageCapacityMax')

        return self

