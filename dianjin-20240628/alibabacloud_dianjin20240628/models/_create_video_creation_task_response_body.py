# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class CreateVideoCreationTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateVideoCreationTaskResponseBodyData = None,
        message: str = None,
        retry_able: bool = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.retry_able = retry_able
        self.success = success

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

        if self.retry_able is not None:
            result['retryAble'] = self.retry_able

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.CreateVideoCreationTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('retryAble') is not None:
            self.retry_able = m.get('retryAble')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class CreateVideoCreationTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        estimated_wait_time_in_seconds: int = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.estimated_wait_time_in_seconds = estimated_wait_time_in_seconds
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.estimated_wait_time_in_seconds is not None:
            result['estimatedWaitTimeInSeconds'] = self.estimated_wait_time_in_seconds

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('estimatedWaitTimeInSeconds') is not None:
            self.estimated_wait_time_in_seconds = m.get('estimatedWaitTimeInSeconds')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

