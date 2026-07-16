# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class ModifyBackupPolicyRequest(DaraModel):
    def __init__(
        self,
        advanced_data_policies: List[main_models.ModifyBackupPolicyRequestAdvancedDataPolicies] = None,
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
        # The advanced backup policies.
        # 
        # > - - This parameter is not supported for PolarDB for PostgreSQL (compatible with Oracle) and PolarDB for PostgreSQL.
        # >
        # > - - This parameter is supported only for clusters for which `BackupPolicyLevel` is set to `Advanced`.
        self.advanced_data_policies = advanced_data_policies
        # The backup frequency. Valid values:
        # 
        # - **Normal** (default): standard backup. The cluster is backed up once a day.
        # 
        # - **2/24H**: high-frequency backup. The cluster is backed up every 2 hours.
        # 
        # - **3/24H**: high-frequency backup. The cluster is backed up every 3 hours.
        # 
        # - **4/24H**: high-frequency backup. The cluster is backed up every 4 hours.
        # 
        # > * * If you enable high-frequency backup, all backups completed within the last 24 hours are retained. For backups older than 24 hours, the system retains only the first backup completed after 00:00 each day and deletes the rest.
        # >
        # > * - If you enable high-frequency backup, the **PreferredBackupPeriod** parameter is automatically set to all days of the week (from Monday to Sunday).
        # >
        # > * - This parameter is not supported if your PolarDB for MySQL cluster is in a region that supports the cross-region backup feature. For more information about the regions that support cross-region backup, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        # >
        # > * - After you enable advanced backup, this parameter is no longer effective. Use the `AdvancedDataPolicies` parameter instead.
        self.backup_frequency = backup_frequency
        # The level of the backup policy. Valid values:
        # 
        # - **Normal**: standard backup
        # 
        # - **Advanced**: advanced backup
        # 
        # > * * This parameter is not supported for PolarDB for PostgreSQL (compatible with Oracle) and PolarDB for PostgreSQL.
        # >
        # > * - Check the `AdvancedPolicyOption` parameter in the response of the [DescribeBackupPolicy](https://help.aliyun.com/document_detail/2319231.html) operation to determine whether the cluster supports advanced backup. If the cluster supports advanced backup, you can request this feature in [Advanced backup settings](~611727~~).
        # >
        # > * - After you enable advanced backup, you **cannot** switch back to standard backup.
        self.backup_policy_level = backup_policy_level
        # Specifies whether to retain backups when you delete the cluster. Valid values:
        # 
        # - **ALL**: Permanently retains all backups.
        # 
        # - **LATEST**: Permanently retains the last backup.
        # 
        # - **NONE**: Does not retain backup sets.
        # 
        # > The default value is `NONE`.
        self.backup_retention_policy_on_cluster_deletion = backup_retention_policy_on_cluster_deletion
        # The cluster ID.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query the details of all clusters in a specified region, including the cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The backup frequency. Valid values:
        # 
        # - **Normal** (default): standard backup. The cluster is backed up once a day.
        # 
        # - **2/24H**: high-frequency backup. The cluster is backed up every 2 hours.
        # 
        # - **3/24H**: high-frequency backup. The cluster is backed up every 3 hours.
        # 
        # - **4/24H**: high-frequency backup. The cluster is backed up every 4 hours.
        # 
        # > * * This parameter is not supported for PolarDB for PostgreSQL (compatible with Oracle) and PolarDB for PostgreSQL.
        # >
        # > * - This parameter is not supported if your PolarDB for MySQL cluster is in a region that supports the cross-region backup feature. For more information about the regions that support cross-region backup, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        # >
        # > * - After you enable advanced backup, this parameter is no longer effective. Use the `AdvancedDataPolicies` parameter instead.
        self.data_level_1backup_frequency = data_level_1backup_frequency
        # The level-1 backup cycle. Valid values:
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
        # > * * You must select at least two days. Separate multiple values with commas.
        # >
        # > * - This parameter is not supported for PolarDB for PostgreSQL (compatible with Oracle) and PolarDB for PostgreSQL.
        # >
        # > * - This parameter is not supported if your PolarDB for MySQL cluster is in a region that supports the cross-region backup feature. For more information about the regions that support cross-region backup, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        # >
        # > * - After you enable advanced backup, this parameter is no longer effective. Use the `AdvancedDataPolicies` parameter instead.
        self.data_level_1backup_period = data_level_1backup_period
        # The retention period for level-1 backups, in days. Valid values: 3 to 14.
        # 
        # > - After you enable advanced backup, this parameter is no longer effective. Use the `AdvancedDataPolicies` parameter instead.
        self.data_level_1backup_retention_period = data_level_1backup_retention_period
        # The time window for automatic backups. Specify the time in UTC and in the `hh:mmZ-hh:mmZ` format. The time window must be a one-hour period that starts on the hour. For example, `14:00Z-15:00Z`.
        # 
        # > - This parameter is not supported for PolarDB for PostgreSQL (compatible with Oracle) and PolarDB for PostgreSQL.
        # >
        # > - This parameter is not supported if your PolarDB for MySQL cluster is in a region that supports the cross-region backup feature. For more information about the regions that support cross-region backup, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        self.data_level_1backup_time = data_level_1backup_time
        # The destination region for the cross-region level-2 backup. For more information about the regions that support cross-region backup, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        # 
        # > - After you enable advanced backup, this parameter is no longer effective. Use the `AdvancedDataPolicies` parameter instead.
        self.data_level_2backup_another_region_region = data_level_2backup_another_region_region
        # The retention period of cross-region level-2 backups. Valid values:
        # 
        # - **0**: Disables the cross-region level-2 backup feature.
        # 
        # - **30 to 7300**: The retention period of cross-region level-2 backups, in days.
        # 
        # - **-1**: Cross-region level-2 backups are permanently retained.
        # 
        # > * * When you create a cluster, the default value is **0**, which disables the cross-region level-2 backup feature.
        # >
        # > * - After you enable advanced backup, this parameter is no longer effective. Use the `AdvancedDataPolicies` parameter instead.
        self.data_level_2backup_another_region_retention_period = data_level_2backup_another_region_retention_period
        # The level-2 backup cycle. Valid values:
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
        # > * * You must select at least two days. Separate multiple values with commas.
        # >
        # > * - This parameter is not supported for PolarDB for PostgreSQL (compatible with Oracle) and PolarDB for PostgreSQL.
        # >
        # > * - This parameter is not supported if your PolarDB for MySQL cluster is in a region that supports the cross-region backup feature. For more information about the regions that support cross-region backup, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        # >
        # > * - After you enable advanced backup, this parameter is no longer effective. Use the `AdvancedDataPolicies` parameter instead.
        self.data_level_2backup_period = data_level_2backup_period
        # The retention period of level-2 backups. Valid values:
        # 
        # - **0**: Disables the level-2 backup feature.
        # 
        # - **30 to 7300**: The retention period of level-2 backups, in days.
        # 
        # - **-1**: Level-2 backups are permanently retained.
        # 
        # > * * When you create a cluster, the default value is **0**, which disables the level-2 backup feature.
        # >
        # > * - After you enable advanced backup, this parameter is no longer effective. Use the `AdvancedDataPolicies` parameter instead.
        self.data_level_2backup_retention_period = data_level_2backup_retention_period
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
        # > * * You must select at least two days. Separate multiple values with commas.
        # >
        # > * - This parameter is not supported if your PolarDB for MySQL cluster is in a region that supports the cross-region backup feature. For more information about the regions that support cross-region backup, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        # >
        # > * - After you enable advanced backup, this parameter is no longer effective. Use the `AdvancedDataPolicies` parameter instead.
        self.preferred_backup_period = preferred_backup_period
        # The time window for automatic backups. Specify the time in UTC and in the `hh:mmZ-hh:mmZ` format. The time window must be a one-hour period that starts on the hour. For example, `14:00Z-15:00Z`.
        self.preferred_backup_time = preferred_backup_time
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.advanced_data_policies:
            for v1 in self.advanced_data_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AdvancedDataPolicies'] = []
        if self.advanced_data_policies is not None:
            for k1 in self.advanced_data_policies:
                result['AdvancedDataPolicies'].append(k1.to_map() if k1 else None)

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
        self.advanced_data_policies = []
        if m.get('AdvancedDataPolicies') is not None:
            for k1 in m.get('AdvancedDataPolicies'):
                temp_model = main_models.ModifyBackupPolicyRequestAdvancedDataPolicies()
                self.advanced_data_policies.append(temp_model.from_map(k1))

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

class ModifyBackupPolicyRequestAdvancedDataPolicies(DaraModel):
    def __init__(
        self,
        action_type: str = None,
        auto_created: bool = None,
        bak_type: str = None,
        dest_region: str = None,
        dest_type: str = None,
        dump_action: str = None,
        filter_key: str = None,
        filter_type: str = None,
        filter_value: str = None,
        only_preserve_one_each_day: bool = None,
        only_preserve_one_each_hour: bool = None,
        policy_id: str = None,
        retention_type: str = None,
        retention_value: str = None,
        src_region: str = None,
        src_type: str = None,
        storage_class: str = None,
    ):
        # The action type. Valid values:
        # 
        # - **CREATE**: Create
        # 
        # - **UPDATE**: Update
        # 
        # - **DELETE**: Delete
        self.action_type = action_type
        # Indicates whether the backup policy is automatically generated by the system.
        # 
        # > This value is automatically generated. You do not need to specify this parameter.
        self.auto_created = auto_created
        # The backup type. Valid values:
        # 
        # - **F**: full backup
        # 
        # > This parameter cannot be modified and is fixed to `F`.
        self.bak_type = bak_type
        # The destination region for the backup policy.
        self.dest_region = dest_region
        # The destination type for the backup policy. Valid values:
        # 
        # - **level1**: level-1 backup
        # 
        # - **level2**: level-2 backup
        # 
        # - **level2Cross**: cross-region level-2 backup
        self.dest_type = dest_type
        # The method to convert a level-1 backup to a level-2 backup. Valid values:
        # 
        # - **copy**: Copy
        self.dump_action = dump_action
        # The scheduling type. Valid values:
        # 
        # - **dayOfWeek**: Weekly schedule
        # 
        # - **dayOfMonth**: Monthly schedule
        # 
        # - **dayOfYear**: Yearly schedule
        # 
        # - **backupInterval**: Fixed interval schedule
        # 
        # > This parameter is required only if `FilterType` is set to **crontab**.
        self.filter_key = filter_key
        # The filter type for the advanced policy. Valid values:
        # 
        # - **crontab**: Recurring schedule
        # 
        # - **event**: Event-based schedule
        self.filter_type = filter_type
        # The backup cycle.
        self.filter_value = filter_value
        # The retention policy for backups that are more than 24 hours old. Valid values:
        # 
        # - **true**: Retains only the first backup set of the day.
        # 
        # - **false**: Retains all backups.
        self.only_preserve_one_each_day = only_preserve_one_each_day
        # The retention policy for hourly backups. Valid values:
        # 
        # - **true**: Retains only the first backup set of each hour for backups that are more than one hour old.
        # 
        # - **false**: Retains all backup sets.
        # 
        # > This parameter cannot be modified and is fixed to `true`.
        self.only_preserve_one_each_hour = only_preserve_one_each_hour
        # The ID of the backup policy. You can call the [DescribeBackupPolicy](https://help.aliyun.com/document_detail/2319231.html) operation to view the ID.
        self.policy_id = policy_id
        # The retention type for the backup set. Valid values:
        # 
        # - **never**: Never expires.
        # 
        # - **delay**: Expires after a specified number of days.
        self.retention_type = retention_type
        # The number of days to retain the backup.
        self.retention_value = retention_value
        # The source region for the backup policy.
        self.src_region = src_region
        # The source type for the backup policy. Valid values:
        # 
        # - **db**: database cluster
        # 
        # - **level1**: level-1 backup
        # 
        # - **level2**: level-2 backup
        # 
        # - **level2Cross**: cross-region level-2 backup
        self.src_type = src_type
        self.storage_class = storage_class

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.auto_created is not None:
            result['AutoCreated'] = self.auto_created

        if self.bak_type is not None:
            result['BakType'] = self.bak_type

        if self.dest_region is not None:
            result['DestRegion'] = self.dest_region

        if self.dest_type is not None:
            result['DestType'] = self.dest_type

        if self.dump_action is not None:
            result['DumpAction'] = self.dump_action

        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key

        if self.filter_type is not None:
            result['FilterType'] = self.filter_type

        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value

        if self.only_preserve_one_each_day is not None:
            result['OnlyPreserveOneEachDay'] = self.only_preserve_one_each_day

        if self.only_preserve_one_each_hour is not None:
            result['OnlyPreserveOneEachHour'] = self.only_preserve_one_each_hour

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.retention_type is not None:
            result['RetentionType'] = self.retention_type

        if self.retention_value is not None:
            result['RetentionValue'] = self.retention_value

        if self.src_region is not None:
            result['SrcRegion'] = self.src_region

        if self.src_type is not None:
            result['SrcType'] = self.src_type

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('AutoCreated') is not None:
            self.auto_created = m.get('AutoCreated')

        if m.get('BakType') is not None:
            self.bak_type = m.get('BakType')

        if m.get('DestRegion') is not None:
            self.dest_region = m.get('DestRegion')

        if m.get('DestType') is not None:
            self.dest_type = m.get('DestType')

        if m.get('DumpAction') is not None:
            self.dump_action = m.get('DumpAction')

        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')

        if m.get('FilterType') is not None:
            self.filter_type = m.get('FilterType')

        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')

        if m.get('OnlyPreserveOneEachDay') is not None:
            self.only_preserve_one_each_day = m.get('OnlyPreserveOneEachDay')

        if m.get('OnlyPreserveOneEachHour') is not None:
            self.only_preserve_one_each_hour = m.get('OnlyPreserveOneEachHour')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('RetentionType') is not None:
            self.retention_type = m.get('RetentionType')

        if m.get('RetentionValue') is not None:
            self.retention_value = m.get('RetentionValue')

        if m.get('SrcRegion') is not None:
            self.src_region = m.get('SrcRegion')

        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        return self

