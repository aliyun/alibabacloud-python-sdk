# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class ApplyTempStorageLeaseResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ApplyTempStorageLeaseResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The returned data fields.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The HTTP status code returned.
        self.status = status
        # Indicates whether the request was successful.
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
            temp_model = main_models.ApplyTempStorageLeaseResponseBodyData()
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

class ApplyTempStorageLeaseResponseBodyData(DaraModel):
    def __init__(
        self,
        param: main_models.ApplyTempStorageLeaseResponseBodyDataParam = None,
        temp_storage_lease_id: str = None,
    ):
        # HTTP parameters used for uploading the file.
        self.param = param
        # Unique lease ID. This parameter is required when retrieving the uploaded file within the application later.
        self.temp_storage_lease_id = temp_storage_lease_id

    def validate(self):
        if self.param:
            self.param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param is not None:
            result['Param'] = self.param.to_map()

        if self.temp_storage_lease_id is not None:
            result['TempStorageLeaseId'] = self.temp_storage_lease_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Param') is not None:
            temp_model = main_models.ApplyTempStorageLeaseResponseBodyDataParam()
            self.param = temp_model.from_map(m.get('Param'))

        if m.get('TempStorageLeaseId') is not None:
            self.temp_storage_lease_id = m.get('TempStorageLeaseId')

        return self

class ApplyTempStorageLeaseResponseBodyDataParam(DaraModel):
    def __init__(
        self,
        headers: Any = None,
        method: str = None,
        url: str = None,
    ):
        # K-V fields to be included in the Header; both Key and Value are strings.
        self.headers = headers
        # HTTP method for the call. Valid values: PUT POST
        self.method = method
        # Authorized URL for the file upload.
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

