# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class DeleteFilesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DeleteFilesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # The status code returned by the API.
        self.status = status
        # Indicates whether the API call is successful. Valid values:
        # - true: The call is successful.
        # - false: The call fails.
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

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DeleteFilesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DeleteFilesResponseBodyData(DaraModel):
    def __init__(
        self,
        delete_file_result_list: List[main_models.DeleteFilesResponseBodyDataDeleteFileResultList] = None,
    ):
        # The deletion results.
        self.delete_file_result_list = delete_file_result_list

    def validate(self):
        if self.delete_file_result_list:
            for v1 in self.delete_file_result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeleteFileResultList'] = []
        if self.delete_file_result_list is not None:
            for k1 in self.delete_file_result_list:
                result['DeleteFileResultList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delete_file_result_list = []
        if m.get('DeleteFileResultList') is not None:
            for k1 in m.get('DeleteFileResultList'):
                temp_model = main_models.DeleteFilesResponseBodyDataDeleteFileResultList()
                self.delete_file_result_list.append(temp_model.from_map(k1))

        return self

class DeleteFilesResponseBodyDataDeleteFileResultList(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        status: str = None,
    ):
        # The file ID.
        self.file_id = file_id
        # The file deletion status. Valid values:
        # 
        # - DELETED: The file is deleted.
        # - FAILED: The file fails to be deleted.
        # - NOT_FOUND: The file is not found.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

