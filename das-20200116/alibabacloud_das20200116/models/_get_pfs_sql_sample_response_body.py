# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetPfsSqlSampleResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.GetPfsSqlSampleResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The SQL sample data.
        self.data = data
        # The returned message.
        # 
        # >  If the request was successful, **Successful** is returned. If the request failed, an error message such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetPfsSqlSampleResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetPfsSqlSampleResponseBodyData(DaraModel):
    def __init__(
        self,
        create_tmp_disk_tables: int = None,
        create_tmp_tables: int = None,
        db: str = None,
        end_event_id: int = None,
        errors: int = None,
        event_id: int = None,
        event_name: str = None,
        instance_id: str = None,
        latency: float = None,
        lock_latency: float = None,
        logic_id: str = None,
        no_good_index_used: int = None,
        no_index_used: int = None,
        node_id: str = None,
        rows_affected: int = None,
        rows_examined: int = None,
        rows_sent: int = None,
        select_full_join: int = None,
        select_full_range_join: int = None,
        select_range: int = None,
        select_range_check: int = None,
        select_scan: int = None,
        sort_merge_passes: int = None,
        sort_range: int = None,
        sort_rows: int = None,
        sort_scan: int = None,
        sql: str = None,
        sql_id: str = None,
        thread_id: int = None,
        timestamp: int = None,
        user_id: str = None,
        warnings: int = None,
    ):
        # The number of internal on-disk temporary tables that were created when the SQL statement was executed.
        self.create_tmp_disk_tables = create_tmp_disk_tables
        # The number of internal temporary tables that were created when the SQL statement was executed.
        self.create_tmp_tables = create_tmp_tables
        # The name of the database.
        self.db = db
        # The end ID of the event. By default, the value of this parameter is NULL when the event starts and is changed to the event ID when the event ends.
        self.end_event_id = end_event_id
        # The number of errors returned for the SQL statement.
        self.errors = errors
        # The event ID.
        self.event_id = event_id
        # The name of the event.
        self.event_name = event_name
        # The instance ID.
        self.instance_id = instance_id
        # The execution duration. Unit: millisecond.
        self.latency = latency
        # The lock wait duration. Unit: millisecond.
        self.lock_latency = lock_latency
        # The ID of the logical database.
        self.logic_id = logic_id
        # Indicates whether the server failed to find an index that can be used for the SQL statement. Valid values:
        # 
        # *   **1**: yes.
        # *   **0**: no.
        self.no_good_index_used = no_good_index_used
        # Indicates whether table scans were performed when indexes were not used. Valid values:
        # 
        # *   **1**: yes.
        # *   **0**: no.
        self.no_index_used = no_index_used
        # The node ID.
        # 
        # >  This parameter is returned only for ApsaraDB RDS for MySQL Cluster Edition instances or PolarDB for MySQL clusters.
        self.node_id = node_id
        # The number of rows affected by the SQL statement.
        self.rows_affected = rows_affected
        # The number of rows scanned by the SQL statement.
        self.rows_examined = rows_examined
        # The number of rows returned by the SQL statement.
        self.rows_sent = rows_sent
        # The number of joins that are used to perform table scans without using indexes.
        # 
        # > : This parameter is used for the scenario in which indexes are not used in a union query. If the returned value is not 0, check the indexes of tables.
        self.select_full_join = select_full_join
        # The number of joins that used ranges on referenced tables.
        self.select_full_range_join = select_full_range_join
        # The number of joins that used ranges on the first table.
        self.select_range = select_range
        # The number of joins that did not have key values. The keys and values were checked for each row of data.
        # 
        # > : This parameter is used for the scenario in which indexes are not used in a union query. If the returned value is not 0, check the indexes of tables.
        self.select_range_check = select_range_check
        # The number of scans.
        self.select_scan = select_scan
        # The number of merges that the sorting algorithm must perform.
        self.sort_merge_passes = sort_merge_passes
        # The number of times the data was sorted by using ranges.
        self.sort_range = sort_range
        # The number of sorted rows.
        self.sort_rows = sort_rows
        # The number of sorts that were performed during table scans.
        self.sort_scan = sort_scan
        # The sample SQL statement.
        self.sql = sql
        # The SQL statement ID.
        self.sql_id = sql_id
        # The thread ID.
        self.thread_id = thread_id
        # The time when the SQL statement was executed. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.timestamp = timestamp
        # The user ID.
        self.user_id = user_id
        # The number of warnings returned for the SQL statement.
        self.warnings = warnings

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_tmp_disk_tables is not None:
            result['CreateTmpDiskTables'] = self.create_tmp_disk_tables

        if self.create_tmp_tables is not None:
            result['CreateTmpTables'] = self.create_tmp_tables

        if self.db is not None:
            result['Db'] = self.db

        if self.end_event_id is not None:
            result['EndEventId'] = self.end_event_id

        if self.errors is not None:
            result['Errors'] = self.errors

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.latency is not None:
            result['Latency'] = self.latency

        if self.lock_latency is not None:
            result['LockLatency'] = self.lock_latency

        if self.logic_id is not None:
            result['LogicId'] = self.logic_id

        if self.no_good_index_used is not None:
            result['NoGoodIndexUsed'] = self.no_good_index_used

        if self.no_index_used is not None:
            result['NoIndexUsed'] = self.no_index_used

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.rows_affected is not None:
            result['RowsAffected'] = self.rows_affected

        if self.rows_examined is not None:
            result['RowsExamined'] = self.rows_examined

        if self.rows_sent is not None:
            result['RowsSent'] = self.rows_sent

        if self.select_full_join is not None:
            result['SelectFullJoin'] = self.select_full_join

        if self.select_full_range_join is not None:
            result['SelectFullRangeJoin'] = self.select_full_range_join

        if self.select_range is not None:
            result['SelectRange'] = self.select_range

        if self.select_range_check is not None:
            result['SelectRangeCheck'] = self.select_range_check

        if self.select_scan is not None:
            result['SelectScan'] = self.select_scan

        if self.sort_merge_passes is not None:
            result['SortMergePasses'] = self.sort_merge_passes

        if self.sort_range is not None:
            result['SortRange'] = self.sort_range

        if self.sort_rows is not None:
            result['SortRows'] = self.sort_rows

        if self.sort_scan is not None:
            result['SortScan'] = self.sort_scan

        if self.sql is not None:
            result['Sql'] = self.sql

        if self.sql_id is not None:
            result['SqlId'] = self.sql_id

        if self.thread_id is not None:
            result['ThreadId'] = self.thread_id

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.warnings is not None:
            result['Warnings'] = self.warnings

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTmpDiskTables') is not None:
            self.create_tmp_disk_tables = m.get('CreateTmpDiskTables')

        if m.get('CreateTmpTables') is not None:
            self.create_tmp_tables = m.get('CreateTmpTables')

        if m.get('Db') is not None:
            self.db = m.get('Db')

        if m.get('EndEventId') is not None:
            self.end_event_id = m.get('EndEventId')

        if m.get('Errors') is not None:
            self.errors = m.get('Errors')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Latency') is not None:
            self.latency = m.get('Latency')

        if m.get('LockLatency') is not None:
            self.lock_latency = m.get('LockLatency')

        if m.get('LogicId') is not None:
            self.logic_id = m.get('LogicId')

        if m.get('NoGoodIndexUsed') is not None:
            self.no_good_index_used = m.get('NoGoodIndexUsed')

        if m.get('NoIndexUsed') is not None:
            self.no_index_used = m.get('NoIndexUsed')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('RowsAffected') is not None:
            self.rows_affected = m.get('RowsAffected')

        if m.get('RowsExamined') is not None:
            self.rows_examined = m.get('RowsExamined')

        if m.get('RowsSent') is not None:
            self.rows_sent = m.get('RowsSent')

        if m.get('SelectFullJoin') is not None:
            self.select_full_join = m.get('SelectFullJoin')

        if m.get('SelectFullRangeJoin') is not None:
            self.select_full_range_join = m.get('SelectFullRangeJoin')

        if m.get('SelectRange') is not None:
            self.select_range = m.get('SelectRange')

        if m.get('SelectRangeCheck') is not None:
            self.select_range_check = m.get('SelectRangeCheck')

        if m.get('SelectScan') is not None:
            self.select_scan = m.get('SelectScan')

        if m.get('SortMergePasses') is not None:
            self.sort_merge_passes = m.get('SortMergePasses')

        if m.get('SortRange') is not None:
            self.sort_range = m.get('SortRange')

        if m.get('SortRows') is not None:
            self.sort_rows = m.get('SortRows')

        if m.get('SortScan') is not None:
            self.sort_scan = m.get('SortScan')

        if m.get('Sql') is not None:
            self.sql = m.get('Sql')

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        if m.get('ThreadId') is not None:
            self.thread_id = m.get('ThreadId')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Warnings') is not None:
            self.warnings = m.get('Warnings')

        return self

