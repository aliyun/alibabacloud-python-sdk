# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceStatusResponseBody(DaraModel):
    def __init__(
        self,
        instance_statuses: main_models.DescribeInstanceStatusResponseBodyInstanceStatuses = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The IDs and status of the ECS instances.
        self.instance_statuses = instance_statuses
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of instances.
        self.total_count = total_count

    def validate(self):
        if self.instance_statuses:
            self.instance_statuses.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_statuses is not None:
            result['InstanceStatuses'] = self.instance_statuses.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceStatuses') is not None:
            temp_model = main_models.DescribeInstanceStatusResponseBodyInstanceStatuses()
            self.instance_statuses = temp_model.from_map(m.get('InstanceStatuses'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstanceStatusResponseBodyInstanceStatuses(DaraModel):
    def __init__(
        self,
        instance_status: List[main_models.DescribeInstanceStatusResponseBodyInstanceStatusesInstanceStatus] = None,
    ):
        self.instance_status = instance_status

    def validate(self):
        if self.instance_status:
            for v1 in self.instance_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceStatus'] = []
        if self.instance_status is not None:
            for k1 in self.instance_status:
                result['InstanceStatus'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_status = []
        if m.get('InstanceStatus') is not None:
            for k1 in m.get('InstanceStatus'):
                temp_model = main_models.DescribeInstanceStatusResponseBodyInstanceStatusesInstanceStatus()
                self.instance_status.append(temp_model.from_map(k1))

        return self

class DescribeInstanceStatusResponseBodyInstanceStatusesInstanceStatus(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        status: str = None,
    ):
        # The ID of the instance.
        self.instance_id = instance_id
        # The status of the instance. Valid values:
        # 
        # *   Pending: The instance is being created.
        # *   Running: The instance is running.
        # *   Starting: The instance is being started.
        # *   Stopping: The instance is being stopped.
        # *   Stopped: The instance is stopped.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

