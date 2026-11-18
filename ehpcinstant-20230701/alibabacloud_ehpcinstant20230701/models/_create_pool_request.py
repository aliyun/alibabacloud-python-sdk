# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class CreatePoolRequest(DaraModel):
    def __init__(
        self,
        pool_name: str = None,
        priority: int = None,
        resource_limits: main_models.CreatePoolRequestResourceLimits = None,
        scheduling_policy_id: str = None,
        tags: List[main_models.CreatePoolRequestTags] = None,
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
        # The resource quota limits for concurrent usage allowed for a user within a resource pool.
        self.resource_limits = resource_limits
        # The scheduling policy.
        self.scheduling_policy_id = scheduling_policy_id
        # The tag information.
        self.tags = tags

    def validate(self):
        if self.resource_limits:
            self.resource_limits.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

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

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ResourceLimits') is not None:
            temp_model = main_models.CreatePoolRequestResourceLimits()
            self.resource_limits = temp_model.from_map(m.get('ResourceLimits'))

        if m.get('SchedulingPolicyId') is not None:
            self.scheduling_policy_id = m.get('SchedulingPolicyId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreatePoolRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class CreatePoolRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreatePoolRequestResourceLimits(DaraModel):
    def __init__(
        self,
        max_executor_num: int = None,
    ):
        # The maximum number of executor nodes that a user can concurrently run within a resource pool.
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

