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
        self.access_ip = access_ip
        # The end time of the query. The time follows the ISO 8601 standard in the *yyyy-MM-ddTHH:mmZ* format. The time is displayed in UTC.
        self.end_time = end_time
        self.failed_count = failed_count
        # The queried performance metrics.
        self.performances = performances
        self.query_count = query_count
        # The request ID.
        self.request_id = request_id
        self.sqlpattern = sqlpattern
        # The start time of the query. The time follows the ISO 8601 standard in the *yyyy-MM-ddTHH:mmZ* format. The time is displayed in UTC.
        self.start_time = start_time
        self.tables = tables
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
        # The queried performance metric. Valid values:
        # 
        # *   **AnalyticDB_PatternQueryCount**: the total number of queries executed in association with the SQL pattern.
        # *   **AnalyticDB_PatternQueryTime**: the total amount of time consumed by the queries executed in association with the SQL pattern.
        # *   **AnalyticDB_PatternExecutionTime**: the execution duration of the queries executed in association with the SQL pattern.
        # *   **AnalyticDB_PatternPeakMemory**: the peak memory usage of the queries executed in association with the SQL pattern.
        # *   **AnalyticDB_PatternScanSize**: the amount of data scanned in the queries executed in association with the SQL pattern.
        self.key = key
        # The values of the performance metrics.
        self.series = series
        # The unit of the performance metric. Valid values:
        # 
        # *   If the performance metric is related to the query time (the value of `Key` is `AnalyticDB_PatternQueryTime` or `AnalyticDB_PatternExecutionTime`), **ms** is returned.
        # *   If the performance metric is related to the peak memory usage (the value of `Key` is `AnalyticDB_PatternPeakMemory`), **MB** is returned.
        # *   If the performance metric is related to the amount of data scanned (the value of `Key` is `AnalyticDB_PatternScanSize`), **MB** is returned.
        # *   If the performance metric is related to the number of queries (the value of `Key` is `AnalyticDB_PatternQueryCount`), null is returned.
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
        # The name of the performance metric value. Valid values:
        # 
        # *   If the value of `Key` is `AnalyticDB_PatternQueryCount`, `pattern_query_count` is returned, which indicates the number of executions of the SQL statements in association with the SQL pattern.
        # 
        # *   If the value of `Key` is `AnalyticDB_PatternQueryTime`, the following values are returned:
        # 
        #     *   `average_query_time`, which indicates the average total amount of time consumed by the SQL statements in association with the SQL pattern.
        #     *   `max_query_time`, which indicates the maximum total amount of time consumed by the SQL statements in association with the SQL pattern.
        # 
        # *   If the value of `Key` is `AnalyticDB_PatternExecutionTime`, the following values are returned:
        # 
        #     *   `average_execution_time`, which indicates the average execution duration of the SQL statements in association with the SQL pattern.
        #     *   `max_execution_time`, which indicates the maximum execution duration of the SQL statements in association with the SQL pattern.
        # 
        # *   If the value of `Key` is `AnalyticDB_PatternPeakMemory`, the following values are returned:
        # 
        #     *   `average_peak_memory`, which indicates the average peak memory usage of the SQL statements in association with the SQL pattern.
        #     *   `max_peak_memory`, which indicates the maximum peak memory usage of the SQL statements in association with the SQL pattern.
        # 
        # *   If the value of `Key` is `AnalyticDB_PatternScanSize`, the following values are returned:
        # 
        #     *   `average_scan_size`, which indicates the average amount of data scanned by the SQL statements in association with the SQL pattern.
        #     *   `max_scan_size`, which indicates the maximum amount of data scanned by the SQL statements in association with the SQL pattern.
        self.name = name
        # The values of the performance metric.
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

