# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeSlowLogRecordsResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        engine: str = None,
        items: main_models.DescribeSlowLogRecordsResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # Cluster ID.
        self.dbcluster_id = dbcluster_id
        # Database engine.
        self.engine = engine
        # List of slow log details.
        self.items = items
        # Page number.
        self.page_number = page_number
        # Number of records on this page.
        self.page_record_count = page_record_count
        # Request ID.
        self.request_id = request_id
        # Total number of SQL statements.
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

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
        dbname: str = None,
        dbnode_id: str = None,
        execution_start_time: str = None,
        host_address: str = None,
        lock_times: int = None,
        parse_row_counts: int = None,
        query_time_ms: int = None,
        query_times: int = None,
        return_row_counts: int = None,
        sqlhash: str = None,
        sqltext: str = None,
    ):
        # Database name.
        self.dbname = dbname
        # Node ID.
        self.dbnode_id = dbnode_id
        # Time when the SQL starts execution. The format is `YYYY-MM-DDThh:mmZ` (UTC time).
        self.execution_start_time = execution_start_time
        # Client address connecting to the database.
        self.host_address = host_address
        # SQL lock duration in seconds.
        self.lock_times = lock_times
        # Number of rows parsed.
        self.parse_row_counts = parse_row_counts
        # Query time. Unit: milliseconds.
        self.query_time_ms = query_time_ms
        # SQL execution duration, in seconds.
        self.query_times = query_times
        # Number of rows returned.
        self.return_row_counts = return_row_counts
        # Unique identifier for the SQL statement in slow log statistics.
        self.sqlhash = sqlhash
        # Query statement.
        self.sqltext = sqltext

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id

        if self.execution_start_time is not None:
            result['ExecutionStartTime'] = self.execution_start_time

        if self.host_address is not None:
            result['HostAddress'] = self.host_address

        if self.lock_times is not None:
            result['LockTimes'] = self.lock_times

        if self.parse_row_counts is not None:
            result['ParseRowCounts'] = self.parse_row_counts

        if self.query_time_ms is not None:
            result['QueryTimeMS'] = self.query_time_ms

        if self.query_times is not None:
            result['QueryTimes'] = self.query_times

        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts

        if self.sqlhash is not None:
            result['SQLHash'] = self.sqlhash

        if self.sqltext is not None:
            result['SQLText'] = self.sqltext

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')

        if m.get('ExecutionStartTime') is not None:
            self.execution_start_time = m.get('ExecutionStartTime')

        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')

        if m.get('LockTimes') is not None:
            self.lock_times = m.get('LockTimes')

        if m.get('ParseRowCounts') is not None:
            self.parse_row_counts = m.get('ParseRowCounts')

        if m.get('QueryTimeMS') is not None:
            self.query_time_ms = m.get('QueryTimeMS')

        if m.get('QueryTimes') is not None:
            self.query_times = m.get('QueryTimes')

        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')

        if m.get('SQLHash') is not None:
            self.sqlhash = m.get('SQLHash')

        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')

        return self

