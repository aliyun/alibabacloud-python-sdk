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
        preferred_backup_period: str = None,
        preferred_backup_time: str = None,
        preferred_next_backup_time: str = None,
        request_id: str = None,
    ):
        self.advanced_data_policies = advanced_data_policies
        self.advanced_policy_option = advanced_policy_option
        # The backup frequency. Default value: Normal. Valid values:
        # 
        # *   **Normal**: standard backup. The system backs up data once a day.
        # *   **2/24H**: enhanced backup. The system backs up data every 2 hours.
        # *   **3/24H**: enhanced backup. The system backs up data every 3 hours.
        # *   **4/24H**: enhanced backup. The system backs up data every 4 hours.
        # 
        # > - If enhanced backup is enabled, all backups are retained for 24 hours. Backups are automatically deleted when the retention period ends. However, the system permanently retains the first backup that is created after 00:00 every day.
        # >-  If enhanced backup is enabled, **PreferredBackupPeriod** is automatically set to all days in a week (from Monday to Sunday).
        self.backup_frequency = backup_frequency
        self.backup_policy_level = backup_policy_level
        # Indicates whether backups are retained when you delete a cluster. Valid values:
        # 
        # *   **ALL**: permanently retains all backups.
        # *   **LATEST**: permanently retains the most recent backup.
        # *   **NONE**: does not retain backups.
        self.backup_retention_policy_on_cluster_deletion = backup_retention_policy_on_cluster_deletion
        # The backup frequency of level-1 backups. Default value: Normal. Valid values:
        # 
        # *   **Normal**: standard backup. The system backs up data once a day.
        # *   **2/24H**: frequent backup. The system backs up data every 2 hours.
        # *   **3/24H**: frequent backup. The system backs up data every 3 hours.
        # *   **4/24H**: frequent backup. The system backs up data every 4 hours.
        # 
        # >- This parameter is not supported for PolarDB for PostgreSQL (Compatible with Oracle) clusters or PolarDB for PostgreSQL clusters.
        # >- This parameter is unavailable if the region where your PolarDB for MySQL cluster is deployed does not support the cross-region backup feature. For information about regions that support the cross-region backup feature, see [Overview](https://help.aliyun.com/document_detail/72672.html).
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
        # >- This parameter is not supported for PolarDB for PostgreSQL (Compatible with Oracle) clusters or PolarDB for PostgreSQL clusters.
        # >- This parameter is unavailable if the region where your PolarDB for MySQL cluster is deployed does not support the cross-region backup feature. For information about regions that support the cross-region backup feature, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        self.data_level_1backup_period = data_level_1backup_period
        # The retention period of level-1 backups. Valid values: 3 to 14. Unit: day.
        self.data_level_1backup_retention_period = data_level_1backup_retention_period
        # The period of time during which automatic backup is performed. The value must be in the `hh:mmZ-hh:mmZ` format. The time must be in UTC. The start time and the end time must be on the hour and must have an interval of 1 hour. Example: `14:00Z-15:00Z`.
        # 
        # >- This parameter is not supported for PolarDB for PostgreSQL (Compatible with Oracle) clusters or PolarDB for PostgreSQL clusters.
        # >- This parameter is unavailable if the region where your PolarDB for MySQL cluster is deployed does not support the cross-region backup feature. For information about regions that support the cross-region backup feature, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        self.data_level_1backup_time = data_level_1backup_time
        # The region where the cross-region level-2 backup is stored. For information about regions that support the cross-region backup feature, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        self.data_level_2backup_another_region_region = data_level_2backup_another_region_region
        # The retention period of cross-region level-2 backups. Valid values:
        # 
        # *   **0**: The cross-region level-2 backup feature is disabled.
        # *   **30 to 7300**: Cross-region level-2 backups are retained for 30 to 7,300 days.
        # *   **1**: Cross-region level-2 backups are retained for a long period of time.
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
        # >- This parameter is not supported for PolarDB for PostgreSQL (Compatible with Oracle) clusters or PolarDB for PostgreSQL clusters.
        # >- This parameter is unavailable if the region where your PolarDB for MySQL cluster is deployed does not support the cross-region backup feature. For information about regions that support the cross-region backup feature, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        self.data_level_2backup_period = data_level_2backup_period
        # The retention period of level-2 backups. Valid values:
        # 
        # *   0: The level-2 backup feature is disabled.
        # *   30 to 7300: Level-2 backups are retained for 30 to 7,300 days.
        # *   \\-1: Level-2 backups are retained for a long period of time.
        # 
        # >  The default value of this parameter is **0**.
        self.data_level_2backup_retention_period = data_level_2backup_retention_period
        # The backup cycle. Valid values:
        # 
        # *   Monday
        # *   Tuesday
        # *   Wednesday
        # *   Thursday
        # *   Friday
        # *   Saturday
        # *   Sunday
        self.preferred_backup_period = preferred_backup_period
        # The time period when automatic backups are performed. The format is `HH:mmZ-HH:mmZ`. The time is displayed in UTC.
        self.preferred_backup_time = preferred_backup_time
        # The time when the next automatic backup will be performed. The format is `YYYY-MM-DDThh:mmZ`. The time is displayed in UTC.
        self.preferred_next_backup_time = preferred_next_backup_time
        # The ID of the request.
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

        return self

