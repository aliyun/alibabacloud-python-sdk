# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class DescribeSlowLogRecordsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeSlowLogRecordsResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeSlowLogRecordsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSlowLogRecordsResponseBodyData(DaraModel):
    def __init__(
        self,
        dbinstance_id: int = None,
        dbinstance_name: str = None,
        result_set: List[main_models.DescribeSlowLogRecordsResponseBodyDataResultSet] = None,
        total_count: int = None,
    ):
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # The cluster name.
        self.dbinstance_name = dbinstance_name
        # The result sets.
        self.result_set = result_set
        # The total number of entries returned.
        self.total_count = total_count

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
        if self.dbinstance_id is not None:
            result['DBInstanceID'] = self.dbinstance_id

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        result['ResultSet'] = []
        if self.result_set is not None:
            for k1 in self.result_set:
                result['ResultSet'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceID') is not None:
            self.dbinstance_id = m.get('DBInstanceID')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        self.result_set = []
        if m.get('ResultSet') is not None:
            for k1 in m.get('ResultSet'):
                temp_model = main_models.DescribeSlowLogRecordsResponseBodyDataResultSet()
                self.result_set.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSlowLogRecordsResponseBodyDataResultSet(DaraModel):
    def __init__(
        self,
        initial_address: str = None,
        initial_query_id: str = None,
        initial_user: str = None,
        memory_usage: int = None,
        query: str = None,
        query_duration_ms: int = None,
        query_start_time: str = None,
        read_bytes: int = None,
        read_rows: int = None,
        result_bytes: int = None,
        type: str = None,
    ):
        # The address to which the query statement is sent.
        self.initial_address = initial_address
        # The query ID.
        self.initial_query_id = initial_query_id
        # The user who executes the query statement.
        self.initial_user = initial_user
        # The peak memory usage for the query. Unit: bytes.
        self.memory_usage = memory_usage
        # The query statement that is running.
        self.query = query
        # The execution duration of slow SQL queries. Minimum value: **1000**. Unit: milliseconds.
        self.query_duration_ms = query_duration_ms
        # The beginning of the time range to query. The time is in the yyyy-MM-dd hh:mm:ss format. The time is displayed in UTC.
        self.query_start_time = query_start_time
        # The size of the data that is scanned. Unit: bytes.
        self.read_bytes = read_bytes
        # The number of read rows.
        self.read_rows = read_rows
        # The size of the result data. Unit: bytes.
        self.result_bytes = result_bytes
        # The type of the slow query logs.
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

