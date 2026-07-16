# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class ApplyFileUploadLeaseResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ApplyFileUploadLeaseResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The data returned.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The status code returned.
        self.status = status
        # Indicates whether the API call is successful. Valid values:
        # 
        # - true: The call is successful.
        # - false: The call failed.
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
            temp_model = main_models.ApplyFileUploadLeaseResponseBodyData()
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

class ApplyFileUploadLeaseResponseBodyData(DaraModel):
    def __init__(
        self,
        file_upload_lease_id: str = None,
        param: main_models.ApplyFileUploadLeaseResponseBodyDataParam = None,
        type: str = None,
    ):
        # The unique ID of the lease. You need to use this parameter when you call the **AddFile** API.
        self.file_upload_lease_id = file_upload_lease_id
        # The HTTP request parameters for uploading the file.
        self.param = param
        # The upload method of the file. Valid values:
        # - OSS.PreSignedURL
        # - HTTP
        self.type = type

    def validate(self):
        if self.param:
            self.param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_upload_lease_id is not None:
            result['FileUploadLeaseId'] = self.file_upload_lease_id

        if self.param is not None:
            result['Param'] = self.param.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUploadLeaseId') is not None:
            self.file_upload_lease_id = m.get('FileUploadLeaseId')

        if m.get('Param') is not None:
            temp_model = main_models.ApplyFileUploadLeaseResponseBodyDataParam()
            self.param = temp_model.from_map(m.get('Param'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ApplyFileUploadLeaseResponseBodyDataParam(DaraModel):
    def __init__(
        self,
        headers: Any = None,
        method: str = None,
        url: str = None,
    ):
        # Key-value pairs that need to be included in the header. Both keys and values are strings.
        # 
        # > The returned Content-Type may be empty. You can upload the file with the empty value.
        self.headers = headers
        # The HTTP method. Valid values:
        # - PUT
        # - POST
        self.method = method
        # The upload URL of the file.
        # 
        # > This URL is a pre-signed URL. FormData upload is not supported. You must upload the file in binary mode.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['Headers'] = self.headers

        if self.method is not None:
            result['Method'] = self.method

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            self.headers = m.get('Headers')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

