# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetAdHocTaskLogResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        log_info: main_models.GetAdHocTaskLogResponseBodyLogInfo = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.log_info = log_info
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.log_info:
            self.log_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.log_info is not None:
            result['LogInfo'] = self.log_info.to_map()

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

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('LogInfo') is not None:
            temp_model = main_models.GetAdHocTaskLogResponseBodyLogInfo()
            self.log_info = temp_model.from_map(m.get('LogInfo'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAdHocTaskLogResponseBodyLogInfo(DaraModel):
    def __init__(
        self,
        content: str = None,
        has_next: bool = None,
        has_result: bool = None,
        next_offset: int = None,
        sub_task_id: int = None,
        task_id: str = None,
        task_status: str = None,
    ):
        self.content = content
        self.has_next = has_next
        self.has_result = has_result
        self.next_offset = next_offset
        self.sub_task_id = sub_task_id
        self.task_id = task_id
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.has_next is not None:
            result['HasNext'] = self.has_next

        if self.has_result is not None:
            result['HasResult'] = self.has_result

        if self.next_offset is not None:
            result['NextOffset'] = self.next_offset

        if self.sub_task_id is not None:
            result['SubTaskId'] = self.sub_task_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')

        if m.get('HasResult') is not None:
            self.has_result = m.get('HasResult')

        if m.get('NextOffset') is not None:
            self.next_offset = m.get('NextOffset')

        if m.get('SubTaskId') is not None:
            self.sub_task_id = m.get('SubTaskId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        return self

