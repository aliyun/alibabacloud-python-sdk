# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class GetStorageAmountSummaryResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetStorageAmountSummaryResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The business error code or an empty value.
        # 
        # - If success is false, a business error code is returned.
        # - If success is true, an empty value is returned.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # Indicates whether the business is successful. If this parameter is not empty and the value is not 200, the business processing failed.
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
            temp_model = main_models.GetStorageAmountSummaryResponseBodyData()
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

class GetStorageAmountSummaryResponseBodyData(DaraModel):
    def __init__(
        self,
        date: str = None,
        timestamp: int = None,
        unit: Dict[str, str] = None,
        value: Dict[str, int] = None,
    ):
        # The date of the statistics.
        self.date = date
        # The timestamp. This API does not return this parameter.
        self.timestamp = timestamp
        # The unit of the storage metrics. This API does not return this parameter.
        self.unit = unit
        # The storage metrics. The metrics include the following:
        # 
        # - projectAmount
        # - schemaAmount
        # - tableAmount
        # - partitionAmount
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['date'] = self.date

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        if self.unit is not None:
            result['unit'] = self.unit

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

