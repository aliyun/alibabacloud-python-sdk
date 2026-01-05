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
        self.advanced_data_policies_shrink = advanced_data_policies_shrink
        # The backup frequency. Default value: Normal. Valid values:
        # 
        # *   **Normal**: standard backup. The system backs up data once a day.
        # *   **2/24H**: enhanced backup. The system backs up data every 2 hours.
        # *   **3/24H**: enhanced backup. The system backs up data every 3 hours.
        # *   **4/24H**: enhanced backup. The system backs up data every 4 hours.
        # 
        # >- If you enable enhanced backup, all backups are retained for 24 hours. For backup files that are created earlier than the previous 24 hours, the system permanently retains only the first backup that is created after 00:00 every day and deletes the rest.
        # >- If you enable enhanced backup, **PreferredBackupPeriod** is automatically set to all days in a week (from Monday to Sunday).
        # >- This parameter is invalid if the region where your PolarDB for MySQL cluster is deployed supports the cross-region backup feature. For information about the regions that support the cross-region backup feature, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        self.backup_frequency = backup_frequency
        self.backup_policy_level = backup_policy_level
        # Specifies whether to retain backups when a cluster is deleted. Valid values:
        # 
        # *   **ALL**: permanently retains all backups.
        # *   **LATEST**: permanently retains the most recent backup.
        # *   **NONE**: does not retain backups.
        # 
        # >  The default value of the parameter is NONE.
        self.backup_retention_policy_on_cluster_deletion = backup_retention_policy_on_cluster_deletion
        # The ID of the cluster.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query information about all clusters that are deployed in a specified region, such as the cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The frequency of level-1 backups. Default value: Normal. Valid values:
        # 
        # *   **Normal**: standard backup. The system backs up data once a day.
        # *   **2/24H**: enhanced backup. The system backs up data every 2 hours.
        # *   **3/24H**: enhanced backup. The system backs up data every 3 hours.
        # *   **4/24H**: enhanced backup. The system backs up data every 4 hours.
        # 
        # >- This parameter is invalid for PolarDB for Oracle clusters or PolarDB for PostgreSQL clusters.
        # >- This parameter is invalid if the region where your PolarDB for MySQL cluster is deployed does not support the cross-region backup feature. For information about the regions that support the cross-region backup feature, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        self.data_level_1backup_frequency = data_level_1backup_frequency
        # The backup cycle of level-1 backups. Valid values:
        # 
        # *   **Monday**
        # *   **Tuesday**
        # *   **Wednesday**
        # *   **Thursday**
        # *   **Friday**
        # *   **Saturday**
        # *   **Sunday**
        # 
        # >- You need to specify at least two values. Separate multiple values with commas (,).
        # >- This parameter is invalid for PolarDB for Oracle clusters or PolarDB for PostgreSQL clusters.
        # >- This parameter is invalid if the region where your PolarDB for MySQL cluster is deployed does not support the cross-region backup feature. For information about the regions that support the cross-region backup feature, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        self.data_level_1backup_period = data_level_1backup_period
        # The retention period of level-1 backups. Valid values: 3 to 14. Unit: days.
        self.data_level_1backup_retention_period = data_level_1backup_retention_period
        # The time period during which automatic backup for level-1 backup is performed. The time period is in the `hh:mmZ-hh:mmZ` format and is displayed in UTC. The start time and end time are on the hour and have an interval of 1 hour. Example: `14:00Z-15:00Z`.
        # >- This parameter is invalid for PolarDB for Oracle clusters or PolarDB for PostgreSQL clusters.
        # >- This parameter is invalid if the region where your PolarDB for MySQL cluster is deployed does not support the cross-region backup feature. For information about the regions that support the cross-region backup feature, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        self.data_level_1backup_time = data_level_1backup_time
        # The region where the cross-region level-2 backup is stored. For information about regions that support the cross-region backup feature, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        self.data_level_2backup_another_region_region = data_level_2backup_another_region_region
        # The retention period of cross-region level-2 backups. Valid values:
        # 
        # *   **0**: The cross-region level-2 backup feature is disabled.
        # *   **30 to 7300**: Cross-region level-2 backups are retained for 30 to 7,300 days.
        # *   **1**: Cross-region level-2 backups are permanently retained.
        # 
        # >  The default value of the parameter is **0**.
        self.data_level_2backup_another_region_retention_period = data_level_2backup_another_region_retention_period
        # The backup cycle of level-2 backups. Valid values:
        # 
        # *   **Monday**
        # *   **Tuesday**
        # *   **Wednesday**
        # *   **Thursday**
        # *   **Friday**
        # *   **Saturday**
        # *   **Sunday**
        # 
        # >- You need to specify at least two values. Separate multiple values with commas (,).
        # >- This parameter is invalid for PolarDB for Oracle clusters or PolarDB for PostgreSQL clusters.
        # >- This parameter is invalid if the region where your PolarDB for MySQL cluster is deployed does not support the cross-region backup feature. For information about the regions that support the cross-region backup feature, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        self.data_level_2backup_period = data_level_2backup_period
        # The retention period of level-2 backups. Valid values:
        # 
        # *   **0**: The level-2 backup feature is disabled.
        # *   **30 to 7300**: Level-2 backups are retained for 30 to 7,300 days.
        # *   **1**: Level-2 backups are permanently retained.
        # 
        # >  The default value of this parameter is **0**.
        self.data_level_2backup_retention_period = data_level_2backup_retention_period
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The backup cycle. Valid values:
        # 
        # *   **Monday**
        # *   **Tuesday**
        # *   **Wednesday**
        # *   **Thursday**
        # *   **Friday**
        # *   **Saturday**
        # *   **Sunday**
        # 
        # >- You need to specify at least two values. Separate multiple values with commas (,).
        # >- This parameter is invalid if the region where your PolarDB for MySQL cluster is deployed supports the cross-region backup feature. For information about the regions that support the cross-region backup feature, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        self.preferred_backup_period = preferred_backup_period
        # The time period during which automatic backup for level-1 backup is performed. The format is `hh:mmZ-hh:mmZ` format. The time is displayed in UTC. The start time and end time are on the hour and with an interval of one hour. Example: `14:00Z-15:00Z`.
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

