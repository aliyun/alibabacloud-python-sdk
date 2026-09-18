# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class GetStorageSummaryComparedResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetStorageSummaryComparedResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # - 1xx: informational response. The request is received and is being processed.
        # 
        # - 2xx: success. The request is successfully received, understood, and accepted by the server.
        # 
        # - 3xx: redirection. The request is redirected. You must take further action to complete the request.
        # 
        # - 4xx: client error. The request contains invalid parameters or syntax, or fails to meet specific conditions.
        # 
        # - 5xx: server error. The server cannot fulfill the request for other reasons.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

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

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetStorageSummaryComparedResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetStorageSummaryComparedResponseBodyData(DaraModel):
    def __init__(
        self,
        begin_date: str = None,
        end_date: str = None,
        rate: Dict[str, float] = None,
        unit: Dict[str, str] = None,
        value: Dict[str, float] = None,
    ):
        # The start date.
        self.begin_date = begin_date
        # The end date.
        self.end_date = end_date
        # The year-on-year (YoY) change rate of the storage usage from the start date to the end date. Valid values:
        # 
        # - lowFreqStorageRate
        # 
        # - totalStorageRate
        # 
        # - standardStorageRate
        # 
        # - longTermStorageRate
        self.rate = rate
        # The unit of the change in the storage usage from the start date to the end date. Valid values:
        # 
        # - lowFreqStorageUnit
        # 
        # - totalStorageUnit
        # 
        # - standardStorageUnit
        # 
        # - longTermStorageUnit
        self.unit = unit
        # The change in the storage usage from the start date to the end date. Valid values:
        # 
        # - lowFreqStorage
        # 
        # - totalStorage
        # 
        # - standardStorage
        # 
        # - longTermStorage
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_date is not None:
            result['beginDate'] = self.begin_date

        if self.end_date is not None:
            result['endDate'] = self.end_date

        if self.rate is not None:
            result['rate'] = self.rate

        if self.unit is not None:
            result['unit'] = self.unit

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beginDate') is not None:
            self.begin_date = m.get('beginDate')

        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')

        if m.get('rate') is not None:
            self.rate = m.get('rate')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

