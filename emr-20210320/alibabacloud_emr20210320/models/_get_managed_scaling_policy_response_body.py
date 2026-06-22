# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class GetManagedScalingPolicyResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_policy: main_models.GetManagedScalingPolicyResponseBodyScalingPolicy = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The elastic scaling policy.
        self.scaling_policy = scaling_policy

    def validate(self):
        if self.scaling_policy:
            self.scaling_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scaling_policy is not None:
            result['ScalingPolicy'] = self.scaling_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScalingPolicy') is not None:
            temp_model = main_models.GetManagedScalingPolicyResponseBodyScalingPolicy()
            self.scaling_policy = temp_model.from_map(m.get('ScalingPolicy'))

        return self

class GetManagedScalingPolicyResponseBodyScalingPolicy(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        constraints: main_models.GetManagedScalingPolicyResponseBodyScalingPolicyConstraints = None,
        scaling_policy_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The constraints on the maximum and minimum values.
        self.constraints = constraints
        # The scaling policy ID.
        self.scaling_policy_id = scaling_policy_id

    def validate(self):
        if self.constraints:
            self.constraints.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.constraints is not None:
            result['Constraints'] = self.constraints.to_map()

        if self.scaling_policy_id is not None:
            result['ScalingPolicyId'] = self.scaling_policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Constraints') is not None:
            temp_model = main_models.GetManagedScalingPolicyResponseBodyScalingPolicyConstraints()
            self.constraints = temp_model.from_map(m.get('Constraints'))

        if m.get('ScalingPolicyId') is not None:
            self.scaling_policy_id = m.get('ScalingPolicyId')

        return self

class GetManagedScalingPolicyResponseBodyScalingPolicyConstraints(DaraModel):
    def __init__(
        self,
        max_capacity: int = None,
        max_on_demand_capacity: int = None,
        min_capacity: int = None,
    ):
        # The maximum value.
        self.max_capacity = max_capacity
        # The maximum number of pay-as-you-go task nodes.
        self.max_on_demand_capacity = max_on_demand_capacity
        # The minimum value.
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

        if self.max_on_demand_capacity is not None:
            result['MaxOnDemandCapacity'] = self.max_on_demand_capacity

        if self.min_capacity is not None:
            result['MinCapacity'] = self.min_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxCapacity') is not None:
            self.max_capacity = m.get('MaxCapacity')

        if m.get('MaxOnDemandCapacity') is not None:
            self.max_on_demand_capacity = m.get('MaxOnDemandCapacity')

        if m.get('MinCapacity') is not None:
            self.min_capacity = m.get('MinCapacity')

        return self

