# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeCacheAnalysisReportListResponseBody(DaraModel):
    def __init__(
        self,
        daily_tasks: main_models.DescribeCacheAnalysisReportListResponseBodyDailyTasks = None,
        instance_id: str = None,
        request_id: str = None,
    ):
        self.daily_tasks = daily_tasks
        # The ID of the instance.
        self.instance_id = instance_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.daily_tasks:
            self.daily_tasks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.daily_tasks is not None:
            result['DailyTasks'] = self.daily_tasks.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DailyTasks') is not None:
            temp_model = main_models.DescribeCacheAnalysisReportListResponseBodyDailyTasks()
            self.daily_tasks = temp_model.from_map(m.get('DailyTasks'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCacheAnalysisReportListResponseBodyDailyTasks(DaraModel):
    def __init__(
        self,
        daily_task: List[main_models.DescribeCacheAnalysisReportListResponseBodyDailyTasksDailyTask] = None,
    ):
        self.daily_task = daily_task

    def validate(self):
        if self.daily_task:
            for v1 in self.daily_task:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DailyTask'] = []
        if self.daily_task is not None:
            for k1 in self.daily_task:
                result['DailyTask'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.daily_task = []
        if m.get('DailyTask') is not None:
            for k1 in m.get('DailyTask'):
                temp_model = main_models.DescribeCacheAnalysisReportListResponseBodyDailyTasksDailyTask()
                self.daily_task.append(temp_model.from_map(k1))

        return self

class DescribeCacheAnalysisReportListResponseBodyDailyTasksDailyTask(DaraModel):
    def __init__(
        self,
        date: str = None,
        tasks: main_models.DescribeCacheAnalysisReportListResponseBodyDailyTasksDailyTaskTasks = None,
    ):
        self.date = date
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            self.tasks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.tasks is not None:
            result['Tasks'] = self.tasks.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('Tasks') is not None:
            temp_model = main_models.DescribeCacheAnalysisReportListResponseBodyDailyTasksDailyTaskTasks()
            self.tasks = temp_model.from_map(m.get('Tasks'))

        return self

class DescribeCacheAnalysisReportListResponseBodyDailyTasksDailyTaskTasks(DaraModel):
    def __init__(
        self,
        task: List[main_models.DescribeCacheAnalysisReportListResponseBodyDailyTasksDailyTaskTasksTask] = None,
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
                temp_model = main_models.DescribeCacheAnalysisReportListResponseBodyDailyTasksDailyTaskTasksTask()
                self.task.append(temp_model.from_map(k1))

        return self

class DescribeCacheAnalysisReportListResponseBodyDailyTasksDailyTaskTasksTask(DaraModel):
    def __init__(
        self,
        node_id: str = None,
        start_time: str = None,
        status: str = None,
        task_id: str = None,
    ):
        self.node_id = node_id
        self.start_time = start_time
        self.status = status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

