# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetFullRequestStatResultByInstanceIdResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetFullRequestStatResultByInstanceIdResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        # 
        # >  If the request was successful, **Successful** is returned. If the request failed, an error message that contains information such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetFullRequestStatResultByInstanceIdResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetFullRequestStatResultByInstanceIdResponseBodyData(DaraModel):
    def __init__(
        self,
        fail: bool = None,
        is_finish: bool = None,
        result: main_models.GetFullRequestStatResultByInstanceIdResponseBodyDataResult = None,
        result_id: str = None,
        state: str = None,
        timestamp: int = None,
    ):
        # Indicates whether the asynchronous request failed. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.fail = fail
        # Indicates whether the asynchronous request was complete. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_finish = is_finish
        # The returned full request data.
        self.result = result
        # The request ID.
        self.result_id = result_id
        # The state of the asynchronous request. Valid values:
        # 
        # *   **RUNNING**
        # *   **SUCCESS**
        # *   **FAIL**
        self.state = state
        # The time when the asynchronous request was sent. The value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.timestamp = timestamp

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail is not None:
            result['Fail'] = self.fail

        if self.is_finish is not None:
            result['IsFinish'] = self.is_finish

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.result_id is not None:
            result['ResultId'] = self.result_id

        if self.state is not None:
            result['State'] = self.state

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fail') is not None:
            self.fail = m.get('Fail')

        if m.get('IsFinish') is not None:
            self.is_finish = m.get('IsFinish')

        if m.get('Result') is not None:
            temp_model = main_models.GetFullRequestStatResultByInstanceIdResponseBodyDataResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('ResultId') is not None:
            self.result_id = m.get('ResultId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class GetFullRequestStatResultByInstanceIdResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        list: List[main_models.GetFullRequestStatResultByInstanceIdResponseBodyDataResultList] = None,
        total: int = None,
    ):
        # The full request data.
        self.list = list
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.GetFullRequestStatResultByInstanceIdResponseBodyDataResultList()
                self.list.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetFullRequestStatResultByInstanceIdResponseBodyDataResultList(DaraModel):
    def __init__(
        self,
        avg_examined_rows: float = None,
        avg_fetch_rows: int = None,
        avg_lock_wait_time: float = None,
        avg_logical_read: float = None,
        avg_physical_async_read: int = None,
        avg_physical_sync_read: int = None,
        avg_returned_rows: float = None,
        avg_rt: float = None,
        avg_sql_count: int = None,
        avg_updated_rows: int = None,
        count: int = None,
        count_rate: float = None,
        database: str = None,
        error_count: int = None,
        examined_rows: int = None,
        fetch_rows: int = None,
        ip: str = None,
        lock_wait_time: float = None,
        logical_read: int = None,
        physical_async_read: int = None,
        physical_sync_read: int = None,
        port: int = None,
        psql: str = None,
        rows: int = None,
        rt_greater_than_one_second_count: int = None,
        rt_rate: float = None,
        sql_count: int = None,
        sql_id: str = None,
        sum_updated_rows: int = None,
        tables: List[str] = None,
        version: int = None,
        vpc_id: str = None,
    ):
        # The average number of scanned rows.
        # 
        # > This parameter is returned only for ApsaraDB RDS for MySQL, ApsaraDB RDS for PostgreSQL, and PolarDB for MySQL databases.
        self.avg_examined_rows = avg_examined_rows
        # The average number of rows that are fetched by compute nodes from data nodes on the PolarDB-X 2.0 instance.
        self.avg_fetch_rows = avg_fetch_rows
        # The average lock wait latency. Unit: seconds.
        self.avg_lock_wait_time = avg_lock_wait_time
        # The average number of logical reads.
        self.avg_logical_read = avg_logical_read
        # The average number of physical asynchronous reads.
        self.avg_physical_async_read = avg_physical_async_read
        # The average number of physical synchronous reads.
        self.avg_physical_sync_read = avg_physical_sync_read
        # The average number of returned rows.
        self.avg_returned_rows = avg_returned_rows
        # The average execution duration.
        self.avg_rt = avg_rt
        # The average number of SQL statements.
        self.avg_sql_count = avg_sql_count
        # The average number of updated rows.
        # 
        #  > This parameter is returned only for ApsaraDB RDS for MySQL and PolarDB-X 2.0 databases.
        self.avg_updated_rows = avg_updated_rows
        # The total number of executions.
        self.count = count
        # The percentage of the total number of executions.
        self.count_rate = count_rate
        # The name of the database.
        self.database = database
        # The number of failed executions.
        self.error_count = error_count
        # The total number of scanned rows.
        # 
        # > This parameter is returned only for ApsaraDB RDS for MySQL, ApsaraDB RDS for PostgreSQL, and PolarDB for MySQL databases.
        self.examined_rows = examined_rows
        # The number of rows that are fetched by compute nodes from data nodes on the PolarDB-X 2.0 instance.
        self.fetch_rows = fetch_rows
        # The IP address of the database instance.
        self.ip = ip
        # The lock wait latency. Unit: seconds.
        self.lock_wait_time = lock_wait_time
        # The number of logical reads.
        self.logical_read = logical_read
        # The number of physical asynchronous reads.
        self.physical_async_read = physical_async_read
        # The number of physical synchronous reads.
        self.physical_sync_read = physical_sync_read
        # The port number that is used to connect to the database instance.
        self.port = port
        # The SQL template.
        self.psql = psql
        # The total number of rows updated or returned by the compute nodes of the PolarDB-X 2.0 instance.
        self.rows = rows
        # The number of SQL statements that take longer than 1 second to execute.
        self.rt_greater_than_one_second_count = rt_greater_than_one_second_count
        # The execution duration percentage.
        self.rt_rate = rt_rate
        # The number of SQL statements.
        self.sql_count = sql_count
        # The SQL ID.
        self.sql_id = sql_id
        # The total number of updated rows.
        self.sum_updated_rows = sum_updated_rows
        # The names of tables in the database.
        self.tables = tables
        # The version number.
        self.version = version
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_examined_rows is not None:
            result['AvgExaminedRows'] = self.avg_examined_rows

        if self.avg_fetch_rows is not None:
            result['AvgFetchRows'] = self.avg_fetch_rows

        if self.avg_lock_wait_time is not None:
            result['AvgLockWaitTime'] = self.avg_lock_wait_time

        if self.avg_logical_read is not None:
            result['AvgLogicalRead'] = self.avg_logical_read

        if self.avg_physical_async_read is not None:
            result['AvgPhysicalAsyncRead'] = self.avg_physical_async_read

        if self.avg_physical_sync_read is not None:
            result['AvgPhysicalSyncRead'] = self.avg_physical_sync_read

        if self.avg_returned_rows is not None:
            result['AvgReturnedRows'] = self.avg_returned_rows

        if self.avg_rt is not None:
            result['AvgRt'] = self.avg_rt

        if self.avg_sql_count is not None:
            result['AvgSqlCount'] = self.avg_sql_count

        if self.avg_updated_rows is not None:
            result['AvgUpdatedRows'] = self.avg_updated_rows

        if self.count is not None:
            result['Count'] = self.count

        if self.count_rate is not None:
            result['CountRate'] = self.count_rate

        if self.database is not None:
            result['Database'] = self.database

        if self.error_count is not None:
            result['ErrorCount'] = self.error_count

        if self.examined_rows is not None:
            result['ExaminedRows'] = self.examined_rows

        if self.fetch_rows is not None:
            result['FetchRows'] = self.fetch_rows

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.lock_wait_time is not None:
            result['LockWaitTime'] = self.lock_wait_time

        if self.logical_read is not None:
            result['LogicalRead'] = self.logical_read

        if self.physical_async_read is not None:
            result['PhysicalAsyncRead'] = self.physical_async_read

        if self.physical_sync_read is not None:
            result['PhysicalSyncRead'] = self.physical_sync_read

        if self.port is not None:
            result['Port'] = self.port

        if self.psql is not None:
            result['Psql'] = self.psql

        if self.rows is not None:
            result['Rows'] = self.rows

        if self.rt_greater_than_one_second_count is not None:
            result['RtGreaterThanOneSecondCount'] = self.rt_greater_than_one_second_count

        if self.rt_rate is not None:
            result['RtRate'] = self.rt_rate

        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count

        if self.sql_id is not None:
            result['SqlId'] = self.sql_id

        if self.sum_updated_rows is not None:
            result['SumUpdatedRows'] = self.sum_updated_rows

        if self.tables is not None:
            result['Tables'] = self.tables

        if self.version is not None:
            result['Version'] = self.version

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgExaminedRows') is not None:
            self.avg_examined_rows = m.get('AvgExaminedRows')

        if m.get('AvgFetchRows') is not None:
            self.avg_fetch_rows = m.get('AvgFetchRows')

        if m.get('AvgLockWaitTime') is not None:
            self.avg_lock_wait_time = m.get('AvgLockWaitTime')

        if m.get('AvgLogicalRead') is not None:
            self.avg_logical_read = m.get('AvgLogicalRead')

        if m.get('AvgPhysicalAsyncRead') is not None:
            self.avg_physical_async_read = m.get('AvgPhysicalAsyncRead')

        if m.get('AvgPhysicalSyncRead') is not None:
            self.avg_physical_sync_read = m.get('AvgPhysicalSyncRead')

        if m.get('AvgReturnedRows') is not None:
            self.avg_returned_rows = m.get('AvgReturnedRows')

        if m.get('AvgRt') is not None:
            self.avg_rt = m.get('AvgRt')

        if m.get('AvgSqlCount') is not None:
            self.avg_sql_count = m.get('AvgSqlCount')

        if m.get('AvgUpdatedRows') is not None:
            self.avg_updated_rows = m.get('AvgUpdatedRows')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CountRate') is not None:
            self.count_rate = m.get('CountRate')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('ErrorCount') is not None:
            self.error_count = m.get('ErrorCount')

        if m.get('ExaminedRows') is not None:
            self.examined_rows = m.get('ExaminedRows')

        if m.get('FetchRows') is not None:
            self.fetch_rows = m.get('FetchRows')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('LockWaitTime') is not None:
            self.lock_wait_time = m.get('LockWaitTime')

        if m.get('LogicalRead') is not None:
            self.logical_read = m.get('LogicalRead')

        if m.get('PhysicalAsyncRead') is not None:
            self.physical_async_read = m.get('PhysicalAsyncRead')

        if m.get('PhysicalSyncRead') is not None:
            self.physical_sync_read = m.get('PhysicalSyncRead')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Psql') is not None:
            self.psql = m.get('Psql')

        if m.get('Rows') is not None:
            self.rows = m.get('Rows')

        if m.get('RtGreaterThanOneSecondCount') is not None:
            self.rt_greater_than_one_second_count = m.get('RtGreaterThanOneSecondCount')

        if m.get('RtRate') is not None:
            self.rt_rate = m.get('RtRate')

        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        if m.get('SumUpdatedRows') is not None:
            self.sum_updated_rows = m.get('SumUpdatedRows')

        if m.get('Tables') is not None:
            self.tables = m.get('Tables')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

