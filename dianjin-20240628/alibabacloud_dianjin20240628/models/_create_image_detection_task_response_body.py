# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class CreateImageDetectionTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateImageDetectionTaskResponseBodyData = None,
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
            temp_model = main_models.CreateImageDetectionTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('retryAble') is not None:
            self.retry_able = m.get('retryAble')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class CreateImageDetectionTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        file_info: main_models.CreateImageDetectionTaskResponseBodyDataFileInfo = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.file_info = file_info
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        if self.file_info:
            self.file_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_info is not None:
            result['fileInfo'] = self.file_info.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileInfo') is not None:
            temp_model = main_models.CreateImageDetectionTaskResponseBodyDataFileInfo()
            self.file_info = temp_model.from_map(m.get('fileInfo'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

class CreateImageDetectionTaskResponseBodyDataFileInfo(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        file_name: str = None,
        file_trace_id: str = None,
        oss_key: str = None,
    ):
        self.file_id = file_id
        self.file_name = file_name
        self.file_trace_id = file_trace_id
        self.oss_key = oss_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['fileId'] = self.file_id

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_trace_id is not None:
            result['fileTraceId'] = self.file_trace_id

        if self.oss_key is not None:
            result['ossKey'] = self.oss_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileTraceId') is not None:
            self.file_trace_id = m.get('fileTraceId')

        if m.get('ossKey') is not None:
            self.oss_key = m.get('ossKey')

        return self

