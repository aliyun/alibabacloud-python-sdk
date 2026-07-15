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
        # The frequency of high-frequency backups. Valid values:
        # 
        # - **-1**: High-frequency backup is disabled.
        # 
        # - **30**: every 30 minutes.
        # 
        # - **60**: every 1 hour.
        # 
        # - **120**: every 2 hours.
        # 
        # - **180**: every 3 hours.
        # 
        # - **240**: every 4 hours.
        # 
        # - **360**: every 6 hours.
        # 
        # - **480**: every 8 hours.
        # 
        # - **720**: every 12 hours.
        # 
        # > * If you set **SnapshotBackupType** to **Standard**, the value of this parameter is -1.
        # >
        # > * High-frequency backup takes effect only if you set **SnapshotBackupType** to **Flash** and set this parameter to a value greater than 0.
        self.backup_interval = backup_interval
        # The number of days to retain full backups.
        # 
        # > - For instances that were created before September 10, 2021, the default retention period is 7 days.
        # >
        # > - For instances that are created after September 10, 2021, the default retention period is 30 days.
        self.backup_retention_period = backup_retention_period
        # The policy to retain backups when you release the instance.
        # 
        # - 0: All backup sets of the instance are deleted when the instance is released.
        # 
        # - 1: An automatic backup is performed when the instance is released, and this backup is retained for a long time.
        # 
        # - 2: An automatic backup is performed when the instance is released, and all backup sets of the instance are retained for a long time.
        # 
        # For more information, see [Long-term backup retention](https://help.aliyun.com/document_detail/2779111.html).
        self.backup_retention_policy_on_cluster_deletion = backup_retention_policy_on_cluster_deletion
        # The days of the week to perform geo-redundant backups. Valid values:
        # 
        # 1. Monday
        # 
        # 2. Tuesday
        # 
        # 3. Wednesday
        # 
        # 4. Thursday
        # 
        # 5. Friday
        # 
        # 6. Saturday
        # 
        # 7. Sunday
        # 
        # > This parameter is required if you enable geo-redundancy.
        # >
        # > - To specify multiple days, separate them with commas (,).
        # >
        # > - If you set the backup method to conventional backup, the days of the week specified by this parameter must be a subset of the days of the week specified by PreferredBackupPeriod.
        self.cross_backup_period = cross_backup_period
        # The policy for geo-redundant backups. Valid values:
        # 
        # - update: Modify the geo-redundancy policy.
        # 
        # - delete: Delete the geo-redundancy policy.
        # 
        # > This parameter is required if you enable geo-redundancy.
        self.cross_backup_type = cross_backup_type
        # The retention policy for cross-region log backups. Valid values:
        # 
        # - delay: Retain the backup for a specified period.
        # 
        # - never: Retain the backup permanently.
        # 
        # > This parameter is required if you enable geo-redundancy.
        self.cross_log_retention_type = cross_log_retention_type
        # The number of days to retain cross-region log backups. Valid values: 3 to 1825. The value must be less than or equal to the value of CrossRetentionValue.
        # 
        # > This parameter is required if you enable geo-redundancy.
        self.cross_log_retention_value = cross_log_retention_value
        # The retention policy for geo-redundant backups. Valid values:
        # 
        # - delay: Retain the backup for a specified period.
        # 
        # - never: Retain the backup permanently.
        # 
        # > This parameter is required if you enable geo-redundancy.
        self.cross_retention_type = cross_retention_type
        # The number of days to retain geo-redundant backups. Valid values: 3 to 1825.
        # 
        # > - This parameter is required if you enable geo-redundancy.
        # >
        # > - This parameter is required if you set CrossRetentionType to delay.
        self.cross_retention_value = cross_retention_value
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The region ID of the geo-redundant backup.
        # 
        # > This parameter is required if you enable geo-redundancy.
        self.dest_region = dest_region
        # Specifies whether to enable log backup. Valid values:
        # 
        # - **0**: Disable log backup. This is the default value.
        # 
        # - **1**: Enable log backup.
        # 
        # >Notice: 
        # 
        # You cannot disable log backup for sharded cluster instances.
        self.enable_backup_log = enable_backup_log
        # Specifies whether to enable cross-region log backup. Valid values:
        # 
        # > This parameter is required if you enable geo-redundancy.
        # >
        # > - 1: Enable cross-region log backup. This value is required for sharded cluster instances. This value is also required for replica set instances if you want to enable geo-redundant point-in-time recovery.
        # >
        # > - 0: Disable cross-region log backup.
        self.enable_cross_log_backup = enable_cross_log_backup
        # The number of days to retain high-frequency backups. Before you specify this parameter, you must set the BackupInterval parameter. The default retention period is 1 day.
        self.high_frequency_backup_retention = high_frequency_backup_retention
        # The instance type. Valid values:
        # 
        # - replicate
        # 
        # - sharding
        # 
        # > * This parameter is required when you restore a deleted instance.
        # >
        # > * This parameter is required when you clone an instance from a geo-redundant backup.
        self.instance_type = instance_type
        # The number of days to retain log backups. Default value: 7.
        # 
        # Valid values: 7 to 730.
        self.log_backup_retention_period = log_backup_retention_period
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The backup cycle. Valid values:
        # 
        # - **Monday**
        # 
        # - **Tuesday**
        # 
        # - **Wednesday**
        # 
        # - **Thursday**
        # 
        # - **Friday**
        # 
        # - **Saturday**
        # 
        # - **Sunday**
        # 
        # >Notice: 
        # 
        # To ensure data security, back up the MongoDB instance at least twice a week.
        # 
        # 
        # 
        # > To specify multiple backup cycles, separate them with commas (,).
        self.preferred_backup_period = preferred_backup_period
        # The time range to perform a backup. Specify the time in the *HH:mm*Z-*HH:mm*Z format. The time is displayed in Coordinated Universal Time (UTC).
        # 
        # > The time range must be 1 hour.
        self.preferred_backup_time = preferred_backup_time
        # Specifies whether to enable hourly sparse backup. Valid values:
        # 
        # - true: If the backup frequency is in minutes, all snapshots that are generated within the last hour are retained. For snapshots that were generated more than 1 hour ago but less than 24 hours ago, only the first snapshot that is generated after each full hour is retained.
        # 
        # - false: All snapshots are retained within the high-frequency backup retention period.
        self.preserve_one_each_hour = preserve_one_each_hour
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The snapshot backup type. Valid values:
        # 
        # - **Flash**: second-level backup.
        # 
        # - **Standard**: conventional backup. This is the default value.
        self.snapshot_backup_type = snapshot_backup_type
        # The region ID of the instance.
        # 
        # > - This parameter is required if you restore a deleted instance.
        # >
        # > - This parameter is required if you enable geo-redundancy.
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

