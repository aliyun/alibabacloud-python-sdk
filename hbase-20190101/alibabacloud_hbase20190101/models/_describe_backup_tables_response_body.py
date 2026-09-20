# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupTablesResponseBody(DaraModel):
    def __init__(
        self,
        backup_records: main_models.DescribeBackupTablesResponseBodyBackupRecords = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tables: main_models.DescribeBackupTablesResponseBodyTables = None,
        total: int = None,
    ):
        self.backup_records = backup_records
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        self.tables = tables
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.backup_records:
            self.backup_records.validate()
        if self.tables:
            self.tables.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_records is not None:
            result['BackupRecords'] = self.backup_records.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tables is not None:
            result['Tables'] = self.tables.to_map()

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupRecords') is not None:
            temp_model = main_models.DescribeBackupTablesResponseBodyBackupRecords()
            self.backup_records = temp_model.from_map(m.get('BackupRecords'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Tables') is not None:
            temp_model = main_models.DescribeBackupTablesResponseBodyTables()
            self.tables = temp_model.from_map(m.get('Tables'))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeBackupTablesResponseBodyTables(DaraModel):
    def __init__(
        self,
        table: List[str] = None,
    ):
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.table is not None:
            result['Table'] = self.table

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Table') is not None:
            self.table = m.get('Table')

        return self

class DescribeBackupTablesResponseBodyBackupRecords(DaraModel):
    def __init__(
        self,
        backup_record: List[main_models.DescribeBackupTablesResponseBodyBackupRecordsBackupRecord] = None,
    ):
        self.backup_record = backup_record

    def validate(self):
        if self.backup_record:
            for v1 in self.backup_record:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BackupRecord'] = []
        if self.backup_record is not None:
            for k1 in self.backup_record:
                result['BackupRecord'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup_record = []
        if m.get('BackupRecord') is not None:
            for k1 in m.get('BackupRecord'):
                temp_model = main_models.DescribeBackupTablesResponseBodyBackupRecordsBackupRecord()
                self.backup_record.append(temp_model.from_map(k1))

        return self

class DescribeBackupTablesResponseBodyBackupRecordsBackupRecord(DaraModel):
    def __init__(
        self,
        data_size: str = None,
        end_time: str = None,
        message: str = None,
        process: str = None,
        speed: str = None,
        start_time: str = None,
        state: str = None,
        table: str = None,
    ):
        self.data_size = data_size
        self.end_time = end_time
        self.message = message
        self.process = process
        self.speed = speed
        self.start_time = start_time
        self.state = state
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.message is not None:
            result['Message'] = self.message

        if self.process is not None:
            result['Process'] = self.process

        if self.speed is not None:
            result['Speed'] = self.speed

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        if self.table is not None:
            result['Table'] = self.table

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Process') is not None:
            self.process = m.get('Process')

        if m.get('Speed') is not None:
            self.speed = m.get('Speed')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Table') is not None:
            self.table = m.get('Table')

        return self

