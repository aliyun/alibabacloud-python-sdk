# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class GetAuditNoteProcessingStatusResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAuditNoteProcessingStatusResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Status code
        self.code = code
        # Response data
        self.data = data
        # HTTP status code
        self.http_status_code = http_status_code
        # Error message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Indicates whether the request succeeded
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

        if m.get('Data') is not None:
            temp_model = main_models.GetAuditNoteProcessingStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAuditNoteProcessingStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        file_key: str = None,
        file_size: int = None,
        note_name: str = None,
        status: str = None,
        task_id: str = None,
        update_time: int = None,
    ):
        # OSS path where the parsed rule library is stored
        self.file_key = file_key
        # Size of the rule library file, in bytes
        self.file_size = file_size
        # Name of the parsed rule library
        self.note_name = note_name
        # Task status. Valid values: PENDING, RUNNING, SUCCESSED, or FAILED
        self.status = status
        # Task ID. Unique identifier for this task.
        self.task_id = task_id
        # Update time
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_key is not None:
            result['FileKey'] = self.file_key

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.note_name is not None:
            result['NoteName'] = self.note_name

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('NoteName') is not None:
            self.note_name = m.get('NoteName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

