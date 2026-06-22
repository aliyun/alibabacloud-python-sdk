# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListAutoScalingActivitiesRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        end_time: int = None,
        instance_charge_types: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        node_group_id: str = None,
        region_id: str = None,
        scaling_activity_states: List[str] = None,
        scaling_activity_type: str = None,
        scaling_policy_type: str = None,
        scaling_rule_name: str = None,
        start_time: int = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The end timestamp for querying the creation time of scaling activities. The unit is milliseconds.
        self.end_time = end_time
        # The billing method of the instance. Valid values:
        # 
        # - ONDEMAND: Pay-as-you-go instance.
        # 
        # - SPOT: Spot instance.The default value is null, which means all billing methods are selected.Example: ["ONDEMAND", "SPOT"]
        self.instance_charge_types = instance_charge_types
        # The maximum number of records to return in a single request.
        self.max_results = max_results
        # The token that marks the position from which the query starts.
        self.next_token = next_token
        # The node group ID.
        self.node_group_id = node_group_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The status of the scaling activity. The number of elements in the array can range from 1 to 20.
        self.scaling_activity_states = scaling_activity_states
        # The type of the scaling activity. Valid values:
        # 
        # - SCALE_OUT: Scale-out.
        # 
        # - SCALE_IN: Scale-in.
        self.scaling_activity_type = scaling_activity_type
        self.scaling_policy_type = scaling_policy_type
        # The name of the scaling rule.
        self.scaling_rule_name = scaling_rule_name
        # The start timestamp for querying the creation time of scaling activities. The unit is milliseconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_charge_types is not None:
            result['InstanceChargeTypes'] = self.instance_charge_types

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scaling_activity_states is not None:
            result['ScalingActivityStates'] = self.scaling_activity_states

        if self.scaling_activity_type is not None:
            result['ScalingActivityType'] = self.scaling_activity_type

        if self.scaling_policy_type is not None:
            result['ScalingPolicyType'] = self.scaling_policy_type

        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceChargeTypes') is not None:
            self.instance_charge_types = m.get('InstanceChargeTypes')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScalingActivityStates') is not None:
            self.scaling_activity_states = m.get('ScalingActivityStates')

        if m.get('ScalingActivityType') is not None:
            self.scaling_activity_type = m.get('ScalingActivityType')

        if m.get('ScalingPolicyType') is not None:
            self.scaling_policy_type = m.get('ScalingPolicyType')

        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

