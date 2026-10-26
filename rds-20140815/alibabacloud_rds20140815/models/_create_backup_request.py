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
        # The backup method. Valid values:
        # * **Logical**: logical backup (supported only for ApsaraDB RDS for MySQL instances with local SSDs)
        # * **Physical**: physical backup (supported for ApsaraDB RDS for MySQL instances with local SSDs, ApsaraDB RDS for SQL Server, and ApsaraDB RDS for PostgreSQL)
        # * **Snapshot**: snapshot backup (supported for ApsaraDB RDS for MySQL instances with cloud disks, ApsaraDB RDS for SQL Server, ApsaraDB RDS for PostgreSQL, and ApsaraDB RDS for MariaDB)
        # 
        # Default value: **Physical**.
        # 
        # > * When you use logical backup, the database must contain data.
        # > * ApsaraDB RDS for MariaDB instances support only snapshot backup, but you must set this parameter to **Physical**.
        self.backup_method = backup_method
        # - **SQL Server**: When the BackupStrategy parameter is set to db, the BackupMethod parameter is set to Physical, and the BackupType parameter is set to FullBackup, you can specify the retention period of the backup set. Valid values: 7 to 730 days, and -1 (long-term retention (LTR)).
        # - **MySQL**: You can specify the retention period of the backup set. Valid values: 7 to 730 days, and -1 (long-term retention (LTR)).
        self.backup_retention_period = backup_retention_period
        # The backup strategy. Valid values:
        # * **db**: database-level backup
        # * **instance**: instance-level backup
        # 
        # > This parameter takes effect only when the following conditions are met:
        # > - For ApsaraDB RDS for MySQL: The **BackupMethod** parameter is set to **Logical**.
        # > - For ApsaraDB RDS for SQL Server: The **BackupType** parameter is set to **FullBackup**.
        self.backup_strategy = backup_strategy
        # The backup type for ApsaraDB RDS for SQL Server instances. Valid values:
        # * **Auto** (default): automatically selects full backup or incremental backup
        # * **FullBackup**: full backup
        # 
        # > This parameter takes effect only when the **BackupMethod** parameter is set to **Physical**.
        self.backup_type = backup_type
        # The instance ID. You can call the DescribeDBInstances operation to obtain the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The list of databases. Separate multiple databases with commas (,).
        # > This parameter takes effect only when the **BackupStrategy** parameter is set to **db**.
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

