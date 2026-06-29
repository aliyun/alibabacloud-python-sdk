# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_openitag20220616 import models as main_models
from darabonba.model import DaraModel

class GetTaskStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_statistics: main_models.TaskStatistic = None,
    ):
        # Return encoding. The default value is 0, indicating Normal execution.
        self.code = code
        # Details.
        self.details = details
        # Error code.
        self.error_code = error_code
        # Response message of the request.
        # 
        # This parameter is required.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Indicates whether the operation Succeeded.
        self.success = success
        # Job statistics.
        self.task_statistics = task_statistics

    def validate(self):
        if self.task_statistics:
            self.task_statistics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.details is not None:
            result['Details'] = self.details

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.task_statistics is not None:
            result['TaskStatistics'] = self.task_statistics.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Details') is not None:
            self.details = m.get('Details')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskStatistics') is not None:
            temp_model = main_models.TaskStatistic()
            self.task_statistics = temp_model.from_map(m.get('TaskStatistics'))

        return self

