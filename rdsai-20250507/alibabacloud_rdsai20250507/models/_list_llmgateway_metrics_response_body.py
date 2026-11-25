# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class ListLLMGatewayMetricsResponseBody(DaraModel):
    def __init__(
        self,
        granularity: str = None,
        metric_items: List[main_models.ListLLMGatewayMetricsResponseBodyMetricItems] = None,
        metric_type: str = None,
        request_id: str = None,
    ):
        self.granularity = granularity
        self.metric_items = metric_items
        self.metric_type = metric_type
        self.request_id = request_id

    def validate(self):
        if self.metric_items:
            for v1 in self.metric_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.granularity is not None:
            result['Granularity'] = self.granularity

        result['MetricItems'] = []
        if self.metric_items is not None:
            for k1 in self.metric_items:
                result['MetricItems'].append(k1.to_map() if k1 else None)

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        self.metric_items = []
        if m.get('MetricItems') is not None:
            for k1 in m.get('MetricItems'):
                temp_model = main_models.ListLLMGatewayMetricsResponseBodyMetricItems()
                self.metric_items.append(temp_model.from_map(k1))

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListLLMGatewayMetricsResponseBodyMetricItems(DaraModel):
    def __init__(
        self,
        data_points: List[main_models.ListLLMGatewayMetricsResponseBodyMetricItemsDataPoints] = None,
        key: str = None,
        model: str = None,
        unit: str = None,
    ):
        self.data_points = data_points
        self.key = key
        self.model = model
        self.unit = unit

    def validate(self):
        if self.data_points:
            for v1 in self.data_points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataPoints'] = []
        if self.data_points is not None:
            for k1 in self.data_points:
                result['DataPoints'].append(k1.to_map() if k1 else None)

        if self.key is not None:
            result['Key'] = self.key

        if self.model is not None:
            result['Model'] = self.model

        if self.unit is not None:
            result['Unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_points = []
        if m.get('DataPoints') is not None:
            for k1 in m.get('DataPoints'):
                temp_model = main_models.ListLLMGatewayMetricsResponseBodyMetricItemsDataPoints()
                self.data_points.append(temp_model.from_map(k1))

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

class ListLLMGatewayMetricsResponseBodyMetricItemsDataPoints(DaraModel):
    def __init__(
        self,
        timestamp: int = None,
        value: str = None,
    ):
        self.timestamp = timestamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

