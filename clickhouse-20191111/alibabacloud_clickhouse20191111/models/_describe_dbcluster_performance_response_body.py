# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20191111 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterPerformanceResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        performances: List[main_models.DescribeDBClusterPerformanceResponseBodyPerformances] = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The end of the time range to query. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in Coordinated Universal Time (UTC).
        self.end_time = end_time
        # The values of the queried performance metrics of the cluster.
        self.performances = performances
        # The request ID.
        self.request_id = request_id
        # The beginning of the time range to query. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC.
        self.start_time = start_time

    def validate(self):
        if self.performances:
            for v1 in self.performances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['Performances'] = []
        if self.performances is not None:
            for k1 in self.performances:
                result['Performances'].append(k1.to_map() if k1 else None)

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

        self.performances = []
        if m.get('Performances') is not None:
            for k1 in m.get('Performances'):
                temp_model = main_models.DescribeDBClusterPerformanceResponseBodyPerformances()
                self.performances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeDBClusterPerformanceResponseBodyPerformances(DaraModel):
    def __init__(
        self,
        key: str = None,
        name: str = None,
        series: List[main_models.DescribeDBClusterPerformanceResponseBodyPerformancesSeries] = None,
        unit: str = None,
    ):
        # The name of the performance metric.
        self.key = key
        # The name of the performance metric value.
        self.name = name
        # The queried performance pamaters.
        self.series = series
        # The unit of the performance metric.
        self.unit = unit

    def validate(self):
        if self.series:
            for v1 in self.series:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.name is not None:
            result['Name'] = self.name

        result['Series'] = []
        if self.series is not None:
            for k1 in self.series:
                result['Series'].append(k1.to_map() if k1 else None)

        if self.unit is not None:
            result['Unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.series = []
        if m.get('Series') is not None:
            for k1 in m.get('Series'):
                temp_model = main_models.DescribeDBClusterPerformanceResponseBodyPerformancesSeries()
                self.series.append(temp_model.from_map(k1))

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

class DescribeDBClusterPerformanceResponseBodyPerformancesSeries(DaraModel):
    def __init__(
        self,
        name: str = None,
        values: List[main_models.DescribeDBClusterPerformanceResponseBodyPerformancesSeriesValues] = None,
    ):
        # The name of the list of performance metric values.
        self.name = name
        # The values of the performance parameter. Each value of the performance parameter is collected at a point in time.
        self.values = values

    def validate(self):
        if self.values:
            for v1 in self.values:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        result['Values'] = []
        if self.values is not None:
            for k1 in self.values:
                result['Values'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.values = []
        if m.get('Values') is not None:
            for k1 in m.get('Values'):
                temp_model = main_models.DescribeDBClusterPerformanceResponseBodyPerformancesSeriesValues()
                self.values.append(temp_model.from_map(k1))

        return self

class DescribeDBClusterPerformanceResponseBodyPerformancesSeriesValues(DaraModel):
    def __init__(
        self,
        point: List[str] = None,
    ):
        # The values of a metric.
        self.point = point

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.point is not None:
            result['Point'] = self.point

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Point') is not None:
            self.point = m.get('Point')

        return self

