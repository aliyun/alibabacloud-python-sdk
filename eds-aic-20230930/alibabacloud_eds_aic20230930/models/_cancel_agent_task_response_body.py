# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class CancelAgentTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        tasks: List[main_models.CancelAgentTaskResponseBodyTasks] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
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
                temp_model = main_models.CancelAgentTaskResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k1))

        return self

class CancelAgentTaskResponseBodyTasks(DaraModel):
    def __init__(
        self,
        cancel_at: str = None,
        current_status: str = None,
        failed_reason: str = None,
        instance_id: str = None,
        previous_status: str = None,
        task_id: str = None,
    ):
        self.cancel_at = cancel_at
        self.current_status = current_status
        self.failed_reason = failed_reason
        self.instance_id = instance_id
        self.previous_status = previous_status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cancel_at is not None:
            result['CancelAt'] = self.cancel_at

        if self.current_status is not None:
            result['CurrentStatus'] = self.current_status

        if self.failed_reason is not None:
            result['FailedReason'] = self.failed_reason

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.previous_status is not None:
            result['PreviousStatus'] = self.previous_status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CancelAt') is not None:
            self.cancel_at = m.get('CancelAt')

        if m.get('CurrentStatus') is not None:
            self.current_status = m.get('CurrentStatus')

        if m.get('FailedReason') is not None:
            self.failed_reason = m.get('FailedReason')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PreviousStatus') is not None:
            self.previous_status = m.get('PreviousStatus')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

