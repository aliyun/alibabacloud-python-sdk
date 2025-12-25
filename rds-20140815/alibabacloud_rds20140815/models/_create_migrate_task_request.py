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
        # The type of the migration task. Valid values:
        # 
        # *   **FULL**: The migration task migrates full backup files.
        # *   **UPDF**: The migration task migrates incremental or log backup files.
        # 
        # This parameter is required.
        self.backup_mode = backup_mode
        # The consistency check method for the database. Valid values:
        # 
        # *   **SyncExecuteDBCheck**: synchronous database check
        # *   **AsyncExecuteDBCheck**: asynchronous database check
        # 
        # Default value: **AsyncExecuteDBCheck** (compatible with SQL Server 2008 R2)
        # 
        # >  This parameter is valid when **IsOnlineDB** is set to **True**.
        self.check_dbmode = check_dbmode
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the destination database.
        # 
        # This parameter is required.
        self.dbname = dbname
        # Specifies whether to make the restored database data available for user access. Valid values:
        # 
        # *   **True**
        # *   **False**
        # 
        # >  Set the value to **True** for instances that run SQL Server 2008 R2.
        # 
        # This parameter is required.
        self.is_online_db = is_online_db
        # The migration task ID.
        # 
        # *   If you set **BackupMode** to **FULL**, the value of this parameter is empty. The full backup mode is compatible with instance that runs SQL Server 2008 R2.
        # *   If you set **BackupMode** to **UPDF**, the value of this parameter is the ID of the required full migration task.
        # 
        # > *   If you set **IsOnlineDB** to **True**, the value of **BackupMode** must be **FULL**.
        # > *   If you set **IsOnlineDB** to **False**, the value of **BackupMode** must be **UPDF**.
        self.migrate_task_id = migrate_task_id
        # The shared URL of the backup file in the OSS bucket. The URL must be encoded.
        # 
        # If you specify multiple URLs, separate them with vertical bars (|) and then encode them.
        # 
        # >  This parameter is required for instances that run SQL Server 2008 R2.
        self.ossurls = ossurls
        # The information about the backup file in the OSS bucket. The values consist of three parts that are separated by colons (:):
        # 
        # *   OSS endpoint: oss-ap-southeast-1.aliyuncs.com.
        # *   Name of the OSS bucket: rdsmssqlsingapore.
        # *   Key of the backup file in the OSS bucket: autotest_2008R2_TestMigration_FULL.bak.
        # 
        # > *   This parameter is optional for instances that run SQL Server 2008 R2.
        # > *   This parameter is required for instances that run a major engine version later than SQL Server 2008 R2.
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

