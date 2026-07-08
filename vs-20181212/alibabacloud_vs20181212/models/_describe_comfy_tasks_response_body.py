# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeComfyTasksResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tasks: List[main_models.DescribeComfyTasksResponseBodyTasks] = None,
        total: int = None,
    ):
        # The error code. A value of 0 indicates a successful request.
        self.code = code
        # The message that provides details about the result of the request.
        self.message = message
        # The page number of the returned data. The default value is 1.
        self.page_number = page_number
        # The number of tasks per page.
        # 
        # > This parameter applies only to recording queries.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # A list of Comfy tasks.
        self.tasks = tasks
        # The total number of tasks that match the filter criteria.
        self.total = total

    def validate(self):
        if self.tasks:
            for v1 in self.tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.DescribeComfyTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeComfyTasksResponseBodyTasks(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        end_time: str = None,
        hive_id: str = None,
        task_id: str = None,
        task_state: str = None,
        updated_time: str = None,
        workflow_id: str = None,
    ):
        # The creation time of the task.
        self.creation_time = creation_time
        # The end time of the task.
        self.end_time = end_time
        # The ID of the resource pool used by the task.
        self.hive_id = hive_id
        # The task ID.
        self.task_id = task_id
        # The task state.
        self.task_state = task_state
        # The last modified time of the task.
        self.updated_time = updated_time
        # The ID of the Comfy workflow associated with the task.
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.hive_id is not None:
            result['HiveId'] = self.hive_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_state is not None:
            result['TaskState'] = self.task_state

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('HiveId') is not None:
            self.hive_id = m.get('HiveId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

