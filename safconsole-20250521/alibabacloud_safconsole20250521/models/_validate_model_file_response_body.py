# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_safconsole20250521 import models as main_models
from darabonba.model import DaraModel

class ValidateModelFileResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        http_status_code: int = None,
        request_id: str = None,
        result_object: main_models.ValidateModelFileResponseBodyResultObject = None,
        success: bool = None,
    ):
        # Status code. A return value of 200 indicates success.
        self.code = code
        # HTTP status code.
        self.http_status_code = http_status_code
        # Request ID.
        self.request_id = request_id
        # Returned result.
        self.result_object = result_object
        # Indicates whether the call was successful.
        # 
        # - **true**: The call was successful.
        # - **false**: The call failed.
        self.success = success

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.ValidateModelFileResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ValidateModelFileResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        file_valid: bool = None,
    ):
        # Validation result.
        self.file_valid = file_valid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_valid is not None:
            result['FileValid'] = self.file_valid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileValid') is not None:
            self.file_valid = m.get('FileValid')

        return self

