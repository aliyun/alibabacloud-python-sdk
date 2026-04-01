# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class ListUserBackupFilesResponseBody(DaraModel):
    def __init__(
        self,
        records: List[main_models.ListUserBackupFilesResponseBodyRecords] = None,
        request_id: str = None,
    ):
        # The information about the full backup files.
        self.records = records
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.ListUserBackupFilesResponseBodyRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListUserBackupFilesResponseBodyRecords(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        binlog_info: str = None,
        comment: str = None,
        creation_time: str = None,
        engine: str = None,
        engine_version: str = None,
        finish_time: str = None,
        modification_time: str = None,
        oss_bucket: str = None,
        oss_file_meta_data: str = None,
        oss_file_name: str = None,
        oss_file_path: str = None,
        oss_file_size: int = None,
        oss_url: str = None,
        reason: str = None,
        restore_size: str = None,
        retention: int = None,
        status: str = None,
        zone_id: str = None,
    ):
        # The ID of the full backup file.
        self.backup_id = backup_id
        # The information about the binary log file that contains incremental data. If incremental data is generated during the full backup, this parameter is returned.
        self.binlog_info = binlog_info
        # The description of the full backup file.
        self.comment = comment
        # The time when the system started to import the full backup file. The value is a UNIX timestamp. Unit: milliseconds.
        self.creation_time = creation_time
        # The database engine of the instance.
        self.engine = engine
        # The database engine version.
        self.engine_version = engine_version
        # The time when the full backup file is successfully imported. The value is a UNIX timestamp. Unit: milliseconds.
        self.finish_time = finish_time
        # The time when the full backup file is successfully imported. The value is a UNIX timestamp. Unit: milliseconds.
        self.modification_time = modification_time
        # The name of the OSS bucket in which the full backup file is stored as an object.
        self.oss_bucket = oss_bucket
        # The metadata of the full backup file. For more information, see [Manage object metadata](https://help.aliyun.com/document_detail/31859.html).
        self.oss_file_meta_data = oss_file_meta_data
        # The name of the full backup file that is stored as an object in an OSS bucket.
        self.oss_file_name = oss_file_name
        # The path of the full backup file that is stored as an object in an OSS bucket.
        self.oss_file_path = oss_file_path
        # The size of the full backup file that is stored as an object in an OSS bucket. Unit: KB.
        self.oss_file_size = oss_file_size
        # The URL to download the full backup file from the OSS bucket.
        self.oss_url = oss_url
        # The reason why the full backup file failed to be imported.
        self.reason = reason
        # The amount of storage that is required to restore the data of the full backup file. Unit: GB.
        self.restore_size = restore_size
        # The retention period of the full backup file. Unit: days.
        self.retention = retention
        # The status of the full backup file. Valid values:
        # 
        # *   **Importing**: The full backup file is being imported.
        # *   **Failed**: The full backup file fails to be imported.
        # *   **CheckSucccess**: The full backup file passes the check.
        # *   **BackupSuccess**: The full backup file is imported.
        # *   **Deleted**: The full backup file is deleted.
        self.status = status
        # The zone ID of the full backup file.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.binlog_info is not None:
            result['BinlogInfo'] = self.binlog_info

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_file_meta_data is not None:
            result['OssFileMetaData'] = self.oss_file_meta_data

        if self.oss_file_name is not None:
            result['OssFileName'] = self.oss_file_name

        if self.oss_file_path is not None:
            result['OssFilePath'] = self.oss_file_path

        if self.oss_file_size is not None:
            result['OssFileSize'] = self.oss_file_size

        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.restore_size is not None:
            result['RestoreSize'] = self.restore_size

        if self.retention is not None:
            result['Retention'] = self.retention

        if self.status is not None:
            result['Status'] = self.status

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BinlogInfo') is not None:
            self.binlog_info = m.get('BinlogInfo')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssFileMetaData') is not None:
            self.oss_file_meta_data = m.get('OssFileMetaData')

        if m.get('OssFileName') is not None:
            self.oss_file_name = m.get('OssFileName')

        if m.get('OssFilePath') is not None:
            self.oss_file_path = m.get('OssFilePath')

        if m.get('OssFileSize') is not None:
            self.oss_file_size = m.get('OssFileSize')

        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RestoreSize') is not None:
            self.restore_size = m.get('RestoreSize')

        if m.get('Retention') is not None:
            self.retention = m.get('Retention')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

