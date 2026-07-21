# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class CopyCdsFileResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        copy_cds_file_model: main_models.CopyCdsFileResponseBodyCopyCdsFileModel = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The execution result. A value of `success` indicates success. Otherwise, an error message is returned.
        self.code = code
        # The result of copying the file.
        self.copy_cds_file_model = copy_cds_file_model
        # The error message. This parameter is not returned if Code is `success`.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful.
        self.success = success

    def validate(self):
        if self.copy_cds_file_model:
            self.copy_cds_file_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.copy_cds_file_model is not None:
            result['CopyCdsFileModel'] = self.copy_cds_file_model.to_map()

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

        if m.get('CopyCdsFileModel') is not None:
            temp_model = main_models.CopyCdsFileResponseBodyCopyCdsFileModel()
            self.copy_cds_file_model = temp_model.from_map(m.get('CopyCdsFileModel'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CopyCdsFileResponseBodyCopyCdsFileModel(DaraModel):
    def __init__(
        self,
        async_task_id: str = None,
        file_id: str = None,
    ):
        # The asynchronous task ID. This field is not returned when a file is copied. When a folder is copied, the copy operation is performed asynchronously in the background, so this field is returned. You can call [GetAsyncTask](https://help.aliyun.com/document_detail/2357404.html) and pass in this asynchronous task ID to obtain the task details.
        self.async_task_id = async_task_id
        # The ID of the new file or folder after the copy operation.
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_task_id is not None:
            result['AsyncTaskId'] = self.async_task_id

        if self.file_id is not None:
            result['FileId'] = self.file_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncTaskId') is not None:
            self.async_task_id = m.get('AsyncTaskId')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        return self

