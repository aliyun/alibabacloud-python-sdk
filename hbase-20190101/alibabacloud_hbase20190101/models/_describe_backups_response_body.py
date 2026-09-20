# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupsResponseBody(DaraModel):
    def __init__(
        self,
        backups: main_models.DescribeBackupsResponseBodyBackups = None,
        enable_status: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.backups = backups
        # The backup enabling status. Valid values:
        # - enable: Enabled.
        # - disable: Not enabled.
        # - opening: Being enabled.
        self.enable_status = enable_status
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.backups:
            self.backups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backups is not None:
            result['Backups'] = self.backups.to_map()

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

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
        if m.get('Backups') is not None:
            temp_model = main_models.DescribeBackupsResponseBodyBackups()
            self.backups = temp_model.from_map(m.get('Backups'))

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeBackupsResponseBodyBackups(DaraModel):
    def __init__(
        self,
        backup: List[main_models.DescribeBackupsResponseBodyBackupsBackup] = None,
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
                temp_model = main_models.DescribeBackupsResponseBodyBackupsBackup()
                self.backup.append(temp_model.from_map(k1))

        return self

class DescribeBackupsResponseBodyBackupsBackup(DaraModel):
    def __init__(
        self,
        backup_dbnames: str = None,
        backup_download_url: str = None,
        backup_end_time: str = None,
        backup_end_time_utc: str = None,
        backup_id: int = None,
        backup_method: str = None,
        backup_mode: str = None,
        backup_size: str = None,
        backup_start_time: str = None,
        backup_start_time_utc: str = None,
        backup_status: str = None,
        backup_type: str = None,
    ):
        self.backup_dbnames = backup_dbnames
        self.backup_download_url = backup_download_url
        self.backup_end_time = backup_end_time
        self.backup_end_time_utc = backup_end_time_utc
        self.backup_id = backup_id
        self.backup_method = backup_method
        self.backup_mode = backup_mode
        self.backup_size = backup_size
        self.backup_start_time = backup_start_time
        self.backup_start_time_utc = backup_start_time_utc
        self.backup_status = backup_status
        self.backup_type = backup_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_dbnames is not None:
            result['BackupDBNames'] = self.backup_dbnames

        if self.backup_download_url is not None:
            result['BackupDownloadURL'] = self.backup_download_url

        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time

        if self.backup_end_time_utc is not None:
            result['BackupEndTimeUTC'] = self.backup_end_time_utc

        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method

        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode

        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size

        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time

        if self.backup_start_time_utc is not None:
            result['BackupStartTimeUTC'] = self.backup_start_time_utc

        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupDBNames') is not None:
            self.backup_dbnames = m.get('BackupDBNames')

        if m.get('BackupDownloadURL') is not None:
            self.backup_download_url = m.get('BackupDownloadURL')

        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')

        if m.get('BackupEndTimeUTC') is not None:
            self.backup_end_time_utc = m.get('BackupEndTimeUTC')

        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')

        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')

        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')

        if m.get('BackupStartTimeUTC') is not None:
            self.backup_start_time_utc = m.get('BackupStartTimeUTC')

        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        return self

