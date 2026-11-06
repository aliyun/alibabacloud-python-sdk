# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationBackupsResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeApplicationBackupsResponseBodyItems] = None,
        page_numbers: str = None,
        page_record_count: str = None,
        request_id: str = None,
        total_record_count: str = None,
    ):
        # The list of application backup sets.
        self.items = items
        # The current page number.
        self.page_numbers = page_numbers
        # The number of backup sets returned on the current page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of backup sets that meet the query conditions.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_numbers is not None:
            result['PageNumbers'] = self.page_numbers

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeApplicationBackupsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumbers') is not None:
            self.page_numbers = m.get('PageNumbers')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeApplicationBackupsResponseBodyItems(DaraModel):
    def __init__(
        self,
        backup_end_time: str = None,
        backup_id: str = None,
        backup_start_time: str = None,
        backup_status: str = None,
        backup_type: str = None,
        job_mode: str = None,
    ):
        # The end time of the backup. The time is displayed in UTC in the YYYY-MM-DDTHH:mm:ssZ format.
        self.backup_end_time = backup_end_time
        # The backup set ID.
        self.backup_id = backup_id
        # The start time of the backup. The time is displayed in UTC in the YYYY-MM-DDTHH:mm:ssZ format.
        self.backup_start_time = backup_start_time
        # The backup status. A value of Success indicates that the backup is completed, and a value of Failed indicates that the backup failed.
        self.backup_status = backup_status
        # The backup type. A value of FullBackup indicates a full backup, and a value of IncrementalBackup indicates an incremental backup.
        self.backup_type = backup_type
        # The backup mode. A value of Automated indicates an automatic backup, and a value of Manual indicates a manual backup.
        self.job_mode = job_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time

        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time

        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.job_mode is not None:
            result['JobMode'] = self.job_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')

        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')

        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('JobMode') is not None:
            self.job_mode = m.get('JobMode')

        return self

