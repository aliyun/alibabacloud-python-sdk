# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class ScalingStatus(DaraModel):
    def __init__(
        self,
        current_error: str = None,
        current_instances: int = None,
        min_instances: int = None,
        scheduled_policies: List[main_models.ScheduledPolicy] = None,
        target_instances: int = None,
    ):
        self.current_error = current_error
        self.current_instances = current_instances
        self.min_instances = min_instances
        self.scheduled_policies = scheduled_policies
        self.target_instances = target_instances

    def validate(self):
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

        if self.min_instances is not None:
            result['minInstances'] = self.min_instances

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

        if m.get('minInstances') is not None:
            self.min_instances = m.get('minInstances')

        self.scheduled_policies = []
        if m.get('scheduledPolicies') is not None:
            for k1 in m.get('scheduledPolicies'):
                temp_model = main_models.ScheduledPolicy()
                self.scheduled_policies.append(temp_model.from_map(k1))

        if m.get('targetInstances') is not None:
            self.target_instances = m.get('targetInstances')

        return self

