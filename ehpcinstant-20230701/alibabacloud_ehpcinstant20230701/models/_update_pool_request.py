# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class UpdatePoolRequest(DaraModel):
    def __init__(
        self,
        pool_name: str = None,
        priority: int = None,
        resource_limits: main_models.UpdatePoolRequestResourceLimits = None,
        scheduling_policy_id: str = None,
    ):
        # The name of the resource pool.
        # 
        # - The name can be up to 15 characters long.
        # 
        # - The name can contain digits, uppercase letters, lowercase letters, underscores (_), and periods (.).
        # 
        # This parameter is required.
        self.pool_name = pool_name
        # The priority of the resource pool.
        # 
        # - Valid values: 1 to 99. The default value is 1, which specifies the lowest priority.
        # 
        # - Jobs in a higher-priority resource pool are scheduled before pending jobs in lower-priority pools. A resource pool\\"s priority overrides a job\\"s priority.
        self.priority = priority
        # The limits on the resources that a user can use concurrently in the resource pool.
        self.resource_limits = resource_limits
        # The ID of the scheduling policy.
        self.scheduling_policy_id = scheduling_policy_id

    def validate(self):
        if self.resource_limits:
            self.resource_limits.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.resource_limits is not None:
            result['ResourceLimits'] = self.resource_limits.to_map()

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
            temp_model = main_models.UpdatePoolRequestResourceLimits()
            self.resource_limits = temp_model.from_map(m.get('ResourceLimits'))

        if m.get('SchedulingPolicyId') is not None:
            self.scheduling_policy_id = m.get('SchedulingPolicyId')

        return self

class UpdatePoolRequestResourceLimits(DaraModel):
    def __init__(
        self,
        max_executor_num: int = None,
    ):
        # The maximum number of executor nodes that a user can run concurrently in a resource pool.
        self.max_executor_num = max_executor_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_executor_num is not None:
            result['MaxExecutorNum'] = self.max_executor_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxExecutorNum') is not None:
            self.max_executor_num = m.get('MaxExecutorNum')

        return self

