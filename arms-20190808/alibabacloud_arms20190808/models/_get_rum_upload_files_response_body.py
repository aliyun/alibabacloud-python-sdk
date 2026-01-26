# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GetRumUploadFilesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetRumUploadFilesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed.
        self.code = code
        # The queried files.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message returned if the request failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
            temp_model = main_models.GetRumUploadFilesResponseBodyData()
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

class GetRumUploadFilesResponseBodyData(DaraModel):
    def __init__(
        self,
        file_list: List[main_models.GetRumUploadFilesResponseBodyDataFileList] = None,
        next_token: str = None,
    ):
        self.file_list = file_list
        self.next_token = next_token

    def validate(self):
        if self.file_list:
            for v1 in self.file_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FileList'] = []
        if self.file_list is not None:
            for k1 in self.file_list:
                result['FileList'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_list = []
        if m.get('FileList') is not None:
            for k1 in m.get('FileList'):
                temp_model = main_models.GetRumUploadFilesResponseBodyDataFileList()
                self.file_list.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class GetRumUploadFilesResponseBodyDataFileList(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        last_modified_time: Any = None,
        size: str = None,
        uuid: str = None,
        version_id: str = None,
    ):
        self.file_name = file_name
        self.last_modified_time = last_modified_time
        self.size = size
        self.uuid = uuid
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time

        if self.size is not None:
            result['Size'] = self.size

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

