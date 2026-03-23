# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeSlowLogsResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        end_time: str = None,
        engine: str = None,
        items: main_models.DescribeSlowLogsResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        start_time: str = None,
        total_record_count: int = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.end_time = end_time
        self.engine = engine
        self.items = items
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.start_time = start_time
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

        if self.end_time is not None:
            result['EndTime'] = self.end_time

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

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeSlowLogsResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeSlowLogsResponseBodyItems(DaraModel):
    def __init__(
        self,
        sqlslow_log: List[main_models.DescribeSlowLogsResponseBodyItemsSQLSlowLog] = None,
    ):
        self.sqlslow_log = sqlslow_log

    def validate(self):
        if self.sqlslow_log:
            for v1 in self.sqlslow_log:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SQLSlowLog'] = []
        if self.sqlslow_log is not None:
            for k1 in self.sqlslow_log:
                result['SQLSlowLog'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sqlslow_log = []
        if m.get('SQLSlowLog') is not None:
            for k1 in m.get('SQLSlowLog'):
                temp_model = main_models.DescribeSlowLogsResponseBodyItemsSQLSlowLog()
                self.sqlslow_log.append(temp_model.from_map(k1))

        return self

class DescribeSlowLogsResponseBodyItemsSQLSlowLog(DaraModel):
    def __init__(
        self,
        avg_execution_time: int = None,
        avg_iowrite_counts: int = None,
        avg_last_rows_affected_counts: int = None,
        avg_logical_read_counts: int = None,
        avg_physical_read_counts: int = None,
        avg_rows_affected_counts: int = None,
        create_time: str = None,
        dbname: str = None,
        max_execution_time: int = None,
        max_execution_time_ms: int = None,
        max_iowrite_counts: int = None,
        max_last_rows_affected_counts: int = None,
        max_lock_time: int = None,
        max_lock_time_ms: int = None,
        max_logical_read_counts: int = None,
        max_physical_read_counts: int = None,
        max_rows_affected_counts: int = None,
        min_iowrite_counts: int = None,
        min_last_rows_affected_counts: int = None,
        min_logical_read_counts: int = None,
        min_physical_read_counts: int = None,
        min_rows_affected_counts: int = None,
        my_sqltotal_execution_counts: int = None,
        my_sqltotal_execution_times: int = None,
        parse_max_row_count: int = None,
        parse_total_row_counts: int = None,
        report_time: str = None,
        return_max_row_count: int = None,
        return_total_row_counts: int = None,
        sqlhash: str = None,
        sqlid_str: str = None,
        sqlserver_avg_cpu_time: int = None,
        sqlserver_avg_execution_time: int = None,
        sqlserver_max_cpu_time: int = None,
        sqlserver_min_cpu_time: int = None,
        sqlserver_min_execution_time: int = None,
        sqlserver_total_cpu_time: int = None,
        sqlserver_total_execution_counts: int = None,
        sqlserver_total_execution_times: int = None,
        sqltext: str = None,
        slow_log_id: int = None,
        total_iowrite_counts: int = None,
        total_last_rows_affected_counts: int = None,
        total_lock_times: int = None,
        total_logical_read_counts: int = None,
        total_physical_read_counts: int = None,
        total_rows_affected_counts: int = None,
    ):
        self.avg_execution_time = avg_execution_time
        self.avg_iowrite_counts = avg_iowrite_counts
        self.avg_last_rows_affected_counts = avg_last_rows_affected_counts
        self.avg_logical_read_counts = avg_logical_read_counts
        self.avg_physical_read_counts = avg_physical_read_counts
        self.avg_rows_affected_counts = avg_rows_affected_counts
        self.create_time = create_time
        self.dbname = dbname
        self.max_execution_time = max_execution_time
        self.max_execution_time_ms = max_execution_time_ms
        self.max_iowrite_counts = max_iowrite_counts
        self.max_last_rows_affected_counts = max_last_rows_affected_counts
        self.max_lock_time = max_lock_time
        self.max_lock_time_ms = max_lock_time_ms
        self.max_logical_read_counts = max_logical_read_counts
        self.max_physical_read_counts = max_physical_read_counts
        self.max_rows_affected_counts = max_rows_affected_counts
        self.min_iowrite_counts = min_iowrite_counts
        self.min_last_rows_affected_counts = min_last_rows_affected_counts
        self.min_logical_read_counts = min_logical_read_counts
        self.min_physical_read_counts = min_physical_read_counts
        self.min_rows_affected_counts = min_rows_affected_counts
        self.my_sqltotal_execution_counts = my_sqltotal_execution_counts
        self.my_sqltotal_execution_times = my_sqltotal_execution_times
        self.parse_max_row_count = parse_max_row_count
        self.parse_total_row_counts = parse_total_row_counts
        self.report_time = report_time
        self.return_max_row_count = return_max_row_count
        self.return_total_row_counts = return_total_row_counts
        self.sqlhash = sqlhash
        self.sqlid_str = sqlid_str
        self.sqlserver_avg_cpu_time = sqlserver_avg_cpu_time
        self.sqlserver_avg_execution_time = sqlserver_avg_execution_time
        self.sqlserver_max_cpu_time = sqlserver_max_cpu_time
        self.sqlserver_min_cpu_time = sqlserver_min_cpu_time
        self.sqlserver_min_execution_time = sqlserver_min_execution_time
        self.sqlserver_total_cpu_time = sqlserver_total_cpu_time
        self.sqlserver_total_execution_counts = sqlserver_total_execution_counts
        self.sqlserver_total_execution_times = sqlserver_total_execution_times
        self.sqltext = sqltext
        self.slow_log_id = slow_log_id
        self.total_iowrite_counts = total_iowrite_counts
        self.total_last_rows_affected_counts = total_last_rows_affected_counts
        self.total_lock_times = total_lock_times
        self.total_logical_read_counts = total_logical_read_counts
        self.total_physical_read_counts = total_physical_read_counts
        self.total_rows_affected_counts = total_rows_affected_counts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_execution_time is not None:
            result['AvgExecutionTime'] = self.avg_execution_time

        if self.avg_iowrite_counts is not None:
            result['AvgIOWriteCounts'] = self.avg_iowrite_counts

        if self.avg_last_rows_affected_counts is not None:
            result['AvgLastRowsAffectedCounts'] = self.avg_last_rows_affected_counts

        if self.avg_logical_read_counts is not None:
            result['AvgLogicalReadCounts'] = self.avg_logical_read_counts

        if self.avg_physical_read_counts is not None:
            result['AvgPhysicalReadCounts'] = self.avg_physical_read_counts

        if self.avg_rows_affected_counts is not None:
            result['AvgRowsAffectedCounts'] = self.avg_rows_affected_counts

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.max_execution_time is not None:
            result['MaxExecutionTime'] = self.max_execution_time

        if self.max_execution_time_ms is not None:
            result['MaxExecutionTimeMS'] = self.max_execution_time_ms

        if self.max_iowrite_counts is not None:
            result['MaxIOWriteCounts'] = self.max_iowrite_counts

        if self.max_last_rows_affected_counts is not None:
            result['MaxLastRowsAffectedCounts'] = self.max_last_rows_affected_counts

        if self.max_lock_time is not None:
            result['MaxLockTime'] = self.max_lock_time

        if self.max_lock_time_ms is not None:
            result['MaxLockTimeMS'] = self.max_lock_time_ms

        if self.max_logical_read_counts is not None:
            result['MaxLogicalReadCounts'] = self.max_logical_read_counts

        if self.max_physical_read_counts is not None:
            result['MaxPhysicalReadCounts'] = self.max_physical_read_counts

        if self.max_rows_affected_counts is not None:
            result['MaxRowsAffectedCounts'] = self.max_rows_affected_counts

        if self.min_iowrite_counts is not None:
            result['MinIOWriteCounts'] = self.min_iowrite_counts

        if self.min_last_rows_affected_counts is not None:
            result['MinLastRowsAffectedCounts'] = self.min_last_rows_affected_counts

        if self.min_logical_read_counts is not None:
            result['MinLogicalReadCounts'] = self.min_logical_read_counts

        if self.min_physical_read_counts is not None:
            result['MinPhysicalReadCounts'] = self.min_physical_read_counts

        if self.min_rows_affected_counts is not None:
            result['MinRowsAffectedCounts'] = self.min_rows_affected_counts

        if self.my_sqltotal_execution_counts is not None:
            result['MySQLTotalExecutionCounts'] = self.my_sqltotal_execution_counts

        if self.my_sqltotal_execution_times is not None:
            result['MySQLTotalExecutionTimes'] = self.my_sqltotal_execution_times

        if self.parse_max_row_count is not None:
            result['ParseMaxRowCount'] = self.parse_max_row_count

        if self.parse_total_row_counts is not None:
            result['ParseTotalRowCounts'] = self.parse_total_row_counts

        if self.report_time is not None:
            result['ReportTime'] = self.report_time

        if self.return_max_row_count is not None:
            result['ReturnMaxRowCount'] = self.return_max_row_count

        if self.return_total_row_counts is not None:
            result['ReturnTotalRowCounts'] = self.return_total_row_counts

        if self.sqlhash is not None:
            result['SQLHASH'] = self.sqlhash

        if self.sqlid_str is not None:
            result['SQLIdStr'] = self.sqlid_str

        if self.sqlserver_avg_cpu_time is not None:
            result['SQLServerAvgCpuTime'] = self.sqlserver_avg_cpu_time

        if self.sqlserver_avg_execution_time is not None:
            result['SQLServerAvgExecutionTime'] = self.sqlserver_avg_execution_time

        if self.sqlserver_max_cpu_time is not None:
            result['SQLServerMaxCpuTime'] = self.sqlserver_max_cpu_time

        if self.sqlserver_min_cpu_time is not None:
            result['SQLServerMinCpuTime'] = self.sqlserver_min_cpu_time

        if self.sqlserver_min_execution_time is not None:
            result['SQLServerMinExecutionTime'] = self.sqlserver_min_execution_time

        if self.sqlserver_total_cpu_time is not None:
            result['SQLServerTotalCpuTime'] = self.sqlserver_total_cpu_time

        if self.sqlserver_total_execution_counts is not None:
            result['SQLServerTotalExecutionCounts'] = self.sqlserver_total_execution_counts

        if self.sqlserver_total_execution_times is not None:
            result['SQLServerTotalExecutionTimes'] = self.sqlserver_total_execution_times

        if self.sqltext is not None:
            result['SQLText'] = self.sqltext

        if self.slow_log_id is not None:
            result['SlowLogId'] = self.slow_log_id

        if self.total_iowrite_counts is not None:
            result['TotalIOWriteCounts'] = self.total_iowrite_counts

        if self.total_last_rows_affected_counts is not None:
            result['TotalLastRowsAffectedCounts'] = self.total_last_rows_affected_counts

        if self.total_lock_times is not None:
            result['TotalLockTimes'] = self.total_lock_times

        if self.total_logical_read_counts is not None:
            result['TotalLogicalReadCounts'] = self.total_logical_read_counts

        if self.total_physical_read_counts is not None:
            result['TotalPhysicalReadCounts'] = self.total_physical_read_counts

        if self.total_rows_affected_counts is not None:
            result['TotalRowsAffectedCounts'] = self.total_rows_affected_counts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgExecutionTime') is not None:
            self.avg_execution_time = m.get('AvgExecutionTime')

        if m.get('AvgIOWriteCounts') is not None:
            self.avg_iowrite_counts = m.get('AvgIOWriteCounts')

        if m.get('AvgLastRowsAffectedCounts') is not None:
            self.avg_last_rows_affected_counts = m.get('AvgLastRowsAffectedCounts')

        if m.get('AvgLogicalReadCounts') is not None:
            self.avg_logical_read_counts = m.get('AvgLogicalReadCounts')

        if m.get('AvgPhysicalReadCounts') is not None:
            self.avg_physical_read_counts = m.get('AvgPhysicalReadCounts')

        if m.get('AvgRowsAffectedCounts') is not None:
            self.avg_rows_affected_counts = m.get('AvgRowsAffectedCounts')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('MaxExecutionTime') is not None:
            self.max_execution_time = m.get('MaxExecutionTime')

        if m.get('MaxExecutionTimeMS') is not None:
            self.max_execution_time_ms = m.get('MaxExecutionTimeMS')

        if m.get('MaxIOWriteCounts') is not None:
            self.max_iowrite_counts = m.get('MaxIOWriteCounts')

        if m.get('MaxLastRowsAffectedCounts') is not None:
            self.max_last_rows_affected_counts = m.get('MaxLastRowsAffectedCounts')

        if m.get('MaxLockTime') is not None:
            self.max_lock_time = m.get('MaxLockTime')

        if m.get('MaxLockTimeMS') is not None:
            self.max_lock_time_ms = m.get('MaxLockTimeMS')

        if m.get('MaxLogicalReadCounts') is not None:
            self.max_logical_read_counts = m.get('MaxLogicalReadCounts')

        if m.get('MaxPhysicalReadCounts') is not None:
            self.max_physical_read_counts = m.get('MaxPhysicalReadCounts')

        if m.get('MaxRowsAffectedCounts') is not None:
            self.max_rows_affected_counts = m.get('MaxRowsAffectedCounts')

        if m.get('MinIOWriteCounts') is not None:
            self.min_iowrite_counts = m.get('MinIOWriteCounts')

        if m.get('MinLastRowsAffectedCounts') is not None:
            self.min_last_rows_affected_counts = m.get('MinLastRowsAffectedCounts')

        if m.get('MinLogicalReadCounts') is not None:
            self.min_logical_read_counts = m.get('MinLogicalReadCounts')

        if m.get('MinPhysicalReadCounts') is not None:
            self.min_physical_read_counts = m.get('MinPhysicalReadCounts')

        if m.get('MinRowsAffectedCounts') is not None:
            self.min_rows_affected_counts = m.get('MinRowsAffectedCounts')

        if m.get('MySQLTotalExecutionCounts') is not None:
            self.my_sqltotal_execution_counts = m.get('MySQLTotalExecutionCounts')

        if m.get('MySQLTotalExecutionTimes') is not None:
            self.my_sqltotal_execution_times = m.get('MySQLTotalExecutionTimes')

        if m.get('ParseMaxRowCount') is not None:
            self.parse_max_row_count = m.get('ParseMaxRowCount')

        if m.get('ParseTotalRowCounts') is not None:
            self.parse_total_row_counts = m.get('ParseTotalRowCounts')

        if m.get('ReportTime') is not None:
            self.report_time = m.get('ReportTime')

        if m.get('ReturnMaxRowCount') is not None:
            self.return_max_row_count = m.get('ReturnMaxRowCount')

        if m.get('ReturnTotalRowCounts') is not None:
            self.return_total_row_counts = m.get('ReturnTotalRowCounts')

        if m.get('SQLHASH') is not None:
            self.sqlhash = m.get('SQLHASH')

        if m.get('SQLIdStr') is not None:
            self.sqlid_str = m.get('SQLIdStr')

        if m.get('SQLServerAvgCpuTime') is not None:
            self.sqlserver_avg_cpu_time = m.get('SQLServerAvgCpuTime')

        if m.get('SQLServerAvgExecutionTime') is not None:
            self.sqlserver_avg_execution_time = m.get('SQLServerAvgExecutionTime')

        if m.get('SQLServerMaxCpuTime') is not None:
            self.sqlserver_max_cpu_time = m.get('SQLServerMaxCpuTime')

        if m.get('SQLServerMinCpuTime') is not None:
            self.sqlserver_min_cpu_time = m.get('SQLServerMinCpuTime')

        if m.get('SQLServerMinExecutionTime') is not None:
            self.sqlserver_min_execution_time = m.get('SQLServerMinExecutionTime')

        if m.get('SQLServerTotalCpuTime') is not None:
            self.sqlserver_total_cpu_time = m.get('SQLServerTotalCpuTime')

        if m.get('SQLServerTotalExecutionCounts') is not None:
            self.sqlserver_total_execution_counts = m.get('SQLServerTotalExecutionCounts')

        if m.get('SQLServerTotalExecutionTimes') is not None:
            self.sqlserver_total_execution_times = m.get('SQLServerTotalExecutionTimes')

        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')

        if m.get('SlowLogId') is not None:
            self.slow_log_id = m.get('SlowLogId')

        if m.get('TotalIOWriteCounts') is not None:
            self.total_iowrite_counts = m.get('TotalIOWriteCounts')

        if m.get('TotalLastRowsAffectedCounts') is not None:
            self.total_last_rows_affected_counts = m.get('TotalLastRowsAffectedCounts')

        if m.get('TotalLockTimes') is not None:
            self.total_lock_times = m.get('TotalLockTimes')

        if m.get('TotalLogicalReadCounts') is not None:
            self.total_logical_read_counts = m.get('TotalLogicalReadCounts')

        if m.get('TotalPhysicalReadCounts') is not None:
            self.total_physical_read_counts = m.get('TotalPhysicalReadCounts')

        if m.get('TotalRowsAffectedCounts') is not None:
            self.total_rows_affected_counts = m.get('TotalRowsAffectedCounts')

        return self

