# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class QueryQuotaMetricResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.QueryQuotaMetricResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.http_code = http_code
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
            temp_model = main_models.QueryQuotaMetricResponseBodyData()
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

class QueryQuotaMetricResponseBodyData(DaraModel):
    def __init__(
        self,
        category: str = None,
        metrics: List[main_models.QueryQuotaMetricResponseBodyDataMetrics] = None,
        name: str = None,
        period: int = None,
    ):
        self.category = category
        self.metrics = metrics
        self.name = name
        self.period = period

    def validate(self):
        if self.metrics:
            for v1 in self.metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        result['metrics'] = []
        if self.metrics is not None:
            for k1 in self.metrics:
                result['metrics'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.period is not None:
            result['period'] = self.period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        self.metrics = []
        if m.get('metrics') is not None:
            for k1 in m.get('metrics'):
                temp_model = main_models.QueryQuotaMetricResponseBodyDataMetrics()
                self.metrics.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('period') is not None:
            self.period = m.get('period')

        return self

class QueryQuotaMetricResponseBodyDataMetrics(DaraModel):
    def __init__(
        self,
        metric: Dict[str, str] = None,
        values: List[List[float]] = None,
    ):
        self.metric = metric
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric is not None:
            result['metric'] = self.metric

        if self.values is not None:
            result['values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metric') is not None:
            self.metric = m.get('metric')

        if m.get('values') is not None:
            self.values = m.get('values')

        return self

