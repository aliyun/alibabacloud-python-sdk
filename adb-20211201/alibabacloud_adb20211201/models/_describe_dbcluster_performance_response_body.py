# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
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
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/454250.html) operation to query the IDs of all AnalyticDB for MySQL Data Lakehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        # The end time of the query. The time follows the ISO 8601 standard in the *yyyy-MM-ddTHH:mmZ* format. The time is displayed in UTC.
        self.end_time = end_time
        # The queried performance metrics.
        self.performances = performances
        # The request ID.
        self.request_id = request_id
        # The start time of the query. The time follows the ISO 8601 standard in the *yyyy-MM-ddTHH:mmZ* format. The time is displayed in UTC.
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
        series: List[main_models.DescribeDBClusterPerformanceResponseBodyPerformancesSeries] = None,
        unit: str = None,
    ):
        # The name of the performance metric.
        self.key = key
        # The queried performance metric data.
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
        tags: str = None,
        translate_key: str = None,
        values: List[str] = None,
    ):
        # The name of the performance metric value. For more information about the performance metrics, see [Metric overview](https://help.aliyun.com/document_detail/2863211.html).
        self.name = name
        # The tags that are added to the cluster.
        self.tags = tags
        self.translate_key = translate_key
        # The values of the performance metric at different points in time.
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

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.translate_key is not None:
            result['TranslateKey'] = self.translate_key

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TranslateKey') is not None:
            self.translate_key = m.get('TranslateKey')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

