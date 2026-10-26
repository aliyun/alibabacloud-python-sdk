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
        # The storage space occupied by archive backups. Unit: bytes.
        self.archive_backup_size = archive_backup_size
        # The total storage space occupied by data backups, excluding archive backups. Unit: bytes.
        # 
        # > For **SQL Server** instances, this parameter indicates the total size of physical backups and snapshot backups.
        self.backup_data_size = backup_data_size
        # The storage space occupied by snapshot backups of **SQL Server** instances. Unit: bytes. A value of 0 indicates that no data is available.
        self.backup_ecs_snapshot_size = backup_ecs_snapshot_size
        # The total storage space occupied by log backups, excluding archive backups. Unit: bytes.
        self.backup_log_size = backup_log_size
        # The size of data files in backup sets stored in OSS. Unit: bytes. A value of 0 indicates that no data is available.
        # 
        # > For **SQL Server** instances, this parameter indicates the storage space occupied by physical backups.
        self.backup_oss_data_size = backup_oss_data_size
        # The size of log files in backup sets stored in OSS. Unit: bytes. A value of 0 indicates that no data is available.
        self.backup_oss_log_size = backup_oss_log_size
        # The storage space occupied by backups, including data backups and log backups. Unit: bytes. A value of -1 indicates that no data is available.
        self.backup_size = backup_size
        # The storage space occupied by cold backups. Unit: bytes. A value of -1 indicates that no data is available.
        self.cold_backup_size = cold_backup_size
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The storage space occupied by data files. Unit: bytes. A value of -1 indicates that no data is available.
        self.data_size = data_size
        # The used storage space, which is the sum of DataSize and LogSize. Unit: bytes. A value of -1 indicates that no data is available.
        self.disk_used = disk_used
        # The database engine.
        self.engine = engine
        # The storage space occupied by logs. Unit: bytes. A value of -1 indicates that no data is available.
        self.log_size = log_size
        # The storage space occupied by backups that you are billed for after the free quota is deducted. Unit: bytes.
        self.paid_backup_size = paid_backup_size
        # The ID of the request.
        self.request_id = request_id
        # The storage space occupied by SQL data. Unit: bytes. A value of -1 indicates that no data is available.
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

