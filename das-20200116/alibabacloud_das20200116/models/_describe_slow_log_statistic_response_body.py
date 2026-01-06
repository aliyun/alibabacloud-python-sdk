# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class DescribeSlowLogStatisticResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeSlowLogStatisticResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        # AsyncResult<DBLogRecords<SlowLogStat>>
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.DescribeSlowLogStatisticResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSlowLogStatisticResponseBodyData(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeSlowLogStatisticResponseBodyDataData = None,
        error_code: int = None,
        is_finish: bool = None,
        message: str = None,
        request_key: str = None,
        result_id: str = None,
        state: str = None,
        timestamp: int = None,
    ):
        self.data = data
        self.error_code = error_code
        self.is_finish = is_finish
        self.message = message
        self.request_key = request_key
        self.result_id = result_id
        self.state = state
        self.timestamp = timestamp

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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.is_finish is not None:
            result['IsFinish'] = self.is_finish

        if self.message is not None:
            result['Message'] = self.message

        if self.request_key is not None:
            result['RequestKey'] = self.request_key

        if self.result_id is not None:
            result['ResultId'] = self.result_id

        if self.state is not None:
            result['State'] = self.state

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeSlowLogStatisticResponseBodyDataData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('IsFinish') is not None:
            self.is_finish = m.get('IsFinish')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestKey') is not None:
            self.request_key = m.get('RequestKey')

        if m.get('ResultId') is not None:
            self.result_id = m.get('ResultId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class DescribeSlowLogStatisticResponseBodyDataData(DaraModel):
    def __init__(
        self,
        db_instance_id: int = None,
        db_instance_name: str = None,
        end_time: str = None,
        items_numbers: int = None,
        logs: List[main_models.DescribeSlowLogStatisticResponseBodyDataDataLogs] = None,
        max_records_per_page: int = None,
        node_id: str = None,
        page_numbers: int = None,
        start_time: str = None,
        total_records: int = None,
    ):
        self.db_instance_id = db_instance_id
        self.db_instance_name = db_instance_name
        self.end_time = end_time
        self.items_numbers = items_numbers
        self.logs = logs
        self.max_records_per_page = max_records_per_page
        self.node_id = node_id
        self.page_numbers = page_numbers
        self.start_time = start_time
        self.total_records = total_records

    def validate(self):
        if self.logs:
            for v1 in self.logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id

        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.items_numbers is not None:
            result['ItemsNumbers'] = self.items_numbers

        result['Logs'] = []
        if self.logs is not None:
            for k1 in self.logs:
                result['Logs'].append(k1.to_map() if k1 else None)

        if self.max_records_per_page is not None:
            result['MaxRecordsPerPage'] = self.max_records_per_page

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.page_numbers is not None:
            result['PageNumbers'] = self.page_numbers

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.total_records is not None:
            result['TotalRecords'] = self.total_records

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')

        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ItemsNumbers') is not None:
            self.items_numbers = m.get('ItemsNumbers')

        self.logs = []
        if m.get('Logs') is not None:
            for k1 in m.get('Logs'):
                temp_model = main_models.DescribeSlowLogStatisticResponseBodyDataDataLogs()
                self.logs.append(temp_model.from_map(k1))

        if m.get('MaxRecordsPerPage') is not None:
            self.max_records_per_page = m.get('MaxRecordsPerPage')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('PageNumbers') is not None:
            self.page_numbers = m.get('PageNumbers')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TotalRecords') is not None:
            self.total_records = m.get('TotalRecords')

        return self

class DescribeSlowLogStatisticResponseBodyDataDataLogs(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        avg_cputime: float = None,
        avg_cputime_seconds: float = None,
        avg_doc_examined: float = None,
        avg_frows: float = None,
        avg_iowrites: float = None,
        avg_keys_examined: float = None,
        avg_last_rows_count_affected: float = None,
        avg_lock_time: float = None,
        avg_lock_time_seconds: float = None,
        avg_logical_ioreads: float = None,
        avg_physical_ioreads: float = None,
        avg_query_time: float = None,
        avg_query_time_seconds: float = None,
        avg_request_size: float = None,
        avg_response_size: float = None,
        avg_return_num: float = None,
        avg_rows: float = None,
        avg_rows_count_affected: float = None,
        avg_rows_examined: float = None,
        avg_rows_sent: float = None,
        avg_rt: float = None,
        avg_scnt: float = None,
        cputime: float = None,
        cputime_seconds: float = None,
        client_ip: str = None,
        cmd: str = None,
        command: str = None,
        count: int = None,
        count_rate: float = None,
        dbname: str = None,
        database: str = None,
        db_id: str = None,
        db_instance_name: str = None,
        doc_examined: int = None,
        docs_examined: int = None,
        frows: int = None,
        histogram: main_models.DescribeSlowLogStatisticResponseBodyDataDataLogsHistogram = None,
        host_address: str = None,
        host_ins_id: str = None,
        iowrites: int = None,
        ins_name: str = None,
        ins_role: str = None,
        keys_examined: int = None,
        last_rows_count_affected: int = None,
        lock_time: float = None,
        lock_time_seconds: float = None,
        logical_ioreads: int = None,
        max_cputime: float = None,
        max_cputime_seconds: float = None,
        max_doc_examined: int = None,
        max_frows: int = None,
        max_iowrites: int = None,
        max_keys_examined: int = None,
        max_last_rows_count_affected: int = None,
        max_lock_time: float = None,
        max_lock_time_seconds: float = None,
        max_logical_ioreads: int = None,
        max_physical_ioreads: int = None,
        max_query_time: float = None,
        max_query_time_seconds: float = None,
        max_request_size: float = None,
        max_response_size: float = None,
        max_return_num: int = None,
        max_rows: int = None,
        max_rows_count_affected: int = None,
        max_rows_examined: int = None,
        max_rows_sent: int = None,
        max_rt: float = None,
        max_scnt: int = None,
        namespace: str = None,
        node_type: str = None,
        op_type: str = None,
        origin_alias: str = None,
        physical_ioreads: int = None,
        psql: str = None,
        query_id: str = None,
        query_start_time: str = None,
        query_time: int = None,
        query_time_rate: float = None,
        query_time_seconds: float = None,
        return_item_numbers: str = None,
        return_num: int = None,
        rows: int = None,
        rows_count_affected: int = None,
        rows_examined: int = None,
        rows_sent: int = None,
        rule_id: str = None,
        sqltext: str = None,
        scheme: str = None,
        scnt: int = None,
        sql_id: str = None,
        sql_tag: main_models.DescribeSlowLogStatisticResponseBodyDataDataLogsSqlTag = None,
        sql_type: str = None,
        sub_instance_id: str = None,
        table_name: str = None,
        thread_id: str = None,
        timestamp: int = None,
        total_count: int = None,
        trend: List[main_models.DescribeSlowLogStatisticResponseBodyDataDataLogsTrend] = None,
        user: str = None,
    ):
        self.account_name = account_name
        self.avg_cputime = avg_cputime
        self.avg_cputime_seconds = avg_cputime_seconds
        self.avg_doc_examined = avg_doc_examined
        self.avg_frows = avg_frows
        self.avg_iowrites = avg_iowrites
        self.avg_keys_examined = avg_keys_examined
        self.avg_last_rows_count_affected = avg_last_rows_count_affected
        self.avg_lock_time = avg_lock_time
        self.avg_lock_time_seconds = avg_lock_time_seconds
        self.avg_logical_ioreads = avg_logical_ioreads
        self.avg_physical_ioreads = avg_physical_ioreads
        self.avg_query_time = avg_query_time
        self.avg_query_time_seconds = avg_query_time_seconds
        self.avg_request_size = avg_request_size
        self.avg_response_size = avg_response_size
        self.avg_return_num = avg_return_num
        self.avg_rows = avg_rows
        self.avg_rows_count_affected = avg_rows_count_affected
        self.avg_rows_examined = avg_rows_examined
        self.avg_rows_sent = avg_rows_sent
        self.avg_rt = avg_rt
        self.avg_scnt = avg_scnt
        self.cputime = cputime
        self.cputime_seconds = cputime_seconds
        self.client_ip = client_ip
        self.cmd = cmd
        self.command = command
        self.count = count
        self.count_rate = count_rate
        self.dbname = dbname
        self.database = database
        self.db_id = db_id
        self.db_instance_name = db_instance_name
        self.doc_examined = doc_examined
        self.docs_examined = docs_examined
        self.frows = frows
        self.histogram = histogram
        self.host_address = host_address
        self.host_ins_id = host_ins_id
        self.iowrites = iowrites
        self.ins_name = ins_name
        self.ins_role = ins_role
        self.keys_examined = keys_examined
        self.last_rows_count_affected = last_rows_count_affected
        self.lock_time = lock_time
        self.lock_time_seconds = lock_time_seconds
        self.logical_ioreads = logical_ioreads
        self.max_cputime = max_cputime
        self.max_cputime_seconds = max_cputime_seconds
        self.max_doc_examined = max_doc_examined
        self.max_frows = max_frows
        self.max_iowrites = max_iowrites
        self.max_keys_examined = max_keys_examined
        self.max_last_rows_count_affected = max_last_rows_count_affected
        self.max_lock_time = max_lock_time
        self.max_lock_time_seconds = max_lock_time_seconds
        self.max_logical_ioreads = max_logical_ioreads
        self.max_physical_ioreads = max_physical_ioreads
        self.max_query_time = max_query_time
        self.max_query_time_seconds = max_query_time_seconds
        self.max_request_size = max_request_size
        self.max_response_size = max_response_size
        self.max_return_num = max_return_num
        self.max_rows = max_rows
        self.max_rows_count_affected = max_rows_count_affected
        self.max_rows_examined = max_rows_examined
        self.max_rows_sent = max_rows_sent
        self.max_rt = max_rt
        self.max_scnt = max_scnt
        self.namespace = namespace
        self.node_type = node_type
        self.op_type = op_type
        self.origin_alias = origin_alias
        self.physical_ioreads = physical_ioreads
        self.psql = psql
        self.query_id = query_id
        self.query_start_time = query_start_time
        self.query_time = query_time
        self.query_time_rate = query_time_rate
        self.query_time_seconds = query_time_seconds
        self.return_item_numbers = return_item_numbers
        self.return_num = return_num
        self.rows = rows
        self.rows_count_affected = rows_count_affected
        self.rows_examined = rows_examined
        self.rows_sent = rows_sent
        self.rule_id = rule_id
        self.sqltext = sqltext
        self.scheme = scheme
        self.scnt = scnt
        # SQL ID。
        self.sql_id = sql_id
        self.sql_tag = sql_tag
        self.sql_type = sql_type
        self.sub_instance_id = sub_instance_id
        self.table_name = table_name
        self.thread_id = thread_id
        self.timestamp = timestamp
        self.total_count = total_count
        self.trend = trend
        self.user = user

    def validate(self):
        if self.histogram:
            self.histogram.validate()
        if self.sql_tag:
            self.sql_tag.validate()
        if self.trend:
            for v1 in self.trend:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.avg_cputime is not None:
            result['AvgCPUTime'] = self.avg_cputime

        if self.avg_cputime_seconds is not None:
            result['AvgCPUTimeSeconds'] = self.avg_cputime_seconds

        if self.avg_doc_examined is not None:
            result['AvgDocExamined'] = self.avg_doc_examined

        if self.avg_frows is not None:
            result['AvgFrows'] = self.avg_frows

        if self.avg_iowrites is not None:
            result['AvgIOWrites'] = self.avg_iowrites

        if self.avg_keys_examined is not None:
            result['AvgKeysExamined'] = self.avg_keys_examined

        if self.avg_last_rows_count_affected is not None:
            result['AvgLastRowsCountAffected'] = self.avg_last_rows_count_affected

        if self.avg_lock_time is not None:
            result['AvgLockTime'] = self.avg_lock_time

        if self.avg_lock_time_seconds is not None:
            result['AvgLockTimeSeconds'] = self.avg_lock_time_seconds

        if self.avg_logical_ioreads is not None:
            result['AvgLogicalIOReads'] = self.avg_logical_ioreads

        if self.avg_physical_ioreads is not None:
            result['AvgPhysicalIOReads'] = self.avg_physical_ioreads

        if self.avg_query_time is not None:
            result['AvgQueryTime'] = self.avg_query_time

        if self.avg_query_time_seconds is not None:
            result['AvgQueryTimeSeconds'] = self.avg_query_time_seconds

        if self.avg_request_size is not None:
            result['AvgRequestSize'] = self.avg_request_size

        if self.avg_response_size is not None:
            result['AvgResponseSize'] = self.avg_response_size

        if self.avg_return_num is not None:
            result['AvgReturnNum'] = self.avg_return_num

        if self.avg_rows is not None:
            result['AvgRows'] = self.avg_rows

        if self.avg_rows_count_affected is not None:
            result['AvgRowsCountAffected'] = self.avg_rows_count_affected

        if self.avg_rows_examined is not None:
            result['AvgRowsExamined'] = self.avg_rows_examined

        if self.avg_rows_sent is not None:
            result['AvgRowsSent'] = self.avg_rows_sent

        if self.avg_rt is not None:
            result['AvgRt'] = self.avg_rt

        if self.avg_scnt is not None:
            result['AvgScnt'] = self.avg_scnt

        if self.cputime is not None:
            result['CPUTime'] = self.cputime

        if self.cputime_seconds is not None:
            result['CPUTimeSeconds'] = self.cputime_seconds

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.cmd is not None:
            result['Cmd'] = self.cmd

        if self.command is not None:
            result['Command'] = self.command

        if self.count is not None:
            result['Count'] = self.count

        if self.count_rate is not None:
            result['CountRate'] = self.count_rate

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.database is not None:
            result['Database'] = self.database

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name

        if self.doc_examined is not None:
            result['DocExamined'] = self.doc_examined

        if self.docs_examined is not None:
            result['DocsExamined'] = self.docs_examined

        if self.frows is not None:
            result['Frows'] = self.frows

        if self.histogram is not None:
            result['Histogram'] = self.histogram.to_map()

        if self.host_address is not None:
            result['HostAddress'] = self.host_address

        if self.host_ins_id is not None:
            result['HostInsId'] = self.host_ins_id

        if self.iowrites is not None:
            result['IOWrites'] = self.iowrites

        if self.ins_name is not None:
            result['InsName'] = self.ins_name

        if self.ins_role is not None:
            result['InsRole'] = self.ins_role

        if self.keys_examined is not None:
            result['KeysExamined'] = self.keys_examined

        if self.last_rows_count_affected is not None:
            result['LastRowsCountAffected'] = self.last_rows_count_affected

        if self.lock_time is not None:
            result['LockTime'] = self.lock_time

        if self.lock_time_seconds is not None:
            result['LockTimeSeconds'] = self.lock_time_seconds

        if self.logical_ioreads is not None:
            result['LogicalIOReads'] = self.logical_ioreads

        if self.max_cputime is not None:
            result['MaxCPUTime'] = self.max_cputime

        if self.max_cputime_seconds is not None:
            result['MaxCPUTimeSeconds'] = self.max_cputime_seconds

        if self.max_doc_examined is not None:
            result['MaxDocExamined'] = self.max_doc_examined

        if self.max_frows is not None:
            result['MaxFrows'] = self.max_frows

        if self.max_iowrites is not None:
            result['MaxIOWrites'] = self.max_iowrites

        if self.max_keys_examined is not None:
            result['MaxKeysExamined'] = self.max_keys_examined

        if self.max_last_rows_count_affected is not None:
            result['MaxLastRowsCountAffected'] = self.max_last_rows_count_affected

        if self.max_lock_time is not None:
            result['MaxLockTime'] = self.max_lock_time

        if self.max_lock_time_seconds is not None:
            result['MaxLockTimeSeconds'] = self.max_lock_time_seconds

        if self.max_logical_ioreads is not None:
            result['MaxLogicalIOReads'] = self.max_logical_ioreads

        if self.max_physical_ioreads is not None:
            result['MaxPhysicalIOReads'] = self.max_physical_ioreads

        if self.max_query_time is not None:
            result['MaxQueryTime'] = self.max_query_time

        if self.max_query_time_seconds is not None:
            result['MaxQueryTimeSeconds'] = self.max_query_time_seconds

        if self.max_request_size is not None:
            result['MaxRequestSize'] = self.max_request_size

        if self.max_response_size is not None:
            result['MaxResponseSize'] = self.max_response_size

        if self.max_return_num is not None:
            result['MaxReturnNum'] = self.max_return_num

        if self.max_rows is not None:
            result['MaxRows'] = self.max_rows

        if self.max_rows_count_affected is not None:
            result['MaxRowsCountAffected'] = self.max_rows_count_affected

        if self.max_rows_examined is not None:
            result['MaxRowsExamined'] = self.max_rows_examined

        if self.max_rows_sent is not None:
            result['MaxRowsSent'] = self.max_rows_sent

        if self.max_rt is not None:
            result['MaxRt'] = self.max_rt

        if self.max_scnt is not None:
            result['MaxScnt'] = self.max_scnt

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.op_type is not None:
            result['OpType'] = self.op_type

        if self.origin_alias is not None:
            result['OriginAlias'] = self.origin_alias

        if self.physical_ioreads is not None:
            result['PhysicalIOReads'] = self.physical_ioreads

        if self.psql is not None:
            result['Psql'] = self.psql

        if self.query_id is not None:
            result['QueryId'] = self.query_id

        if self.query_start_time is not None:
            result['QueryStartTime'] = self.query_start_time

        if self.query_time is not None:
            result['QueryTime'] = self.query_time

        if self.query_time_rate is not None:
            result['QueryTimeRate'] = self.query_time_rate

        if self.query_time_seconds is not None:
            result['QueryTimeSeconds'] = self.query_time_seconds

        if self.return_item_numbers is not None:
            result['ReturnItemNumbers'] = self.return_item_numbers

        if self.return_num is not None:
            result['ReturnNum'] = self.return_num

        if self.rows is not None:
            result['Rows'] = self.rows

        if self.rows_count_affected is not None:
            result['RowsCountAffected'] = self.rows_count_affected

        if self.rows_examined is not None:
            result['RowsExamined'] = self.rows_examined

        if self.rows_sent is not None:
            result['RowsSent'] = self.rows_sent

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.sqltext is not None:
            result['SQLText'] = self.sqltext

        if self.scheme is not None:
            result['Scheme'] = self.scheme

        if self.scnt is not None:
            result['Scnt'] = self.scnt

        if self.sql_id is not None:
            result['SqlId'] = self.sql_id

        if self.sql_tag is not None:
            result['SqlTag'] = self.sql_tag.to_map()

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        if self.sub_instance_id is not None:
            result['SubInstanceId'] = self.sub_instance_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.thread_id is not None:
            result['ThreadId'] = self.thread_id

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['Trend'] = []
        if self.trend is not None:
            for k1 in self.trend:
                result['Trend'].append(k1.to_map() if k1 else None)

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AvgCPUTime') is not None:
            self.avg_cputime = m.get('AvgCPUTime')

        if m.get('AvgCPUTimeSeconds') is not None:
            self.avg_cputime_seconds = m.get('AvgCPUTimeSeconds')

        if m.get('AvgDocExamined') is not None:
            self.avg_doc_examined = m.get('AvgDocExamined')

        if m.get('AvgFrows') is not None:
            self.avg_frows = m.get('AvgFrows')

        if m.get('AvgIOWrites') is not None:
            self.avg_iowrites = m.get('AvgIOWrites')

        if m.get('AvgKeysExamined') is not None:
            self.avg_keys_examined = m.get('AvgKeysExamined')

        if m.get('AvgLastRowsCountAffected') is not None:
            self.avg_last_rows_count_affected = m.get('AvgLastRowsCountAffected')

        if m.get('AvgLockTime') is not None:
            self.avg_lock_time = m.get('AvgLockTime')

        if m.get('AvgLockTimeSeconds') is not None:
            self.avg_lock_time_seconds = m.get('AvgLockTimeSeconds')

        if m.get('AvgLogicalIOReads') is not None:
            self.avg_logical_ioreads = m.get('AvgLogicalIOReads')

        if m.get('AvgPhysicalIOReads') is not None:
            self.avg_physical_ioreads = m.get('AvgPhysicalIOReads')

        if m.get('AvgQueryTime') is not None:
            self.avg_query_time = m.get('AvgQueryTime')

        if m.get('AvgQueryTimeSeconds') is not None:
            self.avg_query_time_seconds = m.get('AvgQueryTimeSeconds')

        if m.get('AvgRequestSize') is not None:
            self.avg_request_size = m.get('AvgRequestSize')

        if m.get('AvgResponseSize') is not None:
            self.avg_response_size = m.get('AvgResponseSize')

        if m.get('AvgReturnNum') is not None:
            self.avg_return_num = m.get('AvgReturnNum')

        if m.get('AvgRows') is not None:
            self.avg_rows = m.get('AvgRows')

        if m.get('AvgRowsCountAffected') is not None:
            self.avg_rows_count_affected = m.get('AvgRowsCountAffected')

        if m.get('AvgRowsExamined') is not None:
            self.avg_rows_examined = m.get('AvgRowsExamined')

        if m.get('AvgRowsSent') is not None:
            self.avg_rows_sent = m.get('AvgRowsSent')

        if m.get('AvgRt') is not None:
            self.avg_rt = m.get('AvgRt')

        if m.get('AvgScnt') is not None:
            self.avg_scnt = m.get('AvgScnt')

        if m.get('CPUTime') is not None:
            self.cputime = m.get('CPUTime')

        if m.get('CPUTimeSeconds') is not None:
            self.cputime_seconds = m.get('CPUTimeSeconds')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('Cmd') is not None:
            self.cmd = m.get('Cmd')

        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CountRate') is not None:
            self.count_rate = m.get('CountRate')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')

        if m.get('DocExamined') is not None:
            self.doc_examined = m.get('DocExamined')

        if m.get('DocsExamined') is not None:
            self.docs_examined = m.get('DocsExamined')

        if m.get('Frows') is not None:
            self.frows = m.get('Frows')

        if m.get('Histogram') is not None:
            temp_model = main_models.DescribeSlowLogStatisticResponseBodyDataDataLogsHistogram()
            self.histogram = temp_model.from_map(m.get('Histogram'))

        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')

        if m.get('HostInsId') is not None:
            self.host_ins_id = m.get('HostInsId')

        if m.get('IOWrites') is not None:
            self.iowrites = m.get('IOWrites')

        if m.get('InsName') is not None:
            self.ins_name = m.get('InsName')

        if m.get('InsRole') is not None:
            self.ins_role = m.get('InsRole')

        if m.get('KeysExamined') is not None:
            self.keys_examined = m.get('KeysExamined')

        if m.get('LastRowsCountAffected') is not None:
            self.last_rows_count_affected = m.get('LastRowsCountAffected')

        if m.get('LockTime') is not None:
            self.lock_time = m.get('LockTime')

        if m.get('LockTimeSeconds') is not None:
            self.lock_time_seconds = m.get('LockTimeSeconds')

        if m.get('LogicalIOReads') is not None:
            self.logical_ioreads = m.get('LogicalIOReads')

        if m.get('MaxCPUTime') is not None:
            self.max_cputime = m.get('MaxCPUTime')

        if m.get('MaxCPUTimeSeconds') is not None:
            self.max_cputime_seconds = m.get('MaxCPUTimeSeconds')

        if m.get('MaxDocExamined') is not None:
            self.max_doc_examined = m.get('MaxDocExamined')

        if m.get('MaxFrows') is not None:
            self.max_frows = m.get('MaxFrows')

        if m.get('MaxIOWrites') is not None:
            self.max_iowrites = m.get('MaxIOWrites')

        if m.get('MaxKeysExamined') is not None:
            self.max_keys_examined = m.get('MaxKeysExamined')

        if m.get('MaxLastRowsCountAffected') is not None:
            self.max_last_rows_count_affected = m.get('MaxLastRowsCountAffected')

        if m.get('MaxLockTime') is not None:
            self.max_lock_time = m.get('MaxLockTime')

        if m.get('MaxLockTimeSeconds') is not None:
            self.max_lock_time_seconds = m.get('MaxLockTimeSeconds')

        if m.get('MaxLogicalIOReads') is not None:
            self.max_logical_ioreads = m.get('MaxLogicalIOReads')

        if m.get('MaxPhysicalIOReads') is not None:
            self.max_physical_ioreads = m.get('MaxPhysicalIOReads')

        if m.get('MaxQueryTime') is not None:
            self.max_query_time = m.get('MaxQueryTime')

        if m.get('MaxQueryTimeSeconds') is not None:
            self.max_query_time_seconds = m.get('MaxQueryTimeSeconds')

        if m.get('MaxRequestSize') is not None:
            self.max_request_size = m.get('MaxRequestSize')

        if m.get('MaxResponseSize') is not None:
            self.max_response_size = m.get('MaxResponseSize')

        if m.get('MaxReturnNum') is not None:
            self.max_return_num = m.get('MaxReturnNum')

        if m.get('MaxRows') is not None:
            self.max_rows = m.get('MaxRows')

        if m.get('MaxRowsCountAffected') is not None:
            self.max_rows_count_affected = m.get('MaxRowsCountAffected')

        if m.get('MaxRowsExamined') is not None:
            self.max_rows_examined = m.get('MaxRowsExamined')

        if m.get('MaxRowsSent') is not None:
            self.max_rows_sent = m.get('MaxRowsSent')

        if m.get('MaxRt') is not None:
            self.max_rt = m.get('MaxRt')

        if m.get('MaxScnt') is not None:
            self.max_scnt = m.get('MaxScnt')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')

        if m.get('OriginAlias') is not None:
            self.origin_alias = m.get('OriginAlias')

        if m.get('PhysicalIOReads') is not None:
            self.physical_ioreads = m.get('PhysicalIOReads')

        if m.get('Psql') is not None:
            self.psql = m.get('Psql')

        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')

        if m.get('QueryStartTime') is not None:
            self.query_start_time = m.get('QueryStartTime')

        if m.get('QueryTime') is not None:
            self.query_time = m.get('QueryTime')

        if m.get('QueryTimeRate') is not None:
            self.query_time_rate = m.get('QueryTimeRate')

        if m.get('QueryTimeSeconds') is not None:
            self.query_time_seconds = m.get('QueryTimeSeconds')

        if m.get('ReturnItemNumbers') is not None:
            self.return_item_numbers = m.get('ReturnItemNumbers')

        if m.get('ReturnNum') is not None:
            self.return_num = m.get('ReturnNum')

        if m.get('Rows') is not None:
            self.rows = m.get('Rows')

        if m.get('RowsCountAffected') is not None:
            self.rows_count_affected = m.get('RowsCountAffected')

        if m.get('RowsExamined') is not None:
            self.rows_examined = m.get('RowsExamined')

        if m.get('RowsSent') is not None:
            self.rows_sent = m.get('RowsSent')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')

        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')

        if m.get('Scnt') is not None:
            self.scnt = m.get('Scnt')

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        if m.get('SqlTag') is not None:
            temp_model = main_models.DescribeSlowLogStatisticResponseBodyDataDataLogsSqlTag()
            self.sql_tag = temp_model.from_map(m.get('SqlTag'))

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('SubInstanceId') is not None:
            self.sub_instance_id = m.get('SubInstanceId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('ThreadId') is not None:
            self.thread_id = m.get('ThreadId')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.trend = []
        if m.get('Trend') is not None:
            for k1 in m.get('Trend'):
                temp_model = main_models.DescribeSlowLogStatisticResponseBodyDataDataLogsTrend()
                self.trend.append(temp_model.from_map(k1))

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

class DescribeSlowLogStatisticResponseBodyDataDataLogsTrend(DaraModel):
    def __init__(
        self,
        timestamp: int = None,
        value: Any = None,
    ):
        self.timestamp = timestamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeSlowLogStatisticResponseBodyDataDataLogsSqlTag(DaraModel):
    def __init__(
        self,
        comments: str = None,
        sql_id: str = None,
        tags: str = None,
    ):
        self.comments = comments
        # SQL ID。
        self.sql_id = sql_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comments is not None:
            result['Comments'] = self.comments

        if self.sql_id is not None:
            result['SqlId'] = self.sql_id

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

class DescribeSlowLogStatisticResponseBodyDataDataLogsHistogram(DaraModel):
    def __init__(
        self,
        avg_lock_time: List[float] = None,
        avg_rows_examined: List[float] = None,
        avg_rows_sent: List[float] = None,
        avg_rt: List[float] = None,
        count: List[int] = None,
        item: List[main_models.DescribeSlowLogStatisticResponseBodyDataDataLogsHistogramItem] = None,
        lock_time: List[float] = None,
        max_lock_time: List[float] = None,
        max_rows_examined: List[int] = None,
        max_rows_sent: List[int] = None,
        max_rt: List[float] = None,
        rows_examined: List[int] = None,
        rows_sent: List[int] = None,
        rt: List[float] = None,
        total: int = None,
        ts: List[int] = None,
        ts_end: List[int] = None,
    ):
        self.avg_lock_time = avg_lock_time
        self.avg_rows_examined = avg_rows_examined
        self.avg_rows_sent = avg_rows_sent
        self.avg_rt = avg_rt
        self.count = count
        self.item = item
        self.lock_time = lock_time
        self.max_lock_time = max_lock_time
        self.max_rows_examined = max_rows_examined
        self.max_rows_sent = max_rows_sent
        self.max_rt = max_rt
        self.rows_examined = rows_examined
        self.rows_sent = rows_sent
        self.rt = rt
        self.total = total
        self.ts = ts
        self.ts_end = ts_end

    def validate(self):
        if self.item:
            for v1 in self.item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_lock_time is not None:
            result['AvgLockTime'] = self.avg_lock_time

        if self.avg_rows_examined is not None:
            result['AvgRowsExamined'] = self.avg_rows_examined

        if self.avg_rows_sent is not None:
            result['AvgRowsSent'] = self.avg_rows_sent

        if self.avg_rt is not None:
            result['AvgRt'] = self.avg_rt

        if self.count is not None:
            result['Count'] = self.count

        result['Item'] = []
        if self.item is not None:
            for k1 in self.item:
                result['Item'].append(k1.to_map() if k1 else None)

        if self.lock_time is not None:
            result['LockTime'] = self.lock_time

        if self.max_lock_time is not None:
            result['MaxLockTime'] = self.max_lock_time

        if self.max_rows_examined is not None:
            result['MaxRowsExamined'] = self.max_rows_examined

        if self.max_rows_sent is not None:
            result['MaxRowsSent'] = self.max_rows_sent

        if self.max_rt is not None:
            result['MaxRt'] = self.max_rt

        if self.rows_examined is not None:
            result['RowsExamined'] = self.rows_examined

        if self.rows_sent is not None:
            result['RowsSent'] = self.rows_sent

        if self.rt is not None:
            result['Rt'] = self.rt

        if self.total is not None:
            result['Total'] = self.total

        if self.ts is not None:
            result['Ts'] = self.ts

        if self.ts_end is not None:
            result['TsEnd'] = self.ts_end

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgLockTime') is not None:
            self.avg_lock_time = m.get('AvgLockTime')

        if m.get('AvgRowsExamined') is not None:
            self.avg_rows_examined = m.get('AvgRowsExamined')

        if m.get('AvgRowsSent') is not None:
            self.avg_rows_sent = m.get('AvgRowsSent')

        if m.get('AvgRt') is not None:
            self.avg_rt = m.get('AvgRt')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.item = []
        if m.get('Item') is not None:
            for k1 in m.get('Item'):
                temp_model = main_models.DescribeSlowLogStatisticResponseBodyDataDataLogsHistogramItem()
                self.item.append(temp_model.from_map(k1))

        if m.get('LockTime') is not None:
            self.lock_time = m.get('LockTime')

        if m.get('MaxLockTime') is not None:
            self.max_lock_time = m.get('MaxLockTime')

        if m.get('MaxRowsExamined') is not None:
            self.max_rows_examined = m.get('MaxRowsExamined')

        if m.get('MaxRowsSent') is not None:
            self.max_rows_sent = m.get('MaxRowsSent')

        if m.get('MaxRt') is not None:
            self.max_rt = m.get('MaxRt')

        if m.get('RowsExamined') is not None:
            self.rows_examined = m.get('RowsExamined')

        if m.get('RowsSent') is not None:
            self.rows_sent = m.get('RowsSent')

        if m.get('Rt') is not None:
            self.rt = m.get('Rt')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('Ts') is not None:
            self.ts = m.get('Ts')

        if m.get('TsEnd') is not None:
            self.ts_end = m.get('TsEnd')

        return self

class DescribeSlowLogStatisticResponseBodyDataDataLogsHistogramItem(DaraModel):
    def __init__(
        self,
        count: List[int] = None,
        node_id: str = None,
    ):
        self.count = count
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self

