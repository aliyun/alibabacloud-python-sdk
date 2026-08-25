# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class GetTaskStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_status: main_models.GetTaskStatusResponseBodyTaskStatus = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The status information about the task.
        self.task_status = task_status

    def validate(self):
        if self.task_status:
            self.task_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskStatus') is not None:
            temp_model = main_models.GetTaskStatusResponseBodyTaskStatus()
            self.task_status = temp_model.from_map(m.get('TaskStatus'))

        return self

class GetTaskStatusResponseBodyTaskStatus(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        failure_reason: str = None,
        start_time: str = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        # The end time of the task.
        self.end_time = end_time
        # The cause of the task failure.
        # 
        # >  This parameter is returned only when the value of `Status` is `Failed`.
        self.failure_reason = failure_reason
        # The start time of the task.
        self.start_time = start_time
        # The task status. Valid values:
        # 
        # *   InProgress: The task is running.
        # *   Success: The task is successful.
        # *   Failed: The task failed.
        self.status = status
        # The task ID.
        self.task_id = task_id
        # The task type. Valid values:
        # 
        # *   ProvisionAccessConfiguration: An access configuration is provisioned.
        # *   DeprovisionAccessConfiguration: An access configuration is de-provisioned.
        # *   CreateAccessAssignment: Access permissions on an account in the resource directory are assigned.
        # *   DeleteAccessAssignment: Access permissions on an account in the resource directory are removed.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.failure_reason is not None:
            result['FailureReason'] = self.failure_reason

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FailureReason') is not None:
            self.failure_reason = m.get('FailureReason')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

