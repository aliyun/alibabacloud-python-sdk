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
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.tasks = tasks
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
        self.creation_time = creation_time
        self.end_time = end_time
        self.hive_id = hive_id
        self.task_id = task_id
        self.task_state = task_state
        self.updated_time = updated_time
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

