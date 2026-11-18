# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePoolShrinkRequest(DaraModel):
    def __init__(
        self,
        pool_name: str = None,
        priority: int = None,
        resource_limits_shrink: str = None,
        scheduling_policy_id: str = None,
    ):
        # The name of the resource pool.
        # - The name can be up to 15 characters in length.
        # - The name can contain digits, uppercase letters, lowercase letters, underscores (_), and periods (.).
        # 
        # This parameter is required.
        self.pool_name = pool_name
        # The priority of the resource pool.
        # 
        # - Valid values: 1 to 99. Default value: 1, which indicates the lowest priority.
        # - Jobs submitted to a resource pool with a higher priority value are scheduled before pending jobs in resource pools with lower priority values. The priority of a resource pool takes precedence over the priority of a job.
        self.priority = priority
        # The resource quota limit for concurrent usage by a user within a resource pool.
        self.resource_limits_shrink = resource_limits_shrink
        # The scheduling policy ID.
        self.scheduling_policy_id = scheduling_policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.resource_limits_shrink is not None:
            result['ResourceLimits'] = self.resource_limits_shrink

        if self.scheduling_policy_id is not None:
            result['SchedulingPolicyId'] = self.scheduling_policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ResourceLimits') is not None:
            self.resource_limits_shrink = m.get('ResourceLimits')

        if m.get('SchedulingPolicyId') is not None:
            self.scheduling_policy_id = m.get('SchedulingPolicyId')

        return self

