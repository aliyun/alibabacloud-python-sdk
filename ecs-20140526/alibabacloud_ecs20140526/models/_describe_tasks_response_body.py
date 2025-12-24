# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeTasksResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        request_id: str = None,
        task_set: main_models.DescribeTasksResponseBodyTaskSet = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # Details about the tasks.
        self.task_set = task_set
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.task_set:
            self.task_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_set is not None:
            result['TaskSet'] = self.task_set.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskSet') is not None:
            temp_model = main_models.DescribeTasksResponseBodyTaskSet()
            self.task_set = temp_model.from_map(m.get('TaskSet'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeTasksResponseBodyTaskSet(DaraModel):
    def __init__(
        self,
        task: List[main_models.DescribeTasksResponseBodyTaskSetTask] = None,
    ):
        self.task = task

    def validate(self):
        if self.task:
            for v1 in self.task:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Task'] = []
        if self.task is not None:
            for k1 in self.task:
                result['Task'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task = []
        if m.get('Task') is not None:
            for k1 in m.get('Task'):
                temp_model = main_models.DescribeTasksResponseBodyTaskSetTask()
                self.task.append(temp_model.from_map(k1))

        return self

class DescribeTasksResponseBodyTaskSetTask(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        finished_time: str = None,
        resource_id: str = None,
        support_cancel: str = None,
        task_action: str = None,
        task_id: str = None,
        task_status: str = None,
    ):
        # The time when the task was created.
        self.creation_time = creation_time
        # The time when the task ended.
        self.finished_time = finished_time
        # The resource ID.
        self.resource_id = resource_id
        # Indicates whether the task can be canceled.
        self.support_cancel = support_cancel
        # The name of the operation that generates the task.
        self.task_action = task_action
        # The task ID.
        self.task_id = task_id
        # The task status.
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.support_cancel is not None:
            result['SupportCancel'] = self.support_cancel

        if self.task_action is not None:
            result['TaskAction'] = self.task_action

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('SupportCancel') is not None:
            self.support_cancel = m.get('SupportCancel')

        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        return self

