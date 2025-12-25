# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBackupRequest(DaraModel):
    def __init__(
        self,
        backup_method: str = None,
        backup_retention_period: int = None,
        backup_strategy: str = None,
        backup_type: str = None,
        dbinstance_id: str = None,
        dbname: str = None,
        resource_owner_id: int = None,
    ):
        # The backup type of the instance. Valid values:
        # 
        # *   **Logical**: logical backup
        # *   **Physical**: physical backup
        # *   **Snapshot**: snapshot backup
        # 
        # Default value: **Physical**.
        # 
        # > *   You can perform a logical backup only when databases are created on the instance.
        # > *   When you perform a snapshot backup on an ApsaraDB RDS for MariaDB instance, you must set this parameter to **Physical**.
        # > *   For more information about the supported backup types, see [Use the data backup feature](https://help.aliyun.com/document_detail/98818.html).
        # > *   When you perform a snapshot backup on an ApsaraDB RDS for SQL Server instance that uses cloud disks, you must set this parameter to **Snapshot**.
        self.backup_method = backup_method
        self.backup_retention_period = backup_retention_period
        # The backup policy. Valid values:
        # 
        # *   **db**: a database-level backup.
        # *   **instance**: an instance-level backup.
        # 
        # > You can specify this parameter when you perform a logical backup on an ApsaraDB RDS for MySQL instance. You can also specify this parameter when you perform a full physical backup on an ApsaraDB RDS for SQL Server instance.
        self.backup_strategy = backup_strategy
        # The backup method. Valid values:
        # 
        # *   **Auto**: full or incremental backup that is automatically selected
        # *   **FullBackup**: full backup
        # 
        # Default value: **Auto**.
        # 
        # > *   You must set this parameter only when the instance runs SQL Server.
        # > *   This parameter is valid only when you set the **BackupMethod** parameter to **Physical**.
        self.backup_type = backup_type
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The names of the databases whose data you want to back up. Separate the names of the databases with commas (,).
        # 
        # > You can specify this parameter when you perform a logical backup on individual databases of an ApsaraDB RDS for MySQL instance. You can also specify this parameter when you perform a full physical backup on individual databases of an ApsaraDB RDS for SQL Server instance.
        self.dbname = dbname
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method

        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period

        if self.backup_strategy is not None:
            result['BackupStrategy'] = self.backup_strategy

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')

        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')

        if m.get('BackupStrategy') is not None:
            self.backup_strategy = m.get('BackupStrategy')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

