# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class SumComputeMetricsByUsageResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.SumComputeMetricsByUsageResponseBodyData] = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The usage data for each metering type.
        self.data = data
        # The HTTP status code.
        # 
        # - `1xx`: Informational response. The request is received and is being processed.
        # 
        # - `2xx`: Success. The request was successfully received, understood, and accepted.
        # 
        # - `3xx`: Redirection. Further action is required to complete the request.
        # 
        # - `4xx`: Client error. The request has invalid syntax or cannot be fulfilled.
        # 
        # - `5xx`: Server error. The server failed to fulfill an otherwise valid request.
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
                temp_model = main_models.SumComputeMetricsByUsageResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class SumComputeMetricsByUsageResponseBodyData(DaraModel):
    def __init__(
        self,
        daily_compute_metrics: List[main_models.SumComputeMetricsByUsageResponseBodyDataDailyComputeMetrics] = None,
        type: str = None,
    ):
        # The daily usage statistics.
        self.daily_compute_metrics = daily_compute_metrics
        # The metering type.
        # 
        # `ComputationSql`: Metering data for SQL jobs on internal tables.
        # 
        # `ComputationSqlOTS`: Metering data for SQL jobs on OTS external tables.
        # 
        # `ComputationSqlOSS`: Metering data for SQL jobs on OSS external tables.
        # 
        # `MapReduce`: Metering data for MapReduce jobs.
        # 
        # `spark`: Metering data for Spark jobs.
        # 
        # `mars`: Metering data for Mars jobs.
        self.type = type

    def validate(self):
        if self.daily_compute_metrics:
            for v1 in self.daily_compute_metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['dailyComputeMetrics'] = []
        if self.daily_compute_metrics is not None:
            for k1 in self.daily_compute_metrics:
                result['dailyComputeMetrics'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.daily_compute_metrics = []
        if m.get('dailyComputeMetrics') is not None:
            for k1 in m.get('dailyComputeMetrics'):
                temp_model = main_models.SumComputeMetricsByUsageResponseBodyDataDailyComputeMetrics()
                self.daily_compute_metrics.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class SumComputeMetricsByUsageResponseBodyDataDailyComputeMetrics(DaraModel):
    def __init__(
        self,
        date_time: str = None,
        unit: str = None,
        usage: str = None,
    ):
        # The date of the usage, in `yyyyMMdd` format.
        self.date_time = date_time
        # The unit of compute usage.
        self.unit = unit
        # The total usage for the day.
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date_time is not None:
            result['dateTime'] = self.date_time

        if self.unit is not None:
            result['unit'] = self.unit

        if self.usage is not None:
            result['usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateTime') is not None:
            self.date_time = m.get('dateTime')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        if m.get('usage') is not None:
            self.usage = m.get('usage')

        return self

