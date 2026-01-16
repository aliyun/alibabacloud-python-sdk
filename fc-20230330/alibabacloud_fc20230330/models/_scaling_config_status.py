# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class ScalingConfigStatus(DaraModel):
    def __init__(
        self,
        current_error: str = None,
        current_instances: int = None,
        enable_mix_mode: bool = None,
        enable_on_demand_scaling: bool = None,
        function_arn: str = None,
        horizontal_scaling_policies: List[main_models.ScalingPolicy] = None,
        min_instances: int = None,
        request_dispatch_policy: str = None,
        resident_pool_id: str = None,
        scheduled_policies: List[main_models.ScheduledPolicy] = None,
        target_instances: int = None,
    ):
        self.current_error = current_error
        self.current_instances = current_instances
        self.enable_mix_mode = enable_mix_mode
        self.enable_on_demand_scaling = enable_on_demand_scaling
        self.function_arn = function_arn
        self.horizontal_scaling_policies = horizontal_scaling_policies
        self.min_instances = min_instances
        self.request_dispatch_policy = request_dispatch_policy
        self.resident_pool_id = resident_pool_id
        self.scheduled_policies = scheduled_policies
        self.target_instances = target_instances

    def validate(self):
        if self.horizontal_scaling_policies:
            for v1 in self.horizontal_scaling_policies:
                 if v1:
                    v1.validate()
        if self.scheduled_policies:
            for v1 in self.scheduled_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_error is not None:
            result['currentError'] = self.current_error

        if self.current_instances is not None:
            result['currentInstances'] = self.current_instances

        if self.enable_mix_mode is not None:
            result['enableMixMode'] = self.enable_mix_mode

        if self.enable_on_demand_scaling is not None:
            result['enableOnDemandScaling'] = self.enable_on_demand_scaling

        if self.function_arn is not None:
            result['functionArn'] = self.function_arn

        result['horizontalScalingPolicies'] = []
        if self.horizontal_scaling_policies is not None:
            for k1 in self.horizontal_scaling_policies:
                result['horizontalScalingPolicies'].append(k1.to_map() if k1 else None)

        if self.min_instances is not None:
            result['minInstances'] = self.min_instances

        if self.request_dispatch_policy is not None:
            result['requestDispatchPolicy'] = self.request_dispatch_policy

        if self.resident_pool_id is not None:
            result['residentPoolId'] = self.resident_pool_id

        result['scheduledPolicies'] = []
        if self.scheduled_policies is not None:
            for k1 in self.scheduled_policies:
                result['scheduledPolicies'].append(k1.to_map() if k1 else None)

        if self.target_instances is not None:
            result['targetInstances'] = self.target_instances

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentError') is not None:
            self.current_error = m.get('currentError')

        if m.get('currentInstances') is not None:
            self.current_instances = m.get('currentInstances')

        if m.get('enableMixMode') is not None:
            self.enable_mix_mode = m.get('enableMixMode')

        if m.get('enableOnDemandScaling') is not None:
            self.enable_on_demand_scaling = m.get('enableOnDemandScaling')

        if m.get('functionArn') is not None:
            self.function_arn = m.get('functionArn')

        self.horizontal_scaling_policies = []
        if m.get('horizontalScalingPolicies') is not None:
            for k1 in m.get('horizontalScalingPolicies'):
                temp_model = main_models.ScalingPolicy()
                self.horizontal_scaling_policies.append(temp_model.from_map(k1))

        if m.get('minInstances') is not None:
            self.min_instances = m.get('minInstances')

        if m.get('requestDispatchPolicy') is not None:
            self.request_dispatch_policy = m.get('requestDispatchPolicy')

        if m.get('residentPoolId') is not None:
            self.resident_pool_id = m.get('residentPoolId')

        self.scheduled_policies = []
        if m.get('scheduledPolicies') is not None:
            for k1 in m.get('scheduledPolicies'):
                temp_model = main_models.ScheduledPolicy()
                self.scheduled_policies.append(temp_model.from_map(k1))

        if m.get('targetInstances') is not None:
            self.target_instances = m.get('targetInstances')

        return self

