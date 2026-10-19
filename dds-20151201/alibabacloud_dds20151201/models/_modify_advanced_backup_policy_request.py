# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class ModifyAdvancedBackupPolicyRequest(DaraModel):
    def __init__(
        self,
        advanced_backup_data_policies: List[main_models.ModifyAdvancedBackupPolicyRequestAdvancedBackupDataPolicies] = None,
        advanced_backup_log_policies: List[main_models.ModifyAdvancedBackupPolicyRequestAdvancedBackupLogPolicies] = None,
        backup_retention_policy_on_cluster_deletion: int = None,
        dbinstance_id: str = None,
        preferred_backup_time: str = None,
        snapshot_backup_type: str = None,
    ):
        # The list of backup policies.
        self.advanced_backup_data_policies = advanced_backup_data_policies
        # The list of log backup policies.
        self.advanced_backup_log_policies = advanced_backup_log_policies
        # The backup retention policy. Valid values:
        # 
        # - 0: All backup sets of the instance are deleted immediately when the instance is released.
        # - 1: The last backup set is retained for long-term retention (LTR) when the instance is released.
        # - 2: All backup sets are retained for long-term retention (LTR) when the instance is released.
        # 
        # This parameter is required.
        self.backup_retention_policy_on_cluster_deletion = backup_retention_policy_on_cluster_deletion
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The time period during which the backup is performed. The format is <i>HH:mm</i>Z-<i>HH:mm</i>Z (UTC).
        # 
        # > The time range is limited to 1 hour.
        self.preferred_backup_time = preferred_backup_time
        # The snapshot backup type. Valid values:
        # 
        # - **Flash**: backup within seconds.
        # - **Standard**: standard backup. This is the default value.
        self.snapshot_backup_type = snapshot_backup_type

    def validate(self):
        if self.advanced_backup_data_policies:
            for v1 in self.advanced_backup_data_policies:
                 if v1:
                    v1.validate()
        if self.advanced_backup_log_policies:
            for v1 in self.advanced_backup_log_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AdvancedBackupDataPolicies'] = []
        if self.advanced_backup_data_policies is not None:
            for k1 in self.advanced_backup_data_policies:
                result['AdvancedBackupDataPolicies'].append(k1.to_map() if k1 else None)

        result['AdvancedBackupLogPolicies'] = []
        if self.advanced_backup_log_policies is not None:
            for k1 in self.advanced_backup_log_policies:
                result['AdvancedBackupLogPolicies'].append(k1.to_map() if k1 else None)

        if self.backup_retention_policy_on_cluster_deletion is not None:
            result['BackupRetentionPolicyOnClusterDeletion'] = self.backup_retention_policy_on_cluster_deletion

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time

        if self.snapshot_backup_type is not None:
            result['SnapshotBackupType'] = self.snapshot_backup_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.advanced_backup_data_policies = []
        if m.get('AdvancedBackupDataPolicies') is not None:
            for k1 in m.get('AdvancedBackupDataPolicies'):
                temp_model = main_models.ModifyAdvancedBackupPolicyRequestAdvancedBackupDataPolicies()
                self.advanced_backup_data_policies.append(temp_model.from_map(k1))

        self.advanced_backup_log_policies = []
        if m.get('AdvancedBackupLogPolicies') is not None:
            for k1 in m.get('AdvancedBackupLogPolicies'):
                temp_model = main_models.ModifyAdvancedBackupPolicyRequestAdvancedBackupLogPolicies()
                self.advanced_backup_log_policies.append(temp_model.from_map(k1))

        if m.get('BackupRetentionPolicyOnClusterDeletion') is not None:
            self.backup_retention_policy_on_cluster_deletion = m.get('BackupRetentionPolicyOnClusterDeletion')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')

        if m.get('SnapshotBackupType') is not None:
            self.snapshot_backup_type = m.get('SnapshotBackupType')

        return self

class ModifyAdvancedBackupPolicyRequestAdvancedBackupLogPolicies(DaraModel):
    def __init__(
        self,
        action_type: str = None,
        dest_region: str = None,
        dest_type: str = None,
        enable_log_backup: int = None,
        policy_id: str = None,
        retention_period: int = None,
        retention_type: str = None,
        src_region: str = None,
        src_type: str = None,
    ):
        # The operation type. Valid values:
        # 
        # - CREATE: Creates a policy.
        # - UPDATE: Updates a policy.
        # 
        # >Notice: This parameter takes effect only for geo-redundancy. To delete geo-redundancy, set EnableLogBackup to 0 and set ActionType to UPDATE.
        # 
        # This parameter is required.
        self.action_type = action_type
        # The region where the geo-redundancy log backup is stored.
        # 
        # > Required for geo-redundancy.
        self.dest_region = dest_region
        # The destination type of the log backup policy. Valid values:
        #  
        # - level1: same-region backup. 
        # - level2Cross: cross-region backup.
        self.dest_type = dest_type
        # Specifies whether to enable log backup. Valid values:
        # 
        # - **1**: enabled.
        # - **0**: disabled.
        # 
        # > 
        # > - Log backup must be enabled for sharded instances.
        # > - You must enable same-region log backup before you can enable cross-region log backup.
        # 
        # This parameter is required.
        self.enable_log_backup = enable_log_backup
        # The ID of the log backup policy. This parameter is required only for cross-region log backup policies.
        self.policy_id = policy_id
        # The retention period of the log backup in days. This parameter takes effect when RetentionType is set to delay. Valid values:
        # 
        # - Same-region backup: 7 to 7300 days. 
        # - Geo-redundancy: 3 to 1825 days. The value must be less than the backup retention period of the geo-redundancy policy.
        self.retention_period = retention_period
        # The retention cycle type of the log backup. Valid values:
        # 
        # - **never**: long-term retention (LTR).
        # - **delay**: retention for a fixed number of days.
        self.retention_type = retention_type
        # The region where the source instance resides.
        self.src_region = src_region
        # The source type of the log backup policy. Valid values:
        #   
        # - db: same-region backup.
        # - level1: cross-region backup.
        self.src_type = src_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.dest_region is not None:
            result['DestRegion'] = self.dest_region

        if self.dest_type is not None:
            result['DestType'] = self.dest_type

        if self.enable_log_backup is not None:
            result['EnableLogBackup'] = self.enable_log_backup

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.retention_period is not None:
            result['RetentionPeriod'] = self.retention_period

        if self.retention_type is not None:
            result['RetentionType'] = self.retention_type

        if self.src_region is not None:
            result['SrcRegion'] = self.src_region

        if self.src_type is not None:
            result['SrcType'] = self.src_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('DestRegion') is not None:
            self.dest_region = m.get('DestRegion')

        if m.get('DestType') is not None:
            self.dest_type = m.get('DestType')

        if m.get('EnableLogBackup') is not None:
            self.enable_log_backup = m.get('EnableLogBackup')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('RetentionPeriod') is not None:
            self.retention_period = m.get('RetentionPeriod')

        if m.get('RetentionType') is not None:
            self.retention_type = m.get('RetentionType')

        if m.get('SrcRegion') is not None:
            self.src_region = m.get('SrcRegion')

        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')

        return self

class ModifyAdvancedBackupPolicyRequestAdvancedBackupDataPolicies(DaraModel):
    def __init__(
        self,
        action_type: str = None,
        backup_policy: str = None,
        dest_region: str = None,
        dest_type: str = None,
        policy_id: str = None,
        preferred_backup_period: str = None,
        preserve_one_each_hour: bool = None,
        retention_period: int = None,
        retention_type: str = None,
        src_region: str = None,
        src_type: str = None,
    ):
        # The action. Valid values:
        # 
        # - **CREATE**: Creates a policy.
        # - **UPDATE**: Updates a policy.
        # - **DELETE**: Deletes a policy. If this value is specified, only the PolicyId parameter is required.
        # 
        # This parameter is required.
        self.action_type = action_type
        # The scheduling type of the advanced policy. Valid values:
        # 
        # - dayOfWeek: scheduled by week.
        # - dayOfMonth: scheduled by month.
        # - dayOfYear: scheduled by year.
        # - backupInterval: scheduled at a fixed interval (high-frequency backup).
        # 
        # > 
        # > - Multiple high-frequency backup policies are not supported.
        # > - Multiple geo-redundancy backups are not supported, and geo-redundancy policies only support dayOfWeek.
        # 
        # >Notice: Required when ActionType is not DELETE.
        self.backup_policy = backup_policy
        # The destination region of the backup policy.
        # 
        # >Notice: Required when ActionType is not DELETE.
        self.dest_region = dest_region
        # The destination type of the backup policy. Valid values:
        #  
        # - level1: same-region backup.
        # - level2Cross: cross-region backup.
        # 
        # >Notice: Required when ActionType is not DELETE.
        self.dest_type = dest_type
        # The ID of the backup policy.
        # 
        # 
        # >Notice: Required when ActionType is not CREATE.
        self.policy_id = policy_id
        # The backup cycle. Valid values:
        # 
        # - When BackupPolicy is set to dayOfWeek: 1, 2, 3, 4, 5, 6, and 7 represent Monday to Sunday. At least two backups must be performed per week.
        # - When BackupPolicy is set to dayOfMonth: 1, 3, and -1 represent the 1st, 3rd, and last day of each month. -1 represents the last day of the month.
        # - When BackupPolicy is set to dayOfYear: 01-07 represents January 7. Only one day can be selected.
        # - When BackupPolicy is set to backupInterval: specify one of the following numbers in minutes. For sharded clusters, the valid values are 30, 60, 120, 180, 240, 360, 480, and 720. For replica sets, the valid values are 15, 30, 60, 120, 180, 240, 360, 480, and 720.
        # 
        # Note:
        # 
        # >Notice: Required when ActionType is not DELETE.
        # Geo-redundancy policies only support dayOfWeek.
        self.preferred_backup_period = preferred_backup_period
        # Specifies whether to enable hourly sparse backup. Valid values:
        # 
        # - true: When the backup frequency is in minutes, all snapshots taken within 1 hour from the current time are retained. For snapshots taken more than 1 hour but within 24 hours from the current time, only the first snapshot after the hour is retained.
        # - false: All snapshots within the retention period of high-frequency backups are retained.
        self.preserve_one_each_hour = preserve_one_each_hour
        # The retention period of the backup plan in days. Valid values:
        # 
        # - Same-region backup: 7 to 7300 days.
        # - Geo-redundancy: 3 to 1825 days.
        # 
        # >Notice: Required when RetentionType is set to delay.
        self.retention_period = retention_period
        # The retention cycle type of the backup set. Valid values:
        # 
        # - **never**: long-term retention (LTR).
        # - **delay**: retention for a fixed number of days.
        # 
        # >Notice: Required when ActionType is not DELETE.
        self.retention_type = retention_type
        # The region where the instance resides.
        # 
        # >Notice: Required when ActionType is not DELETE.
        self.src_region = src_region
        # The source type of the backup policy. Valid values:
        #   
        # - db: same-region backup.
        # - level1: cross-region backup.
        # 
        # >Notice: Required when ActionType is not DELETE.
        self.src_type = src_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.backup_policy is not None:
            result['BackupPolicy'] = self.backup_policy

        if self.dest_region is not None:
            result['DestRegion'] = self.dest_region

        if self.dest_type is not None:
            result['DestType'] = self.dest_type

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period

        if self.preserve_one_each_hour is not None:
            result['PreserveOneEachHour'] = self.preserve_one_each_hour

        if self.retention_period is not None:
            result['RetentionPeriod'] = self.retention_period

        if self.retention_type is not None:
            result['RetentionType'] = self.retention_type

        if self.src_region is not None:
            result['SrcRegion'] = self.src_region

        if self.src_type is not None:
            result['SrcType'] = self.src_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('BackupPolicy') is not None:
            self.backup_policy = m.get('BackupPolicy')

        if m.get('DestRegion') is not None:
            self.dest_region = m.get('DestRegion')

        if m.get('DestType') is not None:
            self.dest_type = m.get('DestType')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')

        if m.get('PreserveOneEachHour') is not None:
            self.preserve_one_each_hour = m.get('PreserveOneEachHour')

        if m.get('RetentionPeriod') is not None:
            self.retention_period = m.get('RetentionPeriod')

        if m.get('RetentionType') is not None:
            self.retention_type = m.get('RetentionType')

        if m.get('SrcRegion') is not None:
            self.src_region = m.get('SrcRegion')

        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')

        return self

