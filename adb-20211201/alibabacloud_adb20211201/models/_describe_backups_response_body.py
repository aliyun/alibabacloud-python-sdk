# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupsResponseBody(DaraModel):
    def __init__(
        self,
        free_backup_size: int = None,
        items: main_models.DescribeBackupsResponseBodyItems = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_backup_size: int = None,
        total_count: str = None,
    ):
        self.free_backup_size = free_backup_size
        # The queried backup sets.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        self.total_backup_size = total_backup_size
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
        if self.free_backup_size is not None:
            result['FreeBackupSize'] = self.free_backup_size

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_backup_size is not None:
            result['TotalBackupSize'] = self.total_backup_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FreeBackupSize') is not None:
            self.free_backup_size = m.get('FreeBackupSize')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeBackupsResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalBackupSize') is not None:
            self.total_backup_size = m.get('TotalBackupSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeBackupsResponseBodyItems(DaraModel):
    def __init__(
        self,
        backup: List[main_models.DescribeBackupsResponseBodyItemsBackup] = None,
    ):
        self.backup = backup

    def validate(self):
        if self.backup:
            for v1 in self.backup:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Backup'] = []
        if self.backup is not None:
            for k1 in self.backup:
                result['Backup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup = []
        if m.get('Backup') is not None:
            for k1 in m.get('Backup'):
                temp_model = main_models.DescribeBackupsResponseBodyItemsBackup()
                self.backup.append(temp_model.from_map(k1))

        return self

class DescribeBackupsResponseBodyItemsBackup(DaraModel):
    def __init__(
        self,
        backup_end_time: str = None,
        backup_expired_time: str = None,
        backup_id: str = None,
        backup_method: str = None,
        backup_region: str = None,
        backup_size: int = None,
        backup_start_time: str = None,
        backup_status: str = None,
        backup_type: str = None,
        dbcluster_id: str = None,
        parent_backup_id: str = None,
    ):
        # The end time of the backup.
        self.backup_end_time = backup_end_time
        self.backup_expired_time = backup_expired_time
        # The backup set ID.
        self.backup_id = backup_id
        # The backup method. Snapshot is returned.
        self.backup_method = backup_method
        self.backup_region = backup_region
        # The size of the backup set. Unit: bytes.
        self.backup_size = backup_size
        # The start time of the backup.
        self.backup_start_time = backup_start_time
        self.backup_status = backup_status
        # The backup type. Valid values:
        # 
        # *   **FullBackup**
        # *   **IncrementalBackup**
        self.backup_type = backup_type
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition cluster.
        self.dbcluster_id = dbcluster_id
        self.parent_backup_id = parent_backup_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time

        if self.backup_expired_time is not None:
            result['BackupExpiredTime'] = self.backup_expired_time

        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method

        if self.backup_region is not None:
            result['BackupRegion'] = self.backup_region

        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size

        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time

        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.parent_backup_id is not None:
            result['ParentBackupId'] = self.parent_backup_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')

        if m.get('BackupExpiredTime') is not None:
            self.backup_expired_time = m.get('BackupExpiredTime')

        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')

        if m.get('BackupRegion') is not None:
            self.backup_region = m.get('BackupRegion')

        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')

        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')

        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ParentBackupId') is not None:
            self.parent_backup_id = m.get('ParentBackupId')

        return self

