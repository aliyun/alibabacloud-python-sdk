# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class GetHistoricalCallerReportResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetHistoricalCallerReportResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetHistoricalCallerReportResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetHistoricalCallerReportResponseBodyData(DaraModel):
    def __init__(
        self,
        last_calling_time: int = None,
        total_calls: int = None,
    ):
        self.last_calling_time = last_calling_time
        self.total_calls = total_calls

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_calling_time is not None:
            result['LastCallingTime'] = self.last_calling_time

        if self.total_calls is not None:
            result['TotalCalls'] = self.total_calls

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastCallingTime') is not None:
            self.last_calling_time = m.get('LastCallingTime')

        if m.get('TotalCalls') is not None:
            self.total_calls = m.get('TotalCalls')

        return self

