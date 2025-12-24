# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class MoveCdsFileResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        move_cds_file_model: main_models.MoveCdsFileResponseBodyMoveCdsFileModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The result of the modification. A value of success indicates that the modification is successful. If the modification failed, an error message is returned.
        self.code = code
        # The error message that is returned. This parameter is not returned if the value of Code is success.
        self.message = message
        # The response object when you move a file.
        self.move_cds_file_model = move_cds_file_model
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        # 
        # Valid values:
        # 
        # *   <!-- -->
        # 
        #     true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   <!-- -->
        # 
        #     false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.success = success

    def validate(self):
        if self.move_cds_file_model:
            self.move_cds_file_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.move_cds_file_model is not None:
            result['MoveCdsFileModel'] = self.move_cds_file_model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('MoveCdsFileModel') is not None:
            temp_model = main_models.MoveCdsFileResponseBodyMoveCdsFileModel()
            self.move_cds_file_model = temp_model.from_map(m.get('MoveCdsFileModel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class MoveCdsFileResponseBodyMoveCdsFileModel(DaraModel):
    def __init__(
        self,
        async_task_id: str = None,
        exist: bool = None,
        file_id: str = None,
    ):
        # The ID of the asynchronous task. This parameter is not returned if you copy files. This parameter is returned if you copy folders in the backend in an asynchronous manner. You can call the GetAsyncTask operation to obtain the ID and details of an asynchronous task.
        self.async_task_id = async_task_id
        # Indicates whether the file exists.
        # 
        # Valid values:
        # 
        # *   <!-- -->
        # 
        #     true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   <!-- -->
        # 
        #     false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.exist = exist
        # The ID of the file.
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

        if self.exist is not None:
            result['Exist'] = self.exist

        if self.file_id is not None:
            result['FileId'] = self.file_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncTaskId') is not None:
            self.async_task_id = m.get('AsyncTaskId')

        if m.get('Exist') is not None:
            self.exist = m.get('Exist')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        return self

