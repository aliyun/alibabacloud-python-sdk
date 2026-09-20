# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupSummaryResponseBody(DaraModel):
    def __init__(
        self,
        full: main_models.DescribeBackupSummaryResponseBodyFull = None,
        incr: main_models.DescribeBackupSummaryResponseBodyIncr = None,
        request_id: str = None,
    ):
        # The details of the full backup.
        self.full = full
        # The details of the incremental backup.
        self.incr = incr
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.full:
            self.full.validate()
        if self.incr:
            self.incr.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.full is not None:
            result['Full'] = self.full.to_map()

        if self.incr is not None:
            result['Incr'] = self.incr.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Full') is not None:
            temp_model = main_models.DescribeBackupSummaryResponseBodyFull()
            self.full = temp_model.from_map(m.get('Full'))

        if m.get('Incr') is not None:
            temp_model = main_models.DescribeBackupSummaryResponseBodyIncr()
            self.incr = temp_model.from_map(m.get('Incr'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeBackupSummaryResponseBodyIncr(DaraModel):
    def __init__(
        self,
        backup_log_size: str = None,
        pos: str = None,
        queue_log_num: str = None,
        running_log_num: str = None,
        speed: str = None,
        status: str = None,
    ):
        # The data size.
        self.backup_log_size = backup_log_size
        # The synchronization point.
        self.pos = pos
        # The number of logs in the queue.
        self.queue_log_num = queue_log_num
        # The number of logs being backed up.
        self.running_log_num = running_log_num
        # The current write speed of the incremental backup.
        self.speed = speed
        # The status of the incremental backup.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_log_size is not None:
            result['BackupLogSize'] = self.backup_log_size

        if self.pos is not None:
            result['Pos'] = self.pos

        if self.queue_log_num is not None:
            result['QueueLogNum'] = self.queue_log_num

        if self.running_log_num is not None:
            result['RunningLogNum'] = self.running_log_num

        if self.speed is not None:
            result['Speed'] = self.speed

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupLogSize') is not None:
            self.backup_log_size = m.get('BackupLogSize')

        if m.get('Pos') is not None:
            self.pos = m.get('Pos')

        if m.get('QueueLogNum') is not None:
            self.queue_log_num = m.get('QueueLogNum')

        if m.get('RunningLogNum') is not None:
            self.running_log_num = m.get('RunningLogNum')

        if m.get('Speed') is not None:
            self.speed = m.get('Speed')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeBackupSummaryResponseBodyFull(DaraModel):
    def __init__(
        self,
        has_more: str = None,
        next_full_backup_date: str = None,
        page_number: int = None,
        page_size: int = None,
        records: main_models.DescribeBackupSummaryResponseBodyFullRecords = None,
        total: int = None,
    ):
        # Indicates whether there is a next page. Valid values:
        # 
        # - true: There is a next page.
        # - false: There is no next page.
        self.has_more = has_more
        # The time of the next full backup.
        self.next_full_backup_date = next_full_backup_date
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        self.records = records
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.records:
            self.records.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_more is not None:
            result['HasMore'] = self.has_more

        if self.next_full_backup_date is not None:
            result['NextFullBackupDate'] = self.next_full_backup_date

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.records is not None:
            result['Records'] = self.records.to_map()

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        if m.get('NextFullBackupDate') is not None:
            self.next_full_backup_date = m.get('NextFullBackupDate')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Records') is not None:
            temp_model = main_models.DescribeBackupSummaryResponseBodyFullRecords()
            self.records = temp_model.from_map(m.get('Records'))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeBackupSummaryResponseBodyFullRecords(DaraModel):
    def __init__(
        self,
        record: List[main_models.DescribeBackupSummaryResponseBodyFullRecordsRecord] = None,
    ):
        self.record = record

    def validate(self):
        if self.record:
            for v1 in self.record:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Record'] = []
        if self.record is not None:
            for k1 in self.record:
                result['Record'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record = []
        if m.get('Record') is not None:
            for k1 in m.get('Record'):
                temp_model = main_models.DescribeBackupSummaryResponseBodyFullRecordsRecord()
                self.record.append(temp_model.from_map(k1))

        return self

class DescribeBackupSummaryResponseBodyFullRecordsRecord(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        data_size: str = None,
        finish_time: str = None,
        process: str = None,
        record_id: str = None,
        speed: str = None,
        status: str = None,
    ):
        self.create_time = create_time
        self.data_size = data_size
        self.finish_time = finish_time
        self.process = process
        self.record_id = record_id
        self.speed = speed
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.process is not None:
            result['Process'] = self.process

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.speed is not None:
            result['Speed'] = self.speed

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Process') is not None:
            self.process = m.get('Process')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('Speed') is not None:
            self.speed = m.get('Speed')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

