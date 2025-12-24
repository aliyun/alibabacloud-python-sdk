# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLifecycleActionsRequest(DaraModel):
    def __init__(
        self,
        lifecycle_action_status: str = None,
        max_results: int = None,
        next_token: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_activity_id: str = None,
    ):
        # The status of the lifecycle action. Valid values:
        # 
        # *   If a lifecycle action is in the Pending state, Elastic Compute Service (ECS) instances are waiting to be added to a scaling group or waiting to be removed from a scaling group.
        # *   If a lifecycle action is in the Timeout state, the lifecycle hook that triggers the lifecycle action ends, and ECS instances are added to or removed from the scaling group.
        # *   If a lifecycle action is in the Completed state, you manually end the lifecycle hook that triggers the lifecycle action ahead of schedule.
        self.lifecycle_action_status = lifecycle_action_status
        # The maximum number of entries to return on each page. Valid values: 1 to 50.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The token that is used to specify the lifecycle action from which the query starts.
        # 
        # For example, after the first 10 lifecycle actions are queried, the query starts from the 11th lifecycle action. Set this parameter to the NextToken value that is returned in the previous API call. If you do not specify this parameter, the query starts from the beginning.
        self.next_token = next_token
        self.owner_id = owner_id
        # The region ID of the scaling group.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The ID of the scaling activity.
        # 
        # This parameter is required.
        self.scaling_activity_id = scaling_activity_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lifecycle_action_status is not None:
            result['LifecycleActionStatus'] = self.lifecycle_action_status

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LifecycleActionStatus') is not None:
            self.lifecycle_action_status = m.get('LifecycleActionStatus')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')

        return self

