# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterResourcePoolPerformanceResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        performances: List[main_models.DescribeDBClusterResourcePoolPerformanceResponseBodyPerformances] = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The end of the time range for monitoring the resource group. The time follows the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time is displayed in UTC.
        self.end_time = end_time
        # The queried monitoring information about the metrics.
        self.performances = performances
        # The request ID.
        self.request_id = request_id
        # The beginning of the time range for monitoring the resource group. The time follows the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time is displayed in UTC.
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
                temp_model = main_models.DescribeDBClusterResourcePoolPerformanceResponseBodyPerformances()
                self.performances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeDBClusterResourcePoolPerformanceResponseBodyPerformances(DaraModel):
    def __init__(
        self,
        key: str = None,
        resource_pool_performances: List[main_models.DescribeDBClusterResourcePoolPerformanceResponseBodyPerformancesResourcePoolPerformances] = None,
        unit: str = None,
    ):
        # The metric of the resource group.
        self.key = key
        # The queried monitoring information about the resource groups.
        self.resource_pool_performances = resource_pool_performances
        # The unit of the metric value.
        self.unit = unit

    def validate(self):
        if self.resource_pool_performances:
            for v1 in self.resource_pool_performances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        result['ResourcePoolPerformances'] = []
        if self.resource_pool_performances is not None:
            for k1 in self.resource_pool_performances:
                result['ResourcePoolPerformances'].append(k1.to_map() if k1 else None)

        if self.unit is not None:
            result['Unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        self.resource_pool_performances = []
        if m.get('ResourcePoolPerformances') is not None:
            for k1 in m.get('ResourcePoolPerformances'):
                temp_model = main_models.DescribeDBClusterResourcePoolPerformanceResponseBodyPerformancesResourcePoolPerformances()
                self.resource_pool_performances.append(temp_model.from_map(k1))

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

class DescribeDBClusterResourcePoolPerformanceResponseBodyPerformancesResourcePoolPerformances(DaraModel):
    def __init__(
        self,
        resource_pool_name: str = None,
        resource_pool_series: List[main_models.DescribeDBClusterResourcePoolPerformanceResponseBodyPerformancesResourcePoolPerformancesResourcePoolSeries] = None,
    ):
        # The name of the resource group.
        self.resource_pool_name = resource_pool_name
        # The sequential monitoring information about the resource groups.
        self.resource_pool_series = resource_pool_series

    def validate(self):
        if self.resource_pool_series:
            for v1 in self.resource_pool_series:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_pool_name is not None:
            result['ResourcePoolName'] = self.resource_pool_name

        result['ResourcePoolSeries'] = []
        if self.resource_pool_series is not None:
            for k1 in self.resource_pool_series:
                result['ResourcePoolSeries'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourcePoolName') is not None:
            self.resource_pool_name = m.get('ResourcePoolName')

        self.resource_pool_series = []
        if m.get('ResourcePoolSeries') is not None:
            for k1 in m.get('ResourcePoolSeries'):
                temp_model = main_models.DescribeDBClusterResourcePoolPerformanceResponseBodyPerformancesResourcePoolPerformancesResourcePoolSeries()
                self.resource_pool_series.append(temp_model.from_map(k1))

        return self

class DescribeDBClusterResourcePoolPerformanceResponseBodyPerformancesResourcePoolPerformancesResourcePoolSeries(DaraModel):
    def __init__(
        self,
        name: str = None,
        values: List[str] = None,
    ):
        # The name of the metric.
        self.name = name
        # The value of the metric.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

