# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeAgenticDBPerformanceResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        performance_keys: main_models.DescribeAgenticDBPerformanceResponseBodyPerformanceKeys = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The AgenticDB cluster ID.
        self.dbcluster_id = dbcluster_id
        # The end time of the query. Specify the time in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        self.end_time = end_time
        self.performance_keys = performance_keys
        # The request ID.
        self.request_id = request_id
        # The start time of the query. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format and in UTC.
        self.start_time = start_time

    def validate(self):
        if self.performance_keys:
            self.performance_keys.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.performance_keys is not None:
            result['PerformanceKeys'] = self.performance_keys.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PerformanceKeys') is not None:
            temp_model = main_models.DescribeAgenticDBPerformanceResponseBodyPerformanceKeys()
            self.performance_keys = temp_model.from_map(m.get('PerformanceKeys'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeAgenticDBPerformanceResponseBodyPerformanceKeys(DaraModel):
    def __init__(
        self,
        performance_keys: List[main_models.DescribeAgenticDBPerformanceResponseBodyPerformanceKeysPerformanceKeys] = None,
    ):
        self.performance_keys = performance_keys

    def validate(self):
        if self.performance_keys:
            for v1 in self.performance_keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['performanceKeys'] = []
        if self.performance_keys is not None:
            for k1 in self.performance_keys:
                result['performanceKeys'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.performance_keys = []
        if m.get('performanceKeys') is not None:
            for k1 in m.get('performanceKeys'):
                temp_model = main_models.DescribeAgenticDBPerformanceResponseBodyPerformanceKeysPerformanceKeys()
                self.performance_keys.append(temp_model.from_map(k1))

        return self

class DescribeAgenticDBPerformanceResponseBodyPerformanceKeysPerformanceKeys(DaraModel):
    def __init__(
        self,
        branch_id: str = None,
        measurement: str = None,
        metric_name: str = None,
        points: main_models.DescribeAgenticDBPerformanceResponseBodyPerformanceKeysPerformanceKeysPoints = None,
    ):
        self.branch_id = branch_id
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
        if self.branch_id is not None:
            result['BranchId'] = self.branch_id

        if self.measurement is not None:
            result['Measurement'] = self.measurement

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.points is not None:
            result['Points'] = self.points.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchId') is not None:
            self.branch_id = m.get('BranchId')

        if m.get('Measurement') is not None:
            self.measurement = m.get('Measurement')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Points') is not None:
            temp_model = main_models.DescribeAgenticDBPerformanceResponseBodyPerformanceKeysPerformanceKeysPoints()
            self.points = temp_model.from_map(m.get('Points'))

        return self

class DescribeAgenticDBPerformanceResponseBodyPerformanceKeysPerformanceKeysPoints(DaraModel):
    def __init__(
        self,
        points: List[main_models.DescribeAgenticDBPerformanceResponseBodyPerformanceKeysPerformanceKeysPointsPoints] = None,
    ):
        self.points = points

    def validate(self):
        if self.points:
            for v1 in self.points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['points'] = []
        if self.points is not None:
            for k1 in self.points:
                result['points'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.points = []
        if m.get('points') is not None:
            for k1 in m.get('points'):
                temp_model = main_models.DescribeAgenticDBPerformanceResponseBodyPerformanceKeysPerformanceKeysPointsPoints()
                self.points.append(temp_model.from_map(k1))

        return self

class DescribeAgenticDBPerformanceResponseBodyPerformanceKeysPerformanceKeysPointsPoints(DaraModel):
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

