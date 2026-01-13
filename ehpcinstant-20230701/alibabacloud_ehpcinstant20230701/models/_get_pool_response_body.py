# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class GetPoolResponseBody(DaraModel):
    def __init__(
        self,
        pool_info: main_models.GetPoolResponseBodyPoolInfo = None,
        request_id: str = None,
    ):
        # The information about the resource pool.
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
        exector_usage: int = None,
        is_default: bool = None,
        max_exector_num: int = None,
        pool_name: str = None,
        priority: int = None,
        reason: str = None,
        status: str = None,
        update_time: str = None,
    ):
        # The time when the resource pool is created.
        self.create_time = create_time
        # The usage of execution nodes that are running in a resource pool.
        self.exector_usage = exector_usage
        # Indices whether the resource pool is the default resource pool. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_default = is_default
        # The maximum number of execution nodes that can run concurrently in a resource pool.
        self.max_exector_num = max_exector_num
        # The name of the resource group.
        # 
        # *   The value can be up to 15 characters in length.
        # *   It can contain digits, uppercase letters, lowercase letters, underscores (_), and dots (.).
        self.pool_name = pool_name
        # The priority of the resource pool.
        # 
        # *   You can set a priority in the range of 1 to 99. The default value is 1, which is the lowest priority.
        # *   Jobs submitted to a resource pool with a higher priority level value will be scheduled before pending jobs in a resource pool with a lower priority level value, and the priority level of the resource pool takes precedence over the priority of the job.
        self.priority = priority
        # The cause of the error.
        self.reason = reason
        # The status of the resource pool. Valid values:
        # 
        # *   Creating: The resource pool is being created.
        # *   Updating: The resource pool is being updated.
        # *   Deleting: The resource pool is being deleted.
        # *   Working: The resource pool is working.
        # *   Deleted: The resource pool is deleted.
        self.status = status
        # The time when the resource pool was updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.exector_usage is not None:
            result['ExectorUsage'] = self.exector_usage

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.max_exector_num is not None:
            result['MaxExectorNum'] = self.max_exector_num

        if self.pool_name is not None:
            result['PoolName'] = self.pool_name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExectorUsage') is not None:
            self.exector_usage = m.get('ExectorUsage')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('MaxExectorNum') is not None:
            self.max_exector_num = m.get('MaxExectorNum')

        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

