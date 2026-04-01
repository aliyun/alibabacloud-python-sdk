# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeResourceUsageResponseBody(DaraModel):
    def __init__(
        self,
        archive_backup_size: int = None,
        backup_data_size: int = None,
        backup_ecs_snapshot_size: str = None,
        backup_log_size: int = None,
        backup_oss_data_size: int = None,
        backup_oss_log_size: int = None,
        backup_size: int = None,
        cold_backup_size: int = None,
        dbinstance_id: str = None,
        data_size: int = None,
        disk_used: int = None,
        engine: str = None,
        log_size: int = None,
        paid_backup_size: int = None,
        request_id: str = None,
        sqlsize: int = None,
    ):
        # The storage that is occupied by archived backup files on the instance. Unit: bytes.
        self.archive_backup_size = archive_backup_size
        # The storage that is occupied by data backup files, excluding archived backup files, on the instance. Unit: bytes.
        self.backup_data_size = backup_data_size
        # The storage capacity that is used to store the snapshot backup files of the **RDS for SQL Server** instance. Unit: bytes. The value 0 indicates that no snapshot backup files are stored for the instance.
        self.backup_ecs_snapshot_size = backup_ecs_snapshot_size
        # The storage that is occupied by log backup files, excluding archived backup files, on the instance. Unit: bytes.
        self.backup_log_size = backup_log_size
        # The size of data backup files that are stored in Object Storage Service (OSS) buckets. Unit: bytes. The value 0 indicates no data backup files are stored in OSS buckets.
        self.backup_oss_data_size = backup_oss_data_size
        # The size of log backup files that are stored in OSS buckets. Unit: bytes. The value 0 indicates no log backup files are stored in OSS buckets.
        self.backup_oss_log_size = backup_oss_log_size
        # The storage that is used to store backup files. Unit: bytes. The value -1 indicates that no backup files are stored.
        self.backup_size = backup_size
        # The storage that is used to store cold backup files. Unit: bytes. The value -1 indicates that no cold backup files are stored.
        self.cold_backup_size = cold_backup_size
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The storage that is used to store data files. Unit: bytes. The value -1 indicates that no data files are stored.
        self.data_size = data_size
        # The total storage that is occupied by data files and log files on the instance. Unit: bytes. The value -1 indicates that no data files or log files are stored on the instance.
        self.disk_used = disk_used
        # The database engine of the instance.
        self.engine = engine
        # The storage that is used to store log files. Unit: bytes. The value -1 indicates that no log files are stored.
        self.log_size = log_size
        # The backup storage for which you must pay. The system provides a free quota on backup storage. You must pay for the backup storage that exceeds the free quota. Unit: bytes.
        self.paid_backup_size = paid_backup_size
        # The request ID.
        self.request_id = request_id
        # The storage that is occupied to execute SQL statements on the instance. Unit: bytes. The value -1 indicates that no SQL statements are executed.
        self.sqlsize = sqlsize

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.archive_backup_size is not None:
            result['ArchiveBackupSize'] = self.archive_backup_size

        if self.backup_data_size is not None:
            result['BackupDataSize'] = self.backup_data_size

        if self.backup_ecs_snapshot_size is not None:
            result['BackupEcsSnapshotSize'] = self.backup_ecs_snapshot_size

        if self.backup_log_size is not None:
            result['BackupLogSize'] = self.backup_log_size

        if self.backup_oss_data_size is not None:
            result['BackupOssDataSize'] = self.backup_oss_data_size

        if self.backup_oss_log_size is not None:
            result['BackupOssLogSize'] = self.backup_oss_log_size

        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size

        if self.cold_backup_size is not None:
            result['ColdBackupSize'] = self.cold_backup_size

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.disk_used is not None:
            result['DiskUsed'] = self.disk_used

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.log_size is not None:
            result['LogSize'] = self.log_size

        if self.paid_backup_size is not None:
            result['PaidBackupSize'] = self.paid_backup_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sqlsize is not None:
            result['SQLSize'] = self.sqlsize

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveBackupSize') is not None:
            self.archive_backup_size = m.get('ArchiveBackupSize')

        if m.get('BackupDataSize') is not None:
            self.backup_data_size = m.get('BackupDataSize')

        if m.get('BackupEcsSnapshotSize') is not None:
            self.backup_ecs_snapshot_size = m.get('BackupEcsSnapshotSize')

        if m.get('BackupLogSize') is not None:
            self.backup_log_size = m.get('BackupLogSize')

        if m.get('BackupOssDataSize') is not None:
            self.backup_oss_data_size = m.get('BackupOssDataSize')

        if m.get('BackupOssLogSize') is not None:
            self.backup_oss_log_size = m.get('BackupOssLogSize')

        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')

        if m.get('ColdBackupSize') is not None:
            self.cold_backup_size = m.get('ColdBackupSize')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('DiskUsed') is not None:
            self.disk_used = m.get('DiskUsed')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('LogSize') is not None:
            self.log_size = m.get('LogSize')

        if m.get('PaidBackupSize') is not None:
            self.paid_backup_size = m.get('PaidBackupSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SQLSize') is not None:
            self.sqlsize = m.get('SQLSize')

        return self

