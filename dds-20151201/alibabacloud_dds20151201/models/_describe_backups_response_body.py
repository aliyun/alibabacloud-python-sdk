# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupsResponseBody(DaraModel):
    def __init__(
        self,
        backups: main_models.DescribeBackupsResponseBodyBackups = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of the backup set.
        self.backups = backups
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**
        # *   **100**
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of backup sets.
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
        backup_expire_time: str = None,
        backup_id: str = None,
        backup_intranet_download_url: str = None,
        backup_job_id: str = None,
        backup_method: str = None,
        backup_mode: str = None,
        backup_name: str = None,
        backup_scale: str = None,
        backup_size: int = None,
        backup_start_time: str = None,
        backup_status: str = None,
        backup_type: str = None,
        engine_version: str = None,
        is_avail: bool = None,
    ):
        # The name of the database that has been backed up.
        self.backup_dbnames = backup_dbnames
        # The URL that is used to download the backup set over the Internet. If the backup set cannot be downloaded, an empty string is returned.
        self.backup_download_url = backup_download_url
        # The end time of the backup. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.backup_end_time = backup_end_time
        self.backup_expire_time = backup_expire_time
        # The ID of the backup set.
        self.backup_id = backup_id
        # The internal download URL of the backup set.
        # 
        # >  You can use the URL to download the specified backup set on an Elastic Compute Service (ECS) instance that is in the same virtual private cloud (VPC) as the ApsaraDB for MongoDB instance.
        self.backup_intranet_download_url = backup_intranet_download_url
        # The ID of the backup task.
        self.backup_job_id = backup_job_id
        # The method that is used to generate the backup set. Valid values:
        # 
        # *   **Snapshot**
        # *   **Physical**
        # *   **Logical**
        self.backup_method = backup_method
        # The backup mode of the backup set. Valid values:
        # 
        # *   **Automated**
        # *   **Manual**
        self.backup_mode = backup_mode
        # The name of the backup set. The parameter is invalid.
        self.backup_name = backup_name
        # The backup granularity. The parameter is invalid.
        self.backup_scale = backup_scale
        # The size of the backup set. Unit: bytes.
        self.backup_size = backup_size
        # The start time of the backup. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.backup_start_time = backup_start_time
        # The status of the backup task. Valid values:
        # 
        # *   **Success**: The backup task is successful.
        # *   **Failed**: The backup task failed.
        self.backup_status = backup_status
        # The backup type. Valid values:
        # 
        # *   **FullBackup**
        # *   **IncrementalBackup**
        self.backup_type = backup_type
        # Version of the backuped instance.
        # 
        # *   **6.0**
        # *   **5.0**
        # *   **4.4**
        # *   **4.2**
        # *   **4.0**
        # *   **3.4**
        self.engine_version = engine_version
        # Availability of the backup set.
        # - 0: unavailable
        # - 1: available
        self.is_avail = is_avail

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

        if self.backup_expire_time is not None:
            result['BackupExpireTime'] = self.backup_expire_time

        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.backup_intranet_download_url is not None:
            result['BackupIntranetDownloadURL'] = self.backup_intranet_download_url

        if self.backup_job_id is not None:
            result['BackupJobId'] = self.backup_job_id

        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method

        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode

        if self.backup_name is not None:
            result['BackupName'] = self.backup_name

        if self.backup_scale is not None:
            result['BackupScale'] = self.backup_scale

        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size

        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time

        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.is_avail is not None:
            result['IsAvail'] = self.is_avail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupDBNames') is not None:
            self.backup_dbnames = m.get('BackupDBNames')

        if m.get('BackupDownloadURL') is not None:
            self.backup_download_url = m.get('BackupDownloadURL')

        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')

        if m.get('BackupExpireTime') is not None:
            self.backup_expire_time = m.get('BackupExpireTime')

        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BackupIntranetDownloadURL') is not None:
            self.backup_intranet_download_url = m.get('BackupIntranetDownloadURL')

        if m.get('BackupJobId') is not None:
            self.backup_job_id = m.get('BackupJobId')

        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')

        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('BackupName') is not None:
            self.backup_name = m.get('BackupName')

        if m.get('BackupScale') is not None:
            self.backup_scale = m.get('BackupScale')

        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')

        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')

        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('IsAvail') is not None:
            self.is_avail = m.get('IsAvail')

        return self

