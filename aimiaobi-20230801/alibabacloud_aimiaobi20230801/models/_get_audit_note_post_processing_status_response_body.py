# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class GetAuditNotePostProcessingStatusResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAuditNotePostProcessingStatusResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # This parameter is required.
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        # This parameter is required.
        self.message = message
        # Id of the request
        # 
        # This parameter is required.
        self.request_id = request_id
        # This parameter is required.
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
            temp_model = main_models.GetAuditNotePostProcessingStatusResponseBodyData()
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

class GetAuditNotePostProcessingStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        completion_time: str = None,
        create_time: str = None,
        error_message: str = None,
        note_id: str = None,
        processed_lines: int = None,
        status: str = None,
        total_lines: int = None,
    ):
        self.completion_time = completion_time
        self.create_time = create_time
        self.error_message = error_message
        self.note_id = note_id
        self.processed_lines = processed_lines
        self.status = status
        self.total_lines = total_lines

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completion_time is not None:
            result['CompletionTime'] = self.completion_time

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.note_id is not None:
            result['NoteId'] = self.note_id

        if self.processed_lines is not None:
            result['ProcessedLines'] = self.processed_lines

        if self.status is not None:
            result['Status'] = self.status

        if self.total_lines is not None:
            result['TotalLines'] = self.total_lines

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletionTime') is not None:
            self.completion_time = m.get('CompletionTime')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('NoteId') is not None:
            self.note_id = m.get('NoteId')

        if m.get('ProcessedLines') is not None:
            self.processed_lines = m.get('ProcessedLines')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalLines') is not None:
            self.total_lines = m.get('TotalLines')

        return self

