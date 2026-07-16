# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ListAutoScalingActivitiesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        scaling_activities: List[main_models.ListAutoScalingActivitiesResponseBodyScalingActivities] = None,
        total_count: int = None,
    ):
        # The maximum number of entries returned for this request.
        self.max_results = max_results
        # The token that is used to start the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The list of scaling activities.
        self.scaling_activities = scaling_activities
        # The total number of entries that meet the query conditions.
        self.total_count = total_count

    def validate(self):
        if self.scaling_activities:
            for v1 in self.scaling_activities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ScalingActivities'] = []
        if self.scaling_activities is not None:
            for k1 in self.scaling_activities:
                result['ScalingActivities'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.scaling_activities = []
        if m.get('ScalingActivities') is not None:
            for k1 in m.get('ScalingActivities'):
                temp_model = main_models.ListAutoScalingActivitiesResponseBodyScalingActivities()
                self.scaling_activities.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAutoScalingActivitiesResponseBodyScalingActivities(DaraModel):
    def __init__(
        self,
        activity_id: str = None,
        activity_state: str = None,
        activity_type: str = None,
        cluster_id: str = None,
        description: str = None,
        end_time: int = None,
        expect_num: int = None,
        instance_type_details: List[main_models.ListAutoScalingActivitiesResponseBodyScalingActivitiesInstanceTypeDetails] = None,
        instance_type_to_num: Dict[str, int] = None,
        node_group_id: str = None,
        node_group_name: str = None,
        operation_id: str = None,
        policy_type: str = None,
        rule_name: str = None,
        start_time: int = None,
    ):
        # The ID of the scaling activity.
        self.activity_id = activity_id
        # The status of the scaling activity. Valid values:
        # 
        # - REJECTED: The scaling activity is rejected.
        # 
        # - SUCCESSFUL: The scaling activity is successful.
        # 
        # - FAILED: The scaling activity failed.
        # 
        # - IN_PROGRESS: The scaling activity is in progress.
        self.activity_state = activity_state
        # The type of the scaling activity. Valid values:
        # 
        # - SCALE_OUT: Scale-out.
        # 
        # - SCALE_IN: Scale-in.
        self.activity_type = activity_type
        # The cluster ID.
        self.cluster_id = cluster_id
        # The description of the scaling activity.
        self.description = description
        # The end time of the scaling activity. The unit is milliseconds.
        self.end_time = end_time
        # The number of instances to be added or removed in this scaling activity.
        self.expect_num = expect_num
        self.instance_type_details = instance_type_details
        self.instance_type_to_num = instance_type_to_num
        # The node group ID.
        self.node_group_id = node_group_id
        # The name of the node group.
        self.node_group_name = node_group_name
        # The operation ID.
        self.operation_id = operation_id
        self.policy_type = policy_type
        # The name of the scaling rule.
        self.rule_name = rule_name
        # The start time of the scaling activity. The unit is milliseconds.
        self.start_time = start_time

    def validate(self):
        if self.instance_type_details:
            for v1 in self.instance_type_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id

        if self.activity_state is not None:
            result['ActivityState'] = self.activity_state

        if self.activity_type is not None:
            result['ActivityType'] = self.activity_type

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.description is not None:
            result['Description'] = self.description

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.expect_num is not None:
            result['ExpectNum'] = self.expect_num

        result['InstanceTypeDetails'] = []
        if self.instance_type_details is not None:
            for k1 in self.instance_type_details:
                result['InstanceTypeDetails'].append(k1.to_map() if k1 else None)

        if self.instance_type_to_num is not None:
            result['InstanceTypeToNum'] = self.instance_type_to_num

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name

        if self.operation_id is not None:
            result['OperationId'] = self.operation_id

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')

        if m.get('ActivityState') is not None:
            self.activity_state = m.get('ActivityState')

        if m.get('ActivityType') is not None:
            self.activity_type = m.get('ActivityType')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExpectNum') is not None:
            self.expect_num = m.get('ExpectNum')

        self.instance_type_details = []
        if m.get('InstanceTypeDetails') is not None:
            for k1 in m.get('InstanceTypeDetails'):
                temp_model = main_models.ListAutoScalingActivitiesResponseBodyScalingActivitiesInstanceTypeDetails()
                self.instance_type_details.append(temp_model.from_map(k1))

        if m.get('InstanceTypeToNum') is not None:
            self.instance_type_to_num = m.get('InstanceTypeToNum')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')

        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class ListAutoScalingActivitiesResponseBodyScalingActivitiesInstanceTypeDetails(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        on_demand_instance_ids: List[str] = None,
        spot_instance_ids: List[str] = None,
    ):
        self.instance_type = instance_type
        self.on_demand_instance_ids = on_demand_instance_ids
        self.spot_instance_ids = spot_instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.on_demand_instance_ids is not None:
            result['OnDemandInstanceIds'] = self.on_demand_instance_ids

        if self.spot_instance_ids is not None:
            result['SpotInstanceIds'] = self.spot_instance_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('OnDemandInstanceIds') is not None:
            self.on_demand_instance_ids = m.get('OnDemandInstanceIds')

        if m.get('SpotInstanceIds') is not None:
            self.spot_instance_ids = m.get('SpotInstanceIds')

        return self

