# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeTasksResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeTasksResponseBodyItems] = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The list of result items.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

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
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeTasksResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

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
        begin_time: str = None,
        dbname: str = None,
        finish_time: str = None,
        progress: str = None,
        progress_info: str = None,
        scale_out_token: str = None,
        status: str = None,
        task_action: str = None,
        task_error_code: str = None,
        task_error_message: str = None,
        task_id: str = None,
    ):
        # The start time of the task, in the yyyy-MM-dd\\"T\\"HH:mm:ss\\"Z\\" format.
        self.begin_time = begin_time
        # The database name associated with the task. This parameter is generally empty.
        self.dbname = dbname
        # The end time of the task, in the yyyy-MM-dd\\"T\\"HH:mm:ss\\"Z\\" format.
        self.finish_time = finish_time
        # The task progress, in percentage.
        self.progress = progress
        # The detailed progress information of the task. This parameter is generally empty.
        self.progress_info = progress_info
        # The scale-out ID if the task is a scale-out task. This value serves as a unique key in the backend.
        self.scale_out_token = scale_out_token
        # The task status. Valid values:
        # 
        # - **RUNNING**: The task is running.
        # - **FAILED**: The task failed.
        self.status = status
        # The task action, which serves as the unique key for the backend task type.
        self.task_action = task_action
        # The error code of the failed task.
        self.task_error_code = task_error_code
        # The error message of the failed task.
        self.task_error_message = task_error_message
        # The task ID.
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

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.progress_info is not None:
            result['ProgressInfo'] = self.progress_info

        if self.scale_out_token is not None:
            result['ScaleOutToken'] = self.scale_out_token

        if self.status is not None:
            result['Status'] = self.status

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

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('ProgressInfo') is not None:
            self.progress_info = m.get('ProgressInfo')

        if m.get('ScaleOutToken') is not None:
            self.scale_out_token = m.get('ScaleOutToken')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')

        if m.get('TaskErrorCode') is not None:
            self.task_error_code = m.get('TaskErrorCode')

        if m.get('TaskErrorMessage') is not None:
            self.task_error_message = m.get('TaskErrorMessage')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

