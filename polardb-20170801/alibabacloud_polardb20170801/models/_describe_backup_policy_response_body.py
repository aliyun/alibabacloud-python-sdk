# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupPolicyResponseBody(DaraModel):
    def __init__(
        self,
        advanced_data_policies: main_models.DescribeBackupPolicyResponseBodyAdvancedDataPolicies = None,
        advanced_policy_option: str = None,
        backup_frequency: str = None,
        backup_policy_level: str = None,
        backup_retention_policy_on_cluster_deletion: str = None,
        data_level_1backup_frequency: str = None,
        data_level_1backup_period: str = None,
        data_level_1backup_retention_period: str = None,
        data_level_1backup_time: str = None,
        data_level_2backup_another_region_region: str = None,
        data_level_2backup_another_region_retention_period: str = None,
        data_level_2backup_period: str = None,
        data_level_2backup_retention_period: str = None,
        enable_cross_region_immutable_backup: bool = None,
        enable_immutable_backup: bool = None,
        preferred_backup_period: str = None,
        preferred_backup_time: str = None,
        preferred_next_backup_time: str = None,
        request_id: str = None,
    ):
        self.advanced_data_policies = advanced_data_policies
        # The advanced backup policy option. Valid values:
        # * **enable**: Advanced backup is enabled.
        # * **disable**: Advanced backup is not enabled but can be enabled.
        # * **notSupport**: Advanced backup is not supported.
        # > *  This parameter is not supported for PolarDB for PostgreSQL (Compatible with Oracle) or PolarDB for PostgreSQL.
        self.advanced_policy_option = advanced_policy_option
        # The backup frequency. Valid values:
        # 
        # - **Normal** (default): regular backup. A backup is performed once a day at a scheduled time.
        # - **2/24H**: enhanced backup. A backup is performed every 2 hours.
        # - **3/24H**: enhanced backup. A backup is performed every 3 hours.
        # - **4/24H**: enhanced backup. A backup is performed every 4 hours.
        # 
        # > * After enhanced backup is enabled, all backups completed within 24 hours are retained. For backups older than 24 hours, only the first backup completed after 00:00 each day is retained, and all others are deleted.
        # >* After enhanced backup is enabled, the backup cycle parameter **PreferredBackupPeriod** is set to all days of the week by default (Monday through Sunday).
        self.backup_frequency = backup_frequency
        # The current backup policy level. Valid values:
        # * **Normal**: regular backup
        # * **Advanced**: advanced backup
        # > *  This parameter is not supported for PolarDB for PostgreSQL (Compatible with Oracle) or PolarDB for PostgreSQL.
        self.backup_policy_level = backup_policy_level
        # Specifies whether to retain backups when the cluster is deleted. Valid values:
        # 
        # * **ALL**: All backups are retained with long-term retention (LTR).
        # * **LATEST**: The last backup is retained with long-term retention (LTR).
        # * **NONE** (default): No backups are retained.
        self.backup_retention_policy_on_cluster_deletion = backup_retention_policy_on_cluster_deletion
        # The backup frequency. Valid values:
        # 
        # - **Normal** (default): regular backup. A backup is performed once a day at a scheduled time.
        # - **2/24H**: high-frequency backup. A backup is performed every 2 hours.
        # - **3/24H**: high-frequency backup. A backup is performed every 3 hours.
        # - **4/24H**: high-frequency backup. A backup is performed every 4 hours.
        # 
        # > *  * This parameter is not supported for PolarDB for PostgreSQL (Compatible with Oracle) or PolarDB for PostgreSQL.
        # >*  * If the region of your PolarDB for MySQL cluster does not support the cross-region backup feature, this parameter is not supported. For the regions that support cross-region backup, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        # >*  * After advanced backup is enabled, use the AdvancedDataPolicies parameter instead of this parameter.
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
        # > * * At least two days must be selected. Separate multiple values with commas (,).
        # >*  * This parameter is not supported for PolarDB for PostgreSQL (Compatible with Oracle) or PolarDB for PostgreSQL.
        # >* * If the region of your PolarDB for MySQL cluster does not support the cross-region backup feature, this parameter is not supported. For the regions that support cross-region backup, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        # >* * After advanced backup is enabled, use the AdvancedDataPolicies parameter instead of this parameter.
        self.data_level_1backup_period = data_level_1backup_period
        # The retention period of level-1 backups. Valid values: 3 to 14. Unit: days.
        # > After advanced backup is enabled, use the AdvancedDataPolicies parameter instead of this parameter.
        self.data_level_1backup_retention_period = data_level_1backup_retention_period
        # The time period during which automatic backups are performed. The value is in the `hh:mmZ-hh:mmZ` format (UTC). The start and end times must be on the hour and exactly 1 hour apart. Example: `14:00Z-15:00Z`.
        # 
        # > *  This parameter is not supported for PolarDB for PostgreSQL (Compatible with Oracle) or PolarDB for PostgreSQL.
        # >*  If the region of your PolarDB for MySQL cluster does not support the cross-region backup feature, this parameter is not supported. For the regions that support cross-region backup, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        self.data_level_1backup_time = data_level_1backup_time
        # The cross-region backup region for level-2 backups. For the regions that support cross-region backup, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        # 
        # > After advanced backup is enabled, use the AdvancedDataPolicies parameter instead of this parameter.
        self.data_level_2backup_another_region_region = data_level_2backup_another_region_region
        # The retention epoch of cross-region backups for level-2 backups. Valid values:
        # 
        # - **0**: The level-2 backup feature is shutdown.
        # 
        # - **30 to 7300**: The retention epoch of level-2 backups. Unit: days.
        # 
        # - **-1**: Level-2 backups are retained with long-term retention (LTR).
        # 
        #  >
        # >- - When a cluster is created, the default value is **0**, which means the cross-region backup feature for level-2 backups is shutdown.
        # >- - After advanced backup is enabled, use the AdvancedDataPolicies parameter instead of this parameter.
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
        # > * * At least two days must be selected. Separate multiple values with commas (,).
        # >*  * This parameter is not supported for PolarDB for PostgreSQL (Compatible with Oracle) or PolarDB for PostgreSQL.
        # >* * If the region of your PolarDB for MySQL cluster does not support the cross-region backup feature, this parameter is not supported. For the regions that support cross-region backup, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        # >* * After advanced backup is enabled, use the AdvancedDataPolicies parameter instead of this parameter.
        self.data_level_2backup_period = data_level_2backup_period
        # The retention epoch of level-2 backups. Valid values:
        #  * 0: The level-2 backup feature is shutdown.
        #  * 30 to 7300: The retention epoch of level-2 backups. Unit: days.
        #  * -1: Level-2 backups are retained with long-term retention (LTR).
        # 
        #  >
        # >- * When a cluster is created, the default value is **0**, which means the level-2 backup feature is shutdown.
        # >- * After advanced backup is enabled, use the AdvancedDataPolicies parameter instead of this parameter.
        self.data_level_2backup_retention_period = data_level_2backup_retention_period
        # Indicates whether immutable cross-region backup is enabled.
        self.enable_cross_region_immutable_backup = enable_cross_region_immutable_backup
        # Indicates whether immutable backup is enabled.
        self.enable_immutable_backup = enable_immutable_backup
        # The data backup cycle. Valid values:
        # 
        # - Monday
        # - Tuesday
        # - Wednesday
        # - Thursday
        # - Friday
        # - Saturday
        # - Sunday
        # > After advanced backup is enabled, use the AdvancedDataPolicies parameter instead of this parameter.
        self.preferred_backup_period = preferred_backup_period
        # The time period during which automatic backups are performed. The value is in the `HH:mmZ-HH:mmZ` format (UTC).
        self.preferred_backup_time = preferred_backup_time
        # The time of the next backup. The value is in the `YYYY-MM-DDThh:mmZ` format (UTC).
        self.preferred_next_backup_time = preferred_next_backup_time
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.advanced_data_policies:
            self.advanced_data_policies.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_data_policies is not None:
            result['AdvancedDataPolicies'] = self.advanced_data_policies.to_map()

        if self.advanced_policy_option is not None:
            result['AdvancedPolicyOption'] = self.advanced_policy_option

        if self.backup_frequency is not None:
            result['BackupFrequency'] = self.backup_frequency

        if self.backup_policy_level is not None:
            result['BackupPolicyLevel'] = self.backup_policy_level

        if self.backup_retention_policy_on_cluster_deletion is not None:
            result['BackupRetentionPolicyOnClusterDeletion'] = self.backup_retention_policy_on_cluster_deletion

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

        if self.enable_cross_region_immutable_backup is not None:
            result['EnableCrossRegionImmutableBackup'] = self.enable_cross_region_immutable_backup

        if self.enable_immutable_backup is not None:
            result['EnableImmutableBackup'] = self.enable_immutable_backup

        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period

        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time

        if self.preferred_next_backup_time is not None:
            result['PreferredNextBackupTime'] = self.preferred_next_backup_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedDataPolicies') is not None:
            temp_model = main_models.DescribeBackupPolicyResponseBodyAdvancedDataPolicies()
            self.advanced_data_policies = temp_model.from_map(m.get('AdvancedDataPolicies'))

        if m.get('AdvancedPolicyOption') is not None:
            self.advanced_policy_option = m.get('AdvancedPolicyOption')

        if m.get('BackupFrequency') is not None:
            self.backup_frequency = m.get('BackupFrequency')

        if m.get('BackupPolicyLevel') is not None:
            self.backup_policy_level = m.get('BackupPolicyLevel')

        if m.get('BackupRetentionPolicyOnClusterDeletion') is not None:
            self.backup_retention_policy_on_cluster_deletion = m.get('BackupRetentionPolicyOnClusterDeletion')

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

        if m.get('EnableCrossRegionImmutableBackup') is not None:
            self.enable_cross_region_immutable_backup = m.get('EnableCrossRegionImmutableBackup')

        if m.get('EnableImmutableBackup') is not None:
            self.enable_immutable_backup = m.get('EnableImmutableBackup')

        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')

        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')

        if m.get('PreferredNextBackupTime') is not None:
            self.preferred_next_backup_time = m.get('PreferredNextBackupTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeBackupPolicyResponseBodyAdvancedDataPolicies(DaraModel):
    def __init__(
        self,
        advanced_data_policy: List[main_models.DescribeBackupPolicyResponseBodyAdvancedDataPoliciesAdvancedDataPolicy] = None,
    ):
        self.advanced_data_policy = advanced_data_policy

    def validate(self):
        if self.advanced_data_policy:
            for v1 in self.advanced_data_policy:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AdvancedDataPolicy'] = []
        if self.advanced_data_policy is not None:
            for k1 in self.advanced_data_policy:
                result['AdvancedDataPolicy'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.advanced_data_policy = []
        if m.get('AdvancedDataPolicy') is not None:
            for k1 in m.get('AdvancedDataPolicy'):
                temp_model = main_models.DescribeBackupPolicyResponseBodyAdvancedDataPoliciesAdvancedDataPolicy()
                self.advanced_data_policy.append(temp_model.from_map(k1))

        return self

class DescribeBackupPolicyResponseBodyAdvancedDataPoliciesAdvancedDataPolicy(DaraModel):
    def __init__(
        self,
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
        self.auto_created = auto_created
        self.bak_type = bak_type
        self.dest_region = dest_region
        self.dest_type = dest_type
        self.dump_action = dump_action
        self.filter_key = filter_key
        self.filter_type = filter_type
        self.filter_value = filter_value
        self.only_preserve_one_each_day = only_preserve_one_each_day
        self.only_preserve_one_each_hour = only_preserve_one_each_hour
        self.policy_id = policy_id
        self.retention_type = retention_type
        self.retention_value = retention_value
        self.src_region = src_region
        self.src_type = src_type
        self.storage_class = storage_class

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

