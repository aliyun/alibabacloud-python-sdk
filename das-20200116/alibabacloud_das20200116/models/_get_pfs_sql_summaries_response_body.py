# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetPfsSqlSummariesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetPfsSqlSummariesResponseBodyData = None,
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
        # >  If the request was successful, **Successful** is returned. If the request failed, an error message such as an error code is returned.
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
            temp_model = main_models.GetPfsSqlSummariesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetPfsSqlSummariesResponseBodyData(DaraModel):
    def __init__(
        self,
        extra: Any = None,
        list: List[main_models.GetPfsSqlSummariesResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The reserved parameter.
        self.extra = extra
        # The details of the data returned.
        self.list = list
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
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
        if self.extra is not None:
            result['Extra'] = self.extra

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.GetPfsSqlSummariesResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetPfsSqlSummariesResponseBodyDataList(DaraModel):
    def __init__(
        self,
        avg_latency: float = None,
        count: int = None,
        count_rate: float = None,
        cpu_rate: float = None,
        cpu_time: float = None,
        data_read_time: float = None,
        data_reads: int = None,
        data_write_time: float = None,
        data_writes: int = None,
        db: str = None,
        elapsed_time: float = None,
        err_count: int = None,
        first_time: int = None,
        full_scan: bool = None,
        id: int = None,
        instance_id: str = None,
        last_time: int = None,
        lock_latency_avg: float = None,
        logic_id: int = None,
        logic_reads: int = None,
        max_latency: float = None,
        mutex_spins: int = None,
        mutex_waits: int = None,
        node_id: str = None,
        physical_async_reads: int = None,
        physical_reads: int = None,
        psql: str = None,
        redo_writes: int = None,
        rows_affected: int = None,
        rows_affected_avg: float = None,
        rows_examined: int = None,
        rows_examined_avg: float = None,
        rows_send_avg: float = None,
        rows_sent: int = None,
        rows_sent_avg: float = None,
        rows_sorted: int = None,
        rt_rate: float = None,
        rwlock_os_waits: int = None,
        rwlock_spin_rounds: int = None,
        rwlock_spin_waits: int = None,
        select_full_join_avg: float = None,
        select_full_range_join_avg: float = None,
        select_range_avg: float = None,
        select_scan_avg: float = None,
        semisync_delay_time: float = None,
        server_lock_time: float = None,
        sort_merge_passes: int = None,
        sort_range_avg: float = None,
        sort_rows_avg: float = None,
        sort_scan_avg: float = None,
        sql_id: str = None,
        sql_type: str = None,
        tables: List[str] = None,
        timer_wait_avg: float = None,
        timestamp: int = None,
        tmp_disk_tables: int = None,
        tmp_disk_tables_avg: float = None,
        tmp_tables: int = None,
        tmp_tables_avg: float = None,
        total_latency: float = None,
        transaction_lock_time: float = None,
        user_id: str = None,
        warn_count: int = None,
    ):
        # The average execution latency. Unit: millisecond.
        self.avg_latency = avg_latency
        # The total number of executions.
        self.count = count
        # The percentage of the number of executions.
        self.count_rate = count_rate
        # The ratio of the CPU execution duration to the total execution duration of the SQL statement.
        self.cpu_rate = cpu_rate
        # The CPU execution duration. Unit: millisecond.
        self.cpu_time = cpu_time
        # The data read duration. Unit: millisecond.
        self.data_read_time = data_read_time
        # The number of nodes from which data can be read.
        self.data_reads = data_reads
        # The data write duration. Unit: millisecond.
        self.data_write_time = data_write_time
        # The number of nodes to which data can be written.
        self.data_writes = data_writes
        # The name of the database.
        self.db = db
        # The execution duration. Unit: millisecond.
        self.elapsed_time = elapsed_time
        # The number of errors.
        self.err_count = err_count
        # The time when the SQL statement was executed for the first time. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.first_time = first_time
        # Indicates whether full table scan was enabled. Valid values:
        # 
        # * **true**
        # * **false**
        self.full_scan = full_scan
        # The primary key ID.
        self.id = id
        # The instance ID.
        self.instance_id = instance_id
        # The time when the SQL statement was last modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.last_time = last_time
        # The average lock wait latency. Unit: millisecond.
        self.lock_latency_avg = lock_latency_avg
        # The logical database ID.
        self.logic_id = logic_id
        # The number of logical nodes.
        self.logic_reads = logic_reads
        # The maximum execution latency. Unit: millisecond.
        self.max_latency = max_latency
        # The number of mutex spins.
        self.mutex_spins = mutex_spins
        # The number of mutex waits.
        self.mutex_waits = mutex_waits
        # The node ID.
        # 
        # >  This parameter is returned only if the database instance is an ApsaraDB RDS for MySQL Cluster Edition instance or a PolarDB for MySQL cluster.
        self.node_id = node_id
        # The number of physical asynchronous nodes.
        self.physical_async_reads = physical_async_reads
        # The number of physical nodes.
        self.physical_reads = physical_reads
        # The SQL template.
        self.psql = psql
        # The number of redo nodes.
        self.redo_writes = redo_writes
        # The number of rows that are affected by the SQL statement.
        self.rows_affected = rows_affected
        # The average number of rows affected by the SQL statement.
        self.rows_affected_avg = rows_affected_avg
        # The total number of scanned rows.
        self.rows_examined = rows_examined
        # The average number of scanned rows.
        self.rows_examined_avg = rows_examined_avg
        # The average number of returned rows.
        self.rows_send_avg = rows_send_avg
        # The number of rows returned by the SQL statement.
        self.rows_sent = rows_sent
        # The average number of rows returned for the SQL statement.
        self.rows_sent_avg = rows_sent_avg
        # The number of sorted rows.
        self.rows_sorted = rows_sorted
        # The execution duration percentage.
        self.rt_rate = rt_rate
        # Indicates whether read/write splitting was enabled. Valid values:
        # 
        # * **0:** Read/write splitting was disabled.
        # * **1:** Read/write splitting was enabled.
        self.rwlock_os_waits = rwlock_os_waits
        # The read/write splitting parameters.
        self.rwlock_spin_rounds = rwlock_spin_rounds
        # Indices whether multi-index scanning was enabled. Valid values:
        # 
        # * **0:** Multi-index scanning was disabled.
        # * **1:** Multi-index scanning was enabled.
        self.rwlock_spin_waits = rwlock_spin_waits
        # The average number of joins that performed table scans without using indexes.
        # 
        # > If the value of this parameter is not 0, check the table indexes.
        self.select_full_join_avg = select_full_join_avg
        # The average number of joins that selected a range.
        self.select_full_range_join_avg = select_full_range_join_avg
        # The average selected range.
        self.select_range_avg = select_range_avg
        # The average number of scanned rows.
        self.select_scan_avg = select_scan_avg
        # The semi-synchronous replication latency. Unit: millisecond.
        self.semisync_delay_time = semisync_delay_time
        # The amount of time consumed for locking the server. Unit: millisecond.
        self.server_lock_time = server_lock_time
        # The number of merges that the sorting algorithm must perform.
        self.sort_merge_passes = sort_merge_passes
        # The average number of sorts that were performed by using a range.
        self.sort_range_avg = sort_range_avg
        # The average number of sorted rows.
        self.sort_rows_avg = sort_rows_avg
        # The average number of sorts that were performed during table scans.
        self.sort_scan_avg = sort_scan_avg
        # The SQL template ID.
        self.sql_id = sql_id
        # The type of the SQL statement. Valid values:
        # 
        # * **SELECT**
        # * **UPDATE**
        # * **DELETE**
        self.sql_type = sql_type
        # The names of tables in the database.
        self.tables = tables
        # The reserved parameter.
        self.timer_wait_avg = timer_wait_avg
        # The data timestamp. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.timestamp = timestamp
        # The number of on-disk temporary tables.
        self.tmp_disk_tables = tmp_disk_tables
        # The average number of on-disk temporary tables.
        self.tmp_disk_tables_avg = tmp_disk_tables_avg
        # The number of temporary tables.
        self.tmp_tables = tmp_tables
        # The average number of temporary tables.
        self.tmp_tables_avg = tmp_tables_avg
        # The execution latency. Unit: millisecond.
        self.total_latency = total_latency
        # The amount of time consumed for locking the storage transaction. Unit: millisecond.
        self.transaction_lock_time = transaction_lock_time
        # The user ID.
        self.user_id = user_id
        # The number of warnings.
        self.warn_count = warn_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_latency is not None:
            result['AvgLatency'] = self.avg_latency

        if self.count is not None:
            result['Count'] = self.count

        if self.count_rate is not None:
            result['CountRate'] = self.count_rate

        if self.cpu_rate is not None:
            result['CpuRate'] = self.cpu_rate

        if self.cpu_time is not None:
            result['CpuTime'] = self.cpu_time

        if self.data_read_time is not None:
            result['DataReadTime'] = self.data_read_time

        if self.data_reads is not None:
            result['DataReads'] = self.data_reads

        if self.data_write_time is not None:
            result['DataWriteTime'] = self.data_write_time

        if self.data_writes is not None:
            result['DataWrites'] = self.data_writes

        if self.db is not None:
            result['Db'] = self.db

        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time

        if self.err_count is not None:
            result['ErrCount'] = self.err_count

        if self.first_time is not None:
            result['FirstTime'] = self.first_time

        if self.full_scan is not None:
            result['FullScan'] = self.full_scan

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.last_time is not None:
            result['LastTime'] = self.last_time

        if self.lock_latency_avg is not None:
            result['LockLatencyAvg'] = self.lock_latency_avg

        if self.logic_id is not None:
            result['LogicId'] = self.logic_id

        if self.logic_reads is not None:
            result['LogicReads'] = self.logic_reads

        if self.max_latency is not None:
            result['MaxLatency'] = self.max_latency

        if self.mutex_spins is not None:
            result['MutexSpins'] = self.mutex_spins

        if self.mutex_waits is not None:
            result['MutexWaits'] = self.mutex_waits

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.physical_async_reads is not None:
            result['PhysicalAsyncReads'] = self.physical_async_reads

        if self.physical_reads is not None:
            result['PhysicalReads'] = self.physical_reads

        if self.psql is not None:
            result['Psql'] = self.psql

        if self.redo_writes is not None:
            result['RedoWrites'] = self.redo_writes

        if self.rows_affected is not None:
            result['RowsAffected'] = self.rows_affected

        if self.rows_affected_avg is not None:
            result['RowsAffectedAvg'] = self.rows_affected_avg

        if self.rows_examined is not None:
            result['RowsExamined'] = self.rows_examined

        if self.rows_examined_avg is not None:
            result['RowsExaminedAvg'] = self.rows_examined_avg

        if self.rows_send_avg is not None:
            result['RowsSendAvg'] = self.rows_send_avg

        if self.rows_sent is not None:
            result['RowsSent'] = self.rows_sent

        if self.rows_sent_avg is not None:
            result['RowsSentAvg'] = self.rows_sent_avg

        if self.rows_sorted is not None:
            result['RowsSorted'] = self.rows_sorted

        if self.rt_rate is not None:
            result['RtRate'] = self.rt_rate

        if self.rwlock_os_waits is not None:
            result['RwlockOsWaits'] = self.rwlock_os_waits

        if self.rwlock_spin_rounds is not None:
            result['RwlockSpinRounds'] = self.rwlock_spin_rounds

        if self.rwlock_spin_waits is not None:
            result['RwlockSpinWaits'] = self.rwlock_spin_waits

        if self.select_full_join_avg is not None:
            result['SelectFullJoinAvg'] = self.select_full_join_avg

        if self.select_full_range_join_avg is not None:
            result['SelectFullRangeJoinAvg'] = self.select_full_range_join_avg

        if self.select_range_avg is not None:
            result['SelectRangeAvg'] = self.select_range_avg

        if self.select_scan_avg is not None:
            result['SelectScanAvg'] = self.select_scan_avg

        if self.semisync_delay_time is not None:
            result['SemisyncDelayTime'] = self.semisync_delay_time

        if self.server_lock_time is not None:
            result['ServerLockTime'] = self.server_lock_time

        if self.sort_merge_passes is not None:
            result['SortMergePasses'] = self.sort_merge_passes

        if self.sort_range_avg is not None:
            result['SortRangeAvg'] = self.sort_range_avg

        if self.sort_rows_avg is not None:
            result['SortRowsAvg'] = self.sort_rows_avg

        if self.sort_scan_avg is not None:
            result['SortScanAvg'] = self.sort_scan_avg

        if self.sql_id is not None:
            result['SqlId'] = self.sql_id

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        if self.tables is not None:
            result['Tables'] = self.tables

        if self.timer_wait_avg is not None:
            result['TimerWaitAvg'] = self.timer_wait_avg

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.tmp_disk_tables is not None:
            result['TmpDiskTables'] = self.tmp_disk_tables

        if self.tmp_disk_tables_avg is not None:
            result['TmpDiskTablesAvg'] = self.tmp_disk_tables_avg

        if self.tmp_tables is not None:
            result['TmpTables'] = self.tmp_tables

        if self.tmp_tables_avg is not None:
            result['TmpTablesAvg'] = self.tmp_tables_avg

        if self.total_latency is not None:
            result['TotalLatency'] = self.total_latency

        if self.transaction_lock_time is not None:
            result['TransactionLockTime'] = self.transaction_lock_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.warn_count is not None:
            result['WarnCount'] = self.warn_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgLatency') is not None:
            self.avg_latency = m.get('AvgLatency')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CountRate') is not None:
            self.count_rate = m.get('CountRate')

        if m.get('CpuRate') is not None:
            self.cpu_rate = m.get('CpuRate')

        if m.get('CpuTime') is not None:
            self.cpu_time = m.get('CpuTime')

        if m.get('DataReadTime') is not None:
            self.data_read_time = m.get('DataReadTime')

        if m.get('DataReads') is not None:
            self.data_reads = m.get('DataReads')

        if m.get('DataWriteTime') is not None:
            self.data_write_time = m.get('DataWriteTime')

        if m.get('DataWrites') is not None:
            self.data_writes = m.get('DataWrites')

        if m.get('Db') is not None:
            self.db = m.get('Db')

        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')

        if m.get('ErrCount') is not None:
            self.err_count = m.get('ErrCount')

        if m.get('FirstTime') is not None:
            self.first_time = m.get('FirstTime')

        if m.get('FullScan') is not None:
            self.full_scan = m.get('FullScan')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')

        if m.get('LockLatencyAvg') is not None:
            self.lock_latency_avg = m.get('LockLatencyAvg')

        if m.get('LogicId') is not None:
            self.logic_id = m.get('LogicId')

        if m.get('LogicReads') is not None:
            self.logic_reads = m.get('LogicReads')

        if m.get('MaxLatency') is not None:
            self.max_latency = m.get('MaxLatency')

        if m.get('MutexSpins') is not None:
            self.mutex_spins = m.get('MutexSpins')

        if m.get('MutexWaits') is not None:
            self.mutex_waits = m.get('MutexWaits')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('PhysicalAsyncReads') is not None:
            self.physical_async_reads = m.get('PhysicalAsyncReads')

        if m.get('PhysicalReads') is not None:
            self.physical_reads = m.get('PhysicalReads')

        if m.get('Psql') is not None:
            self.psql = m.get('Psql')

        if m.get('RedoWrites') is not None:
            self.redo_writes = m.get('RedoWrites')

        if m.get('RowsAffected') is not None:
            self.rows_affected = m.get('RowsAffected')

        if m.get('RowsAffectedAvg') is not None:
            self.rows_affected_avg = m.get('RowsAffectedAvg')

        if m.get('RowsExamined') is not None:
            self.rows_examined = m.get('RowsExamined')

        if m.get('RowsExaminedAvg') is not None:
            self.rows_examined_avg = m.get('RowsExaminedAvg')

        if m.get('RowsSendAvg') is not None:
            self.rows_send_avg = m.get('RowsSendAvg')

        if m.get('RowsSent') is not None:
            self.rows_sent = m.get('RowsSent')

        if m.get('RowsSentAvg') is not None:
            self.rows_sent_avg = m.get('RowsSentAvg')

        if m.get('RowsSorted') is not None:
            self.rows_sorted = m.get('RowsSorted')

        if m.get('RtRate') is not None:
            self.rt_rate = m.get('RtRate')

        if m.get('RwlockOsWaits') is not None:
            self.rwlock_os_waits = m.get('RwlockOsWaits')

        if m.get('RwlockSpinRounds') is not None:
            self.rwlock_spin_rounds = m.get('RwlockSpinRounds')

        if m.get('RwlockSpinWaits') is not None:
            self.rwlock_spin_waits = m.get('RwlockSpinWaits')

        if m.get('SelectFullJoinAvg') is not None:
            self.select_full_join_avg = m.get('SelectFullJoinAvg')

        if m.get('SelectFullRangeJoinAvg') is not None:
            self.select_full_range_join_avg = m.get('SelectFullRangeJoinAvg')

        if m.get('SelectRangeAvg') is not None:
            self.select_range_avg = m.get('SelectRangeAvg')

        if m.get('SelectScanAvg') is not None:
            self.select_scan_avg = m.get('SelectScanAvg')

        if m.get('SemisyncDelayTime') is not None:
            self.semisync_delay_time = m.get('SemisyncDelayTime')

        if m.get('ServerLockTime') is not None:
            self.server_lock_time = m.get('ServerLockTime')

        if m.get('SortMergePasses') is not None:
            self.sort_merge_passes = m.get('SortMergePasses')

        if m.get('SortRangeAvg') is not None:
            self.sort_range_avg = m.get('SortRangeAvg')

        if m.get('SortRowsAvg') is not None:
            self.sort_rows_avg = m.get('SortRowsAvg')

        if m.get('SortScanAvg') is not None:
            self.sort_scan_avg = m.get('SortScanAvg')

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('Tables') is not None:
            self.tables = m.get('Tables')

        if m.get('TimerWaitAvg') is not None:
            self.timer_wait_avg = m.get('TimerWaitAvg')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('TmpDiskTables') is not None:
            self.tmp_disk_tables = m.get('TmpDiskTables')

        if m.get('TmpDiskTablesAvg') is not None:
            self.tmp_disk_tables_avg = m.get('TmpDiskTablesAvg')

        if m.get('TmpTables') is not None:
            self.tmp_tables = m.get('TmpTables')

        if m.get('TmpTablesAvg') is not None:
            self.tmp_tables_avg = m.get('TmpTablesAvg')

        if m.get('TotalLatency') is not None:
            self.total_latency = m.get('TotalLatency')

        if m.get('TransactionLockTime') is not None:
            self.transaction_lock_time = m.get('TransactionLockTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WarnCount') is not None:
            self.warn_count = m.get('WarnCount')

        return self

