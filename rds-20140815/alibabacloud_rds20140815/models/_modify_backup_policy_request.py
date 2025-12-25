# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBackupPolicyRequest(DaraModel):
    def __init__(
        self,
        archive_backup_keep_count: int = None,
        archive_backup_keep_policy: str = None,
        archive_backup_retention_period: str = None,
        backup_interval: str = None,
        backup_log: str = None,
        backup_method: str = None,
        backup_policy_mode: str = None,
        backup_priority: int = None,
        backup_retention_period: str = None,
        category: str = None,
        compress_type: str = None,
        dbinstance_id: str = None,
        enable_backup_log: str = None,
        enable_increment_data_backup: bool = None,
        high_space_usage_protection: str = None,
        local_log_retention_hours: str = None,
        local_log_retention_space: str = None,
        log_backup_frequency: str = None,
        log_backup_local_retention_number: int = None,
        log_backup_retention_period: str = None,
        owner_account: str = None,
        owner_id: int = None,
        preferred_backup_period: str = None,
        preferred_backup_time: str = None,
        released_keep_policy: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The number of archived backup files that are retained. Default value: **1**. Valid values:
        # 
        # *   Valid values when **ArchiveBackupKeepPolicy** is set to **ByMonth**: **1** to **31**.
        # *   Valid values when **ArchiveBackupKeepPolicy** is set to **ByWeek**: **1** to **7**.
        # 
        # > *   You do not need to specify this parameter when **ArchiveBackupKeepPolicy** is set to **KeepAll**.
        # > *   This parameter takes effect only when **BackupPolicyMode** is set to **DataBackupPolicy**.
        self.archive_backup_keep_count = archive_backup_keep_count
        # The retention period of archived backup files. The number of archived backup files that can be retained within the specified retention period is specified by **ArchiveBackupKeepCount**. Default value: **0**. Valid values:
        # 
        # *   **ByMonth**
        # *   **ByWeek**
        # *   **KeepAll**
        # 
        # > This parameter takes effect only when **BackupPolicyMode** is set to **DataBackupPolicy**.
        self.archive_backup_keep_policy = archive_backup_keep_policy
        # The number of days for which the archived backup is retained. The default value **0** specifies that the backup archiving feature is disabled. Valid values: **30** to **1095**.
        # 
        # > This parameter takes effect only when **BackupPolicyMode** is set to **DataBackupPolicy**.
        self.archive_backup_retention_period = archive_backup_retention_period
        # The frequency at which you want to perform a snapshot backup on the instance. Valid values:
        # 
        # *   **-1**: No backup frequencies are specified.
        # *   **30**: A snapshot backup is performed every 30 minutes.
        # *   **60**: A snapshot backup is performed every 60 minutes.
        # *   **120**: A snapshot backup is performed every 120 minutes.
        # *   **240**: A snapshot backup is performed every 240 minutes.
        # *   **480**: A snapshot backup is performed every 480 minutes.
        # 
        # > *   You can configure a backup policy by using this parameter and the **PreferredBackupPeriod** parameter. For example, if you set **PreferredBackupPeriod** to Saturday,Sunday and BackupInterval to \\*\\*-1\\*\\*, a snapshot backup is performed on every Saturday and Sunday.
        # > *   If the instance runs PostgreSQL, BackupInterval is supported only when the instance is equipped with cloud disks.
        # > *   If the instance runs SQL Server, BackupInterval is supported only when the snapshot backup feature is enabled for the instance. For more information, see [Enable snapshot backups for an ApsaraDB RDS for SQL Server instance](https://help.aliyun.com/document_detail/211143.html).
        # > *   If **Category** is set to **Flash**, BackupInterval is invalid.
        # > *   This parameter takes effect only when **BackupPolicyMode** is set to **DataBackupPolicy**.
        self.backup_interval = backup_interval
        # Specifies whether to enable the log backup feature. Valid values:
        # 
        # *   **Enable**: enables the feature.
        # *   **Disabled**: disables the feature.
        # 
        # > *   This parameter must be specified when **BackupPolicyMode** is set to **DataBackupPolicy**.
        # > *   This parameter takes effect only when **BackupPolicyMode** is set to **DataBackupPolicy**.
        self.backup_log = backup_log
        # The backup method of the instance. Valid values:
        # 
        # *   **Physical**: physical backup
        # *   **Snapshot**: snapshot backup
        # 
        # Default value: **Physical**.
        # 
        # > *   This parameter takes effect only on instances that run SQL Server with cloud disks.
        # > *   This parameter takes effect only when **BackupPolicyMode** is set to **DataBackupPolicy**.
        self.backup_method = backup_method
        # The type of the backup. Valid values:
        # 
        # *   **DataBackupPolicy**: data backup
        # *   **LogBackupPolicy**: log backup
        self.backup_policy_mode = backup_policy_mode
        # Specifies whether the backup settings of a secondary instance are configured. Valid values:
        # 
        # *   **1**: secondary instance preferred
        # *   **2**: primary instance preferred
        # 
        # > *   This parameter is suitable only for instances that run SQL Server on RDS Cluster Edition.
        # > *   This parameter takes effect only when **BackupMethod** is set to **Physical**. If **BackupMethod** is set to **Snapshot**, backups are forcefully performed on the primary instance that runs SQL Server on RDS Cluster Edition.
        self.backup_priority = backup_priority
        # The number of days for which you want to retain data backup files. Valid values: **7 to 730**.
        # 
        # > *   This parameter must be specified when **BackupPolicyMode** is set to **DataBackupPolicy**.
        # > *   This parameter takes effect only when **BackupPolicyMode** is set to **DataBackupPolicy**.
        self.backup_retention_period = backup_retention_period
        # Specifies whether to enable the single-digit second backup feature. Valid values:
        # 
        # *   **Flash**: enables the feature.
        # *   **Standard**: disables the feature.
        # 
        # > This parameter takes effect only when **BackupPolicyMode** is set to **DataBackupPolicy**.
        self.category = category
        # The format that is used to compress backup data. Valid values:
        # 
        # *   **0**: Backups are not compressed.
        # *   **1**: The zlib tool is used to compress backups into .tar.gz files.
        # *   **2**: The zlib tool is used to compress backups in parallel.
        # *   **4**: The QuickLZ tool is used to compress backups into .xb.gz files. This compression format is supported for instances that run MySQL 5.6 or MySQL 5.7. Backups in this compression format can be used to restore individual databases and tables. For more information, see [Restore individual databases and tables of an ApsaraDB RDS for MySQL instance](https://help.aliyun.com/document_detail/103175.html).
        # *   **8**: The QuickLZ tool is used to compress backups into .xb.gz files. This compression format is supported only for instances that run MySQL 8.0. Backups in this compression format cannot be used to restore individual databases and tables.
        # 
        # > This parameter takes effect only when **BackupPolicyMode** is set to **DataBackupPolicy**.
        self.compress_type = compress_type
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Specifies whether to enable the log backup feature. Valid values:
        # 
        # *   **True** or **1**: enables the log backup feature.
        # *   **False** or **0**: disables the log backup feature.
        # 
        # > 
        # 
        # *   You must specify this parameter when you set the **BackupPolicyMode** parameter to **LogBackupPolicy**.
        # 
        # *   This parameter takes effect only when you set the **BackupPolicyMode** parameter to **LogBackupPolicy**.
        self.enable_backup_log = enable_backup_log
        # Specifies whether to enable incremental backup. Valid values:
        # 
        # *   **false** (default): disables the feature.
        # *   **true**: enables the feature.
        # 
        # > *   This parameter takes effect only on instances that run SQL Server with cloud disks.
        # > *   This parameter takes effect only when **BackupPolicyMode** is set to **DataBackupPolicy**.
        self.enable_increment_data_backup = enable_increment_data_backup
        # Specifies whether to forcefully delete log backup files from the instance when the storage usage of the instance exceeds 80% or the amount of remaining storage on the instance is less than 5 GB. Valid values: **Enable and Disable**. You can retain the default value.
        # 
        # > *   You must specify this parameter when you set the **BackupPolicyMode** parameter to **LogBackupPolicy**.
        # > *   This parameter takes effect only when you set the **BackupPolicyMode** parameter to **LogBackupPolicy**.
        self.high_space_usage_protection = high_space_usage_protection
        # The number of hours for which you want to retain log backup files on the instance. Valid values: **0 to 168**. The value 0 specifies that log backup files are not retained on the instance. The value 168 is calculated based on the following formula: 7 × 24.
        # 
        # > *   This parameter must be specified when **BackupPolicyMode** is set to **LogBackupPolicy**.
        # > *   This parameter takes effect only when **BackupPolicyMode** is set to **LogBackupPolicy**.
        self.local_log_retention_hours = local_log_retention_hours
        # The maximum storage usage that is allowed for log backup files on the instance. If the storage usage for log backup files on the instance exceeds the value of this parameter, the system deletes earlier log backup files until the storage usage falls below the value of this parameter. Valid values:**0 to 50**. You can retain the default value.
        # 
        # > *   This parameter must be specified when **BackupPolicyMode** is set to **LogBackupPolicy**.
        # > *   This parameter takes effect only when **BackupPolicyMode** is set to **LogBackupPolicy**.
        self.local_log_retention_space = local_log_retention_space
        # The frequency at which you want to back up the logs of the instance. Valid values:
        # 
        # *   **LogInterval**: A log backup is performed every 30 minutes.
        # *   The default value is the same as the data backup frequency.
        # 
        # > *   The value **LogInterval** is supported only for instances that run SQL Server.
        # > *   This parameter takes effect only when **BackupPolicyMode** is set to **DataBackupPolicy**.
        self.log_backup_frequency = log_backup_frequency
        # The number of binary log files that you want to retain on the instance. Default value: **60**. Valid values: **6** to **100**.
        # 
        # > 
        # 
        # *   This parameter takes effect only when you set the **BackupPolicyMode** parameter to **LogBackupPolicy**.
        # 
        # *   If the instance runs MySQL, you can set this parameter to \\*\\*-1\\*\\*. The value \\*\\*-1\\*\\* specifies that an unlimited number of binary log files can be retained on the instance.
        self.log_backup_local_retention_number = log_backup_local_retention_number
        # The number of days for which the log backup is retained. Valid values: **7 to 730**. The log backup retention period cannot be longer than the data backup retention period.
        # 
        # > *   If you enable the log backup feature, you can specify the log backup retention period. This parameter is supported for instances that run MySQL and PostgreSQL.
        # > *   This parameter takes effect only when **BackupPolicyMode** is set to **DataBackupPolicy** or **LogBackupPolicy**.
        self.log_backup_retention_period = log_backup_retention_period
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The backup cycle. Specify at least two days of the week and separate the days with commas (,). Valid values:
        # 
        # *   **Monday**
        # *   **Tuesday**
        # *   **Wednesday**
        # *   **Thursday**
        # *   **Friday**
        # *   **Saturday**
        # *   **Sunday**
        # 
        # > *   You can configure a backup policy by using this parameter and the **BackupInterval** parameter. For example, if you set this parameter to Saturday,Sunday and the **BackupInterval** parameter to 30, a backup is performed every 30 minutes on every Saturday and Sunday.
        # > *   This parameter must be specified when **BackupPolicyMode** is set to **DataBackupPolicy**.
        # > *   This parameter takes effect only when **BackupPolicyMode** is set to **DataBackupPolicy**.
        self.preferred_backup_period = preferred_backup_period
        # The time at which you want to perform a backup. Specify the time in the ISO 8601 standard in the *HH:mm*Z-*HH:mm*Z format. The time must be in UTC.
        # 
        # > *   This parameter must be specified when **BackupPolicyMode** is set to **DataBackupPolicy**.
        # > *   This parameter takes effect only when **BackupPolicyMode** is set to **DataBackupPolicy**.
        self.preferred_backup_time = preferred_backup_time
        # The policy that is used to retain archived backup files if the instance is released. Valid values:
        # 
        # *   **None**: No archived backup files are retained.
        # *   **Lastest**: Only the last archived backup file is retained.
        # *   **All**: All archived backup files are retained.
        # 
        # > *   This parameter takes effect only when you set the **BackupPolicyMode** parameter to **DataBackupPolicy**.
        # > *   If the instance uses cloud disks and was created on or after February 1, 2024, this parameter is automatically set to **Lastest**. If the instance uses local disks in the same scenario, this parameter is automatically set to **None**. For more information, see [Backup for deleted instances](https://help.aliyun.com/document_detail/2836955.html).
        self.released_keep_policy = released_keep_policy
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.archive_backup_keep_count is not None:
            result['ArchiveBackupKeepCount'] = self.archive_backup_keep_count

        if self.archive_backup_keep_policy is not None:
            result['ArchiveBackupKeepPolicy'] = self.archive_backup_keep_policy

        if self.archive_backup_retention_period is not None:
            result['ArchiveBackupRetentionPeriod'] = self.archive_backup_retention_period

        if self.backup_interval is not None:
            result['BackupInterval'] = self.backup_interval

        if self.backup_log is not None:
            result['BackupLog'] = self.backup_log

        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method

        if self.backup_policy_mode is not None:
            result['BackupPolicyMode'] = self.backup_policy_mode

        if self.backup_priority is not None:
            result['BackupPriority'] = self.backup_priority

        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period

        if self.category is not None:
            result['Category'] = self.category

        if self.compress_type is not None:
            result['CompressType'] = self.compress_type

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log

        if self.enable_increment_data_backup is not None:
            result['EnableIncrementDataBackup'] = self.enable_increment_data_backup

        if self.high_space_usage_protection is not None:
            result['HighSpaceUsageProtection'] = self.high_space_usage_protection

        if self.local_log_retention_hours is not None:
            result['LocalLogRetentionHours'] = self.local_log_retention_hours

        if self.local_log_retention_space is not None:
            result['LocalLogRetentionSpace'] = self.local_log_retention_space

        if self.log_backup_frequency is not None:
            result['LogBackupFrequency'] = self.log_backup_frequency

        if self.log_backup_local_retention_number is not None:
            result['LogBackupLocalRetentionNumber'] = self.log_backup_local_retention_number

        if self.log_backup_retention_period is not None:
            result['LogBackupRetentionPeriod'] = self.log_backup_retention_period

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period

        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time

        if self.released_keep_policy is not None:
            result['ReleasedKeepPolicy'] = self.released_keep_policy

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveBackupKeepCount') is not None:
            self.archive_backup_keep_count = m.get('ArchiveBackupKeepCount')

        if m.get('ArchiveBackupKeepPolicy') is not None:
            self.archive_backup_keep_policy = m.get('ArchiveBackupKeepPolicy')

        if m.get('ArchiveBackupRetentionPeriod') is not None:
            self.archive_backup_retention_period = m.get('ArchiveBackupRetentionPeriod')

        if m.get('BackupInterval') is not None:
            self.backup_interval = m.get('BackupInterval')

        if m.get('BackupLog') is not None:
            self.backup_log = m.get('BackupLog')

        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')

        if m.get('BackupPolicyMode') is not None:
            self.backup_policy_mode = m.get('BackupPolicyMode')

        if m.get('BackupPriority') is not None:
            self.backup_priority = m.get('BackupPriority')

        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CompressType') is not None:
            self.compress_type = m.get('CompressType')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')

        if m.get('EnableIncrementDataBackup') is not None:
            self.enable_increment_data_backup = m.get('EnableIncrementDataBackup')

        if m.get('HighSpaceUsageProtection') is not None:
            self.high_space_usage_protection = m.get('HighSpaceUsageProtection')

        if m.get('LocalLogRetentionHours') is not None:
            self.local_log_retention_hours = m.get('LocalLogRetentionHours')

        if m.get('LocalLogRetentionSpace') is not None:
            self.local_log_retention_space = m.get('LocalLogRetentionSpace')

        if m.get('LogBackupFrequency') is not None:
            self.log_backup_frequency = m.get('LogBackupFrequency')

        if m.get('LogBackupLocalRetentionNumber') is not None:
            self.log_backup_local_retention_number = m.get('LogBackupLocalRetentionNumber')

        if m.get('LogBackupRetentionPeriod') is not None:
            self.log_backup_retention_period = m.get('LogBackupRetentionPeriod')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')

        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')

        if m.get('ReleasedKeepPolicy') is not None:
            self.released_keep_policy = m.get('ReleasedKeepPolicy')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

