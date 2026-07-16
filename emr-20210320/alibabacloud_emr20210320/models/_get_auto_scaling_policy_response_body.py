# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class GetAutoScalingPolicyResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_policy: main_models.GetAutoScalingPolicyResponseBodyScalingPolicy = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The Auto Scaling policy.
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
            temp_model = main_models.GetAutoScalingPolicyResponseBodyScalingPolicy()
            self.scaling_policy = temp_model.from_map(m.get('ScalingPolicy'))

        return self

class GetAutoScalingPolicyResponseBodyScalingPolicy(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        constraints: main_models.GetAutoScalingPolicyResponseBodyScalingPolicyConstraints = None,
        node_group_id: str = None,
        scaling_policy_id: str = None,
        scaling_rules: List[main_models.GetAutoScalingPolicyResponseBodyScalingPolicyScalingRules] = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The constraints on the minimum and maximum number of nodes in the node group.
        self.constraints = constraints
        # The node group ID.
        self.node_group_id = node_group_id
        # The scaling policy ID.
        self.scaling_policy_id = scaling_policy_id
        # The list of scaling rules.
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

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.scaling_policy_id is not None:
            result['ScalingPolicyId'] = self.scaling_policy_id

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
            temp_model = main_models.GetAutoScalingPolicyResponseBodyScalingPolicyConstraints()
            self.constraints = temp_model.from_map(m.get('Constraints'))

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('ScalingPolicyId') is not None:
            self.scaling_policy_id = m.get('ScalingPolicyId')

        self.scaling_rules = []
        if m.get('ScalingRules') is not None:
            for k1 in m.get('ScalingRules'):
                temp_model = main_models.GetAutoScalingPolicyResponseBodyScalingPolicyScalingRules()
                self.scaling_rules.append(temp_model.from_map(k1))

        return self

class GetAutoScalingPolicyResponseBodyScalingPolicyScalingRules(DaraModel):
    def __init__(
        self,
        activity_type: str = None,
        adjustment_type: str = None,
        adjustment_value: int = None,
        collation_time_zone: main_models.CollationTimeZone = None,
        metrics_trigger: main_models.MetricsTrigger = None,
        rule_name: str = None,
        time_trigger: main_models.TimeTrigger = None,
        trigger_type: str = None,
    ):
        # The type of the scaling activity. Valid values:
        # 
        # - SCALE_OUT: scale-out.
        # 
        # - SCALE_IN: scale-in.
        self.activity_type = activity_type
        # The adjustment type.
        self.adjustment_type = adjustment_type
        # The adjustment value. The value must be a positive integer. It specifies the number of instances to add or remove.
        self.adjustment_value = adjustment_value
        self.collation_time_zone = collation_time_zone
        # The description of the metric-based scaling rule.
        self.metrics_trigger = metrics_trigger
        # The name of the scaling rule.
        self.rule_name = rule_name
        # The description of the time-based scaling rule.
        self.time_trigger = time_trigger
        # The type of the scaling rule. Valid values:
        # 
        # - TIME_TRIGGER: a time-based scaling rule.
        # 
        # - METRICS_TRIGGER: a metric-based scaling rule.
        self.trigger_type = trigger_type

    def validate(self):
        if self.collation_time_zone:
            self.collation_time_zone.validate()
        if self.metrics_trigger:
            self.metrics_trigger.validate()
        if self.time_trigger:
            self.time_trigger.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_type is not None:
            result['ActivityType'] = self.activity_type

        if self.adjustment_type is not None:
            result['AdjustmentType'] = self.adjustment_type

        if self.adjustment_value is not None:
            result['AdjustmentValue'] = self.adjustment_value

        if self.collation_time_zone is not None:
            result['CollationTimeZone'] = self.collation_time_zone.to_map()

        if self.metrics_trigger is not None:
            result['MetricsTrigger'] = self.metrics_trigger.to_map()

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.time_trigger is not None:
            result['TimeTrigger'] = self.time_trigger.to_map()

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityType') is not None:
            self.activity_type = m.get('ActivityType')

        if m.get('AdjustmentType') is not None:
            self.adjustment_type = m.get('AdjustmentType')

        if m.get('AdjustmentValue') is not None:
            self.adjustment_value = m.get('AdjustmentValue')

        if m.get('CollationTimeZone') is not None:
            temp_model = main_models.CollationTimeZone()
            self.collation_time_zone = temp_model.from_map(m.get('CollationTimeZone'))

        if m.get('MetricsTrigger') is not None:
            temp_model = main_models.MetricsTrigger()
            self.metrics_trigger = temp_model.from_map(m.get('MetricsTrigger'))

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('TimeTrigger') is not None:
            temp_model = main_models.TimeTrigger()
            self.time_trigger = temp_model.from_map(m.get('TimeTrigger'))

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        return self

class GetAutoScalingPolicyResponseBodyScalingPolicyConstraints(DaraModel):
    def __init__(
        self,
        max_capacity: int = None,
        min_capacity: int = None,
    ):
        # The maximum number of nodes in the node group.
        # Default value: 2000.
        self.max_capacity = max_capacity
        # The minimum number of nodes in the node group.
        # Default value: 0.
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

