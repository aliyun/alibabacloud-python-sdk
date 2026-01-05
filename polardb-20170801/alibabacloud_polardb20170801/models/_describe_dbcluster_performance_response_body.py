# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterPerformanceResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbtype: str = None,
        dbversion: str = None,
        end_time: str = None,
        performance_keys: main_models.DescribeDBClusterPerformanceResponseBodyPerformanceKeys = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The type of the database engine.
        self.dbtype = dbtype
        # The version of the database engine.
        self.dbversion = dbversion
        # The end time of the query. The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.end_time = end_time
        # The cluster performance metrics.
        self.performance_keys = performance_keys
        # The request ID.
        self.request_id = request_id
        # The start time of the query. The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
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

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

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

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PerformanceKeys') is not None:
            temp_model = main_models.DescribeDBClusterPerformanceResponseBodyPerformanceKeys()
            self.performance_keys = temp_model.from_map(m.get('PerformanceKeys'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeDBClusterPerformanceResponseBodyPerformanceKeys(DaraModel):
    def __init__(
        self,
        performance_item: List[main_models.DescribeDBClusterPerformanceResponseBodyPerformanceKeysPerformanceItem] = None,
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
                temp_model = main_models.DescribeDBClusterPerformanceResponseBodyPerformanceKeysPerformanceItem()
                self.performance_item.append(temp_model.from_map(k1))

        return self

class DescribeDBClusterPerformanceResponseBodyPerformanceKeysPerformanceItem(DaraModel):
    def __init__(
        self,
        dbnode_id: str = None,
        measurement: str = None,
        metric_name: str = None,
        points: main_models.DescribeDBClusterPerformanceResponseBodyPerformanceKeysPerformanceItemPoints = None,
    ):
        # The ID of the cluster node.
        # 
        # >  The value of this parameter is not returned if the `Key` parameter is set to `PolarDBDiskUsage`.
        self.dbnode_id = dbnode_id
        # The performance metrics that are returned.
        self.measurement = measurement
        # The name of the performance metric.
        self.metric_name = metric_name
        # The performance metrics.
        self.points = points

    def validate(self):
        if self.points:
            self.points.validate()

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

        if self.points is not None:
            result['Points'] = self.points.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')

        if m.get('Measurement') is not None:
            self.measurement = m.get('Measurement')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Points') is not None:
            temp_model = main_models.DescribeDBClusterPerformanceResponseBodyPerformanceKeysPerformanceItemPoints()
            self.points = temp_model.from_map(m.get('Points'))

        return self

class DescribeDBClusterPerformanceResponseBodyPerformanceKeysPerformanceItemPoints(DaraModel):
    def __init__(
        self,
        performance_item_value: List[main_models.DescribeDBClusterPerformanceResponseBodyPerformanceKeysPerformanceItemPointsPerformanceItemValue] = None,
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
                temp_model = main_models.DescribeDBClusterPerformanceResponseBodyPerformanceKeysPerformanceItemPointsPerformanceItemValue()
                self.performance_item_value.append(temp_model.from_map(k1))

        return self

class DescribeDBClusterPerformanceResponseBodyPerformanceKeysPerformanceItemPointsPerformanceItemValue(DaraModel):
    def __init__(
        self,
        timestamp: int = None,
        value: str = None,
    ):
        # The timestamp of the metric. This value is a UNIX timestamp. Unit: millisecond.
        self.timestamp = timestamp
        # The value of the metric.
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

