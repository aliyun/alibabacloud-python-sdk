# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class CreatePoolRequest(DaraModel):
    def __init__(
        self,
        pool_name: str = None,
        priority: int = None,
        resource_limits: main_models.CreatePoolRequestResourceLimits = None,
    ):
        # The name of the resource pool.
        # 
        # *   The name can be up to 15 characters in length.
        # *   It can contain digits, uppercase letters, lowercase letters, underscores (_), and dots (.).
        # 
        # This parameter is required.
        self.pool_name = pool_name
        # The priority of the resource pool.
        # 
        # *   You can set a priority in the range of 1 to 99. The default value is 1, which is the lowest priority.
        # *   Jobs submitted to a resource pool with a higher priority level value will be scheduled before pending jobs in a resource pool with a lower priority level value, and the priority level of the resource pool takes precedence over the priority of the job.
        self.priority = priority
        # The quota of resources that users are allowed to concurrently use in a resource pool.
        self.resource_limits = resource_limits

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

        return self

class CreatePoolRequestResourceLimits(DaraModel):
    def __init__(
        self,
        max_exector_num: int = None,
    ):
        # The maximum number of concurrent execution nodes in a resource pool.
        self.max_exector_num = max_exector_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_exector_num is not None:
            result['MaxExectorNum'] = self.max_exector_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxExectorNum') is not None:
            self.max_exector_num = m.get('MaxExectorNum')

        return self

