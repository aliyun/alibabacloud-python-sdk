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
        keep_cdc: bool = None,
        migrate_task_id: str = None,
        ossurls: str = None,
        oss_object_positions: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The type of the cloud migration task. Valid values:
        # * **FULL**: restores data by using a full backup file. This value is applicable to the first migration or full data recovery scenarios.
        # * **UPDF**: restores incremental data by using an incremental backup file or log file. This value is applicable to incremental synchronization scenarios based on an existing full backup.
        # 
        # This parameter is required.
        self.backup_mode = backup_mode
        # The consistency check method used after the database is opened. This parameter takes effect only when IsOnlineDB is set to True. Valid values:
        # 
        # - **SyncExecuteDBCheck**: synchronously executes the database check. This value is applicable to scenarios that require high data consistency.
        # - **AsyncExecuteDBCheck**: asynchronously executes the database check. This value provides higher performance but may delay the discovery of potential issues.
        # 
        # Default value: **AsyncExecuteDBCheck** (compatible with SQL Server 2008 R2).
        self.check_dbmode = check_dbmode
        # The instance ID. You can call the DescribeDBInstances operation to query the ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the destination database.
        # 
        # This parameter is required.
        self.dbname = dbname
        # Specifies whether to bring the restored database online for user access. Valid values:
        # 
        # * **True**: brings the database online.
        # * **False**: does not bring the database online.
        # 
        # > * For SQL Server 2008 R2, this value is always True.
        # > * If **IsOnlineDB** is set to **True**, **BackupMode** must be set to **FULL**.
        # > * If **IsOnlineDB** is set to **False**, **BackupMode** must be set to **UPDF**.
        # 
        # This parameter is required.
        self.is_online_db = is_online_db
        # Specifies whether to retain the database- and table-level Change Data Capture (CDC) switches and change table data. This parameter takes effect only when IsOnlineDB is set to True. Regardless of the value of this parameter, CDC jobs are not rebuilt.
        self.keep_cdc = keep_cdc
        # The ID of the migration task. Valid values:
        # 
        # - If **BackupMode** is set to **FULL**, leave this parameter empty. This ensures compatibility with SQL Server 2008 R2.
        # - If **BackupMode** is set to **UPDF**, set this parameter to the ID of the corresponding FULL task. You can call the DescribeMigrateTasks operation to query the ID.
        self.migrate_task_id = migrate_task_id
        # The shared URL of the backup file in OSS. The URL must be encoded. If multiple URLs exist, separate them with vertical bars (|) and then encode the string before passing it as the parameter value.
        # 
        # > This parameter is required for SQL Server 2008 R2.
        self.ossurls = ossurls
        # The components of the OSS file. The value consists of the following three parts separated by colons (:):
        # - **OSS endpoint**: oss-ap-southeast-1.aliyuncs.com.
        # - **OSS bucket name**: rdsmssqlsingapore.
        # - **Backup file name in OSS**: autotest_2008R2_TestMigration_FULL.bak.
        # 
        # > This parameter is required for SQL Server versions later than 2008 R2.
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

        if self.keep_cdc is not None:
            result['KeepCDC'] = self.keep_cdc

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

        if m.get('KeepCDC') is not None:
            self.keep_cdc = m.get('KeepCDC')

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

