# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RescaleApplicationVerticallyRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        cpu: str = None,
        deploy: bool = None,
        disk_size: str = None,
        memory: str = None,
        resource_type: str = None,
        v_switch_id: str = None,
        auto_enable_application_scaling_rule: bool = None,
        min_ready_instance_ratio: int = None,
        min_ready_instances: int = None,
    ):
        # The app ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # Target CPU specification. Unit: millicore.
        # 
        # This parameter is required.
        self.cpu = cpu
        self.deploy = deploy
        # The disk size. Unit: GB.
        self.disk_size = disk_size
        # Target memory specification. Unit: MB.
        # 
        # This parameter is required.
        self.memory = memory
        self.resource_type = resource_type
        self.v_switch_id = v_switch_id
        # Enable application scale rules automatically.
        self.auto_enable_application_scaling_rule = auto_enable_application_scaling_rule
        # The ratio of minimum ready instances.
        self.min_ready_instance_ratio = min_ready_instance_ratio
        # Minimum ready instances.
        self.min_ready_instances = min_ready_instances

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.deploy is not None:
            result['Deploy'] = self.deploy

        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.auto_enable_application_scaling_rule is not None:
            result['autoEnableApplicationScalingRule'] = self.auto_enable_application_scaling_rule

        if self.min_ready_instance_ratio is not None:
            result['minReadyInstanceRatio'] = self.min_ready_instance_ratio

        if self.min_ready_instances is not None:
            result['minReadyInstances'] = self.min_ready_instances

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Deploy') is not None:
            self.deploy = m.get('Deploy')

        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('autoEnableApplicationScalingRule') is not None:
            self.auto_enable_application_scaling_rule = m.get('autoEnableApplicationScalingRule')

        if m.get('minReadyInstanceRatio') is not None:
            self.min_ready_instance_ratio = m.get('minReadyInstanceRatio')

        if m.get('minReadyInstances') is not None:
            self.min_ready_instances = m.get('minReadyInstances')

        return self

