# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class GetPoolResponseBody(DaraModel):
    def __init__(
        self,
        pool_info: main_models.GetPoolResponseBodyPoolInfo = None,
        request_id: str = None,
    ):
        # The resource pool information.
        self.pool_info = pool_info
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.pool_info:
            self.pool_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pool_info is not None:
            result['PoolInfo'] = self.pool_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PoolInfo') is not None:
            temp_model = main_models.GetPoolResponseBodyPoolInfo()
            self.pool_info = temp_model.from_map(m.get('PoolInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPoolResponseBodyPoolInfo(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        creator: str = None,
        executor_usage: int = None,
        is_default: bool = None,
        max_executor_num: int = None,
        pool_name: str = None,
        priority: int = None,
        reason: str = None,
        scheduling_policy_id: str = None,
        status: str = None,
        tags: List[main_models.GetPoolResponseBodyPoolInfoTags] = None,
        update_time: str = None,
    ):
        # The time when the resource pool was created.
        self.create_time = create_time
        # The ID of the resource pool creator.
        self.creator = creator
        # The number of executor nodes that are currently running in the resource pool.
        self.executor_usage = executor_usage
        # Indicates whether the resource pool is the default resource pool. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.is_default = is_default
        # The maximum number of executor nodes that can run concurrently in the resource pool.
        self.max_executor_num = max_executor_num
        # The resource pool name.
        # - The name can be up to 15 characters in length.
        # - The name can contain digits, uppercase letters, lowercase letters, underscores (_), and periods (.).
        self.pool_name = pool_name
        # The priority of the resource pool.
        # 
        # - Valid values: 1 to 99. Default value: 1, which indicates the lowest priority.
        # - Jobs submitted to a resource pool with a higher priority value are scheduled before pending jobs in a resource pool with a lower priority value. The resource pool priority takes precedence over the job priority.
        self.priority = priority
        # The error reason.
        self.reason = reason
        # The scheduling policy ID.
        self.scheduling_policy_id = scheduling_policy_id
        # The resource pool status. Valid values:
        # 
        # - Creating: The resource pool is being created.
        # - Updating: The resource pool is being updated.
        # - Deleting: The resource pool is being deleted.
        # - Working: The resource pool is running.
        # - Deleted: The resource pool has been deleted.
        self.status = status
        # The tag information.
        self.tags = tags
        # The time when the resource pool was last updated.
        self.update_time = update_time

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.executor_usage is not None:
            result['ExecutorUsage'] = self.executor_usage

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.max_executor_num is not None:
            result['MaxExecutorNum'] = self.max_executor_num

        if self.pool_name is not None:
            result['PoolName'] = self.pool_name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.scheduling_policy_id is not None:
            result['SchedulingPolicyId'] = self.scheduling_policy_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('ExecutorUsage') is not None:
            self.executor_usage = m.get('ExecutorUsage')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('MaxExecutorNum') is not None:
            self.max_executor_num = m.get('MaxExecutorNum')

        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('SchedulingPolicyId') is not None:
            self.scheduling_policy_id = m.get('SchedulingPolicyId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetPoolResponseBodyPoolInfoTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetPoolResponseBodyPoolInfoTags(DaraModel):
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

