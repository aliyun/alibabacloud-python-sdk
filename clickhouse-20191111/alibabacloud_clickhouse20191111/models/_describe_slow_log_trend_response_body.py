# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20191111 import models as main_models
from darabonba.model import DaraModel

class DescribeSlowLogTrendResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        slow_log_trend: main_models.DescribeSlowLogTrendResponseBodySlowLogTrend = None,
    ):
        self.request_id = request_id
        self.slow_log_trend = slow_log_trend

    def validate(self):
        if self.slow_log_trend:
            self.slow_log_trend.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.slow_log_trend is not None:
            result['SlowLogTrend'] = self.slow_log_trend.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SlowLogTrend') is not None:
            temp_model = main_models.DescribeSlowLogTrendResponseBodySlowLogTrend()
            self.slow_log_trend = temp_model.from_map(m.get('SlowLogTrend'))

        return self

class DescribeSlowLogTrendResponseBodySlowLogTrend(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeSlowLogTrendResponseBodySlowLogTrendData = None,
        rows: str = None,
        rows_before_limit_at_least: str = None,
        statistics: main_models.DescribeSlowLogTrendResponseBodySlowLogTrendStatistics = None,
        table_schema: main_models.DescribeSlowLogTrendResponseBodySlowLogTrendTableSchema = None,
    ):
        self.data = data
        self.rows = rows
        self.rows_before_limit_at_least = rows_before_limit_at_least
        self.statistics = statistics
        self.table_schema = table_schema

    def validate(self):
        if self.data:
            self.data.validate()
        if self.statistics:
            self.statistics.validate()
        if self.table_schema:
            self.table_schema.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.rows is not None:
            result['Rows'] = self.rows

        if self.rows_before_limit_at_least is not None:
            result['RowsBeforeLimitAtLeast'] = self.rows_before_limit_at_least

        if self.statistics is not None:
            result['Statistics'] = self.statistics.to_map()

        if self.table_schema is not None:
            result['TableSchema'] = self.table_schema.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeSlowLogTrendResponseBodySlowLogTrendData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Rows') is not None:
            self.rows = m.get('Rows')

        if m.get('RowsBeforeLimitAtLeast') is not None:
            self.rows_before_limit_at_least = m.get('RowsBeforeLimitAtLeast')

        if m.get('Statistics') is not None:
            temp_model = main_models.DescribeSlowLogTrendResponseBodySlowLogTrendStatistics()
            self.statistics = temp_model.from_map(m.get('Statistics'))

        if m.get('TableSchema') is not None:
            temp_model = main_models.DescribeSlowLogTrendResponseBodySlowLogTrendTableSchema()
            self.table_schema = temp_model.from_map(m.get('TableSchema'))

        return self

class DescribeSlowLogTrendResponseBodySlowLogTrendTableSchema(DaraModel):
    def __init__(
        self,
        result_set: List[main_models.DescribeSlowLogTrendResponseBodySlowLogTrendTableSchemaResultSet] = None,
    ):
        self.result_set = result_set

    def validate(self):
        if self.result_set:
            for v1 in self.result_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ResultSet'] = []
        if self.result_set is not None:
            for k1 in self.result_set:
                result['ResultSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result_set = []
        if m.get('ResultSet') is not None:
            for k1 in m.get('ResultSet'):
                temp_model = main_models.DescribeSlowLogTrendResponseBodySlowLogTrendTableSchemaResultSet()
                self.result_set.append(temp_model.from_map(k1))

        return self

class DescribeSlowLogTrendResponseBodySlowLogTrendTableSchemaResultSet(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeSlowLogTrendResponseBodySlowLogTrendStatistics(DaraModel):
    def __init__(
        self,
        bytes_read: int = None,
        elapsed_time: float = None,
        rows_read: int = None,
    ):
        self.bytes_read = bytes_read
        self.elapsed_time = elapsed_time
        self.rows_read = rows_read

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bytes_read is not None:
            result['BytesRead'] = self.bytes_read

        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time

        if self.rows_read is not None:
            result['RowsRead'] = self.rows_read

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BytesRead') is not None:
            self.bytes_read = m.get('BytesRead')

        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')

        if m.get('RowsRead') is not None:
            self.rows_read = m.get('RowsRead')

        return self

class DescribeSlowLogTrendResponseBodySlowLogTrendData(DaraModel):
    def __init__(
        self,
        result_set: List[main_models.DescribeSlowLogTrendResponseBodySlowLogTrendDataResultSet] = None,
    ):
        self.result_set = result_set

    def validate(self):
        if self.result_set:
            for v1 in self.result_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ResultSet'] = []
        if self.result_set is not None:
            for k1 in self.result_set:
                result['ResultSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result_set = []
        if m.get('ResultSet') is not None:
            for k1 in m.get('ResultSet'):
                temp_model = main_models.DescribeSlowLogTrendResponseBodySlowLogTrendDataResultSet()
                self.result_set.append(temp_model.from_map(k1))

        return self

class DescribeSlowLogTrendResponseBodySlowLogTrendDataResultSet(DaraModel):
    def __init__(
        self,
        avg_query_duration_ms: str = None,
        count: str = None,
        max_query_duration_ms: str = None,
        min_query_duration_ms: str = None,
        query_start_time: str = None,
    ):
        self.avg_query_duration_ms = avg_query_duration_ms
        self.count = count
        self.max_query_duration_ms = max_query_duration_ms
        self.min_query_duration_ms = min_query_duration_ms
        self.query_start_time = query_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_query_duration_ms is not None:
            result['AvgQueryDurationMs'] = self.avg_query_duration_ms

        if self.count is not None:
            result['Count'] = self.count

        if self.max_query_duration_ms is not None:
            result['MaxQueryDurationMs'] = self.max_query_duration_ms

        if self.min_query_duration_ms is not None:
            result['MinQueryDurationMs'] = self.min_query_duration_ms

        if self.query_start_time is not None:
            result['QueryStartTime'] = self.query_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgQueryDurationMs') is not None:
            self.avg_query_duration_ms = m.get('AvgQueryDurationMs')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('MaxQueryDurationMs') is not None:
            self.max_query_duration_ms = m.get('MaxQueryDurationMs')

        if m.get('MinQueryDurationMs') is not None:
            self.min_query_duration_ms = m.get('MinQueryDurationMs')

        if m.get('QueryStartTime') is not None:
            self.query_start_time = m.get('QueryStartTime')

        return self

