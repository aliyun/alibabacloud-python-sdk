# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20191111 import models as main_models
from darabonba.model import DaraModel

class DescribeProcessListResponseBody(DaraModel):
    def __init__(
        self,
        process_list: main_models.DescribeProcessListResponseBodyProcessList = None,
        request_id: str = None,
    ):
        # The queries.
        self.process_list = process_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.process_list:
            self.process_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.process_list is not None:
            result['ProcessList'] = self.process_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProcessList') is not None:
            temp_model = main_models.DescribeProcessListResponseBodyProcessList()
            self.process_list = temp_model.from_map(m.get('ProcessList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeProcessListResponseBodyProcessList(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeProcessListResponseBodyProcessListData = None,
        rows: str = None,
        rows_before_limit_at_least: str = None,
        statistics: main_models.DescribeProcessListResponseBodyProcessListStatistics = None,
        table_schema: main_models.DescribeProcessListResponseBodyProcessListTableSchema = None,
    ):
        # The details of the query.
        self.data = data
        # The number of rows returned for the query.
        self.rows = rows
        # The number of entries returned per page.
        self.rows_before_limit_at_least = rows_before_limit_at_least
        # The statistics of the results.
        self.statistics = statistics
        # Details of the columns.
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
            temp_model = main_models.DescribeProcessListResponseBodyProcessListData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Rows') is not None:
            self.rows = m.get('Rows')

        if m.get('RowsBeforeLimitAtLeast') is not None:
            self.rows_before_limit_at_least = m.get('RowsBeforeLimitAtLeast')

        if m.get('Statistics') is not None:
            temp_model = main_models.DescribeProcessListResponseBodyProcessListStatistics()
            self.statistics = temp_model.from_map(m.get('Statistics'))

        if m.get('TableSchema') is not None:
            temp_model = main_models.DescribeProcessListResponseBodyProcessListTableSchema()
            self.table_schema = temp_model.from_map(m.get('TableSchema'))

        return self

class DescribeProcessListResponseBodyProcessListTableSchema(DaraModel):
    def __init__(
        self,
        result_set: List[main_models.DescribeProcessListResponseBodyProcessListTableSchemaResultSet] = None,
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
                temp_model = main_models.DescribeProcessListResponseBodyProcessListTableSchemaResultSet()
                self.result_set.append(temp_model.from_map(k1))

        return self

class DescribeProcessListResponseBodyProcessListTableSchemaResultSet(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The column name.
        self.name = name
        # The column type.
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

class DescribeProcessListResponseBodyProcessListStatistics(DaraModel):
    def __init__(
        self,
        bytes_read: int = None,
        elapsed_time: float = None,
        rows_read: int = None,
    ):
        # The size of the data that was scanned. Unit: bytes.
        self.bytes_read = bytes_read
        # The average response time.
        self.elapsed_time = elapsed_time
        # The number of scanned rows.
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

class DescribeProcessListResponseBodyProcessListData(DaraModel):
    def __init__(
        self,
        result_set: List[main_models.DescribeProcessListResponseBodyProcessListDataResultSet] = None,
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
                temp_model = main_models.DescribeProcessListResponseBodyProcessListDataResultSet()
                self.result_set.append(temp_model.from_map(k1))

        return self

class DescribeProcessListResponseBodyProcessListDataResultSet(DaraModel):
    def __init__(
        self,
        initial_address: str = None,
        initial_query_id: str = None,
        initial_user: str = None,
        query: str = None,
        query_duration_ms: str = None,
        query_start_time: str = None,
    ):
        # The IP address of the client that initiates the query.
        self.initial_address = initial_address
        # The query ID.
        self.initial_query_id = initial_query_id
        # The database account.
        self.initial_user = initial_user
        # The SQL statement that is executed in the query.
        self.query = query
        # The execution duration of the query. Unit: milliseconds.
        self.query_duration_ms = query_duration_ms
        # The beginning of the time range to query. The value is in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in Coordinated Universal Time (UTC).
        self.query_start_time = query_start_time

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

        if self.query is not None:
            result['Query'] = self.query

        if self.query_duration_ms is not None:
            result['QueryDurationMs'] = self.query_duration_ms

        if self.query_start_time is not None:
            result['QueryStartTime'] = self.query_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InitialAddress') is not None:
            self.initial_address = m.get('InitialAddress')

        if m.get('InitialQueryId') is not None:
            self.initial_query_id = m.get('InitialQueryId')

        if m.get('InitialUser') is not None:
            self.initial_user = m.get('InitialUser')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('QueryDurationMs') is not None:
            self.query_duration_ms = m.get('QueryDurationMs')

        if m.get('QueryStartTime') is not None:
            self.query_start_time = m.get('QueryStartTime')

        return self

