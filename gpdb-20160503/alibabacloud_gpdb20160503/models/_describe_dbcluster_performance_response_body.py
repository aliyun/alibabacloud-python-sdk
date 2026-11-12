# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterPerformanceResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        performance_keys: List[main_models.DescribeDBClusterPerformanceResponseBodyPerformanceKeys] = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The instance ID.
        self.dbcluster_id = dbcluster_id
        # The end time of the query in UTC. Specify the time in the `YYYY-MM-DDTHH:mmZ` format.
        self.end_time = end_time
        # The list of performance metric values for the instance.
        self.performance_keys = performance_keys
        # The request ID.
        self.request_id = request_id
        # The start time of the query in UTC. Specify the time in the `YYYY-MM-DDTHH:mmZ` format.
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
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.performance_keys = []
        if m.get('PerformanceKeys') is not None:
            for k1 in m.get('PerformanceKeys'):
                temp_model = main_models.DescribeDBClusterPerformanceResponseBodyPerformanceKeys()
                self.performance_keys.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeDBClusterPerformanceResponseBodyPerformanceKeys(DaraModel):
    def __init__(
        self,
        name: str = None,
        series: List[main_models.DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeries] = None,
        unit: str = None,
    ):
        # The name of the performance metric. For more information, see [Performance metric table](https://help.aliyun.com/document_detail/86943.html).
        self.name = name
        # The collection of performance metrics.
        self.series = series
        # The unit of the monitoring metrics.
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
        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.series = []
        if m.get('Series') is not None:
            for k1 in m.get('Series'):
                temp_model = main_models.DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeries()
                self.series.append(temp_model.from_map(k1))

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

class DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeries(DaraModel):
    def __init__(
        self,
        name: str = None,
        role: str = None,
        values: List[main_models.DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeriesValues] = None,
    ):
        # The name of the compute node or compute group.
        self.name = name
        # The role of the node. Valid values:
        # 
        # - **master**: Master node.
        # - **standby**: Standby node.
        # - **segment**: Compute node.
        self.role = role
        # The performance metric values. Each value corresponds to a collection time point.
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

        if self.role is not None:
            result['Role'] = self.role

        result['Values'] = []
        if self.values is not None:
            for k1 in self.values:
                result['Values'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        self.values = []
        if m.get('Values') is not None:
            for k1 in m.get('Values'):
                temp_model = main_models.DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeriesValues()
                self.values.append(temp_model.from_map(k1))

        return self

class DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeriesValues(DaraModel):
    def __init__(
        self,
        point: List[str] = None,
    ):
        # The performance metric value.
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

