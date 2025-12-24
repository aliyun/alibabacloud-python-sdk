# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeScalingRulesRequest(DaraModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
        scaling_rule_aris: List[str] = None,
        scaling_rule_ids: List[str] = None,
        scaling_rule_names: List[str] = None,
        scaling_rule_type: str = None,
        show_alarm_rules: bool = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Maximum value: 50.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the scaling group to which the scaling rules that you want to query belong.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the scaling group.
        self.scaling_group_id = scaling_group_id
        # The unique identifiers of the scaling rules that you want to query.
        self.scaling_rule_aris = scaling_rule_aris
        # The IDs of the scaling rules that you want to query.
        self.scaling_rule_ids = scaling_rule_ids
        # The names of the scaling rules that you want to query.
        self.scaling_rule_names = scaling_rule_names
        # The type of the scaling rule. Valid values:
        # 
        # *   SimpleScalingRule: adjusts the number of ECS instances based on the values of the AdjustmentType and AdjustmentValue parameters.
        # *   TargetTrackingScalingRule: calculates the number of ECS instances that need to be scaled in a dynamic manner and maintains the value of a predefined metric close to the value of the TargetValue parameter.
        # *   StepScalingRule: scales ECS instances in steps based on the specified thresholds and metric values.
        # *   PredictiveScalingRule: uses machine learning to analyze historical monitoring data of the scaling group and predicts the future values of metrics. In addition, Auto Scaling automatically creates scheduled tasks to adjust the boundary values for the scaling group.
        self.scaling_rule_type = scaling_rule_type
        # Specifies whether to return the event-triggered tasks that are associated with the scaling rule. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.show_alarm_rules = show_alarm_rules

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        if self.scaling_rule_aris is not None:
            result['ScalingRuleAris'] = self.scaling_rule_aris

        if self.scaling_rule_ids is not None:
            result['ScalingRuleIds'] = self.scaling_rule_ids

        if self.scaling_rule_names is not None:
            result['ScalingRuleNames'] = self.scaling_rule_names

        if self.scaling_rule_type is not None:
            result['ScalingRuleType'] = self.scaling_rule_type

        if self.show_alarm_rules is not None:
            result['ShowAlarmRules'] = self.show_alarm_rules

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('ScalingRuleAris') is not None:
            self.scaling_rule_aris = m.get('ScalingRuleAris')

        if m.get('ScalingRuleIds') is not None:
            self.scaling_rule_ids = m.get('ScalingRuleIds')

        if m.get('ScalingRuleNames') is not None:
            self.scaling_rule_names = m.get('ScalingRuleNames')

        if m.get('ScalingRuleType') is not None:
            self.scaling_rule_type = m.get('ScalingRuleType')

        if m.get('ShowAlarmRules') is not None:
            self.show_alarm_rules = m.get('ShowAlarmRules')

        return self

