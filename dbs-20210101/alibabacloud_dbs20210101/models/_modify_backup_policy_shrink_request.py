# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBackupPolicyShrinkRequest(DaraModel):
    def __init__(
        self,
        advance_data_policies_shrink: str = None,
        advance_inc_policies_shrink: str = None,
        advance_log_policies_shrink: str = None,
        backup_method: str = None,
        backup_priority: int = None,
        backup_retention_policy_on_cluster_deletion: str = None,
        category: str = None,
        enable_inc_backup: bool = None,
        instance_name: str = None,
        preferred_backup_window_begin: str = None,
        region_code: str = None,
    ):
        # The details of data backup policies.
        self.advance_data_policies_shrink = advance_data_policies_shrink
        self.advance_inc_policies_shrink = advance_inc_policies_shrink
        self.advance_log_policies_shrink = advance_log_policies_shrink
        self.backup_method = backup_method
        self.backup_priority = backup_priority
        self.backup_retention_policy_on_cluster_deletion = backup_retention_policy_on_cluster_deletion
        self.category = category
        self.enable_inc_backup = enable_inc_backup
        # The ID of the PolarDB instance.
        self.instance_name = instance_name
        # The start time of a basic backup.
        self.preferred_backup_window_begin = preferred_backup_window_begin
        # The region in which backup sets reside.
        self.region_code = region_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advance_data_policies_shrink is not None:
            result['AdvanceDataPolicies'] = self.advance_data_policies_shrink

        if self.advance_inc_policies_shrink is not None:
            result['AdvanceIncPolicies'] = self.advance_inc_policies_shrink

        if self.advance_log_policies_shrink is not None:
            result['AdvanceLogPolicies'] = self.advance_log_policies_shrink

        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method

        if self.backup_priority is not None:
            result['BackupPriority'] = self.backup_priority

        if self.backup_retention_policy_on_cluster_deletion is not None:
            result['BackupRetentionPolicyOnClusterDeletion'] = self.backup_retention_policy_on_cluster_deletion

        if self.category is not None:
            result['Category'] = self.category

        if self.enable_inc_backup is not None:
            result['EnableIncBackup'] = self.enable_inc_backup

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.preferred_backup_window_begin is not None:
            result['PreferredBackupWindowBegin'] = self.preferred_backup_window_begin

        if self.region_code is not None:
            result['RegionCode'] = self.region_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvanceDataPolicies') is not None:
            self.advance_data_policies_shrink = m.get('AdvanceDataPolicies')

        if m.get('AdvanceIncPolicies') is not None:
            self.advance_inc_policies_shrink = m.get('AdvanceIncPolicies')

        if m.get('AdvanceLogPolicies') is not None:
            self.advance_log_policies_shrink = m.get('AdvanceLogPolicies')

        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')

        if m.get('BackupPriority') is not None:
            self.backup_priority = m.get('BackupPriority')

        if m.get('BackupRetentionPolicyOnClusterDeletion') is not None:
            self.backup_retention_policy_on_cluster_deletion = m.get('BackupRetentionPolicyOnClusterDeletion')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('EnableIncBackup') is not None:
            self.enable_inc_backup = m.get('EnableIncBackup')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PreferredBackupWindowBegin') is not None:
            self.preferred_backup_window_begin = m.get('PreferredBackupWindowBegin')

        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')

        return self

