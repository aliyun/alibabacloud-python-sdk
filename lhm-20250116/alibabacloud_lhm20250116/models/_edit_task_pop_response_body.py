# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class EditTaskPopResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.EditTaskPopResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data body returned by the operation. For the field structure, see the child parameter descriptions.
        self.data = data
        # The error code. An empty string is returned if the call is successful.
        self.err_code = err_code
        # The error message. An empty string is returned if the call is successful.
        self.err_message = err_message
        # The request ID, which is used to locate and troubleshoot issues with this call.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # - true: Successful.
        # - false: Failed. Check errCode and errMessage for troubleshooting.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.EditTaskPopResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class EditTaskPopResponseBodyData(DaraModel):
    def __init__(
        self,
        file_upload_parse_id: int = None,
        id: int = None,
        message: str = None,
        success: bool = None,
        task_id: int = None,
    ):
        # The file upload and parsing ID.
        self.file_upload_parse_id = file_upload_parse_id
        # The primary key ID that uniquely identifies a record.
        self.id = id
        # The message content. In error scenarios, this field contains the error message. In log scenarios, this field contains the log content. In instance progress scenarios, this field may return a status or progress value.
        self.message = message
        # Indicates whether the call is successful. Valid values:
        # 
        # - true: Successful.
        # - false: Failed. Check errCode and errMessage for troubleshooting.
        self.success = success
        # The task ID that uniquely identifies a task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_upload_parse_id is not None:
            result['fileUploadParseId'] = self.file_upload_parse_id

        if self.id is not None:
            result['id'] = self.id

        if self.message is not None:
            result['message'] = self.message

        if self.success is not None:
            result['success'] = self.success

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileUploadParseId') is not None:
            self.file_upload_parse_id = m.get('fileUploadParseId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

