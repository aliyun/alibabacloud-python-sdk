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
        # The request ID.
        self.request_id = request_id
        # The list of tasks.
        self.tasks = tasks
        # The total number of tasks.
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
        # The time when the task was created.
        self.gmt_create_time = gmt_create_time
        # The time when the task was executed.
        self.gmt_executed_time = gmt_executed_time
        # The time when the task was completed.
        self.gmt_finished_time = gmt_finished_time
        # The ID of the object.
        self.object_id = object_id
        # The type of the object. Valid values:
        # 
        # ● ModelFeature: a model feature.
        # 
        # ● FeatureView: a feature view.
        self.object_type = object_type
        # The project ID.
        self.project_id = project_id
        # The project name.
        self.project_name = project_name
        # The status of the task. Valid values:
        # 
        # ● Initializing: The task is being initialized.
        # 
        # ● Running: The task is in progress.
        # 
        # ● Success: The task is successful.
        # 
        # ● Failure: The task failed.
        self.status = status
        # The task ID.
        self.task_id = task_id
        # The task type. Valid values:
        # 
        # ● OfflineToOnline: The task synchronizes data from offline to online.
        # 
        # ● ExportTrainingSet: The task exports a training set.
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

