# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20191111 import models as main_models
from darabonba.model import DaraModel

class DescribeSlowLogRecordsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        slow_log_records: main_models.DescribeSlowLogRecordsResponseBodySlowLogRecords = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details about the slow query logs.
        self.slow_log_records = slow_log_records

    def validate(self):
        if self.slow_log_records:
            self.slow_log_records.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.slow_log_records is not None:
            result['SlowLogRecords'] = self.slow_log_records.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SlowLogRecords') is not None:
            temp_model = main_models.DescribeSlowLogRecordsResponseBodySlowLogRecords()
            self.slow_log_records = temp_model.from_map(m.get('SlowLogRecords'))

        return self

class DescribeSlowLogRecordsResponseBodySlowLogRecords(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeSlowLogRecordsResponseBodySlowLogRecordsData = None,
        rows: str = None,
        rows_before_limit_at_least: str = None,
        statistics: main_models.DescribeSlowLogRecordsResponseBodySlowLogRecordsStatistics = None,
        table_schema: main_models.DescribeSlowLogRecordsResponseBodySlowLogRecordsTableSchema = None,
    ):
        # Details about the slow query logs.
        self.data = data
        # The number of rows in the result set.
        self.rows = rows
        # The number of entries per page.
        self.rows_before_limit_at_least = rows_before_limit_at_least
        # The statistics of the results.
        self.statistics = statistics
        # The schema of the table in the database.
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
            temp_model = main_models.DescribeSlowLogRecordsResponseBodySlowLogRecordsData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Rows') is not None:
            self.rows = m.get('Rows')

        if m.get('RowsBeforeLimitAtLeast') is not None:
            self.rows_before_limit_at_least = m.get('RowsBeforeLimitAtLeast')

        if m.get('Statistics') is not None:
            temp_model = main_models.DescribeSlowLogRecordsResponseBodySlowLogRecordsStatistics()
            self.statistics = temp_model.from_map(m.get('Statistics'))

        if m.get('TableSchema') is not None:
            temp_model = main_models.DescribeSlowLogRecordsResponseBodySlowLogRecordsTableSchema()
            self.table_schema = temp_model.from_map(m.get('TableSchema'))

        return self

class DescribeSlowLogRecordsResponseBodySlowLogRecordsTableSchema(DaraModel):
    def __init__(
        self,
        result_set: List[main_models.DescribeSlowLogRecordsResponseBodySlowLogRecordsTableSchemaResultSet] = None,
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
                temp_model = main_models.DescribeSlowLogRecordsResponseBodySlowLogRecordsTableSchemaResultSet()
                self.result_set.append(temp_model.from_map(k1))

        return self

class DescribeSlowLogRecordsResponseBodySlowLogRecordsTableSchemaResultSet(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The name of the column.
        self.name = name
        # The type of the column.
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

class DescribeSlowLogRecordsResponseBodySlowLogRecordsStatistics(DaraModel):
    def __init__(
        self,
        bytes_read: int = None,
        elapsed_time: float = None,
        rows_read: int = None,
    ):
        # The total size of data that were read. Unit: bytes.
        self.bytes_read = bytes_read
        # The time consumed by the slow query. Unit: milliseconds.
        self.elapsed_time = elapsed_time
        # The total number of rows that were read.
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

class DescribeSlowLogRecordsResponseBodySlowLogRecordsData(DaraModel):
    def __init__(
        self,
        result_set: List[main_models.DescribeSlowLogRecordsResponseBodySlowLogRecordsDataResultSet] = None,
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
                temp_model = main_models.DescribeSlowLogRecordsResponseBodySlowLogRecordsDataResultSet()
                self.result_set.append(temp_model.from_map(k1))

        return self

class DescribeSlowLogRecordsResponseBodySlowLogRecordsDataResultSet(DaraModel):
    def __init__(
        self,
        initial_address: str = None,
        initial_query_id: str = None,
        initial_user: str = None,
        memory_usage: str = None,
        query: str = None,
        query_duration_ms: str = None,
        query_start_time: str = None,
        read_bytes: str = None,
        read_rows: str = None,
        result_bytes: str = None,
        type: str = None,
    ):
        # The IP address of the client that initiated the query.
        self.initial_address = initial_address
        # The query ID.
        self.initial_query_id = initial_query_id
        # The username that is used to initiate the query.
        self.initial_user = initial_user
        # The peak memory usage for the query. Unit: bytes.
        self.memory_usage = memory_usage
        # The statement that was executed in the query.
        self.query = query
        # The duration of the query. Unit: milliseconds.
        self.query_duration_ms = query_duration_ms
        # The beginning of the time range to query. The time is in the yyyy-MM-dd hh:mm:ss format. The time is displayed in UTC.
        self.query_start_time = query_start_time
        # The size of the data read by executing the statement. Unit: bytes.
        self.read_bytes = read_bytes
        # The number of rows read by executing the statement.
        self.read_rows = read_rows
        # The size of the result data. Unit: bytes.
        self.result_bytes = result_bytes
        # The query status. Valid values:
        # 
        # *   **QueryFinish**: The query is complete.
        # *   **Processing**: The query is running.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.initial_address is not None:
            result['InitialAddress'] = self.initial_address

        if self.initial_query_id is not None:
            result['InitialQueryId'] = self.initial_query_id

        if self.initial_user is not None:
            result['InitialUser'] = self.initial_user

        if self.memory_usage is not None:
            result['MemoryUsage'] = self.memory_usage

        if self.query is not None:
            result['Query'] = self.query

        if self.query_duration_ms is not None:
            result['QueryDurationMs'] = self.query_duration_ms

        if self.query_start_time is not None:
            result['QueryStartTime'] = self.query_start_time

        if self.read_bytes is not None:
            result['ReadBytes'] = self.read_bytes

        if self.read_rows is not None:
            result['ReadRows'] = self.read_rows

        if self.result_bytes is not None:
            result['ResultBytes'] = self.result_bytes

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InitialAddress') is not None:
            self.initial_address = m.get('InitialAddress')

        if m.get('InitialQueryId') is not None:
            self.initial_query_id = m.get('InitialQueryId')

        if m.get('InitialUser') is not None:
            self.initial_user = m.get('InitialUser')

        if m.get('MemoryUsage') is not None:
            self.memory_usage = m.get('MemoryUsage')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('QueryDurationMs') is not None:
            self.query_duration_ms = m.get('QueryDurationMs')

        if m.get('QueryStartTime') is not None:
            self.query_start_time = m.get('QueryStartTime')

        if m.get('ReadBytes') is not None:
            self.read_bytes = m.get('ReadBytes')

        if m.get('ReadRows') is not None:
            self.read_rows = m.get('ReadRows')

        if m.get('ResultBytes') is not None:
            self.result_bytes = m.get('ResultBytes')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

