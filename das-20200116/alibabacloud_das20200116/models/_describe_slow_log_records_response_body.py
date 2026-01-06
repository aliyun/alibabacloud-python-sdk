# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class DescribeSlowLogRecordsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeSlowLogRecordsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        # DBLogRecords<SlowLogItem>
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
            temp_model = main_models.DescribeSlowLogRecordsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSlowLogRecordsResponseBodyData(DaraModel):
    def __init__(
        self,
        db_instance_id: int = None,
        db_instance_name: str = None,
        end_time: str = None,
        items_numbers: int = None,
        logs: List[main_models.DescribeSlowLogRecordsResponseBodyDataLogs] = None,
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
                temp_model = main_models.DescribeSlowLogRecordsResponseBodyDataLogs()
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

class DescribeSlowLogRecordsResponseBodyDataLogs(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        application_name: str = None,
        cputime: float = None,
        cputime_seconds: float = None,
        client_ip: str = None,
        cmd: str = None,
        command: str = None,
        dbname: str = None,
        db_id: str = None,
        db_instance_name: str = None,
        docs_examined: str = None,
        frows: int = None,
        host_address: str = None,
        iowrites: int = None,
        ins_name: str = None,
        keys_examined: str = None,
        last_rows_count_affected: int = None,
        lock_time: float = None,
        lock_time_seconds: float = None,
        logical_ioreads: int = None,
        namespace: str = None,
        node_id: str = None,
        op_type: str = None,
        origin_time: str = None,
        physical_ioreads: int = None,
        psql: str = None,
        query_id: str = None,
        query_start_time: str = None,
        query_time: int = None,
        query_time_seconds: float = None,
        request_size: int = None,
        response_size: int = None,
        return_item_numbers: str = None,
        return_num: str = None,
        rows: int = None,
        rows_count_affected: int = None,
        rows_examined: int = None,
        rows_sent: int = None,
        rt: int = None,
        sqltext: str = None,
        scheme: str = None,
        scnt: int = None,
        sql_id: str = None,
        sql_tag: main_models.DescribeSlowLogRecordsResponseBodyDataLogsSqlTag = None,
        sql_type: str = None,
        sub_instance_id: str = None,
        table_name: str = None,
        template_id: str = None,
        thread_id: str = None,
        timestamp: int = None,
        trace_id: str = None,
    ):
        self.account_name = account_name
        self.application_name = application_name
        self.cputime = cputime
        self.cputime_seconds = cputime_seconds
        self.client_ip = client_ip
        self.cmd = cmd
        self.command = command
        self.dbname = dbname
        self.db_id = db_id
        self.db_instance_name = db_instance_name
        self.docs_examined = docs_examined
        self.frows = frows
        self.host_address = host_address
        self.iowrites = iowrites
        self.ins_name = ins_name
        self.keys_examined = keys_examined
        self.last_rows_count_affected = last_rows_count_affected
        self.lock_time = lock_time
        self.lock_time_seconds = lock_time_seconds
        self.logical_ioreads = logical_ioreads
        self.namespace = namespace
        self.node_id = node_id
        self.op_type = op_type
        self.origin_time = origin_time
        self.physical_ioreads = physical_ioreads
        self.psql = psql
        self.query_id = query_id
        self.query_start_time = query_start_time
        self.query_time = query_time
        self.query_time_seconds = query_time_seconds
        self.request_size = request_size
        self.response_size = response_size
        self.return_item_numbers = return_item_numbers
        self.return_num = return_num
        self.rows = rows
        self.rows_count_affected = rows_count_affected
        self.rows_examined = rows_examined
        self.rows_sent = rows_sent
        self.rt = rt
        self.sqltext = sqltext
        self.scheme = scheme
        self.scnt = scnt
        self.sql_id = sql_id
        self.sql_tag = sql_tag
        self.sql_type = sql_type
        self.sub_instance_id = sub_instance_id
        self.table_name = table_name
        self.template_id = template_id
        self.thread_id = thread_id
        self.timestamp = timestamp
        self.trace_id = trace_id

    def validate(self):
        if self.sql_tag:
            self.sql_tag.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

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

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name

        if self.docs_examined is not None:
            result['DocsExamined'] = self.docs_examined

        if self.frows is not None:
            result['Frows'] = self.frows

        if self.host_address is not None:
            result['HostAddress'] = self.host_address

        if self.iowrites is not None:
            result['IOWrites'] = self.iowrites

        if self.ins_name is not None:
            result['InsName'] = self.ins_name

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

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.op_type is not None:
            result['OpType'] = self.op_type

        if self.origin_time is not None:
            result['OriginTime'] = self.origin_time

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

        if self.query_time_seconds is not None:
            result['QueryTimeSeconds'] = self.query_time_seconds

        if self.request_size is not None:
            result['RequestSize'] = self.request_size

        if self.response_size is not None:
            result['ResponseSize'] = self.response_size

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

        if self.rt is not None:
            result['Rt'] = self.rt

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

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.thread_id is not None:
            result['ThreadId'] = self.thread_id

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

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

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')

        if m.get('DocsExamined') is not None:
            self.docs_examined = m.get('DocsExamined')

        if m.get('Frows') is not None:
            self.frows = m.get('Frows')

        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')

        if m.get('IOWrites') is not None:
            self.iowrites = m.get('IOWrites')

        if m.get('InsName') is not None:
            self.ins_name = m.get('InsName')

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

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')

        if m.get('OriginTime') is not None:
            self.origin_time = m.get('OriginTime')

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

        if m.get('QueryTimeSeconds') is not None:
            self.query_time_seconds = m.get('QueryTimeSeconds')

        if m.get('RequestSize') is not None:
            self.request_size = m.get('RequestSize')

        if m.get('ResponseSize') is not None:
            self.response_size = m.get('ResponseSize')

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

        if m.get('Rt') is not None:
            self.rt = m.get('Rt')

        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')

        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')

        if m.get('Scnt') is not None:
            self.scnt = m.get('Scnt')

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        if m.get('SqlTag') is not None:
            temp_model = main_models.DescribeSlowLogRecordsResponseBodyDataLogsSqlTag()
            self.sql_tag = temp_model.from_map(m.get('SqlTag'))

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('SubInstanceId') is not None:
            self.sub_instance_id = m.get('SubInstanceId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('ThreadId') is not None:
            self.thread_id = m.get('ThreadId')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class DescribeSlowLogRecordsResponseBodyDataLogsSqlTag(DaraModel):
    def __init__(
        self,
        comments: str = None,
        sql_id: str = None,
        tags: str = None,
    ):
        self.comments = comments
        # sqlid。
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

