# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class TriggerPatrolResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.TriggerPatrolResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response data of the triggered inspection.
        self.data = data
        # When success is false, this value is not empty and indicates the business error code. When success is true, this value is empty.
        self.error_code = error_code
        # When success is false, this value is not empty and indicates the business error message. When success is true, this value is empty.
        self.error_message = error_message
        # The business status code, which is uniformly 200. Use success to determine whether the business request is successful.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the business request is successful.
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

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.TriggerPatrolResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class TriggerPatrolResponseBodyData(DaraModel):
    def __init__(
        self,
        report_id: str = None,
        status: str = None,
    ):
        # The generated report ID.
        self.report_id = report_id
        # The report status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.report_id is not None:
            result['reportId'] = self.report_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

