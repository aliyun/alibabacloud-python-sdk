# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetLastOnceTaskInfoResponseBody(DaraModel):
    def __init__(
        self,
        collect_time: int = None,
        finish_count: int = None,
        request_id: str = None,
        task_id: int = None,
        task_info: main_models.GetLastOnceTaskInfoResponseBodyTaskInfo = None,
        total_count: int = None,
    ):
        # The time at which the task was run.
        self.collect_time = collect_time
        # The number of tasks that have been completed.
        self.finish_count = finish_count
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The ID of the latest scan task.
        self.task_id = task_id
        # The information about the latest task.
        self.task_info = task_info
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.task_info:
            self.task_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collect_time is not None:
            result['CollectTime'] = self.collect_time

        if self.finish_count is not None:
            result['FinishCount'] = self.finish_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_info is not None:
            result['TaskInfo'] = self.task_info.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CollectTime') is not None:
            self.collect_time = m.get('CollectTime')

        if m.get('FinishCount') is not None:
            self.finish_count = m.get('FinishCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskInfo') is not None:
            temp_model = main_models.GetLastOnceTaskInfoResponseBodyTaskInfo()
            self.task_info = temp_model.from_map(m.get('TaskInfo'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetLastOnceTaskInfoResponseBodyTaskInfo(DaraModel):
    def __init__(
        self,
        progress: int = None,
        result: str = None,
        status: str = None,
    ):
        # The progress of the task in percentage.
        self.progress = progress
        # The result of the scan task. Valid values:
        # 
        # *   **SUCCESS**: The task is successful.
        # *   **TASK_NOT_SUPPORT_REGION**: The images are deployed in a region that is not supported by container image scan.
        # *   **TASK_NOT_EXISTS**: The task does not exist.
        self.result = result
        # The status of the task. Valid values:
        # 
        # *   **INIT**: The task is not started.
        # *   **START**: The task is started.
        # *   **SUCCESS**: The task is complete.
        # *   **TIMEOUT**: The task timed out.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.progress is not None:
            result['Progress'] = self.progress

        if self.result is not None:
            result['Result'] = self.result

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

