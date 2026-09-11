# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBackupPolicyShrinkRequest(DaraModel):
    def __init__(
        self,
        advanced_data_policies_shrink: str = None,
        backup_frequency: str = None,
        backup_policy_level: str = None,
        backup_retention_policy_on_cluster_deletion: str = None,
        dbcluster_id: str = None,
        data_level_1backup_frequency: str = None,
        data_level_1backup_period: str = None,
        data_level_1backup_retention_period: str = None,
        data_level_1backup_time: str = None,
        data_level_2backup_another_region_region: str = None,
        data_level_2backup_another_region_retention_period: str = None,
        data_level_2backup_period: str = None,
        data_level_2backup_retention_period: str = None,
        owner_account: str = None,
        owner_id: int = None,
        preferred_backup_period: str = None,
        preferred_backup_time: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The advanced backup policy.
        # > * * PolarDB for PostgreSQL (Compatible with Oracle) and PolarDB for PostgreSQL do not support this parameter.
        # > * * Only clusters with BackupPolicyLevel set to Advanced support this parameter.
        self.advanced_data_policies_shrink = advanced_data_policies_shrink
        # The backup frequency. Valid values:
        # 
        # - **Normal** (default): regular backup. Automatic backup is performed once a day at a scheduled time.
        # - **2/24H**: high-frequency backup. Backup is performed every 2 hours.
        # - **3/24H**: high-frequency backup. Backup is performed every 3 hours.
        # - **4/24H**: high-frequency backup. Backup is performed every 4 hours.
        # 
        # > * * After high-frequency backup is enabled, all backups completed within 24 hours are retained. For backups older than 24 hours, only the first backup completed after 00:00 each day is retained, and all others are deleted.
        # > * * After high-frequency backup is enabled, the backup cycle parameter PreferredBackupPeriod defaults to all days of the week (Monday through Sunday).
        # > * * If the region of your PolarDB for MySQL cluster supports the cross-region backup feature, this parameter is not supported. For regions that support cross-region backup, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        # > * * After advanced backup is enabled, this parameter no longer takes effect. Use the AdvancedDataPolicies parameter instead.
        self.backup_frequency = backup_frequency
        # The backup policy level. Valid values:
        # * **Normal**: regular backup.
        # * **Advanced**: advanced backup.
        # > * * PolarDB for PostgreSQL (Compatible with Oracle) and PolarDB for PostgreSQL do not support this parameter.
        # > * * You can check the AdvancedPolicyOption response parameter of the [DescribeBackupPolicy](https://help.aliyun.com/document_detail/2319231.html) operation to determine whether the cluster supports advanced backup. If the cluster supports advanced backup, you can apply to use this feature through [Advanced backup settings](~611727~~).
        # > * * After advanced backup is enabled, rollback to regular backup is **not supported**.
        self.backup_policy_level = backup_policy_level
        # Specifies whether to retain backups when the cluster is deleted. Valid values:
        # 
        # - **ALL**: Long-term retention (LTR) of all backups.
        # 
        # - **LATEST**: Long-term retention (LTR) of only the last backup.
        # 
        # - **NONE**: Does not retain any backups.
        # 
        # > Default value: NONE.
        self.backup_retention_policy_on_cluster_deletion = backup_retention_policy_on_cluster_deletion
        # The cluster ID.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query information about all clusters in a specific region, including cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The backup frequency. Valid values:
        # 
        # - **Normal** (default): regular backup. Automatic backup is performed once a day at a scheduled time.
        # - **2/24H**: high-frequency backup. Backup is performed every 2 hours.
        # - **3/24H**: high-frequency backup. Backup is performed every 3 hours.
        # - **4/24H**: high-frequency backup. Backup is performed every 4 hours.
        # 
        # > * * PolarDB for PostgreSQL (Compatible with Oracle) and PolarDB for PostgreSQL do not support this parameter.
        # > * * If the region of your PolarDB for MySQL cluster does not support the cross-region backup feature, this parameter is not supported. For regions that support cross-region backup, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        # > * * After advanced backup is enabled, this parameter no longer takes effect. Use the AdvancedDataPolicies parameter instead.
        self.data_level_1backup_frequency = data_level_1backup_frequency
        # The level-1 backup cycle. Valid values: 
        # * **Monday**
        # * **Tuesday**
        # * **Wednesday**
        # * **Thursday**
        # * **Friday**
        # * **Saturday**
        # * **Sunday**
        # 
        # > * * Select at least 2 days. Separate multiple values with commas (,).
        # > * * PolarDB for PostgreSQL (Compatible with Oracle) and PolarDB for PostgreSQL do not support this parameter.
        # > * * If the region of your PolarDB for MySQL cluster does not support the cross-region backup feature, this parameter is not supported. For regions that support cross-region backup, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        # > * * After advanced backup is enabled, this parameter no longer takes effect. Use the AdvancedDataPolicies parameter instead.
        self.data_level_1backup_period = data_level_1backup_period
        # The retention period of level-1 backups. Valid values: 3 to 14. Unit: days.
        # 
        # > * After advanced backup is enabled, this parameter no longer takes effect. Use the AdvancedDataPolicies parameter instead.
        self.data_level_1backup_retention_period = data_level_1backup_retention_period
        # The time period during which automatic backup is performed. Specify the time period in the `hh:mmZ-hh:mmZ` format in UTC. The values must be on the hour with an interval of 1 hour, such as `14:00Z-15:00Z`.
        # 
        # > * PolarDB for PostgreSQL (Compatible with Oracle) and PolarDB for PostgreSQL do not support this parameter.
        # > * If the region of your PolarDB for MySQL cluster does not support the cross-region backup feature, this parameter is not supported. For regions that support cross-region backup, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        self.data_level_1backup_time = data_level_1backup_time
        # The destination region for cross-region level-2 backups. For regions that support cross-region backup, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        # > * After advanced backup is enabled, this parameter no longer takes effect. Use the AdvancedDataPolicies parameter instead.
        self.data_level_2backup_another_region_region = data_level_2backup_another_region_region
        # The retention period of cross-region backups for level-2 backups. Valid values:
        # 
        # - **0**: Disables the level-2 cross-region backup feature.
        # 
        # - **30 to 7300**: The retention period of level-2 backups. Unit: days.
        # 
        # - **-1**: Long-term retention (LTR) of level-2 backups.
        # 
        #  > * * When a cluster is created, the default value is **0**, which means the level-2 cross-region backup feature is disabled.
        # > * * After advanced backup is enabled, this parameter no longer takes effect. Use the AdvancedDataPolicies parameter instead.
        self.data_level_2backup_another_region_retention_period = data_level_2backup_another_region_retention_period
        # The level-2 backup cycle. Valid values: 
        # * **Monday**
        # * **Tuesday**
        # * **Wednesday**
        # * **Thursday**
        # * **Friday**
        # * **Saturday**
        # * **Sunday**
        # 
        # > * * Select at least 2 days. Separate multiple values with commas (,).
        # > * * PolarDB for PostgreSQL (Compatible with Oracle) and PolarDB for PostgreSQL do not support this parameter.
        # > * * If the region of your PolarDB for MySQL cluster does not support the cross-region backup feature, this parameter is not supported. For regions that support cross-region backup, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        # > * * After advanced backup is enabled, this parameter no longer takes effect. Use the AdvancedDataPolicies parameter instead.
        self.data_level_2backup_period = data_level_2backup_period
        # The retention period of level-2 backups. Valid values:
        # 
        # - **0**: Disables the level-2 backup feature.
        # 
        # - **30 to 7300**: The retention period of level-2 backups. Unit: days.
        # 
        # - **-1**: Long-term retention (LTR) of level-2 backups.
        # 
        #  > * * When a cluster is created, the default value is **0**, which means the level-2 backup feature is disabled.
        # > * * After advanced backup is enabled, this parameter no longer takes effect. Use the AdvancedDataPolicies parameter instead.
        self.data_level_2backup_retention_period = data_level_2backup_retention_period
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The backup cycle. Valid values: 
        # * **Monday**
        # * **Tuesday**
        # * **Wednesday**
        # * **Thursday**
        # * **Friday**
        # * **Saturday**
        # * **Sunday**
        # 
        # > * * Select at least 2 days. Separate multiple values with commas (,).
        # > * * If the region of your PolarDB for MySQL cluster supports the cross-region backup feature, this parameter is not supported. For regions that support cross-region backup, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        # > * * After advanced backup is enabled, this parameter no longer takes effect. Use the AdvancedDataPolicies parameter instead.
        self.preferred_backup_period = preferred_backup_period
        # The time period during which automatic backup is performed. Specify the time period in the `hh:mmZ-hh:mmZ` format in UTC. The values must be on the hour with an interval of 1 hour, such as `14:00Z-15:00Z`.
        self.preferred_backup_time = preferred_backup_time
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_data_policies_shrink is not None:
            result['AdvancedDataPolicies'] = self.advanced_data_policies_shrink

        if self.backup_frequency is not None:
            result['BackupFrequency'] = self.backup_frequency

        if self.backup_policy_level is not None:
            result['BackupPolicyLevel'] = self.backup_policy_level

        if self.backup_retention_policy_on_cluster_deletion is not None:
            result['BackupRetentionPolicyOnClusterDeletion'] = self.backup_retention_policy_on_cluster_deletion

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.data_level_1backup_frequency is not None:
            result['DataLevel1BackupFrequency'] = self.data_level_1backup_frequency

        if self.data_level_1backup_period is not None:
            result['DataLevel1BackupPeriod'] = self.data_level_1backup_period

        if self.data_level_1backup_retention_period is not None:
            result['DataLevel1BackupRetentionPeriod'] = self.data_level_1backup_retention_period

        if self.data_level_1backup_time is not None:
            result['DataLevel1BackupTime'] = self.data_level_1backup_time

        if self.data_level_2backup_another_region_region is not None:
            result['DataLevel2BackupAnotherRegionRegion'] = self.data_level_2backup_another_region_region

        if self.data_level_2backup_another_region_retention_period is not None:
            result['DataLevel2BackupAnotherRegionRetentionPeriod'] = self.data_level_2backup_another_region_retention_period

        if self.data_level_2backup_period is not None:
            result['DataLevel2BackupPeriod'] = self.data_level_2backup_period

        if self.data_level_2backup_retention_period is not None:
            result['DataLevel2BackupRetentionPeriod'] = self.data_level_2backup_retention_period

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period

        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedDataPolicies') is not None:
            self.advanced_data_policies_shrink = m.get('AdvancedDataPolicies')

        if m.get('BackupFrequency') is not None:
            self.backup_frequency = m.get('BackupFrequency')

        if m.get('BackupPolicyLevel') is not None:
            self.backup_policy_level = m.get('BackupPolicyLevel')

        if m.get('BackupRetentionPolicyOnClusterDeletion') is not None:
            self.backup_retention_policy_on_cluster_deletion = m.get('BackupRetentionPolicyOnClusterDeletion')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DataLevel1BackupFrequency') is not None:
            self.data_level_1backup_frequency = m.get('DataLevel1BackupFrequency')

        if m.get('DataLevel1BackupPeriod') is not None:
            self.data_level_1backup_period = m.get('DataLevel1BackupPeriod')

        if m.get('DataLevel1BackupRetentionPeriod') is not None:
            self.data_level_1backup_retention_period = m.get('DataLevel1BackupRetentionPeriod')

        if m.get('DataLevel1BackupTime') is not None:
            self.data_level_1backup_time = m.get('DataLevel1BackupTime')

        if m.get('DataLevel2BackupAnotherRegionRegion') is not None:
            self.data_level_2backup_another_region_region = m.get('DataLevel2BackupAnotherRegionRegion')

        if m.get('DataLevel2BackupAnotherRegionRetentionPeriod') is not None:
            self.data_level_2backup_another_region_retention_period = m.get('DataLevel2BackupAnotherRegionRetentionPeriod')

        if m.get('DataLevel2BackupPeriod') is not None:
            self.data_level_2backup_period = m.get('DataLevel2BackupPeriod')

        if m.get('DataLevel2BackupRetentionPeriod') is not None:
            self.data_level_2backup_retention_period = m.get('DataLevel2BackupRetentionPeriod')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')

        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

