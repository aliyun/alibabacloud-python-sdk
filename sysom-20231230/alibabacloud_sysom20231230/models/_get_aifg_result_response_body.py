# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class GetAifgResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAifgResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The data details.
        self.data = data
        # The message content.
        self.message = message
        # The unique identifier of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetAifgResultResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetAifgResultResponseBodyData(DaraModel):
    def __init__(
        self,
        result: Any = None,
        service_name: str = None,
        status: str = None,
        submit_time: str = None,
        task_id: str = None,
        trace_task_id: str = None,
    ):
        # The diagnostic results.
        self.result = result
        # The service name.
        self.service_name = service_name
        # The root data status.
        self.status = status
        # The data creation time.
        self.submit_time = submit_time
        # The unique identifier of the task.
        self.task_id = task_id
        # The training task ID.
        self.trace_task_id = trace_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.result is not None:
            result['result'] = self.result

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        if self.status is not None:
            result['status'] = self.status

        if self.submit_time is not None:
            result['submitTime'] = self.submit_time

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.trace_task_id is not None:
            result['traceTaskId'] = self.trace_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('submitTime') is not None:
            self.submit_time = m.get('submitTime')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('traceTaskId') is not None:
            self.trace_task_id = m.get('traceTaskId')

        return self

