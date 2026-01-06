# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class DescribeSqlLogRecordsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeSqlLogRecordsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The data that is returned.
        self.data = data
        # The message that is returned.
        # 
        # >  If the request is successful, **Successful** is returned. If the request fails, an error message that contains information such as an error code is returned.
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
            temp_model = main_models.DescribeSqlLogRecordsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSqlLogRecordsResponseBodyData(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        finish: str = None,
        items: main_models.DescribeSqlLogRecordsResponseBodyDataItems = None,
        job_id: str = None,
        start_time: int = None,
        total_records: int = None,
    ):
        # The end of the time range to query. This value is a UNIX timestamp. Unit: millisecond.
        self.end_time = end_time
        # Indicates whether the task was complete. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        # 
        # >  If the value of **Finish** is 0 and the value of **JobId** is returned, the request is an asynchronous request and the return result cannot be directly obtained. You must query the return result based on the value of **JobId**. Specify JobId as the key of **Filters** and the value of **JobId** as the value of Filters. Example: `Filters=[{"Key": "JobId", "Value": "******"}]`.
        self.finish = finish
        # The data.
        self.items = items
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The beginning of the time range to query. This value is a UNIX timestamp. Unit: millisecond.
        self.start_time = start_time
        # The total number of entries.
        self.total_records = total_records

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.finish is not None:
            result['Finish'] = self.finish

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.total_records is not None:
            result['TotalRecords'] = self.total_records

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Finish') is not None:
            self.finish = m.get('Finish')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeSqlLogRecordsResponseBodyDataItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TotalRecords') is not None:
            self.total_records = m.get('TotalRecords')

        return self

class DescribeSqlLogRecordsResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        sqllog_record: List[main_models.DescribeSqlLogRecordsResponseBodyDataItemsSQLLogRecord] = None,
    ):
        # The SQL log data.
        self.sqllog_record = sqllog_record

    def validate(self):
        if self.sqllog_record:
            for v1 in self.sqllog_record:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SQLLogRecord'] = []
        if self.sqllog_record is not None:
            for k1 in self.sqllog_record:
                result['SQLLogRecord'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sqllog_record = []
        if m.get('SQLLogRecord') is not None:
            for k1 in m.get('SQLLogRecord'):
                temp_model = main_models.DescribeSqlLogRecordsResponseBodyDataItemsSQLLogRecord()
                self.sqllog_record.append(temp_model.from_map(k1))

        return self

class DescribeSqlLogRecordsResponseBodyDataItemsSQLLogRecord(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        collection: str = None,
        consume: int = None,
        cpu_time: int = None,
        dbname: str = None,
        execute_time: str = None,
        ext: str = None,
        frows: int = None,
        host_address: str = None,
        lock_time: int = None,
        logic_read: int = None,
        node_id: str = None,
        origin_time: int = None,
        parallel_degree: str = None,
        parallel_queue_time: str = None,
        physic_async_read: int = None,
        physic_read: int = None,
        physic_sync_read: int = None,
        return_rows: int = None,
        rows: int = None,
        scan_rows: int = None,
        scnt: int = None,
        sql_id: str = None,
        sql_text: str = None,
        sql_type: str = None,
        state: str = None,
        table_name: str = None,
        thread_id: int = None,
        trace_id: str = None,
        trx_id: str = None,
        update_rows: int = None,
        use_imci_engine: str = None,
        vip: str = None,
        writes: int = None,
    ):
        # The account of the database.
        self.account_name = account_name
        # A reserved parameter.
        self.collection = collection
        # The amount of time that is consumed to execute the SQL statement. Unit: millisecond.
        self.consume = consume
        # The CPU execution duration. Unit: microsecond.
        self.cpu_time = cpu_time
        # The database name.
        self.dbname = dbname
        # The time when the SQL statement was executed. The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.execute_time = execute_time
        # The extended information. This parameter is a reserved parameter.
        self.ext = ext
        # The number of rows that are pulled by the compute nodes of the PolarDB-X 2.0 instance.
        self.frows = frows
        # The IP address of the client.
        self.host_address = host_address
        # The lock wait duration. Unit: millisecond.
        self.lock_time = lock_time
        # The number of logical reads.
        self.logic_read = logic_read
        # The node ID.
        self.node_id = node_id
        # The timestamp generated when the SQL statement was executed. The value of this parameter is a UNIX timestamp. Unit: millisecond.
        self.origin_time = origin_time
        # The parallel queue time of the PolarDB for MySQL instance. Unit: millisecond.
        self.parallel_degree = parallel_degree
        # The parallelism of the PolarDB for MySQL cluster.
        self.parallel_queue_time = parallel_queue_time
        # The number of physical asynchronous reads.
        self.physic_async_read = physic_async_read
        # The total number of physical reads.
        self.physic_read = physic_read
        # The number of physical synchronous reads.
        self.physic_sync_read = physic_sync_read
        # The number of rows returned by the SQL statement.
        self.return_rows = return_rows
        # The total number of rows that are updated or returned by the compute nodes of the PolarDB-X 2.0 instance.
        self.rows = rows
        # The number of scanned rows.
        self.scan_rows = scan_rows
        # The number of requests that are sent from the compute nodes to the data nodes of the PolarDB-X 2.0 instance.
        self.scnt = scnt
        # The SQL statement ID.
        self.sql_id = sql_id
        # The SQL statement.
        self.sql_text = sql_text
        # The type of the SQL statement.
        self.sql_type = sql_type
        # The execution status of the SQL statement.
        # 
        # *   **0**: The execution was successful.
        # *   **1**: The execution failed.
        self.state = state
        self.table_name = table_name
        # The thread ID.
        self.thread_id = thread_id
        # The trace ID of the PolarDB-X 2.0 instance. The value is the execution ID of the SQL statement on the data node.
        self.trace_id = trace_id
        # The transaction ID.
        self.trx_id = trx_id
        # The number of rows that are updated.
        self.update_rows = update_rows
        # Indicates whether the In-Memory Column Index (IMCI) feature is enabled for the PolarDB for MySQL cluster. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.use_imci_engine = use_imci_engine
        # The IP address that is resolved from the endpoint of the query link.
        self.vip = vip
        # The number of writes to the ApsaraDB RDS for SQL Server instance.
        self.writes = writes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.collection is not None:
            result['Collection'] = self.collection

        if self.consume is not None:
            result['Consume'] = self.consume

        if self.cpu_time is not None:
            result['CpuTime'] = self.cpu_time

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time

        if self.ext is not None:
            result['Ext'] = self.ext

        if self.frows is not None:
            result['Frows'] = self.frows

        if self.host_address is not None:
            result['HostAddress'] = self.host_address

        if self.lock_time is not None:
            result['LockTime'] = self.lock_time

        if self.logic_read is not None:
            result['LogicRead'] = self.logic_read

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.origin_time is not None:
            result['OriginTime'] = self.origin_time

        if self.parallel_degree is not None:
            result['ParallelDegree'] = self.parallel_degree

        if self.parallel_queue_time is not None:
            result['ParallelQueueTime'] = self.parallel_queue_time

        if self.physic_async_read is not None:
            result['PhysicAsyncRead'] = self.physic_async_read

        if self.physic_read is not None:
            result['PhysicRead'] = self.physic_read

        if self.physic_sync_read is not None:
            result['PhysicSyncRead'] = self.physic_sync_read

        if self.return_rows is not None:
            result['ReturnRows'] = self.return_rows

        if self.rows is not None:
            result['Rows'] = self.rows

        if self.scan_rows is not None:
            result['ScanRows'] = self.scan_rows

        if self.scnt is not None:
            result['Scnt'] = self.scnt

        if self.sql_id is not None:
            result['SqlId'] = self.sql_id

        if self.sql_text is not None:
            result['SqlText'] = self.sql_text

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        if self.state is not None:
            result['State'] = self.state

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.thread_id is not None:
            result['ThreadId'] = self.thread_id

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        if self.trx_id is not None:
            result['TrxId'] = self.trx_id

        if self.update_rows is not None:
            result['UpdateRows'] = self.update_rows

        if self.use_imci_engine is not None:
            result['UseImciEngine'] = self.use_imci_engine

        if self.vip is not None:
            result['Vip'] = self.vip

        if self.writes is not None:
            result['Writes'] = self.writes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('Collection') is not None:
            self.collection = m.get('Collection')

        if m.get('Consume') is not None:
            self.consume = m.get('Consume')

        if m.get('CpuTime') is not None:
            self.cpu_time = m.get('CpuTime')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')

        if m.get('Ext') is not None:
            self.ext = m.get('Ext')

        if m.get('Frows') is not None:
            self.frows = m.get('Frows')

        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')

        if m.get('LockTime') is not None:
            self.lock_time = m.get('LockTime')

        if m.get('LogicRead') is not None:
            self.logic_read = m.get('LogicRead')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OriginTime') is not None:
            self.origin_time = m.get('OriginTime')

        if m.get('ParallelDegree') is not None:
            self.parallel_degree = m.get('ParallelDegree')

        if m.get('ParallelQueueTime') is not None:
            self.parallel_queue_time = m.get('ParallelQueueTime')

        if m.get('PhysicAsyncRead') is not None:
            self.physic_async_read = m.get('PhysicAsyncRead')

        if m.get('PhysicRead') is not None:
            self.physic_read = m.get('PhysicRead')

        if m.get('PhysicSyncRead') is not None:
            self.physic_sync_read = m.get('PhysicSyncRead')

        if m.get('ReturnRows') is not None:
            self.return_rows = m.get('ReturnRows')

        if m.get('Rows') is not None:
            self.rows = m.get('Rows')

        if m.get('ScanRows') is not None:
            self.scan_rows = m.get('ScanRows')

        if m.get('Scnt') is not None:
            self.scnt = m.get('Scnt')

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        if m.get('SqlText') is not None:
            self.sql_text = m.get('SqlText')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('ThreadId') is not None:
            self.thread_id = m.get('ThreadId')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        if m.get('TrxId') is not None:
            self.trx_id = m.get('TrxId')

        if m.get('UpdateRows') is not None:
            self.update_rows = m.get('UpdateRows')

        if m.get('UseImciEngine') is not None:
            self.use_imci_engine = m.get('UseImciEngine')

        if m.get('Vip') is not None:
            self.vip = m.get('Vip')

        if m.get('Writes') is not None:
            self.writes = m.get('Writes')

        return self

