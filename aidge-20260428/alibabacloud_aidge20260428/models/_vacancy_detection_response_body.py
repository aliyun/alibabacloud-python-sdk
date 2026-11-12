# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class VacancyDetectionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.VacancyDetectionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The submission result of the asynchronous task.
        self.data = data
        # The returned message or failure description.
        self.message = message
        # The unique ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful.
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
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.VacancyDetectionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class VacancyDetectionResponseBodyData(DaraModel):
    def __init__(
        self,
        task_id: str = None,
        usage_map: Dict[str, int] = None,
    ):
        # The ID of the asynchronous task. You can use this ID to call QueryAsyncTaskResult to query the result later.
        self.task_id = task_id
        # The usage details. This parameter is left empty during asynchronous commit and is populated by scheduling after the node reaches the desired state.
        self.usage_map = usage_map

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.usage_map is not None:
            result['UsageMap'] = self.usage_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UsageMap') is not None:
            self.usage_map = m.get('UsageMap')

        return self

