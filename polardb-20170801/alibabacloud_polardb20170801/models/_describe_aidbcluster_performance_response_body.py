# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeAIDBClusterPerformanceResponseBody(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        dbcluster_id: str = None,
        dbtype: str = None,
        dbversion: str = None,
        end_time: str = None,
        interval: str = None,
        performance_keys: List[main_models.DescribeAIDBClusterPerformanceResponseBodyPerformanceKeys] = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.api_key = api_key
        self.dbcluster_id = dbcluster_id
        self.dbtype = dbtype
        self.dbversion = dbversion
        self.end_time = end_time
        self.interval = interval
        self.performance_keys = performance_keys
        self.request_id = request_id
        self.start_time = start_time

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
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.interval is not None:
            result['Interval'] = self.interval

        result['PerformanceKeys'] = []
        if self.performance_keys is not None:
            for k1 in self.performance_keys:
                result['PerformanceKeys'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        self.performance_keys = []
        if m.get('PerformanceKeys') is not None:
            for k1 in m.get('PerformanceKeys'):
                temp_model = main_models.DescribeAIDBClusterPerformanceResponseBodyPerformanceKeys()
                self.performance_keys.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeAIDBClusterPerformanceResponseBodyPerformanceKeys(DaraModel):
    def __init__(
        self,
        dbnode_id: str = None,
        measurement: str = None,
        metric_name: str = None,
        points: List[main_models.DescribeAIDBClusterPerformanceResponseBodyPerformanceKeysPoints] = None,
    ):
        self.dbnode_id = dbnode_id
        self.measurement = measurement
        self.metric_name = metric_name
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
        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id

        if self.measurement is not None:
            result['Measurement'] = self.measurement

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        result['Points'] = []
        if self.points is not None:
            for k1 in self.points:
                result['Points'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')

        if m.get('Measurement') is not None:
            self.measurement = m.get('Measurement')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        self.points = []
        if m.get('Points') is not None:
            for k1 in m.get('Points'):
                temp_model = main_models.DescribeAIDBClusterPerformanceResponseBodyPerformanceKeysPoints()
                self.points.append(temp_model.from_map(k1))

        return self

class DescribeAIDBClusterPerformanceResponseBodyPerformanceKeysPoints(DaraModel):
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

