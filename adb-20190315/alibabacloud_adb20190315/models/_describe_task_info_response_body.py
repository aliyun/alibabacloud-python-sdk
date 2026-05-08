# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeTaskInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_info: main_models.DescribeTaskInfoResponseBodyTaskInfo = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The queried task.
        self.task_info = task_info

    def validate(self):
        if self.task_info:
            self.task_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_info is not None:
            result['TaskInfo'] = self.task_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskInfo') is not None:
            temp_model = main_models.DescribeTaskInfoResponseBodyTaskInfo()
            self.task_info = temp_model.from_map(m.get('TaskInfo'))

        return self

class DescribeTaskInfoResponseBodyTaskInfo(DaraModel):
    def __init__(
        self,
        begin_time: str = None,
        finish_time: str = None,
        progress: str = None,
        status: str = None,
        task_id: int = None,
    ):
        # The start time of the task. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        self.begin_time = begin_time
        # The end time of the task. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        self.finish_time = finish_time
        # The progress of the task. Unit: %.
        self.progress = progress
        # The status. Valid values:
        # 
        # *   Waiting
        # *   Running
        # *   Finished
        # *   Failed
        # *   Closed
        # *   Cancel
        # *   Retry
        # *   Pause
        # *   Stop
        self.status = status
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

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

