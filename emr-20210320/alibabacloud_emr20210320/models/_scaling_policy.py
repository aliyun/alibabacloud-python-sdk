# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ScalingPolicy(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        constraints: main_models.ManagedScalingConstraints = None,
        disabled: bool = None,
        node_group_id: str = None,
        node_group_name: str = None,
        scaling_policy_id: str = None,
        scaling_policy_type: str = None,
        scaling_rules: List[main_models.ScalingRule] = None,
    ):
        self.cluster_id = cluster_id
        self.constraints = constraints
        self.disabled = disabled
        self.node_group_id = node_group_id
        self.node_group_name = node_group_name
        self.scaling_policy_id = scaling_policy_id
        self.scaling_policy_type = scaling_policy_type
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
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.constraints is not None:
            result['Constraints'] = self.constraints.to_map()

        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name

        if self.scaling_policy_id is not None:
            result['ScalingPolicyId'] = self.scaling_policy_id

        if self.scaling_policy_type is not None:
            result['ScalingPolicyType'] = self.scaling_policy_type

        result['ScalingRules'] = []
        if self.scaling_rules is not None:
            for k1 in self.scaling_rules:
                result['ScalingRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Constraints') is not None:
            temp_model = main_models.ManagedScalingConstraints()
            self.constraints = temp_model.from_map(m.get('Constraints'))

        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')

        if m.get('ScalingPolicyId') is not None:
            self.scaling_policy_id = m.get('ScalingPolicyId')

        if m.get('ScalingPolicyType') is not None:
            self.scaling_policy_type = m.get('ScalingPolicyType')

        self.scaling_rules = []
        if m.get('ScalingRules') is not None:
            for k1 in m.get('ScalingRules'):
                temp_model = main_models.ScalingRule()
                self.scaling_rules.append(temp_model.from_map(k1))

        return self

