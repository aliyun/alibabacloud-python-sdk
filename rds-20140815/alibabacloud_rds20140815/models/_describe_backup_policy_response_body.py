# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupPolicyResponseBody(DaraModel):
    def __init__(
        self,
        archive_backup_keep_count: str = None,
        archive_backup_keep_policy: str = None,
        archive_backup_retention_period: str = None,
        backup_interval: str = None,
        backup_log: str = None,
        backup_method: str = None,
        backup_priority: int = None,
        backup_retention_period: int = None,
        category: str = None,
        compress_type: str = None,
        enable_backup_log: str = None,
        enable_increment_data_backup: bool = None,
        enable_pitr_protection: bool = None,
        high_space_usage_protection: str = None,
        local_log_retention_hours: int = None,
        local_log_retention_space: str = None,
        log_backup_frequency: str = None,
        log_backup_local_retention_number: int = None,
        log_backup_retention_period: int = None,
        pitr_retention_period: int = None,
        preferred_backup_period: str = None,
        preferred_backup_time: str = None,
        preferred_next_backup_time: str = None,
        released_keep_policy: str = None,
        request_id: str = None,
        support_modify_backup_priority: bool = None,
        support_released_keep: int = None,
        support_volume_shadow_copy: int = None,
        supports_high_frequency_backup: int = None,
    ):
        # The number of archived backup files that are retained.
        self.archive_backup_keep_count = archive_backup_keep_count
        # The cycle based on which archived backup files are retained.
        self.archive_backup_keep_policy = archive_backup_keep_policy
        # The number of days for which archived backup files are retained.
        self.archive_backup_retention_period = archive_backup_retention_period
        # The backup interval. Unit: minutes.
        # 
        # *   If the instance runs MySQL, the interval is the same as the value of the Snapshot Backup Start Time parameter rather than the Snapshot Backup Period parameter in the ApsaraDB RDS console. For more information, see [Back up an ApsaraDB RDS for MySQL instance](https://help.aliyun.com/document_detail/98818.html).
        # *   If the instance runs SQL Server, the interval is the same as the log backup frequency.
        self.backup_interval = backup_interval
        # Indicates whether the log backup feature is enabled. Valid values:
        # 
        # *   **Enable**
        # *   **Disabled**
        self.backup_log = backup_log
        # The backup method of the instance. Valid values:
        # 
        # *   **Physical**: physical backup
        # *   **Snapshot**: snapshot backup
        # 
        # > This parameter is returned only when the instance runs SQL Server and uses cloud disks.
        self.backup_method = backup_method
        # The backup settings of the secondary instance. Valid values:
        # 
        # *   **1**: Secondary instance preferred
        # *   **2**: Primary instance preferred
        # 
        # >  This parameter is available only for instances that run SQL Server on RDS Cluster Edition. This parameter is returned only when SupportModifyBackupPriority is set to True.
        self.backup_priority = backup_priority
        # The number of days for which data backup files are retained.
        self.backup_retention_period = backup_retention_period
        # Indicates whether to enable the single-digit second backup feature. This feature allows ApsaraDB RDS to complete a backup within single-digit seconds. Valid values:
        # 
        # *   **Flash**: The single-digit second backup feature is enabled.
        # *   **Standard**: The single-digit second backup feature is disabled.
        # 
        # > This parameter takes effect only when you set the **BackupPolicyMode** parameter to **DataBackupPolicy**.
        self.category = category
        # The method that is used to compress backup data. Valid values:
        # 
        # *   **0**: Backup data is not compressed.
        # *   **1**: Backup data is compressed by using zlib.
        # *   **2**: Backup data is compressed by using zlib that invokes more than one thread in parallel for each backup.
        # *   **4**: Backup data is compressed by using QuickLZ and can be used to restore individual databases or tables.
        # *   **8**: Backup data is compressed by using QuickLZ but cannot be used to restore individual databases or tables.
        self.compress_type = compress_type
        # Indicates whether the log backup feature is enabled. Valid values:
        # 
        # *   **1**: enabled
        # *   **0**: disabled
        self.enable_backup_log = enable_backup_log
        # Indicates whether incremental backup is enabled. Valid values:
        # 
        # *   **True**: Incremental backup is enabled.
        # *   **False**: Incremental backup is disabled.
        self.enable_increment_data_backup = enable_increment_data_backup
        # Indicates whether the point-in-time restoration (PITR) feature is enabled. The PITR feature is an enhancement of the log backup feature. Valid values:
        # 
        # *   **True**
        # *   **False**
        # 
        # >  This parameter is returned only when the instance runs MySQL. For more information, see [Configure the PITR feature](https://help.aliyun.com/document_detail/2666046.html).
        self.enable_pitr_protection = enable_pitr_protection
        # Indicates whether the log backup deletion feature is enabled. If the disk usage exceeds 80% or the remaining disk space is less than 5 GB on the instance, this feature deletes binary log files. Valid values:
        # 
        # *   **Disable**
        # *   **Enable**
        self.high_space_usage_protection = high_space_usage_protection
        # The number of hours for which log backup files are retained on the instance.
        self.local_log_retention_hours = local_log_retention_hours
        # The maximum storage usage that is allowed for log files on the instance.
        self.local_log_retention_space = local_log_retention_space
        # The backup frequency of logs. Valid values:
        # 
        # *   **LogInterval**: Log backups are performed every 30 minutes.
        # *   Default value: same as the value of the **PreferredBackupPeriod** parameter.
        # 
        # >  This parameter is returned only when the instance runs SQL Server.
        self.log_backup_frequency = log_backup_frequency
        # The number of binary log files that you want to retain on the instance.
        self.log_backup_local_retention_number = log_backup_local_retention_number
        # The number of days for which log backup files are retained.
        self.log_backup_retention_period = log_backup_retention_period
        # The number of days during which you can restore data of the instance to any point in time.
        self.pitr_retention_period = pitr_retention_period
        # The cycle based on which you want to perform a backup. Separate multiple values with commas (,). Valid values:
        # 
        # *   **Monday**
        # *   **Tuesday**
        # *   **Wednesday**
        # *   **Thursday**
        # *   **Friday**
        # *   **Saturday**
        # *   **Sunday**
        self.preferred_backup_period = preferred_backup_period
        # The time when a data backup is performed. The time follows the ISO 8601 standard in the *HH:mm*Z-*HH:mm*Z format. The time is displayed in UTC.
        self.preferred_backup_time = preferred_backup_time
        # The time when the next backup is performed. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time is displayed in UTC.
        self.preferred_next_backup_time = preferred_next_backup_time
        # The policy that is used to retain archived backup files if the instance is released. Valid values:
        # 
        # *   **None**: No archived backup files are retained.
        # *   **Lastest**: Only the last archived backup file is retained.
        # *   **All**: All archived backup files are retained.
        self.released_keep_policy = released_keep_policy
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the backup settings of a secondary instance can be modified. Valid values:
        # 
        # *   **True**
        # *   **False**
        self.support_modify_backup_priority = support_modify_backup_priority
        # A reserved parameter.
        self.support_released_keep = support_released_keep
        # Indicates whether the instance supports snapshot backups. Valid values:
        # 
        # *   **1**: The instance supports snapshot backups.
        # *   **0**: The instance does not support snapshot backups.
        # 
        # >  This parameter is returned only when the instance runs SQL Server.
        self.support_volume_shadow_copy = support_volume_shadow_copy
        # Indicates whether log backups for SQL Server are performed verery five minutes.
        # 
        # *   0: No
        # *   1: Yes
        self.supports_high_frequency_backup = supports_high_frequency_backup

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

        if self.backup_priority is not None:
            result['BackupPriority'] = self.backup_priority

        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period

        if self.category is not None:
            result['Category'] = self.category

        if self.compress_type is not None:
            result['CompressType'] = self.compress_type

        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log

        if self.enable_increment_data_backup is not None:
            result['EnableIncrementDataBackup'] = self.enable_increment_data_backup

        if self.enable_pitr_protection is not None:
            result['EnablePitrProtection'] = self.enable_pitr_protection

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

        if self.pitr_retention_period is not None:
            result['PitrRetentionPeriod'] = self.pitr_retention_period

        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period

        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time

        if self.preferred_next_backup_time is not None:
            result['PreferredNextBackupTime'] = self.preferred_next_backup_time

        if self.released_keep_policy is not None:
            result['ReleasedKeepPolicy'] = self.released_keep_policy

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.support_modify_backup_priority is not None:
            result['SupportModifyBackupPriority'] = self.support_modify_backup_priority

        if self.support_released_keep is not None:
            result['SupportReleasedKeep'] = self.support_released_keep

        if self.support_volume_shadow_copy is not None:
            result['SupportVolumeShadowCopy'] = self.support_volume_shadow_copy

        if self.supports_high_frequency_backup is not None:
            result['SupportsHighFrequencyBackup'] = self.supports_high_frequency_backup

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

        if m.get('BackupPriority') is not None:
            self.backup_priority = m.get('BackupPriority')

        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CompressType') is not None:
            self.compress_type = m.get('CompressType')

        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')

        if m.get('EnableIncrementDataBackup') is not None:
            self.enable_increment_data_backup = m.get('EnableIncrementDataBackup')

        if m.get('EnablePitrProtection') is not None:
            self.enable_pitr_protection = m.get('EnablePitrProtection')

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

        if m.get('PitrRetentionPeriod') is not None:
            self.pitr_retention_period = m.get('PitrRetentionPeriod')

        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')

        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')

        if m.get('PreferredNextBackupTime') is not None:
            self.preferred_next_backup_time = m.get('PreferredNextBackupTime')

        if m.get('ReleasedKeepPolicy') is not None:
            self.released_keep_policy = m.get('ReleasedKeepPolicy')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SupportModifyBackupPriority') is not None:
            self.support_modify_backup_priority = m.get('SupportModifyBackupPriority')

        if m.get('SupportReleasedKeep') is not None:
            self.support_released_keep = m.get('SupportReleasedKeep')

        if m.get('SupportVolumeShadowCopy') is not None:
            self.support_volume_shadow_copy = m.get('SupportVolumeShadowCopy')

        if m.get('SupportsHighFrequencyBackup') is not None:
            self.supports_high_frequency_backup = m.get('SupportsHighFrequencyBackup')

        return self

