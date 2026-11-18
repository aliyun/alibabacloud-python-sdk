# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class ListPoolsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        pool_list: List[main_models.ListPoolsResponseBodyPoolList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The current page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page in a paging query. Maximum value: 50. Default value: 10.
        self.page_size = page_size
        # The list of resource pools.
        self.pool_list = pool_list
        # Id of the request
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.pool_list:
            for v1 in self.pool_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['PoolList'] = []
        if self.pool_list is not None:
            for k1 in self.pool_list:
                result['PoolList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.pool_list = []
        if m.get('PoolList') is not None:
            for k1 in m.get('PoolList'):
                temp_model = main_models.ListPoolsResponseBodyPoolList()
                self.pool_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPoolsResponseBodyPoolList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        is_default: bool = None,
        max_executor_num: int = None,
        pool_name: str = None,
        priority: int = None,
        scheduling_policy_id: str = None,
        status: str = None,
        tags: List[main_models.ListPoolsResponseBodyPoolListTags] = None,
        update_time: str = None,
    ):
        # The time when the resource pool was created. The time is in the YYYY-MM-DD HH:mm:ss format.
        self.create_time = create_time
        # Specifies whether the resource pool is the default resource pool. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.is_default = is_default
        # The number of running executor nodes in a resource pool.
        self.max_executor_num = max_executor_num
        # The resource pool name.
        # - The name can be up to 15 characters in length.
        # - The name can contain digits, uppercase letters, lowercase letters, underscores (_), and periods (.).
        self.pool_name = pool_name
        # The priority of the resource pool.
        # 
        # - Valid values: 1 to 99. Default value: 1, which indicates the lowest priority.
        # - Jobs submitted to a resource pool with a higher priority level are scheduled before pending jobs in a resource pool with a lower priority level. The priority level of a resource pool takes precedence over the priority of a job.
        self.priority = priority
        # The ID of the scheduling policy.
        self.scheduling_policy_id = scheduling_policy_id
        # The resource pool status. Valid values:
        # 
        # - Creating: The resource pool is being created.
        # - Updating: The resource pool is being updated.
        # - Deleting: The resource pool is being deleted.
        # - Working: The resource pool is working.
        # - Deleted: The resource pool is deleted.
        self.status = status
        # The tag information.
        self.tags = tags
        # The time when the resource pool was updated. The time is in the YYYY-MM-DD HH:mm:ss format.
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

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.max_executor_num is not None:
            result['MaxExecutorNum'] = self.max_executor_num

        if self.pool_name is not None:
            result['PoolName'] = self.pool_name

        if self.priority is not None:
            result['Priority'] = self.priority

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

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('MaxExecutorNum') is not None:
            self.max_executor_num = m.get('MaxExecutorNum')

        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('SchedulingPolicyId') is not None:
            self.scheduling_policy_id = m.get('SchedulingPolicyId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListPoolsResponseBodyPoolListTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListPoolsResponseBodyPoolListTags(DaraModel):
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

