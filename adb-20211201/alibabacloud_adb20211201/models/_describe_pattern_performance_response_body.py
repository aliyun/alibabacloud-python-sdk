# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribePatternPerformanceResponseBody(DaraModel):
    def __init__(
        self,
        access_ip: str = None,
        end_time: str = None,
        failed_count: int = None,
        performances: List[main_models.DescribePatternPerformanceResponseBodyPerformances] = None,
        query_count: int = None,
        request_id: str = None,
        sqlpattern: str = None,
        start_time: str = None,
        tables: str = None,
        user: str = None,
    ):
        # The client IP address that submitted the queries that match the sql pattern.
        self.access_ip = access_ip
        # The end of the query time range. The time is in UTC and is formatted as *yyyy-MM-ddTHH:mmZ*.
        self.end_time = end_time
        # The number of failed executions for the sql pattern within the query time range.
        self.failed_count = failed_count
        # The performance metrics.
        self.performances = performances
        # The number of executions for the sql pattern within the query time range.
        self.query_count = query_count
        # The request ID.
        self.request_id = request_id
        # The SQL statement for the sql pattern.
        self.sqlpattern = sqlpattern
        # The start of the query time range. The time is in UTC and is formatted as *yyyy-MM-ddTHH:mmZ*.
        self.start_time = start_time
        # The tables queried by the sql pattern.
        self.tables = tables
        # The database account that executes the SQL statements.
        self.user = user

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
        if self.access_ip is not None:
            result['AccessIp'] = self.access_ip

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        result['Performances'] = []
        if self.performances is not None:
            for k1 in self.performances:
                result['Performances'].append(k1.to_map() if k1 else None)

        if self.query_count is not None:
            result['QueryCount'] = self.query_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sqlpattern is not None:
            result['SQLPattern'] = self.sqlpattern

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.tables is not None:
            result['Tables'] = self.tables

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessIp') is not None:
            self.access_ip = m.get('AccessIp')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        self.performances = []
        if m.get('Performances') is not None:
            for k1 in m.get('Performances'):
                temp_model = main_models.DescribePatternPerformanceResponseBodyPerformances()
                self.performances.append(temp_model.from_map(k1))

        if m.get('QueryCount') is not None:
            self.query_count = m.get('QueryCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SQLPattern') is not None:
            self.sqlpattern = m.get('SQLPattern')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Tables') is not None:
            self.tables = m.get('Tables')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

class DescribePatternPerformanceResponseBodyPerformances(DaraModel):
    def __init__(
        self,
        key: str = None,
        series: List[main_models.DescribePatternPerformanceResponseBodyPerformancesSeries] = None,
        unit: str = None,
    ):
        # The performance metric. Valid values:
        # 
        # - **AnalyticDB_PatternQueryCount**: The total number of queries that match the sql pattern.
        # 
        # - **AnalyticDB_PatternQueryTime**: The total time for queries that match the sql pattern.
        # 
        # - **AnalyticDB_PatternExecutionTime**: The total execution time of queries that match the sql pattern.
        # 
        # - **AnalyticDB_PatternPeakMemory**: The peak memory usage of queries that match the sql pattern.
        # 
        # - **AnalyticDB_PatternScanSize**: The total data scan size of queries that match the sql pattern.
        self.key = key
        # The time series data for the performance metric.
        self.series = series
        # The unit of the performance metric. The returned unit varies based on the value of `Key`:
        # 
        # - If `Key` is `AnalyticDB_PatternQueryTime` or `AnalyticDB_PatternExecutionTime`, the unit is **ms**.
        # 
        # - If `Key` is `AnalyticDB_PatternPeakMemory`, the unit is **MB**.
        # 
        # - If `Key` is `AnalyticDB_PatternScanSize`, the unit is **MB**.
        # 
        # - If `Key` is `AnalyticDB_PatternQueryCount`, this parameter is empty.
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
                temp_model = main_models.DescribePatternPerformanceResponseBodyPerformancesSeries()
                self.series.append(temp_model.from_map(k1))

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

class DescribePatternPerformanceResponseBodyPerformancesSeries(DaraModel):
    def __init__(
        self,
        name: str = None,
        values: List[str] = None,
    ):
        # The name of the performance value. The value of this parameter varies based on the value of `Key`:
        # 
        # - If `Key` is `AnalyticDB_PatternQueryCount`, this parameter returns `pattern_query_count`, which indicates the query count for the sql pattern.
        # 
        # - If `Key` is `AnalyticDB_PatternQueryTime`, this parameter can be one of the following values:
        # 
        #   - `average_query_time`: the average total time of queries that match the sql pattern.
        # 
        #   - `max_query_time`: the maximum total time of queries that match the sql pattern.
        # 
        # - If `Key` is `AnalyticDB_PatternExecutionTime`, this parameter can be one of the following values:
        # 
        #   - `average_execution_time`: the average execution time of queries that match the sql pattern.
        # 
        #   - `max_execution_time`: the maximum execution time of queries that match the sql pattern.
        # 
        # - If `Key` is `AnalyticDB_PatternPeakMemory`, this parameter can be one of the following values:
        # 
        #   - `average_peak_memory`: the average peak memory usage of queries that match the sql pattern.
        # 
        #   - `max_peak_memory`: the maximum peak memory usage of queries that match the sql pattern.
        # 
        # - If `Key` is `AnalyticDB_PatternScanSize`, this parameter can be one of the following values:
        # 
        #   - `average_scan_size`: the average data scan size of queries that match the sql pattern.
        # 
        #   - `max_scan_size`: the maximum data scan size of queries that match the sql pattern.
        self.name = name
        # The list of performance values.
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

