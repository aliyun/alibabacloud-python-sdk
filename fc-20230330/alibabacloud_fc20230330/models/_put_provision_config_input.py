# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class PutProvisionConfigInput(DaraModel):
    def __init__(
        self,
        always_allocate_cpu: bool = None,
        always_allocate_gpu: bool = None,
        default_target: int = None,
        scheduled_actions: List[main_models.ScheduledAction] = None,
        target: int = None,
        target_tracking_policies: List[main_models.TargetTrackingPolicy] = None,
    ):
        # Specifies whether to always allocate CPU. Default value: true.
        self.always_allocate_cpu = always_allocate_cpu
        # Specifies whether to always allocate GPU. Default value: true.
        self.always_allocate_gpu = always_allocate_gpu
        # The default minimum number of provisioned instances. Valid values: 0 to 10000.
        # > - If no metric-based auto elastic policy or scheduled elastic policy is configured, the current minimum number of instances equals the minimum number of instances you configured.
        # > - If you configured multiple elastic policies for the minimum number of instances, the system calculates the minimum number of instances triggered by each policy and uses the maximum value among the elastic policies that are effective at the current time as the current minimum number of instances.
        self.default_target = default_target
        # The scheduled scaling configuration.
        self.scheduled_actions = scheduled_actions
        # >Notice: This parameter is no longer recommended. Use the defaultTarget parameter instead.</notice>
        # The target number of provisioned resources. Valid values: 0 to 10000.
        # 
        # This parameter is required.
        self.target = target
        # The metric-based scaling policy configuration.
        self.target_tracking_policies = target_tracking_policies

    def validate(self):
        if self.scheduled_actions:
            for v1 in self.scheduled_actions:
                 if v1:
                    v1.validate()
        if self.target_tracking_policies:
            for v1 in self.target_tracking_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.always_allocate_cpu is not None:
            result['alwaysAllocateCPU'] = self.always_allocate_cpu

        if self.always_allocate_gpu is not None:
            result['alwaysAllocateGPU'] = self.always_allocate_gpu

        if self.default_target is not None:
            result['defaultTarget'] = self.default_target

        result['scheduledActions'] = []
        if self.scheduled_actions is not None:
            for k1 in self.scheduled_actions:
                result['scheduledActions'].append(k1.to_map() if k1 else None)

        if self.target is not None:
            result['target'] = self.target

        result['targetTrackingPolicies'] = []
        if self.target_tracking_policies is not None:
            for k1 in self.target_tracking_policies:
                result['targetTrackingPolicies'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alwaysAllocateCPU') is not None:
            self.always_allocate_cpu = m.get('alwaysAllocateCPU')

        if m.get('alwaysAllocateGPU') is not None:
            self.always_allocate_gpu = m.get('alwaysAllocateGPU')

        if m.get('defaultTarget') is not None:
            self.default_target = m.get('defaultTarget')

        self.scheduled_actions = []
        if m.get('scheduledActions') is not None:
            for k1 in m.get('scheduledActions'):
                temp_model = main_models.ScheduledAction()
                self.scheduled_actions.append(temp_model.from_map(k1))

        if m.get('target') is not None:
            self.target = m.get('target')

        self.target_tracking_policies = []
        if m.get('targetTrackingPolicies') is not None:
            for k1 in m.get('targetTrackingPolicies'):
                temp_model = main_models.TargetTrackingPolicy()
                self.target_tracking_policies.append(temp_model.from_map(k1))

        return self

