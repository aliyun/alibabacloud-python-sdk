# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class ScalingConfig(DaraModel):
    def __init__(
        self,
        min_instances: int = None,
        scheduled_policies: List[main_models.ScheduledPolicy] = None,
    ):
        self.min_instances = min_instances
        self.scheduled_policies = scheduled_policies

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
        if self.min_instances is not None:
            result['minInstances'] = self.min_instances

        result['scheduledPolicies'] = []
        if self.scheduled_policies is not None:
            for k1 in self.scheduled_policies:
                result['scheduledPolicies'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('minInstances') is not None:
            self.min_instances = m.get('minInstances')

        self.scheduled_policies = []
        if m.get('scheduledPolicies') is not None:
            for k1 in m.get('scheduledPolicies'):
                temp_model = main_models.ScheduledPolicy()
                self.scheduled_policies.append(temp_model.from_map(k1))

        return self

