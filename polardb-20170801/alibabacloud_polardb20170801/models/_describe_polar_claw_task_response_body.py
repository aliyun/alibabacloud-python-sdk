# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribePolarClawTaskResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
        task: main_models.DescribePolarClawTaskResponseBodyTask = None,
    ):
        self.application_id = application_id
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.task = task

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task is not None:
            result['Task'] = self.task.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Task') is not None:
            temp_model = main_models.DescribePolarClawTaskResponseBodyTask()
            self.task = temp_model.from_map(m.get('Task'))

        return self

class DescribePolarClawTaskResponseBodyTask(DaraModel):
    def __init__(
        self,
        created_at_ms: int = None,
        error: main_models.DescribePolarClawTaskResponseBodyTaskError = None,
        operation: str = None,
        result: Dict[str, Any] = None,
        state: str = None,
        task_id: str = None,
        updated_at_ms: int = None,
    ):
        self.created_at_ms = created_at_ms
        self.error = error
        self.operation = operation
        self.result = result
        self.state = state
        self.task_id = task_id
        self.updated_at_ms = updated_at_ms

    def validate(self):
        if self.error:
            self.error.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at_ms is not None:
            result['CreatedAtMs'] = self.created_at_ms

        if self.error is not None:
            result['Error'] = self.error.to_map()

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.result is not None:
            result['Result'] = self.result

        if self.state is not None:
            result['State'] = self.state

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.updated_at_ms is not None:
            result['UpdatedAtMs'] = self.updated_at_ms

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAtMs') is not None:
            self.created_at_ms = m.get('CreatedAtMs')

        if m.get('Error') is not None:
            temp_model = main_models.DescribePolarClawTaskResponseBodyTaskError()
            self.error = temp_model.from_map(m.get('Error'))

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UpdatedAtMs') is not None:
            self.updated_at_ms = m.get('UpdatedAtMs')

        return self

class DescribePolarClawTaskResponseBodyTaskError(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

