# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class ProvisionConfig(DaraModel):
    def __init__(
        self,
        always_allocate_cpu: bool = None,
        always_allocate_gpu: bool = None,
        current: int = None,
        current_error: str = None,
        default_target: int = None,
        function_arn: str = None,
        scheduled_actions: List[main_models.ScheduledAction] = None,
        target: int = None,
        target_tracking_policies: List[main_models.TargetTrackingPolicy] = None,
    ):
        self.always_allocate_cpu = always_allocate_cpu
        self.always_allocate_gpu = always_allocate_gpu
        self.current = current
        self.current_error = current_error
        self.default_target = default_target
        self.function_arn = function_arn
        self.scheduled_actions = scheduled_actions
        self.target = target
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

        if self.current is not None:
            result['current'] = self.current

        if self.current_error is not None:
            result['currentError'] = self.current_error

        if self.default_target is not None:
            result['defaultTarget'] = self.default_target

        if self.function_arn is not None:
            result['functionArn'] = self.function_arn

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

        if m.get('current') is not None:
            self.current = m.get('current')

        if m.get('currentError') is not None:
            self.current_error = m.get('currentError')

        if m.get('defaultTarget') is not None:
            self.default_target = m.get('defaultTarget')

        if m.get('functionArn') is not None:
            self.function_arn = m.get('functionArn')

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

