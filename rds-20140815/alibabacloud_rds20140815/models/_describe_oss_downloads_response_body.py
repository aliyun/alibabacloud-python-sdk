# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeOssDownloadsResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        items: main_models.DescribeOssDownloadsResponseBodyItems = None,
        migrate_task_id: str = None,
        request_id: str = None,
    ):
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # Details of the backup file.
        self.items = items
        # The ID of the migration task.
        self.migrate_task_id = migrate_task_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.migrate_task_id is not None:
            result['MigrateTaskId'] = self.migrate_task_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeOssDownloadsResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('MigrateTaskId') is not None:
            self.migrate_task_id = m.get('MigrateTaskId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeOssDownloadsResponseBodyItems(DaraModel):
    def __init__(
        self,
        oss_download: List[main_models.DescribeOssDownloadsResponseBodyItemsOssDownload] = None,
    ):
        self.oss_download = oss_download

    def validate(self):
        if self.oss_download:
            for v1 in self.oss_download:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OssDownload'] = []
        if self.oss_download is not None:
            for k1 in self.oss_download:
                result['OssDownload'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.oss_download = []
        if m.get('OssDownload') is not None:
            for k1 in m.get('OssDownload'):
                temp_model = main_models.DescribeOssDownloadsResponseBodyItemsOssDownload()
                self.oss_download.append(temp_model.from_map(k1))

        return self

class DescribeOssDownloadsResponseBodyItemsOssDownload(DaraModel):
    def __init__(
        self,
        backup_mode: str = None,
        create_time: str = None,
        description: str = None,
        end_time: str = None,
        file_name: str = None,
        file_size: str = None,
        is_available: str = None,
        status: str = None,
    ):
        # The backup type. Valid values:
        # 
        # *   **Database**: full backup file
        # *   **Differential_Database**: incremental backup file
        # *   **Transaction_Log**: log backup file
        self.backup_mode = backup_mode
        # The time when the backup file was created in the download list. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the backup file.
        self.description = description
        # The end of the time range during which data was queried. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.end_time = end_time
        # The name of the backup file stored in the Object Storage Service (OSS) bucket.
        self.file_name = file_name
        # The size of the backup file. Unit: MB
        self.file_size = file_size
        # Indicates whether the backup file is available. Valid values: **True and False**.
        self.is_available = is_available
        # The state of the backup file. Valid values:
        # 
        # *   **NoStart**
        # *   **Downloading**
        # *   **Finished**
        # *   **DownloadFailed**
        # *   **VerifyFailed**
        # *   **Deleted**
        # *   **DeleteFailed**
        # *   **CheckSuccess**
        # *   **CheckFailed**
        # *   **Restoring**
        # *   **Restored**
        # *   **RestoreFailed**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.is_available is not None:
            result['IsAvailable'] = self.is_available

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('IsAvailable') is not None:
            self.is_available = m.get('IsAvailable')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

