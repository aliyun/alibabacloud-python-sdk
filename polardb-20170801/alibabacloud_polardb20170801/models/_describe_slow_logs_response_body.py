# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeSlowLogsResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        engine: str = None,
        items: main_models.DescribeSlowLogsResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        start_time: str = None,
        total_record_count: int = None,
    ):
        # The ID of cluster.
        self.dbcluster_id = dbcluster_id
        # The end date of the query.
        self.end_time = end_time
        # The type of the database engine.
        self.engine = engine
        # Details about slow query logs.
        self.items = items
        # The number of the returned page.
        self.page_number = page_number
        # The number of SQL statements that are returned on the current page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id
        # The start date of the query.
        self.start_time = start_time
        # The total number of returned entries.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

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
        create_time: str = None,
        dbname: str = None,
        dbnode_id: str = None,
        max_execution_time: int = None,
        max_execution_time_ms: str = None,
        max_lock_time: int = None,
        parse_max_row_count: int = None,
        parse_total_row_counts: int = None,
        return_max_row_count: int = None,
        return_total_row_counts: int = None,
        sqlhash: str = None,
        sqltext: str = None,
        total_execution_counts: int = None,
        total_execution_times: int = None,
        total_lock_times: int = None,
    ):
        # The date when the data was generated.
        self.create_time = create_time
        # The name of the database.
        self.dbname = dbname
        # The ID of the node.
        self.dbnode_id = dbnode_id
        # The longest execution duration of a specific SQL statement in the query. Unit: seconds.
        self.max_execution_time = max_execution_time
        self.max_execution_time_ms = max_execution_time_ms
        # The longest lock duration that was caused by a specific SQL statement in the query. Unit: seconds.
        self.max_lock_time = max_lock_time
        # The largest number of rows that were parsed by a specific SQL statement in the query.
        self.parse_max_row_count = parse_max_row_count
        # The total number of rows that were parsed by all SQL statements in the query.
        self.parse_total_row_counts = parse_total_row_counts
        # The largest number of rows that were returned by a specific SQL statement in the query.
        self.return_max_row_count = return_max_row_count
        # The total number of rows that were returned by all SQL statements in the query.
        self.return_total_row_counts = return_total_row_counts
        # The unique ID of the SQL statement. The ID is used to obtain the slow query logs of the SQL statement.
        self.sqlhash = sqlhash
        # The SQL statement that is executed in the query.
        self.sqltext = sqltext
        # The total number of executions of the SQL statements.
        self.total_execution_counts = total_execution_counts
        # The total duration that was caused by all SQL statements in the query. Unit: seconds.
        self.total_execution_times = total_execution_times
        # The total lock duration that was caused by all SQL statements in the query. Unit: seconds.
        self.total_lock_times = total_lock_times

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id

        if self.max_execution_time is not None:
            result['MaxExecutionTime'] = self.max_execution_time

        if self.max_execution_time_ms is not None:
            result['MaxExecutionTimeMs'] = self.max_execution_time_ms

        if self.max_lock_time is not None:
            result['MaxLockTime'] = self.max_lock_time

        if self.parse_max_row_count is not None:
            result['ParseMaxRowCount'] = self.parse_max_row_count

        if self.parse_total_row_counts is not None:
            result['ParseTotalRowCounts'] = self.parse_total_row_counts

        if self.return_max_row_count is not None:
            result['ReturnMaxRowCount'] = self.return_max_row_count

        if self.return_total_row_counts is not None:
            result['ReturnTotalRowCounts'] = self.return_total_row_counts

        if self.sqlhash is not None:
            result['SQLHASH'] = self.sqlhash

        if self.sqltext is not None:
            result['SQLText'] = self.sqltext

        if self.total_execution_counts is not None:
            result['TotalExecutionCounts'] = self.total_execution_counts

        if self.total_execution_times is not None:
            result['TotalExecutionTimes'] = self.total_execution_times

        if self.total_lock_times is not None:
            result['TotalLockTimes'] = self.total_lock_times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')

        if m.get('MaxExecutionTime') is not None:
            self.max_execution_time = m.get('MaxExecutionTime')

        if m.get('MaxExecutionTimeMs') is not None:
            self.max_execution_time_ms = m.get('MaxExecutionTimeMs')

        if m.get('MaxLockTime') is not None:
            self.max_lock_time = m.get('MaxLockTime')

        if m.get('ParseMaxRowCount') is not None:
            self.parse_max_row_count = m.get('ParseMaxRowCount')

        if m.get('ParseTotalRowCounts') is not None:
            self.parse_total_row_counts = m.get('ParseTotalRowCounts')

        if m.get('ReturnMaxRowCount') is not None:
            self.return_max_row_count = m.get('ReturnMaxRowCount')

        if m.get('ReturnTotalRowCounts') is not None:
            self.return_total_row_counts = m.get('ReturnTotalRowCounts')

        if m.get('SQLHASH') is not None:
            self.sqlhash = m.get('SQLHASH')

        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')

        if m.get('TotalExecutionCounts') is not None:
            self.total_execution_counts = m.get('TotalExecutionCounts')

        if m.get('TotalExecutionTimes') is not None:
            self.total_execution_times = m.get('TotalExecutionTimes')

        if m.get('TotalLockTimes') is not None:
            self.total_lock_times = m.get('TotalLockTimes')

        return self

