# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class ElasticConfigStatus(DaraModel):
    def __init__(
        self,
        current_error: str = None,
        current_instances: int = None,
        function_arn: str = None,
        min_instances: int = None,
        resident_pool_id: str = None,
        scaling_policies: List[main_models.ScalingPolicy] = None,
        scheduled_policies: List[main_models.ScheduledPolicy] = None,
        target_instances: int = None,
    ):
        self.current_error = current_error
        self.current_instances = current_instances
        self.function_arn = function_arn
        self.min_instances = min_instances
        self.resident_pool_id = resident_pool_id
        self.scaling_policies = scaling_policies
        self.scheduled_policies = scheduled_policies
        self.target_instances = target_instances

    def validate(self):
        if self.scaling_policies:
            for v1 in self.scaling_policies:
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

        if self.function_arn is not None:
            result['functionArn'] = self.function_arn

        if self.min_instances is not None:
            result['minInstances'] = self.min_instances

        if self.resident_pool_id is not None:
            result['residentPoolId'] = self.resident_pool_id

        result['scalingPolicies'] = []
        if self.scaling_policies is not None:
            for k1 in self.scaling_policies:
                result['scalingPolicies'].append(k1.to_map() if k1 else None)

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

        if m.get('functionArn') is not None:
            self.function_arn = m.get('functionArn')

        if m.get('minInstances') is not None:
            self.min_instances = m.get('minInstances')

        if m.get('residentPoolId') is not None:
            self.resident_pool_id = m.get('residentPoolId')

        self.scaling_policies = []
        if m.get('scalingPolicies') is not None:
            for k1 in m.get('scalingPolicies'):
                temp_model = main_models.ScalingPolicy()
                self.scaling_policies.append(temp_model.from_map(k1))

        self.scheduled_policies = []
        if m.get('scheduledPolicies') is not None:
            for k1 in m.get('scheduledPolicies'):
                temp_model = main_models.ScheduledPolicy()
                self.scheduled_policies.append(temp_model.from_map(k1))

        if m.get('targetInstances') is not None:
            self.target_instances = m.get('targetInstances')

        return self

