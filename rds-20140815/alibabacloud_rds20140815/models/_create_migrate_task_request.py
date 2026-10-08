# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMigrateTaskRequest(DaraModel):
    def __init__(
        self,
        backup_mode: str = None,
        check_dbmode: str = None,
        dbinstance_id: str = None,
        dbname: str = None,
        is_online_db: str = None,
        migrate_task_id: str = None,
        ossurls: str = None,
        oss_object_positions: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The type of the cloud migration task. Valid values:
        # * **FULL**: performs a restore operation by using a full backup file. This value is applicable to first-time migrations or full data recovery scenarios.
        # * **UPDF**: restores incremental data by using an incremental backup file or log file. This value is applicable to incremental synchronization scenarios where a full backup already exists.
        # 
        # This parameter is required.
        self.backup_mode = backup_mode
        # The consistency check method after the database is brought online. This parameter takes effect only when IsOnlineDB is set to True. Valid values:
        # 
        # - **SyncExecuteDBCheck**: performs a synchronous database check. This value is applicable to scenarios that require high data consistency.
        # - **AsyncExecuteDBCheck**: performs an asynchronous database check. This value provides higher performance but may delay the detection of potential issues.
        # 
        # Default value: **AsyncExecuteDBCheck** (compatible with SQL Server 2008 R2).
        self.check_dbmode = check_dbmode
        # The instance ID. You can call DescribeDBInstances to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the destination database.
        # 
        # This parameter is required.
        self.dbname = dbname
        # Specifies whether to bring the restored database online so that users can access it. Valid values:
        # 
        # * **True**: Brings the database online.
        # * **False**: Does not bring the database online.
        # 
        # > * For SQL Server 2008 R2, this value is always True.
        # > * When **IsOnlineDB** is set to **True**, **BackupMode** must be set to **FULL**.
        # > * When **IsOnlineDB** is set to **False**, **BackupMode** must be set to **UPDF**.
        # 
        # This parameter is required.
        self.is_online_db = is_online_db
        # The migration task ID. Valid values:
        # 
        # - When **BackupMode** is set to **FULL**, leave this parameter empty (compatible with SQL Server 2008 R2).
        # - When **BackupMode** is set to **UPDF**, set this parameter to the ID of the corresponding FULL task. You can call DescribeMigrateTasks to query the task ID.
        self.migrate_task_id = migrate_task_id
        # The shared URL of the backup file on OSS (URL-encoded). If multiple URLs exist, separate them with vertical bars (|) before encoding, and then pass the encoded value.
        # 
        # > This parameter is required for SQL Server 2008 R2.
        self.ossurls = ossurls
        # The OSS file information, which consists of the following three parts separated by colons (:):
        # - **OSS endpoint**: oss-ap-southeast-1.aliyuncs.com.
        # - **OSS bucket name**: rdsmssqlsingapore.
        # - **Backup file name on OSS**: autotest_2008R2_TestMigration_FULL.bak.
        # 
        # > This parameter is required for SQL Server versions later than SQL Server 2008 R2.
        self.oss_object_positions = oss_object_positions
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode

        if self.check_dbmode is not None:
            result['CheckDBMode'] = self.check_dbmode

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.is_online_db is not None:
            result['IsOnlineDB'] = self.is_online_db

        if self.migrate_task_id is not None:
            result['MigrateTaskId'] = self.migrate_task_id

        if self.ossurls is not None:
            result['OSSUrls'] = self.ossurls

        if self.oss_object_positions is not None:
            result['OssObjectPositions'] = self.oss_object_positions

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('CheckDBMode') is not None:
            self.check_dbmode = m.get('CheckDBMode')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('IsOnlineDB') is not None:
            self.is_online_db = m.get('IsOnlineDB')

        if m.get('MigrateTaskId') is not None:
            self.migrate_task_id = m.get('MigrateTaskId')

        if m.get('OSSUrls') is not None:
            self.ossurls = m.get('OSSUrls')

        if m.get('OssObjectPositions') is not None:
            self.oss_object_positions = m.get('OssObjectPositions')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

