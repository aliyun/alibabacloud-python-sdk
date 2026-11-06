# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribePolarFsPerformanceResponseBody(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        performance_keys: main_models.DescribePolarFsPerformanceResponseBodyPerformanceKeys = None,
        polar_fs_instance_id: str = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The end time of the query. The time is in UTC.
        self.end_time = end_time
        self.performance_keys = performance_keys
        # The PolarFS instance ID.
        self.polar_fs_instance_id = polar_fs_instance_id
        # The request ID.
        self.request_id = request_id
        # The start time of the query. The time is in UTC.
        self.start_time = start_time

    def validate(self):
        if self.performance_keys:
            self.performance_keys.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.performance_keys is not None:
            result['PerformanceKeys'] = self.performance_keys.to_map()

        if self.polar_fs_instance_id is not None:
            result['PolarFsInstanceId'] = self.polar_fs_instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PerformanceKeys') is not None:
            temp_model = main_models.DescribePolarFsPerformanceResponseBodyPerformanceKeys()
            self.performance_keys = temp_model.from_map(m.get('PerformanceKeys'))

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribePolarFsPerformanceResponseBodyPerformanceKeys(DaraModel):
    def __init__(
        self,
        performance_item: List[main_models.DescribePolarFsPerformanceResponseBodyPerformanceKeysPerformanceItem] = None,
    ):
        self.performance_item = performance_item

    def validate(self):
        if self.performance_item:
            for v1 in self.performance_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PerformanceItem'] = []
        if self.performance_item is not None:
            for k1 in self.performance_item:
                result['PerformanceItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.performance_item = []
        if m.get('PerformanceItem') is not None:
            for k1 in m.get('PerformanceItem'):
                temp_model = main_models.DescribePolarFsPerformanceResponseBodyPerformanceKeysPerformanceItem()
                self.performance_item.append(temp_model.from_map(k1))

        return self

class DescribePolarFsPerformanceResponseBodyPerformanceKeysPerformanceItem(DaraModel):
    def __init__(
        self,
        measurement: str = None,
        metric_name: str = None,
        points: main_models.DescribePolarFsPerformanceResponseBodyPerformanceKeysPerformanceItemPoints = None,
    ):
        self.measurement = measurement
        self.metric_name = metric_name
        self.points = points

    def validate(self):
        if self.points:
            self.points.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.measurement is not None:
            result['Measurement'] = self.measurement

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.points is not None:
            result['Points'] = self.points.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Measurement') is not None:
            self.measurement = m.get('Measurement')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Points') is not None:
            temp_model = main_models.DescribePolarFsPerformanceResponseBodyPerformanceKeysPerformanceItemPoints()
            self.points = temp_model.from_map(m.get('Points'))

        return self

class DescribePolarFsPerformanceResponseBodyPerformanceKeysPerformanceItemPoints(DaraModel):
    def __init__(
        self,
        performance_item_value: List[main_models.DescribePolarFsPerformanceResponseBodyPerformanceKeysPerformanceItemPointsPerformanceItemValue] = None,
    ):
        self.performance_item_value = performance_item_value

    def validate(self):
        if self.performance_item_value:
            for v1 in self.performance_item_value:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PerformanceItemValue'] = []
        if self.performance_item_value is not None:
            for k1 in self.performance_item_value:
                result['PerformanceItemValue'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.performance_item_value = []
        if m.get('PerformanceItemValue') is not None:
            for k1 in m.get('PerformanceItemValue'):
                temp_model = main_models.DescribePolarFsPerformanceResponseBodyPerformanceKeysPerformanceItemPointsPerformanceItemValue()
                self.performance_item_value.append(temp_model.from_map(k1))

        return self

class DescribePolarFsPerformanceResponseBodyPerformanceKeysPerformanceItemPointsPerformanceItemValue(DaraModel):
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

