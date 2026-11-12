# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class DescribeDatabaseSlowLogRecordsResponseBody(DaraModel):
    def __init__(
        self,
        engine: str = None,
        page_number: int = None,
        page_size: int = None,
        physical_ioread: int = None,
        request_id: str = None,
        slow_logs: List[main_models.DescribeDatabaseSlowLogRecordsResponseBodySlowLogs] = None,
        total_count: int = None,
    ):
        # The database engine.
        self.engine = engine
        # The page number of the returned page.
        # 
        # Starts from 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: 30 to 100.
        # 
        # Default value: 30.
        self.page_size = page_size
        # The number of logical reads.
        self.physical_ioread = physical_ioread
        # The request ID.
        self.request_id = request_id
        # The slow query logs.
        self.slow_logs = slow_logs
        # The total number of slow query logs.
        self.total_count = total_count

    def validate(self):
        if self.slow_logs:
            for v1 in self.slow_logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine is not None:
            result['Engine'] = self.engine

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.physical_ioread is not None:
            result['PhysicalIORead'] = self.physical_ioread

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SlowLogs'] = []
        if self.slow_logs is not None:
            for k1 in self.slow_logs:
                result['SlowLogs'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PhysicalIORead') is not None:
            self.physical_ioread = m.get('PhysicalIORead')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.slow_logs = []
        if m.get('SlowLogs') is not None:
            for k1 in m.get('SlowLogs'):
                temp_model = main_models.DescribeDatabaseSlowLogRecordsResponseBodySlowLogs()
                self.slow_logs.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDatabaseSlowLogRecordsResponseBodySlowLogs(DaraModel):
    def __init__(
        self,
        dbname: str = None,
        execution_start_time: str = None,
        host_address: str = None,
        lock_times: int = None,
        parse_row_counts: int = None,
        query_time_ms: int = None,
        query_times: int = None,
        return_row_counts: int = None,
        sqltext: str = None,
    ):
        # The database name.
        self.dbname = dbname
        # The start time of the execution. The time is displayed in UTC and is in the `yyyy-MM-ddTHH:mm:ssZ` format.
        # 
        # > The time displayed in the console is in the UTC+8 time zone, which is 8 hours later than the time in UTC.
        self.execution_start_time = execution_start_time
        # The IP address of the client that is used to connect to the database.
        self.host_address = host_address
        # The lock duration. Unit: seconds.
        self.lock_times = lock_times
        # The number of parsed rows.
        self.parse_row_counts = parse_row_counts
        # The execution duration. Unit: milliseconds.
        self.query_time_ms = query_time_ms
        # The execution duration. Unit: seconds.
        self.query_times = query_times
        # The number of returned rows.
        self.return_row_counts = return_row_counts
        # The details of the SQL statement.
        self.sqltext = sqltext

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.execution_start_time is not None:
            result['ExecutionStartTime'] = self.execution_start_time

        if self.host_address is not None:
            result['HostAddress'] = self.host_address

        if self.lock_times is not None:
            result['LockTimes'] = self.lock_times

        if self.parse_row_counts is not None:
            result['ParseRowCounts'] = self.parse_row_counts

        if self.query_time_ms is not None:
            result['QueryTimeMS'] = self.query_time_ms

        if self.query_times is not None:
            result['QueryTimes'] = self.query_times

        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts

        if self.sqltext is not None:
            result['SQLText'] = self.sqltext

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('ExecutionStartTime') is not None:
            self.execution_start_time = m.get('ExecutionStartTime')

        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')

        if m.get('LockTimes') is not None:
            self.lock_times = m.get('LockTimes')

        if m.get('ParseRowCounts') is not None:
            self.parse_row_counts = m.get('ParseRowCounts')

        if m.get('QueryTimeMS') is not None:
            self.query_time_ms = m.get('QueryTimeMS')

        if m.get('QueryTimes') is not None:
            self.query_times = m.get('QueryTimes')

        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')

        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')

        return self

