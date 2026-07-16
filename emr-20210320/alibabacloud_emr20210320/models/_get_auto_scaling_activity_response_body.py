# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class GetAutoScalingActivityResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_activity: main_models.GetAutoScalingActivityResponseBodyScalingActivity = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details of the scaling activity.
        self.scaling_activity = scaling_activity

    def validate(self):
        if self.scaling_activity:
            self.scaling_activity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scaling_activity is not None:
            result['ScalingActivity'] = self.scaling_activity.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScalingActivity') is not None:
            temp_model = main_models.GetAutoScalingActivityResponseBodyScalingActivity()
            self.scaling_activity = temp_model.from_map(m.get('ScalingActivity'))

        return self

class GetAutoScalingActivityResponseBodyScalingActivity(DaraModel):
    def __init__(
        self,
        activity_id: str = None,
        activity_results: List[main_models.ScalingActivityResult] = None,
        activity_state: str = None,
        activity_type: str = None,
        cluster_id: str = None,
        description: str = None,
        end_time: int = None,
        expect_num: int = None,
        node_group_id: str = None,
        node_group_name: str = None,
        operation_id: str = None,
        policy_type: str = None,
        rule_detail: main_models.ScalingRule = None,
        rule_name: str = None,
        start_time: int = None,
    ):
        # The ID of the scaling activity.
        self.activity_id = activity_id
        # The list of instances involved in the scaling activity.
        self.activity_results = activity_results
        # The state of the scaling activity. Valid values:
        # 
        # - REJECTED: rejected.
        # 
        # - SUCCESSFUL: successful.
        # 
        # - FAILED: failed.
        # 
        # - IN_PROGRESS: in progress.
        self.activity_state = activity_state
        # The type of the scaling activity. Valid values:
        # 
        # - SCALE_OUT: scale-out.
        # 
        # - SCALE_IN: scale-in.
        self.activity_type = activity_type
        # The cluster ID.
        self.cluster_id = cluster_id
        # The description of the scaling activity.
        self.description = description
        # The end time of the scaling activity.
        self.end_time = end_time
        # The number of instances that are added or removed.
        self.expect_num = expect_num
        # The node group ID.
        self.node_group_id = node_group_id
        # The name of the node group.
        self.node_group_name = node_group_name
        # The operation ID.
        self.operation_id = operation_id
        # The policy type.
        self.policy_type = policy_type
        # The details of the scaling rule.
        self.rule_detail = rule_detail
        # The name of the scaling rule.
        self.rule_name = rule_name
        # The start time of the scaling activity.
        self.start_time = start_time

    def validate(self):
        if self.activity_results:
            for v1 in self.activity_results:
                 if v1:
                    v1.validate()
        if self.rule_detail:
            self.rule_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id

        result['ActivityResults'] = []
        if self.activity_results is not None:
            for k1 in self.activity_results:
                result['ActivityResults'].append(k1.to_map() if k1 else None)

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

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name

        if self.operation_id is not None:
            result['OperationId'] = self.operation_id

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.rule_detail is not None:
            result['RuleDetail'] = self.rule_detail.to_map()

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')

        self.activity_results = []
        if m.get('ActivityResults') is not None:
            for k1 in m.get('ActivityResults'):
                temp_model = main_models.ScalingActivityResult()
                self.activity_results.append(temp_model.from_map(k1))

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

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')

        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('RuleDetail') is not None:
            temp_model = main_models.ScalingRule()
            self.rule_detail = temp_model.from_map(m.get('RuleDetail'))

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

