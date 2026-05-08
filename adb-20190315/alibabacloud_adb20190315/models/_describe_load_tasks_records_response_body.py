# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeLoadTasksRecordsResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        load_tasks_records: List[main_models.DescribeLoadTasksRecordsResponseBodyLoadTasksRecords] = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The queried asynchronous import and export tasks.
        self.load_tasks_records = load_tasks_records
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.load_tasks_records:
            for v1 in self.load_tasks_records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        result['LoadTasksRecords'] = []
        if self.load_tasks_records is not None:
            for k1 in self.load_tasks_records:
                result['LoadTasksRecords'].append(k1.to_map() if k1 else None)

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

        self.load_tasks_records = []
        if m.get('LoadTasksRecords') is not None:
            for k1 in m.get('LoadTasksRecords'):
                temp_model = main_models.DescribeLoadTasksRecordsResponseBodyLoadTasksRecords()
                self.load_tasks_records.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeLoadTasksRecordsResponseBodyLoadTasksRecords(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        dbname: str = None,
        job_name: str = None,
        process_id: str = None,
        process_rows: int = None,
        sql: str = None,
        state: str = None,
        update_time: str = None,
    ):
        # The start time of the task. The time is accurate to milliseconds. The time follows the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ss.SSSZ* format. The time is displayed in UTC.
        self.create_time = create_time
        # The name of the database that is involved in the import or export task.
        self.dbname = dbname
        # The task ID.
        self.job_name = job_name
        # The process ID.
        self.process_id = process_id
        # The number of rows that are processed in the asynchronous import or export task.
        self.process_rows = process_rows
        # The SQL statement that is used in the asynchronous import or export task.
        self.sql = sql
        # The state of the task.
        self.state = state
        # The time when the task state was updated. The time is accurate to milliseconds. The time follows the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ss.SSSZ* format. The time is displayed in UTC.
        self.update_time = update_time

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

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.process_id is not None:
            result['ProcessID'] = self.process_id

        if self.process_rows is not None:
            result['ProcessRows'] = self.process_rows

        if self.sql is not None:
            result['Sql'] = self.sql

        if self.state is not None:
            result['State'] = self.state

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('ProcessID') is not None:
            self.process_id = m.get('ProcessID')

        if m.get('ProcessRows') is not None:
            self.process_rows = m.get('ProcessRows')

        if m.get('Sql') is not None:
            self.sql = m.get('Sql')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

