# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class ImportFieldResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.ImportFieldResponseBodyResultObject = None,
        success: bool = None,
    ):
        # API status code.
        self.code = code
        # HTTP status code
        self.http_status_code = http_status_code
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Returned result
        self.result_object = result_object
        # Indicator of whether the request was successful.
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

        if self.message is not None:
            result['Message'] = self.message

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

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.ImportFieldResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ImportFieldResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        fail_field_names: str = None,
        success_num: int = None,
        total_num: int = None,
    ):
        # Names of fields that failed to upload
        self.fail_field_names = fail_field_names
        # Number of successful executions.
        self.success_num = success_num
        # Total number of records.
        self.total_num = total_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_field_names is not None:
            result['FailFieldNames'] = self.fail_field_names

        if self.success_num is not None:
            result['SuccessNum'] = self.success_num

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailFieldNames') is not None:
            self.fail_field_names = m.get('FailFieldNames')

        if m.get('SuccessNum') is not None:
            self.success_num = m.get('SuccessNum')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

