# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScalingActivity(DaraModel):
    def __init__(
        self,
        cause: str = None,
        description: str = None,
        end_time: int = None,
        ess_scaling_rule_id: str = None,
        expect_num: int = None,
        host_group_name: str = None,
        id: str = None,
        instance_ids: str = None,
        scaling_group_id: str = None,
        scaling_rule_name: str = None,
        start_time: int = None,
        status: str = None,
        total_capacity: int = None,
        transition: str = None,
    ):
        self.cause = cause
        self.description = description
        self.end_time = end_time
        self.ess_scaling_rule_id = ess_scaling_rule_id
        self.expect_num = expect_num
        self.host_group_name = host_group_name
        self.id = id
        self.instance_ids = instance_ids
        self.scaling_group_id = scaling_group_id
        self.scaling_rule_name = scaling_rule_name
        self.start_time = start_time
        self.status = status
        self.total_capacity = total_capacity
        self.transition = transition

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cause is not None:
            result['Cause'] = self.cause

        if self.description is not None:
            result['Description'] = self.description

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ess_scaling_rule_id is not None:
            result['EssScalingRuleId'] = self.ess_scaling_rule_id

        if self.expect_num is not None:
            result['ExpectNum'] = self.expect_num

        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.total_capacity is not None:
            result['TotalCapacity'] = self.total_capacity

        if self.transition is not None:
            result['Transition'] = self.transition

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cause') is not None:
            self.cause = m.get('Cause')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EssScalingRuleId') is not None:
            self.ess_scaling_rule_id = m.get('EssScalingRuleId')

        if m.get('ExpectNum') is not None:
            self.expect_num = m.get('ExpectNum')

        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalCapacity') is not None:
            self.total_capacity = m.get('TotalCapacity')

        if m.get('Transition') is not None:
            self.transition = m.get('Transition')

        return self

