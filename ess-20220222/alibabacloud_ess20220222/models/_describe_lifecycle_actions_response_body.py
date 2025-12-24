# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class DescribeLifecycleActionsResponseBody(DaraModel):
    def __init__(
        self,
        lifecycle_actions: List[main_models.DescribeLifecycleActionsResponseBodyLifecycleActions] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The actions of the lifecycle hook.
        self.lifecycle_actions = lifecycle_actions
        # The maximum number of entries returned per page.
        self.max_results = max_results
        # The query token returned in this call.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of the queried lifecycle actions.
        self.total_count = total_count

    def validate(self):
        if self.lifecycle_actions:
            for v1 in self.lifecycle_actions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LifecycleActions'] = []
        if self.lifecycle_actions is not None:
            for k1 in self.lifecycle_actions:
                result['LifecycleActions'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lifecycle_actions = []
        if m.get('LifecycleActions') is not None:
            for k1 in m.get('LifecycleActions'):
                temp_model = main_models.DescribeLifecycleActionsResponseBodyLifecycleActions()
                self.lifecycle_actions.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeLifecycleActionsResponseBodyLifecycleActions(DaraModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        lifecycle_action_result: str = None,
        lifecycle_action_status: str = None,
        lifecycle_action_token: str = None,
        lifecycle_hook_id: str = None,
    ):
        # The IDs of the ECS instances on which the lifecycle hook takes effect
        self.instance_ids = instance_ids
        # The subsequent action that Auto Scaling performs after the lifecycle hook times out. Valid values:
        # 
        # *   CONTINUE: Auto Scaling continues to respond to a scale-in or scale-out request.
        # *   ABANDON: Auto Scaling releases ECS instances that are created during scale-out events, or removes ECS instances from the scaling group during scale-in events.
        self.lifecycle_action_result = lifecycle_action_result
        # The status of the lifecycle hook action.
        self.lifecycle_action_status = lifecycle_action_status
        # The token of the lifecycle hook action.
        self.lifecycle_action_token = lifecycle_action_token
        # The ID of the lifecycle hook.
        self.lifecycle_hook_id = lifecycle_hook_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.lifecycle_action_result is not None:
            result['LifecycleActionResult'] = self.lifecycle_action_result

        if self.lifecycle_action_status is not None:
            result['LifecycleActionStatus'] = self.lifecycle_action_status

        if self.lifecycle_action_token is not None:
            result['LifecycleActionToken'] = self.lifecycle_action_token

        if self.lifecycle_hook_id is not None:
            result['LifecycleHookId'] = self.lifecycle_hook_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('LifecycleActionResult') is not None:
            self.lifecycle_action_result = m.get('LifecycleActionResult')

        if m.get('LifecycleActionStatus') is not None:
            self.lifecycle_action_status = m.get('LifecycleActionStatus')

        if m.get('LifecycleActionToken') is not None:
            self.lifecycle_action_token = m.get('LifecycleActionToken')

        if m.get('LifecycleHookId') is not None:
            self.lifecycle_hook_id = m.get('LifecycleHookId')

        return self

