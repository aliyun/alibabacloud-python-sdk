# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScalingActivity(DaraModel):
    def __init__(
        self,
        component_types: str = None,
        description: str = None,
        end_time: str = None,
        instance_id: str = None,
        policy_type: str = None,
        scaling_activity_id: str = None,
        scaling_activity_state: str = None,
        scaling_policy_id: str = None,
        scaling_rule_detail: str = None,
        scaling_rule_id: str = None,
        scaling_rule_name: str = None,
        start_time: str = None,
        time_zone: str = None,
    ):
        self.component_types = component_types
        self.description = description
        self.end_time = end_time
        self.instance_id = instance_id
        self.policy_type = policy_type
        self.scaling_activity_id = scaling_activity_id
        self.scaling_activity_state = scaling_activity_state
        self.scaling_policy_id = scaling_policy_id
        self.scaling_rule_detail = scaling_rule_detail
        self.scaling_rule_id = scaling_rule_id
        self.scaling_rule_name = scaling_rule_name
        self.start_time = start_time
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_types is not None:
            result['componentTypes'] = self.component_types

        if self.description is not None:
            result['description'] = self.description

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.policy_type is not None:
            result['policyType'] = self.policy_type

        if self.scaling_activity_id is not None:
            result['scalingActivityId'] = self.scaling_activity_id

        if self.scaling_activity_state is not None:
            result['scalingActivityState'] = self.scaling_activity_state

        if self.scaling_policy_id is not None:
            result['scalingPolicyId'] = self.scaling_policy_id

        if self.scaling_rule_detail is not None:
            result['scalingRuleDetail'] = self.scaling_rule_detail

        if self.scaling_rule_id is not None:
            result['scalingRuleId'] = self.scaling_rule_id

        if self.scaling_rule_name is not None:
            result['scalingRuleName'] = self.scaling_rule_name

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.time_zone is not None:
            result['timeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentTypes') is not None:
            self.component_types = m.get('componentTypes')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('policyType') is not None:
            self.policy_type = m.get('policyType')

        if m.get('scalingActivityId') is not None:
            self.scaling_activity_id = m.get('scalingActivityId')

        if m.get('scalingActivityState') is not None:
            self.scaling_activity_state = m.get('scalingActivityState')

        if m.get('scalingPolicyId') is not None:
            self.scaling_policy_id = m.get('scalingPolicyId')

        if m.get('scalingRuleDetail') is not None:
            self.scaling_rule_detail = m.get('scalingRuleDetail')

        if m.get('scalingRuleId') is not None:
            self.scaling_rule_id = m.get('scalingRuleId')

        if m.get('scalingRuleName') is not None:
            self.scaling_rule_name = m.get('scalingRuleName')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')

        return self

