# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeTasksResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        start_time: str = None,
        tasks: main_models.DescribeTasksResponseBodyTasks = None,
        total_record_count: int = None,
    ):
        # The ID of the cluster for which the task was created.
        self.dbcluster_id = dbcluster_id
        # The end time of the query.
        self.end_time = end_time
        # The page number of the page returned.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The start time of the query.
        self.start_time = start_time
        # The details of the task.
        self.tasks = tasks
        # The total number of entries returned.
        self.total_record_count = total_record_count

    def validate(self):
        if self.tasks:
            self.tasks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.tasks is not None:
            result['Tasks'] = self.tasks.to_map()

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Tasks') is not None:
            temp_model = main_models.DescribeTasksResponseBodyTasks()
            self.tasks = temp_model.from_map(m.get('Tasks'))

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeTasksResponseBodyTasks(DaraModel):
    def __init__(
        self,
        task: List[main_models.DescribeTasksResponseBodyTasksTask] = None,
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
                temp_model = main_models.DescribeTasksResponseBodyTasksTask()
                self.task.append(temp_model.from_map(k1))

        return self

class DescribeTasksResponseBodyTasksTask(DaraModel):
    def __init__(
        self,
        begin_time: str = None,
        current_step_name: str = None,
        dbname: str = None,
        expected_finish_time: str = None,
        finish_time: str = None,
        progress: int = None,
        progress_info: str = None,
        remain: int = None,
        step_progress_info: str = None,
        steps_info: str = None,
        task_action: str = None,
        task_error_code: str = None,
        task_error_message: str = None,
        task_id: str = None,
    ):
        # The time when the task was started. The time follows the ISO 8601 standard in the `YYYY-MM-DDThh:mm:ssZ` format. The time is displayed in UTC.
        self.begin_time = begin_time
        # The name of the current step.
        self.current_step_name = current_step_name
        # The database name.
        # 
        # >  This parameter is returned for only the tasks that involve database operations.
        self.dbname = dbname
        # The estimated end time of the task. In most cases, this parameter is empty.
        self.expected_finish_time = expected_finish_time
        # The time when the task was completed. The time follows the ISO 8601 standard in the `YYYY-MM-DDThh:mm:ssZ` format. The time is displayed in UTC.
        self.finish_time = finish_time
        # The progress of the task in percentage.
        self.progress = progress
        # The description of the task progress. If no progress description is provided for the task, this parameter is empty.
        self.progress_info = progress_info
        # The estimated remaining duration of the task. Unit: seconds.
        self.remain = remain
        # The progress of the subtasks. For example, the value `1/4` indicates that the task consists of four subtasks and the first subtask is in progress.
        self.step_progress_info = step_progress_info
        # The details of the subtasks.
        self.steps_info = steps_info
        # The API operation that is used by the task. Example: `CreateDBInstance`.
        self.task_action = task_action
        # The error code that is returned when an error occurs.
        # 
        # >  This parameter is returned only when the task is in the **Stop** state.
        self.task_error_code = task_error_code
        # The error message that is returned when an error occurs.
        # 
        # >  This parameter is returned only when the task is in the **Stop** state.
        self.task_error_message = task_error_message
        # The ID of the task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.current_step_name is not None:
            result['CurrentStepName'] = self.current_step_name

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.expected_finish_time is not None:
            result['ExpectedFinishTime'] = self.expected_finish_time

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.progress_info is not None:
            result['ProgressInfo'] = self.progress_info

        if self.remain is not None:
            result['Remain'] = self.remain

        if self.step_progress_info is not None:
            result['StepProgressInfo'] = self.step_progress_info

        if self.steps_info is not None:
            result['StepsInfo'] = self.steps_info

        if self.task_action is not None:
            result['TaskAction'] = self.task_action

        if self.task_error_code is not None:
            result['TaskErrorCode'] = self.task_error_code

        if self.task_error_message is not None:
            result['TaskErrorMessage'] = self.task_error_message

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('CurrentStepName') is not None:
            self.current_step_name = m.get('CurrentStepName')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('ExpectedFinishTime') is not None:
            self.expected_finish_time = m.get('ExpectedFinishTime')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('ProgressInfo') is not None:
            self.progress_info = m.get('ProgressInfo')

        if m.get('Remain') is not None:
            self.remain = m.get('Remain')

        if m.get('StepProgressInfo') is not None:
            self.step_progress_info = m.get('StepProgressInfo')

        if m.get('StepsInfo') is not None:
            self.steps_info = m.get('StepsInfo')

        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')

        if m.get('TaskErrorCode') is not None:
            self.task_error_code = m.get('TaskErrorCode')

        if m.get('TaskErrorMessage') is not None:
            self.task_error_message = m.get('TaskErrorMessage')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

