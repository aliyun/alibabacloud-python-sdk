# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class DescribeSqlLogTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeSqlLogTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The response code.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        # 
        # >  If the request was successful, **Successful** is returned. If the request failed, an error message is returned.
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
            temp_model = main_models.DescribeSqlLogTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSqlLogTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        end: int = None,
        expire: bool = None,
        export: str = None,
        filters: List[main_models.DescribeSqlLogTaskResponseBodyDataFilters] = None,
        name: str = None,
        queries: List[main_models.DescribeSqlLogTaskResponseBodyDataQueries] = None,
        start: int = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
        total: int = None,
    ):
        # The time when the task was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The end of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.end = end
        # Indicates whether the task has expired. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.expire = expire
        # The download URL of the export task.
        self.export = export
        # The filter parameters.
        self.filters = filters
        # The task name.
        self.name = name
        # The results of the offline querying task.
        self.queries = queries
        # The beginning of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start = start
        # The task state. Valid values:
        # 
        # *   **INIT**: The task is to be scheduled.
        # *   **RUNNING**: The task is running.
        # *   **FAILED**: The task failed.
        # *   **CANCELED**: The task is canceled.
        # *   **COMPLETED**: The task is complete.
        # 
        # >  If a task is in the **COMPLETED** state, you can view the results of the task.
        self.status = status
        # The task ID.
        self.task_id = task_id
        # The task type. Valid values:
        # 
        # *   **Export**
        # *   **Query**
        self.task_type = task_type
        # The total number of tasks.
        self.total = total

    def validate(self):
        if self.filters:
            for v1 in self.filters:
                 if v1:
                    v1.validate()
        if self.queries:
            for v1 in self.queries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.end is not None:
            result['End'] = self.end

        if self.expire is not None:
            result['Expire'] = self.expire

        if self.export is not None:
            result['Export'] = self.export

        result['Filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['Filters'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        result['Queries'] = []
        if self.queries is not None:
            for k1 in self.queries:
                result['Queries'].append(k1.to_map() if k1 else None)

        if self.start is not None:
            result['Start'] = self.start

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Expire') is not None:
            self.expire = m.get('Expire')

        if m.get('Export') is not None:
            self.export = m.get('Export')

        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.DescribeSqlLogTaskResponseBodyDataFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.queries = []
        if m.get('Queries') is not None:
            for k1 in m.get('Queries'):
                temp_model = main_models.DescribeSqlLogTaskResponseBodyDataQueries()
                self.queries.append(temp_model.from_map(k1))

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeSqlLogTaskResponseBodyDataQueries(DaraModel):
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
        sql_command: int = None,
        sql_id: str = None,
        sql_text: str = None,
        sql_type: str = None,
        state: str = None,
        thread_id: int = None,
        trace_id: str = None,
        trx_id: str = None,
        update_rows: int = None,
        use_imci_engine: str = None,
        vip: str = None,
        writes: int = None,
    ):
        # The database account.
        self.account_name = account_name
        self.collection = collection
        # The execution duration. Unit: millisecond.
        self.consume = consume
        # The CPU execution time. Unit: microsecond.
        self.cpu_time = cpu_time
        # The database name.
        self.dbname = dbname
        # The execution time. The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.execute_time = execute_time
        # The extended information. This parameter is a reserved parameter.
        self.ext = ext
        # The number of rows pulled by the CNs of the PolarDB-X 2.0 instance.
        self.frows = frows
        # The IP address of the client.
        self.host_address = host_address
        # The lock wait time. Unit: millisecond.
        self.lock_time = lock_time
        # The number of logical reads.
        self.logic_read = logic_read
        # The ID of the child node.
        self.node_id = node_id
        # The execution timestamp. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.origin_time = origin_time
        # The wait time of parallel queries in the queue in the PolarDB for MySQL instance. Unit: millisecond.
        self.parallel_degree = parallel_degree
        # The degree of parallelism (DOP) value of the PolarDB for MySQL instance.
        self.parallel_queue_time = parallel_queue_time
        # The number of physical asynchronous reads.
        self.physic_async_read = physic_async_read
        # The total number of physical reads.
        self.physic_read = physic_read
        # The number of physical synchronous reads.
        self.physic_sync_read = physic_sync_read
        # The number of rows returned.
        self.return_rows = return_rows
        # The total number of rows updated or returned by the CNs of the PolarDB-X 2.0 instance.
        self.rows = rows
        # The number of rows scanned.
        self.scan_rows = scan_rows
        # The number of requests from the compute nodes (CNs) to the data nodes (DNs) in the PolarDB-X 2.0 instance.
        self.scnt = scnt
        self.sql_command = sql_command
        # The ID of the SQL statement.
        self.sql_id = sql_id
        # The queried SQL statement.
        self.sql_text = sql_text
        # The type of the SQL statement. Valid values:
        # 
        # *   **SELECT**
        # *   **UPDATE**
        # *   **DELETE**
        self.sql_type = sql_type
        # The execution result of the SQL statement. Valid values:
        # 
        # *   **0**: The execution was successful.
        # *   **1**: The execution failed.
        self.state = state
        # The thread ID.
        self.thread_id = thread_id
        # The trace ID of the PolarDB-X 2.0 instance, which is the execution ID of the SQL statement on the DN.
        self.trace_id = trace_id
        # The transaction ID.
        self.trx_id = trx_id
        # The number of rows updated.
        self.update_rows = update_rows
        # Indicates whether the PolarDB for MySQL instance uses In-Memory Column Indexes (IMCIs). Valid values:
        # 
        # *   **true**
        # *   **false**
        self.use_imci_engine = use_imci_engine
        # The IP address to which the endpoint used for query is resolved.
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

        if self.sql_command is not None:
            result['SqlCommand'] = self.sql_command

        if self.sql_id is not None:
            result['SqlId'] = self.sql_id

        if self.sql_text is not None:
            result['SqlText'] = self.sql_text

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        if self.state is not None:
            result['State'] = self.state

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

        if m.get('SqlCommand') is not None:
            self.sql_command = m.get('SqlCommand')

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        if m.get('SqlText') is not None:
            self.sql_text = m.get('SqlText')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('State') is not None:
            self.state = m.get('State')

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

class DescribeSqlLogTaskResponseBodyDataFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: Any = None,
    ):
        # The name of the filter parameter.
        # 
        # >  For more information about the filter parameters, see the **Valid values of Key** section of this topic.
        self.key = key
        # The value of the filter parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

