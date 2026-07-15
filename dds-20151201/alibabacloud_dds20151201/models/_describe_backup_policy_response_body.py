# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupPolicyResponseBody(DaraModel):
    def __init__(
        self,
        backup_interval: int = None,
        backup_retention_period: str = None,
        backup_retention_policy_on_cluster_deletion: int = None,
        cross_backup_period: str = None,
        cross_log_retention_type: str = None,
        cross_log_retention_value: int = None,
        cross_retention_type: str = None,
        cross_retention_value: int = None,
        dest_region: str = None,
        enable_backup_log: int = None,
        enable_cross_log_backup: int = None,
        high_frequency_backup_retention: str = None,
        log_backup_retention_period: int = None,
        preferred_backup_period: str = None,
        preferred_backup_time: str = None,
        preferred_next_backup_time: str = None,
        preserve_one_each_hour: bool = None,
        request_id: str = None,
        snapshot_backup_type: str = None,
        src_region: str = None,
    ):
        # The high-frequency backup frequency. Valid values:
        # 
        # - **-1**: high-frequency backup is disabled.
        # 
        # - **15**: every 15 minutes.
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
        self.backup_interval = backup_interval
        # The backup retention period in days.
        self.backup_retention_period = backup_retention_period
        # The backup retention policy.
        # 
        # 1. 0: All backup sets of the instance are immediately deleted when the instance is released
        # 
        # 2. 1: The instance is automatically backed up when it is released, and the backup set is retained for a long time
        # 
        # 3. 2: The instance is automatically backed up when it is released, and all backup sets of the cluster are retained for a long time
        # 
        # For more information, see [Long-term backup retention](https://help.aliyun.com/document_detail/2779111.html)
        self.backup_retention_policy_on_cluster_deletion = backup_retention_policy_on_cluster_deletion
        # The geo-redundancy backup retention time.
        # 
        # 1. Monday: Monday.
        # 
        # 2. Tuesday: Tuesday.
        # 
        # 3. Wednesday: Wednesday.
        # 
        # 4. Thursday: Thursday.
        # 
        # 5. Friday: Friday.
        # 
        # 6. Saturday: Saturday.
        # 
        # 7. Sunday: Sunday.
        # 
        # > Required for geo-redundancy backup
        self.cross_backup_period = cross_backup_period
        # The geo-redundancy log backup retention type.
        # 
        # - delay: retained for a period of time
        # 
        # - never: never expires
        self.cross_log_retention_type = cross_log_retention_type
        # The geo-redundancy log backup retention period.
        self.cross_log_retention_value = cross_log_retention_value
        # The geo-redundancy backup retention type.
        # 
        # - delay: retained for a period of time
        # 
        # - never: never expires
        self.cross_retention_type = cross_retention_type
        # The geo-redundancy backup retention period.
        self.cross_retention_value = cross_retention_value
        # The region where the geo-redundancy backup is located.
        self.dest_region = dest_region
        # Indicates whether log backup is enabled. Valid values:
        # 
        # - **0**: disabled (default).
        # 
        # - **1**: enabled.
        self.enable_backup_log = enable_backup_log
        # Indicates whether cross-region log backup is enabled.
        # 
        # > Required for geo-redundancy backup
        # >
        # > - 1: enabled (must be 1 for sharded cluster instances)
        # >
        # > - 0: disabled (must be 0 for replica set instances)
        self.enable_cross_log_backup = enable_cross_log_backup
        # The high-frequency backup retention period in days.
        self.high_frequency_backup_retention = high_frequency_backup_retention
        # The log backup retention period in days. Valid values: 7 to 730.
        self.log_backup_retention_period = log_backup_retention_period
        # The backup cycle. Valid values:
        # 
        # - **Monday**: Monday.
        # 
        # - **Tuesday**: Tuesday.
        # 
        # - **Wednesday**: Wednesday.
        # 
        # - **Thursday**: Thursday.
        # 
        # - **Friday**: Friday.
        # 
        # - **Saturday**: Saturday.
        # 
        # - **Sunday**: Sunday.
        self.preferred_backup_period = preferred_backup_period
        # The backup time in the format of *HH:mm*Z-*HH:mm*Z (UTC time).
        self.preferred_backup_time = preferred_backup_time
        # The next regular backup time in the format of *yyyy-mm-dd*t*hh:mm*z (UTC time).
        self.preferred_next_backup_time = preferred_next_backup_time
        # Indicates whether sparse backup within an hour is enabled.
        # 
        # - true: When the backup frequency is at the minute level, all snapshots within 1 hour from the current time are retained. For snapshots that are more than 1 hour but within 24 hours from the current time, only the first snapshot after each hour is retained.
        # 
        # - false: Sparse backup within an hour is disabled: all snapshots within the high-frequency backup retention period are retained.
        self.preserve_one_each_hour = preserve_one_each_hour
        # The request ID.
        self.request_id = request_id
        # The snapshot backup type. Valid values:
        # 
        # - **Flash**: second-level backup.
        # 
        # - **Standard**: regular backup (default).
        self.snapshot_backup_type = snapshot_backup_type
        # The region where the source instance is located.
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

        if self.cross_log_retention_type is not None:
            result['CrossLogRetentionType'] = self.cross_log_retention_type

        if self.cross_log_retention_value is not None:
            result['CrossLogRetentionValue'] = self.cross_log_retention_value

        if self.cross_retention_type is not None:
            result['CrossRetentionType'] = self.cross_retention_type

        if self.cross_retention_value is not None:
            result['CrossRetentionValue'] = self.cross_retention_value

        if self.dest_region is not None:
            result['DestRegion'] = self.dest_region

        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log

        if self.enable_cross_log_backup is not None:
            result['EnableCrossLogBackup'] = self.enable_cross_log_backup

        if self.high_frequency_backup_retention is not None:
            result['HighFrequencyBackupRetention'] = self.high_frequency_backup_retention

        if self.log_backup_retention_period is not None:
            result['LogBackupRetentionPeriod'] = self.log_backup_retention_period

        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period

        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time

        if self.preferred_next_backup_time is not None:
            result['PreferredNextBackupTime'] = self.preferred_next_backup_time

        if self.preserve_one_each_hour is not None:
            result['PreserveOneEachHour'] = self.preserve_one_each_hour

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('CrossLogRetentionType') is not None:
            self.cross_log_retention_type = m.get('CrossLogRetentionType')

        if m.get('CrossLogRetentionValue') is not None:
            self.cross_log_retention_value = m.get('CrossLogRetentionValue')

        if m.get('CrossRetentionType') is not None:
            self.cross_retention_type = m.get('CrossRetentionType')

        if m.get('CrossRetentionValue') is not None:
            self.cross_retention_value = m.get('CrossRetentionValue')

        if m.get('DestRegion') is not None:
            self.dest_region = m.get('DestRegion')

        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')

        if m.get('EnableCrossLogBackup') is not None:
            self.enable_cross_log_backup = m.get('EnableCrossLogBackup')

        if m.get('HighFrequencyBackupRetention') is not None:
            self.high_frequency_backup_retention = m.get('HighFrequencyBackupRetention')

        if m.get('LogBackupRetentionPeriod') is not None:
            self.log_backup_retention_period = m.get('LogBackupRetentionPeriod')

        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')

        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')

        if m.get('PreferredNextBackupTime') is not None:
            self.preferred_next_backup_time = m.get('PreferredNextBackupTime')

        if m.get('PreserveOneEachHour') is not None:
            self.preserve_one_each_hour = m.get('PreserveOneEachHour')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SnapshotBackupType') is not None:
            self.snapshot_backup_type = m.get('SnapshotBackupType')

        if m.get('SrcRegion') is not None:
            self.src_region = m.get('SrcRegion')

        return self

