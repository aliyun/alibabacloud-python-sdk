# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeTasksResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeTasksResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries on the current page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeTasksResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeTasksResponseBodyItems(DaraModel):
    def __init__(
        self,
        task_progress_info: List[main_models.DescribeTasksResponseBodyItemsTaskProgressInfo] = None,
    ):
        self.task_progress_info = task_progress_info

    def validate(self):
        if self.task_progress_info:
            for v1 in self.task_progress_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TaskProgressInfo'] = []
        if self.task_progress_info is not None:
            for k1 in self.task_progress_info:
                result['TaskProgressInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_progress_info = []
        if m.get('TaskProgressInfo') is not None:
            for k1 in m.get('TaskProgressInfo'):
                temp_model = main_models.DescribeTasksResponseBodyItemsTaskProgressInfo()
                self.task_progress_info.append(temp_model.from_map(k1))

        return self

class DescribeTasksResponseBodyItemsTaskProgressInfo(DaraModel):
    def __init__(
        self,
        begin_time: str = None,
        current_step_name: str = None,
        dbname: str = None,
        expected_finish_time: str = None,
        finish_time: str = None,
        progress: str = None,
        progress_info: str = None,
        remain: int = None,
        status: str = None,
        step_progress_info: str = None,
        steps_info: str = None,
        task_action: str = None,
        task_error_code: str = None,
        task_error_message: str = None,
        task_id: str = None,
    ):
        self.begin_time = begin_time
        self.current_step_name = current_step_name
        self.dbname = dbname
        self.expected_finish_time = expected_finish_time
        self.finish_time = finish_time
        self.progress = progress
        self.progress_info = progress_info
        self.remain = remain
        self.status = status
        self.step_progress_info = step_progress_info
        self.steps_info = steps_info
        self.task_action = task_action
        self.task_error_code = task_error_code
        self.task_error_message = task_error_message
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

        if self.status is not None:
            result['Status'] = self.status

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

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

