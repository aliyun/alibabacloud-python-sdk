# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetOnceTaskResultInfoResponseBody(DaraModel):
    def __init__(
        self,
        collect_time: int = None,
        finish_count: int = None,
        request_id: str = None,
        task_id: int = None,
        task_info: main_models.GetOnceTaskResultInfoResponseBodyTaskInfo = None,
        total_count: int = None,
    ):
        # The execution time of the task.
        self.collect_time = collect_time
        # The number of tasks that were completed.
        self.finish_count = finish_count
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The ID of the scan task.
        self.task_id = task_id
        # The information about the task.
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
            temp_model = main_models.GetOnceTaskResultInfoResponseBodyTaskInfo()
            self.task_info = temp_model.from_map(m.get('TaskInfo'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetOnceTaskResultInfoResponseBodyTaskInfo(DaraModel):
    def __init__(
        self,
        status: str = None,
    ):
        # The status of the task. Valid values:
        # 
        # *   **INIT**: The task is not started.
        # *   **START**: The task is started.
        # *   **SUCCESS**: The task is complete.
        # *   **TIMEOUT**: The task times out.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

