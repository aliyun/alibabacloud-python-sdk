# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class SumComputeMetricsByRecordResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.SumComputeMetricsByRecordResponseBodyData] = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The response data.
        self.data = data
        # The HTTP status code.
        # 
        # - 1xx: Informational. The server has received the request and is processing it.
        # 
        # - 2xx: Success. The server successfully received, understood, and accepted the request.
        # 
        # - 3xx: Redirection. The client must take further action to complete the request.
        # 
        # - 4xx: Client-side error. The request contains invalid syntax or parameters and cannot be fulfilled.
        # 
        # - 5xx: Server-side error. The server failed to fulfill a valid request.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.SumComputeMetricsByRecordResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class SumComputeMetricsByRecordResponseBodyData(DaraModel):
    def __init__(
        self,
        daily_compute_records: List[main_models.SumComputeMetricsByRecordResponseBodyDataDailyComputeRecords] = None,
        type: str = None,
    ):
        # A list of daily usage records.
        self.daily_compute_records = daily_compute_records
        # The usage type. For example: ComputationSql
        self.type = type

    def validate(self):
        if self.daily_compute_records:
            for v1 in self.daily_compute_records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['dailyComputeRecords'] = []
        if self.daily_compute_records is not None:
            for k1 in self.daily_compute_records:
                result['dailyComputeRecords'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.daily_compute_records = []
        if m.get('dailyComputeRecords') is not None:
            for k1 in m.get('dailyComputeRecords'):
                temp_model = main_models.SumComputeMetricsByRecordResponseBodyDataDailyComputeRecords()
                self.daily_compute_records.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class SumComputeMetricsByRecordResponseBodyDataDailyComputeRecords(DaraModel):
    def __init__(
        self,
        date_time: str = None,
        percentage: float = None,
        record: str = None,
    ):
        # The statistics date. The format is yyyyMMdd.
        self.date_time = date_time
        # This day\\"s usage as a percentage of the total usage for the specified period. The value does not include a percent sign (%).
        self.percentage = percentage
        # The record count.
        self.record = record

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date_time is not None:
            result['dateTime'] = self.date_time

        if self.percentage is not None:
            result['percentage'] = self.percentage

        if self.record is not None:
            result['record'] = self.record

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateTime') is not None:
            self.date_time = m.get('dateTime')

        if m.get('percentage') is not None:
            self.percentage = m.get('percentage')

        if m.get('record') is not None:
            self.record = m.get('record')

        return self

