# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class WarmPoolCapacityPolicyInput(DaraModel):
    def __init__(
        self,
        min_ready_sandboxes: int = None,
        scheduled_policies: List[main_models.WarmPoolScheduledPolicyInput] = None,
    ):
        # The base target number of ready sandboxes, which is required and can be set to 0.
        # 
        # This parameter is required.
        self.min_ready_sandboxes = min_ready_sandboxes
        # The list of scheduled capacity rules, which is optional.
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
        if self.min_ready_sandboxes is not None:
            result['minReadySandboxes'] = self.min_ready_sandboxes

        if self.scheduled_policies is not None:
            result['scheduledPolicies'] = []
            for k1 in self.scheduled_policies:
                result['scheduledPolicies'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('minReadySandboxes') is not None:
            self.min_ready_sandboxes = m.get('minReadySandboxes')

        if m.get('scheduledPolicies') is not None:
            self.scheduled_policies = []
            for k1 in m.get('scheduledPolicies'):
                temp_model = main_models.WarmPoolScheduledPolicyInput()
                self.scheduled_policies.append(temp_model.from_map(k1))

        return self

