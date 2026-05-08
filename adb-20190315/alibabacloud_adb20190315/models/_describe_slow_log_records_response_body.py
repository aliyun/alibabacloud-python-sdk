# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeSlowLogRecordsResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        items: main_models.DescribeSlowLogRecordsResponseBodyItems = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        self.dbcluster_id = dbcluster_id
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on the current page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

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

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeSlowLogRecordsResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSlowLogRecordsResponseBodyItems(DaraModel):
    def __init__(
        self,
        slow_log_record: List[main_models.DescribeSlowLogRecordsResponseBodyItemsSlowLogRecord] = None,
    ):
        self.slow_log_record = slow_log_record

    def validate(self):
        if self.slow_log_record:
            for v1 in self.slow_log_record:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SlowLogRecord'] = []
        if self.slow_log_record is not None:
            for k1 in self.slow_log_record:
                result['SlowLogRecord'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.slow_log_record = []
        if m.get('SlowLogRecord') is not None:
            for k1 in m.get('SlowLogRecord'):
                temp_model = main_models.DescribeSlowLogRecordsResponseBodyItemsSlowLogRecord()
                self.slow_log_record.append(temp_model.from_map(k1))

        return self

class DescribeSlowLogRecordsResponseBodyItemsSlowLogRecord(DaraModel):
    def __init__(
        self,
        dbname: str = None,
        execution_start_time: str = None,
        host_address: str = None,
        output_size: str = None,
        parse_row_counts: int = None,
        peak_memory_usage: str = None,
        planning_time: int = None,
        process_id: str = None,
        query_time: int = None,
        queue_time: int = None,
        return_row_counts: int = None,
        sqltext: str = None,
        scan_rows: int = None,
        scan_size: str = None,
        scan_time: int = None,
        state: str = None,
        user_name: str = None,
        wall_time: int = None,
    ):
        self.dbname = dbname
        self.execution_start_time = execution_start_time
        self.host_address = host_address
        self.output_size = output_size
        self.parse_row_counts = parse_row_counts
        self.peak_memory_usage = peak_memory_usage
        self.planning_time = planning_time
        self.process_id = process_id
        self.query_time = query_time
        self.queue_time = queue_time
        self.return_row_counts = return_row_counts
        self.sqltext = sqltext
        self.scan_rows = scan_rows
        self.scan_size = scan_size
        self.scan_time = scan_time
        self.state = state
        self.user_name = user_name
        self.wall_time = wall_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.execution_start_time is not None:
            result['ExecutionStartTime'] = self.execution_start_time

        if self.host_address is not None:
            result['HostAddress'] = self.host_address

        if self.output_size is not None:
            result['OutputSize'] = self.output_size

        if self.parse_row_counts is not None:
            result['ParseRowCounts'] = self.parse_row_counts

        if self.peak_memory_usage is not None:
            result['PeakMemoryUsage'] = self.peak_memory_usage

        if self.planning_time is not None:
            result['PlanningTime'] = self.planning_time

        if self.process_id is not None:
            result['ProcessID'] = self.process_id

        if self.query_time is not None:
            result['QueryTime'] = self.query_time

        if self.queue_time is not None:
            result['QueueTime'] = self.queue_time

        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts

        if self.sqltext is not None:
            result['SQLText'] = self.sqltext

        if self.scan_rows is not None:
            result['ScanRows'] = self.scan_rows

        if self.scan_size is not None:
            result['ScanSize'] = self.scan_size

        if self.scan_time is not None:
            result['ScanTime'] = self.scan_time

        if self.state is not None:
            result['State'] = self.state

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.wall_time is not None:
            result['WallTime'] = self.wall_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('ExecutionStartTime') is not None:
            self.execution_start_time = m.get('ExecutionStartTime')

        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')

        if m.get('OutputSize') is not None:
            self.output_size = m.get('OutputSize')

        if m.get('ParseRowCounts') is not None:
            self.parse_row_counts = m.get('ParseRowCounts')

        if m.get('PeakMemoryUsage') is not None:
            self.peak_memory_usage = m.get('PeakMemoryUsage')

        if m.get('PlanningTime') is not None:
            self.planning_time = m.get('PlanningTime')

        if m.get('ProcessID') is not None:
            self.process_id = m.get('ProcessID')

        if m.get('QueryTime') is not None:
            self.query_time = m.get('QueryTime')

        if m.get('QueueTime') is not None:
            self.queue_time = m.get('QueueTime')

        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')

        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')

        if m.get('ScanRows') is not None:
            self.scan_rows = m.get('ScanRows')

        if m.get('ScanSize') is not None:
            self.scan_size = m.get('ScanSize')

        if m.get('ScanTime') is not None:
            self.scan_time = m.get('ScanTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('WallTime') is not None:
            self.wall_time = m.get('WallTime')

        return self

