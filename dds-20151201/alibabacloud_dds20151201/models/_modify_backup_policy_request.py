# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBackupPolicyRequest(DaraModel):
    def __init__(
        self,
        backup_interval: str = None,
        backup_retention_period: int = None,
        backup_retention_policy_on_cluster_deletion: int = None,
        cross_backup_period: str = None,
        cross_backup_type: str = None,
        cross_log_retention_type: str = None,
        cross_log_retention_value: int = None,
        cross_retention_type: str = None,
        cross_retention_value: int = None,
        dbinstance_id: str = None,
        dest_region: str = None,
        enable_backup_log: int = None,
        enable_cross_log_backup: int = None,
        high_frequency_backup_retention: int = None,
        instance_type: str = None,
        log_backup_retention_period: int = None,
        owner_account: str = None,
        owner_id: int = None,
        preferred_backup_period: str = None,
        preferred_backup_time: str = None,
        preserve_one_each_hour: bool = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        snapshot_backup_type: str = None,
        src_region: str = None,
    ):
        # The frequency at which high-frequency backups are generated. Valid values:
        # 
        # *   **-1**: High-frequency backup is disabled.
        # *   **30**: High-frequency backups are generated every 30 minutes.
        # *   **60**: High-frequency backups are generated every 1 hour.
        # *   **120**: High-frequency backups are generated every 2 hours.
        # *   **180**: High-frequency backups are generated every 3 hours.
        # *   **240**: High-frequency backups are generated every 4 hours.
        # *   **360**: High-frequency backups are generated every 6 hours.
        # *   **480**: High-frequency backups are generated every 8 hours.
        # *   **720**: High-frequency backups are generated every 12 hours.
        # 
        # > 
        # 
        # *   If you set the **SnapshotBackupType** parameter to **Standard**, you must fix the value of this parameter to -1.
        # 
        # *   High-frequency backup takes effect only when you set the **SnapshotBackupType** parameter to **Flash** and this parameter to a value greater than 0.
        self.backup_interval = backup_interval
        # The retention period of full backups.
        # 
        # > 
        # 
        # *   If your instance is created before September 10, 2021, backups are retained for seven days by default.
        # 
        # *   If your instance is created after September 10, 2021, backups are retained for 30 days by default.
        self.backup_retention_period = backup_retention_period
        # The backup retention policy configured for the instance. Valid values:
        # 
        # *   0: All backup sets are immediately deleted when the instance is released.
        # *   1: Automatic backup is performed when the instance is released and the backup set is retained for a long period of time.
        # *   2: Automatic backup is performed when the instance is released and all backup sets are retained for a long period of time.
        # 
        # For more information, see [Retain the backup files of an ApsaraDB for MongoDB instance for a long period of time](https://help.aliyun.com/document_detail/2779111.html).
        self.backup_retention_policy_on_cluster_deletion = backup_retention_policy_on_cluster_deletion
        # The day of the week on which the cross-region backup files are retained. Valid values:
        # 
        # 1.  Monday
        # 2.  Tuesday
        # 3.  Wednesday
        # 4.  Thursday
        # 5.  Friday
        # 6.  Saturday
        # 7.  Sunday
        # 
        # >  This parameter is required for a cross-region backup operation.
        # 
        # *   Separate multiple values with commas (,).
        # 
        # *   If you set the SnapshotBackupType parameter to Standard, the parameter value must fall within the value of the PreferredBackupPeriod parameter that specifies the standard backup period.
        self.cross_backup_period = cross_backup_period
        # The action performed for the cross-region backup policy. Valid values:
        # 
        # *   update: modifies the cross-region backup policy.
        # *   delete: deletes the cross-region backup policy.
        # 
        # >  This parameter is required for a cross-region backup operation.
        self.cross_backup_type = cross_backup_type
        # The retention type of the cross-region log backup files. Valid values:
        # 
        # *   delay: retains the cross-region backup files for a period of time.
        # *   never: permanently retains the cross-region backup files.
        # 
        # >  This parameter is required for a cross-region backup operation.
        self.cross_log_retention_type = cross_log_retention_type
        # The retention period of the cross-region log backup files. Valid values: 3 to 1825. Unit: day. The parameter value must be less than or equal to the value of the CrossRetentionValue parameter.
        # 
        # >  This parameter is required for a cross-region backup operation.
        self.cross_log_retention_value = cross_log_retention_value
        # The retention type of the cross-region backup files. Valid values:
        # 
        # *   delay: retains the cross-region backup files for a period of time.
        # *   never: permanently retains the cross-region backup files.
        # 
        # >  This parameter is required for a cross-region backup operation.
        self.cross_retention_type = cross_retention_type
        # The retention period of the cross-region backup files. Valid values: 3 to 1825. Unit: day.
        # 
        # > 
        # 
        # *   This parameter is required for a cross-region backup operation.
        # 
        # *   This parameter is required when you set the CrossRetentionType parameter to delay.
        self.cross_retention_value = cross_retention_value
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The region in which the backup files are retained.
        # 
        # >  This parameter is required for a cross-region backup operation.
        self.dest_region = dest_region
        # Specifies whether to enable the log backup feature. Valid values:
        # 
        # *   **0** (default): The log backup feature is disabled.
        # *   **1**: The log backup feature is enabled.
        self.enable_backup_log = enable_backup_log
        # Specifies whether to enable the cross-region log backup feature.
        # 
        # >  This parameter is required for a cross-region backup operation.
        # 
        # *   Valid values:1: enables the feature. The parameter value must be 1 for sharded cluster instances.
        # 
        # *   0: disables the feature. The parameter value must be 0 for replica set instances.
        self.enable_cross_log_backup = enable_cross_log_backup
        # The number of days for which high-frequency backup files are retained. Before you use this parameter, make sure that you specify the BackupInterval parameter. By default, high-frequency backup files are retained for one day.
        self.high_frequency_backup_retention = high_frequency_backup_retention
        # The instance architecture. Valid values:
        # 
        # *   replicate
        # *   sharding
        # 
        # > 
        # 
        # *   This parameter is required when you set the RestoreType parameter to 2.
        # 
        # *   This parameter is required when you set the RestoreType parameter to 3.
        self.instance_type = instance_type
        # The number of days for which log backups are retained. Default value: 7.
        # 
        # Valid values: 7 to 730.
        self.log_backup_retention_period = log_backup_retention_period
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The day of a week when the system regularly backs up data. Valid values:
        # 
        # *   **Monday**
        # *   **Tuesday**
        # *   **Wednesday**
        # *   **Thursday**
        # *   **Friday**
        # *   **Saturday**
        # *   **Sunday**
        # 
        # **
        # 
        # **Notice**: To ensure data security, make sure that the system backs up data at least twice a week.
        # 
        # >  Separate multiple values with commas (,).
        self.preferred_backup_period = preferred_backup_period
        # The start time of the backup. Specify the time in the ISO 8601 standard in the *HH:mm*Z-*HH:mm*Z format. The time must be in UTC.
        # 
        # >  The time range is 1 hour.
        self.preferred_backup_time = preferred_backup_time
        self.preserve_one_each_hour = preserve_one_each_hour
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The snapshot backup type. Valid values:
        # 
        # *   **Flash**: single-digit second backup
        # *   **Standard** (default): standard backup
        self.snapshot_backup_type = snapshot_backup_type
        # The region ID of the instance.
        # 
        # > 
        # 
        # *   This parameter is required for the data restoration of a deleted instance.
        # 
        # *   This parameter is required for a cross-region backup operation.
        self.src_region = src_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_interval is not None:
            result['BackupInterval'] = self.backup_interval

        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period

        if self.backup_retention_policy_on_cluster_deletion is not None:
            result['BackupRetentionPolicyOnClusterDeletion'] = self.backup_retention_policy_on_cluster_deletion

        if self.cross_backup_period is not None:
            result['CrossBackupPeriod'] = self.cross_backup_period

        if self.cross_backup_type is not None:
            result['CrossBackupType'] = self.cross_backup_type

        if self.cross_log_retention_type is not None:
            result['CrossLogRetentionType'] = self.cross_log_retention_type

        if self.cross_log_retention_value is not None:
            result['CrossLogRetentionValue'] = self.cross_log_retention_value

        if self.cross_retention_type is not None:
            result['CrossRetentionType'] = self.cross_retention_type

        if self.cross_retention_value is not None:
            result['CrossRetentionValue'] = self.cross_retention_value

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dest_region is not None:
            result['DestRegion'] = self.dest_region

        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log

        if self.enable_cross_log_backup is not None:
            result['EnableCrossLogBackup'] = self.enable_cross_log_backup

        if self.high_frequency_backup_retention is not None:
            result['HighFrequencyBackupRetention'] = self.high_frequency_backup_retention

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

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

        if self.preserve_one_each_hour is not None:
            result['PreserveOneEachHour'] = self.preserve_one_each_hour

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.snapshot_backup_type is not None:
            result['SnapshotBackupType'] = self.snapshot_backup_type

        if self.src_region is not None:
            result['SrcRegion'] = self.src_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupInterval') is not None:
            self.backup_interval = m.get('BackupInterval')

        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')

        if m.get('BackupRetentionPolicyOnClusterDeletion') is not None:
            self.backup_retention_policy_on_cluster_deletion = m.get('BackupRetentionPolicyOnClusterDeletion')

        if m.get('CrossBackupPeriod') is not None:
            self.cross_backup_period = m.get('CrossBackupPeriod')

        if m.get('CrossBackupType') is not None:
            self.cross_backup_type = m.get('CrossBackupType')

        if m.get('CrossLogRetentionType') is not None:
            self.cross_log_retention_type = m.get('CrossLogRetentionType')

        if m.get('CrossLogRetentionValue') is not None:
            self.cross_log_retention_value = m.get('CrossLogRetentionValue')

        if m.get('CrossRetentionType') is not None:
            self.cross_retention_type = m.get('CrossRetentionType')

        if m.get('CrossRetentionValue') is not None:
            self.cross_retention_value = m.get('CrossRetentionValue')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DestRegion') is not None:
            self.dest_region = m.get('DestRegion')

        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')

        if m.get('EnableCrossLogBackup') is not None:
            self.enable_cross_log_backup = m.get('EnableCrossLogBackup')

        if m.get('HighFrequencyBackupRetention') is not None:
            self.high_frequency_backup_retention = m.get('HighFrequencyBackupRetention')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

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

        if m.get('PreserveOneEachHour') is not None:
            self.preserve_one_each_hour = m.get('PreserveOneEachHour')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SnapshotBackupType') is not None:
            self.snapshot_backup_type = m.get('SnapshotBackupType')

        if m.get('SrcRegion') is not None:
            self.src_region = m.get('SrcRegion')

        return self

