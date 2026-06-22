# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class AutoScalingPolicy(DaraModel):
    def __init__(
        self,
        constraints: main_models.AutoScalingPolicyConstraints = None,
        scaling_rules: List[main_models.ScalingRule] = None,
    ):
        self.constraints = constraints
        self.scaling_rules = scaling_rules

    def validate(self):
        if self.constraints:
            self.constraints.validate()
        if self.scaling_rules:
            for v1 in self.scaling_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.constraints is not None:
            result['Constraints'] = self.constraints.to_map()

        result['ScalingRules'] = []
        if self.scaling_rules is not None:
            for k1 in self.scaling_rules:
                result['ScalingRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Constraints') is not None:
            temp_model = main_models.AutoScalingPolicyConstraints()
            self.constraints = temp_model.from_map(m.get('Constraints'))

        self.scaling_rules = []
        if m.get('ScalingRules') is not None:
            for k1 in m.get('ScalingRules'):
                temp_model = main_models.ScalingRule()
                self.scaling_rules.append(temp_model.from_map(k1))

        return self

class AutoScalingPolicyConstraints(DaraModel):
    def __init__(
        self,
        max_capacity: int = None,
        min_capacity: int = None,
    ):
        self.max_capacity = max_capacity
        self.min_capacity = min_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_capacity is not None:
            result['MaxCapacity'] = self.max_capacity

        if self.min_capacity is not None:
            result['MinCapacity'] = self.min_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxCapacity') is not None:
            self.max_capacity = m.get('MaxCapacity')

        if m.get('MinCapacity') is not None:
            self.min_capacity = m.get('MinCapacity')

        return self

