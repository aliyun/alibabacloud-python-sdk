# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ExecuteAdHocTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        execute_result: main_models.ExecuteAdHocTaskResponseBodyExecuteResult = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.execute_result = execute_result
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.execute_result:
            self.execute_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.execute_result is not None:
            result['ExecuteResult'] = self.execute_result.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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

        if m.get('ExecuteResult') is not None:
            temp_model = main_models.ExecuteAdHocTaskResponseBodyExecuteResult()
            self.execute_result = temp_model.from_map(m.get('ExecuteResult'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ExecuteAdHocTaskResponseBodyExecuteResult(DaraModel):
    def __init__(
        self,
        sub_task_count: int = None,
        task_id: str = None,
    ):
        self.sub_task_count = sub_task_count
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sub_task_count is not None:
            result['SubTaskCount'] = self.sub_task_count

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubTaskCount') is not None:
            self.sub_task_count = m.get('SubTaskCount')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

