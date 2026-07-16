# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class PauseAgentTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        tasks: List[main_models.PauseAgentTaskResponseBodyTasks] = None,
    ):
        # The status code.
        self.code = code
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # A list of tasks.
        self.tasks = tasks

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
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.PauseAgentTaskResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k1))

        return self

class PauseAgentTaskResponseBodyTasks(DaraModel):
    def __init__(
        self,
        current_status: str = None,
        failed_reason: str = None,
        instance_id: str = None,
        pausing_at: str = None,
        previous_status: str = None,
        task_id: str = None,
    ):
        # The current status of the task. The following are possible values:
        # 
        # PENDING: The task is being created.
        # 
        # RUNNING: The task is running.
        # 
        # COMPLETED: The task is completed.
        # 
        # FAILED: The task failed.
        # 
        # TIMEOUT: The task timed out.
        # 
        # PAUSING: The task is being paused.
        # 
        # PAUSED: The task is paused.
        self.current_status = current_status
        # The reason the task failed to pause.
        self.failed_reason = failed_reason
        # The ID of the Mobile node.
        self.instance_id = instance_id
        # The time when the pause request was initiated, in ISO 8601 format.
        self.pausing_at = pausing_at
        # The status of the task before the pause request. The only valid value is:
        # 
        # RUNNING: The task is running.
        self.previous_status = previous_status
        # The unique ID of the task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_status is not None:
            result['CurrentStatus'] = self.current_status

        if self.failed_reason is not None:
            result['FailedReason'] = self.failed_reason

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.pausing_at is not None:
            result['PausingAt'] = self.pausing_at

        if self.previous_status is not None:
            result['PreviousStatus'] = self.previous_status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentStatus') is not None:
            self.current_status = m.get('CurrentStatus')

        if m.get('FailedReason') is not None:
            self.failed_reason = m.get('FailedReason')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PausingAt') is not None:
            self.pausing_at = m.get('PausingAt')

        if m.get('PreviousStatus') is not None:
            self.previous_status = m.get('PreviousStatus')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

