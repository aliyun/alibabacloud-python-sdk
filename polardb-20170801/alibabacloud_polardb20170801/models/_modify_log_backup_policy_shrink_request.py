# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLogBackupPolicyShrinkRequest(DaraModel):
    def __init__(
        self,
        advanced_log_policies_shrink: str = None,
        dbcluster_id: str = None,
        log_backup_another_region_region: str = None,
        log_backup_another_region_retention_period: str = None,
        log_backup_retention_period: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The advanced backup policies.
        # 
        # > - - This parameter is not supported for PolarDB for PostgreSQL (Oracle Compatible) or PolarDB for PostgreSQL.
        # >
        # > - - This parameter is supported only for clusters for which the BackupPolicyLevel parameter is set to Advanced.
        self.advanced_log_policies_shrink = advanced_log_policies_shrink
        # The cluster ID.
        # 
        # > Call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to view information about all clusters in a specific region, including cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The destination region for cross-region log backups. For information about the regions that support cross-region backup, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        # 
        # > - - After you enable the advanced backup feature, this parameter is no longer valid. Use the AdvancedLogPolicies parameter instead.
        self.log_backup_another_region_region = log_backup_another_region_region
        # The retention period of cross-region log backups. Valid values:
        # 
        # - **0**: Disables the cross-region log backup feature.
        # 
        # - **30 to 7300**: The retention period in days.
        # 
        # - **-1**: long-term retention.
        # 
        # > * * When you create a cluster, the default value of this parameter is **0**. This value disables the cross-region log backup feature.
        # >
        # > * - After you enable the advanced backup feature, this parameter is no longer valid. Use the AdvancedLogPolicies parameter instead.
        self.log_backup_another_region_retention_period = log_backup_another_region_retention_period
        # The retention period of log backups. Valid values:
        # 
        # - 3 to 7300: The retention period in days.
        # 
        # - -1: long-term retention.
        # 
        # > * * After you enable the advanced backup feature, this parameter is no longer valid. Use the AdvancedLogPolicies parameter instead.
        self.log_backup_retention_period = log_backup_retention_period
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_log_policies_shrink is not None:
            result['AdvancedLogPolicies'] = self.advanced_log_policies_shrink

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.log_backup_another_region_region is not None:
            result['LogBackupAnotherRegionRegion'] = self.log_backup_another_region_region

        if self.log_backup_another_region_retention_period is not None:
            result['LogBackupAnotherRegionRetentionPeriod'] = self.log_backup_another_region_retention_period

        if self.log_backup_retention_period is not None:
            result['LogBackupRetentionPeriod'] = self.log_backup_retention_period

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedLogPolicies') is not None:
            self.advanced_log_policies_shrink = m.get('AdvancedLogPolicies')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('LogBackupAnotherRegionRegion') is not None:
            self.log_backup_another_region_region = m.get('LogBackupAnotherRegionRegion')

        if m.get('LogBackupAnotherRegionRetentionPeriod') is not None:
            self.log_backup_another_region_retention_period = m.get('LogBackupAnotherRegionRetentionPeriod')

        if m.get('LogBackupRetentionPeriod') is not None:
            self.log_backup_retention_period = m.get('LogBackupRetentionPeriod')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

