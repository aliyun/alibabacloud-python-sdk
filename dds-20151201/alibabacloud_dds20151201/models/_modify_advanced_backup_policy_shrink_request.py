# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAdvancedBackupPolicyShrinkRequest(DaraModel):
    def __init__(
        self,
        advanced_backup_data_policies_shrink: str = None,
        advanced_backup_log_policies_shrink: str = None,
        backup_retention_policy_on_cluster_deletion: int = None,
        dbinstance_id: str = None,
        preferred_backup_time: str = None,
        snapshot_backup_type: str = None,
    ):
        # The list of backup policies.
        self.advanced_backup_data_policies_shrink = advanced_backup_data_policies_shrink
        # The list of log backup policies.
        self.advanced_backup_log_policies_shrink = advanced_backup_log_policies_shrink
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
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_backup_data_policies_shrink is not None:
            result['AdvancedBackupDataPolicies'] = self.advanced_backup_data_policies_shrink

        if self.advanced_backup_log_policies_shrink is not None:
            result['AdvancedBackupLogPolicies'] = self.advanced_backup_log_policies_shrink

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
        if m.get('AdvancedBackupDataPolicies') is not None:
            self.advanced_backup_data_policies_shrink = m.get('AdvancedBackupDataPolicies')

        if m.get('AdvancedBackupLogPolicies') is not None:
            self.advanced_backup_log_policies_shrink = m.get('AdvancedBackupLogPolicies')

        if m.get('BackupRetentionPolicyOnClusterDeletion') is not None:
            self.backup_retention_policy_on_cluster_deletion = m.get('BackupRetentionPolicyOnClusterDeletion')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')

        if m.get('SnapshotBackupType') is not None:
            self.snapshot_backup_type = m.get('SnapshotBackupType')

        return self

