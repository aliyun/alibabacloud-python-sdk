# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class AuditTaskState(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        runtime_error: main_models.AuditTaskStateRuntimeError = None,
        runtime_status: str = None,
        runtime_status_checked_at: str = None,
        task: Dict[str, Any] = None,
        task_id: str = None,
        version: int = None,
    ):
        # The current expected sharing switch for the task.
        self.enabled = enabled
        # The runtime error, which is returned only when runtimeStatus is error.
        self.runtime_error = runtime_error
        # The runtime status, which appears only when includeRuntimeStatus=true is requested. Valid values: pending, starting, stopping, running, stopped, missing, drifted, and error. The list and get operations do not return deleting.
        self.runtime_status = runtime_status
        # The time when the remote status is checked. This field appears together with runtimeStatus.
        self.runtime_status_checked_at = runtime_status_checked_at
        # The task details in JSON format.
        self.task = task
        # The stable ID of the task, which must be equal to task.taskId.
        self.task_id = task_id
        # The current execution configuration version of the task. The minimum value is 1. Starting or stopping the task does not increment this version.
        self.version = version

    def validate(self):
        if self.runtime_error:
            self.runtime_error.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.runtime_error is not None:
            result['runtimeError'] = self.runtime_error.to_map()

        if self.runtime_status is not None:
            result['runtimeStatus'] = self.runtime_status

        if self.runtime_status_checked_at is not None:
            result['runtimeStatusCheckedAt'] = self.runtime_status_checked_at

        if self.task is not None:
            result['task'] = self.task

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('runtimeError') is not None:
            temp_model = main_models.AuditTaskStateRuntimeError()
            self.runtime_error = temp_model.from_map(m.get('runtimeError'))

        if m.get('runtimeStatus') is not None:
            self.runtime_status = m.get('runtimeStatus')

        if m.get('runtimeStatusCheckedAt') is not None:
            self.runtime_status_checked_at = m.get('runtimeStatusCheckedAt')

        if m.get('task') is not None:
            self.task = m.get('task')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self



class AuditTaskStateRuntimeError(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The error code, such as task_status_query_failed.
        self.code = code
        # The error description.
        self.message = message
        # The ID of the status query request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

