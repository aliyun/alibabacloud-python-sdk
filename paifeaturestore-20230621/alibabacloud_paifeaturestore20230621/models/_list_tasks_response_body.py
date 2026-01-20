# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class ListTasksResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tasks: List[main_models.ListTasksResponseBodyTasks] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.tasks = tasks
        self.total_count = total_count

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.ListTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTasksResponseBodyTasks(DaraModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_executed_time: str = None,
        gmt_finished_time: str = None,
        object_id: str = None,
        object_type: str = None,
        project_id: str = None,
        project_name: str = None,
        status: str = None,
        task_id: str = None,
        type: str = None,
    ):
        self.gmt_create_time = gmt_create_time
        self.gmt_executed_time = gmt_executed_time
        self.gmt_finished_time = gmt_finished_time
        self.object_id = object_id
        self.object_type = object_type
        self.project_id = project_id
        self.project_name = project_name
        self.status = status
        self.task_id = task_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_executed_time is not None:
            result['GmtExecutedTime'] = self.gmt_executed_time

        if self.gmt_finished_time is not None:
            result['GmtFinishedTime'] = self.gmt_finished_time

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtExecutedTime') is not None:
            self.gmt_executed_time = m.get('GmtExecutedTime')

        if m.get('GmtFinishedTime') is not None:
            self.gmt_finished_time = m.get('GmtFinishedTime')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

