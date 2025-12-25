# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeSlowLogRecordsResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        engine: str = None,
        items: main_models.DescribeSlowLogRecordsResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The type of the database engine.
        self.engine = engine
        # An array that consists of the information about each slow log.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of SQL log reports on the current page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeSlowLogRecordsResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeSlowLogRecordsResponseBodyItems(DaraModel):
    def __init__(
        self,
        sqlslow_record: List[main_models.DescribeSlowLogRecordsResponseBodyItemsSQLSlowRecord] = None,
    ):
        self.sqlslow_record = sqlslow_record

    def validate(self):
        if self.sqlslow_record:
            for v1 in self.sqlslow_record:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SQLSlowRecord'] = []
        if self.sqlslow_record is not None:
            for k1 in self.sqlslow_record:
                result['SQLSlowRecord'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sqlslow_record = []
        if m.get('SQLSlowRecord') is not None:
            for k1 in m.get('SQLSlowRecord'):
                temp_model = main_models.DescribeSlowLogRecordsResponseBodyItemsSQLSlowRecord()
                self.sqlslow_record.append(temp_model.from_map(k1))

        return self

class DescribeSlowLogRecordsResponseBodyItemsSQLSlowRecord(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        client_host_name: str = None,
        cpu_time: int = None,
        dbname: str = None,
        execution_start_time: str = None,
        host_address: str = None,
        last_rows_affected_count: int = None,
        lock_times: int = None,
        logical_ioread: int = None,
        parse_row_counts: int = None,
        physical_ioread: int = None,
        query_time_ms: int = None,
        query_times: int = None,
        return_row_counts: int = None,
        rows_affected_count: int = None,
        sqlhash: str = None,
        sqltext: str = None,
        user_name: str = None,
        write_iocount: int = None,
    ):
        # The name of the application that is connected to the instance.
        # 
        # > This parameter is returned only for instances that run SQL Server.
        self.application_name = application_name
        # The hostname of the client.
        # 
        # > This parameter is returned only for instances that run SQL Server.
        self.client_host_name = client_host_name
        # The duration during which the SQL statement is processed by the CPU. Unit: milliseconds.
        # 
        # > This parameter is returned only for instances that run SQL Server.
        self.cpu_time = cpu_time
        # The name of the database.
        self.dbname = dbname
        # The time when the execution of the SQL statement started. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.execution_start_time = execution_start_time
        # The name and IP address of the client that is connected to the database.
        self.host_address = host_address
        # The number of rows that are affected by the last SQL statement.
        # 
        # > This parameter is returned only for instances that run SQL Server.
        self.last_rows_affected_count = last_rows_affected_count
        # The lock duration of the query. Unit: seconds.
        self.lock_times = lock_times
        # The number of logical reads.
        # 
        # > This parameter is returned only for instances that run SQL Server.
        self.logical_ioread = logical_ioread
        # The number of parsed rows.
        self.parse_row_counts = parse_row_counts
        # The number of physical reads.
        # 
        # > This parameter is returned only for instances that run SQL Server.
        self.physical_ioread = physical_ioread
        # The execution duration of the query. Unit: milliseconds.
        self.query_time_ms = query_time_ms
        # The execution duration of the query. Unit: seconds.
        self.query_times = query_times
        # The number of rows returned.
        self.return_row_counts = return_row_counts
        # The number of affected rows.
        # 
        # > This parameter is returned only for instances that run SQL Server.
        self.rows_affected_count = rows_affected_count
        # The unique ID of the SQL statement.
        self.sqlhash = sqlhash
        # The details of the SQL statement.
        self.sqltext = sqltext
        # The name of the user.
        # 
        # > This parameter is returned only for instances that run SQL Server.
        self.user_name = user_name
        # The number of I/O writes.
        # 
        # > This parameter is returned only for instances that run SQL Server.
        self.write_iocount = write_iocount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.client_host_name is not None:
            result['ClientHostName'] = self.client_host_name

        if self.cpu_time is not None:
            result['CpuTime'] = self.cpu_time

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.execution_start_time is not None:
            result['ExecutionStartTime'] = self.execution_start_time

        if self.host_address is not None:
            result['HostAddress'] = self.host_address

        if self.last_rows_affected_count is not None:
            result['LastRowsAffectedCount'] = self.last_rows_affected_count

        if self.lock_times is not None:
            result['LockTimes'] = self.lock_times

        if self.logical_ioread is not None:
            result['LogicalIORead'] = self.logical_ioread

        if self.parse_row_counts is not None:
            result['ParseRowCounts'] = self.parse_row_counts

        if self.physical_ioread is not None:
            result['PhysicalIORead'] = self.physical_ioread

        if self.query_time_ms is not None:
            result['QueryTimeMS'] = self.query_time_ms

        if self.query_times is not None:
            result['QueryTimes'] = self.query_times

        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts

        if self.rows_affected_count is not None:
            result['RowsAffectedCount'] = self.rows_affected_count

        if self.sqlhash is not None:
            result['SQLHash'] = self.sqlhash

        if self.sqltext is not None:
            result['SQLText'] = self.sqltext

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.write_iocount is not None:
            result['WriteIOCount'] = self.write_iocount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ClientHostName') is not None:
            self.client_host_name = m.get('ClientHostName')

        if m.get('CpuTime') is not None:
            self.cpu_time = m.get('CpuTime')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('ExecutionStartTime') is not None:
            self.execution_start_time = m.get('ExecutionStartTime')

        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')

        if m.get('LastRowsAffectedCount') is not None:
            self.last_rows_affected_count = m.get('LastRowsAffectedCount')

        if m.get('LockTimes') is not None:
            self.lock_times = m.get('LockTimes')

        if m.get('LogicalIORead') is not None:
            self.logical_ioread = m.get('LogicalIORead')

        if m.get('ParseRowCounts') is not None:
            self.parse_row_counts = m.get('ParseRowCounts')

        if m.get('PhysicalIORead') is not None:
            self.physical_ioread = m.get('PhysicalIORead')

        if m.get('QueryTimeMS') is not None:
            self.query_time_ms = m.get('QueryTimeMS')

        if m.get('QueryTimes') is not None:
            self.query_times = m.get('QueryTimes')

        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')

        if m.get('RowsAffectedCount') is not None:
            self.rows_affected_count = m.get('RowsAffectedCount')

        if m.get('SQLHash') is not None:
            self.sqlhash = m.get('SQLHash')

        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('WriteIOCount') is not None:
            self.write_iocount = m.get('WriteIOCount')

        return self

