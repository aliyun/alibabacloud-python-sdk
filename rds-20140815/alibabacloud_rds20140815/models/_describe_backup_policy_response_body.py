# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupPolicyResponseBody(DaraModel):
    def __init__(
        self,
        advanced_backup_policy_enabled: bool = None,
        advanced_data_policies: main_models.DescribeBackupPolicyResponseBodyAdvancedDataPolicies = None,
        advanced_log_policies: main_models.DescribeBackupPolicyResponseBodyAdvancedLogPolicies = None,
        archive_backup_keep_count: str = None,
        archive_backup_keep_policy: str = None,
        archive_backup_retention_period: str = None,
        backup_interval: str = None,
        backup_log: str = None,
        backup_method: str = None,
        backup_priority: int = None,
        backup_retention_period: int = None,
        category: str = None,
        compress_type: str = None,
        enable_backup_log: str = None,
        enable_increment_data_backup: bool = None,
        enable_pitr_protection: bool = None,
        high_space_usage_protection: str = None,
        inc_backup_interval: int = None,
        local_log_retention_hours: int = None,
        local_log_retention_space: str = None,
        log_backup_frequency: str = None,
        log_backup_local_retention_number: int = None,
        log_backup_retention_period: int = None,
        pitr_retention_period: int = None,
        preferred_backup_period: str = None,
        preferred_backup_time: str = None,
        preferred_next_backup_time: str = None,
        released_keep_policy: str = None,
        request_id: str = None,
        support_modify_backup_priority: bool = None,
        support_released_keep: int = None,
        support_volume_shadow_copy: int = None,
        supports_high_frequency_backup: int = None,
    ):
        self.advanced_backup_policy_enabled = advanced_backup_policy_enabled
        self.advanced_data_policies = advanced_data_policies
        self.advanced_log_policies = advanced_log_policies
        # The number of archived backups retained for the **MySQL** instance.
        self.archive_backup_keep_count = archive_backup_keep_count
        # The retention cycle of archived backups for the **MySQL** instance.
        self.archive_backup_keep_policy = archive_backup_keep_policy
        # The number of days for which archived backups are retained for the **MySQL** instance.
        self.archive_backup_retention_period = archive_backup_retention_period
        # The backup interval. Unit: minutes.
        # * For MySQL instances: the [snapshot backup frequency](https://help.aliyun.com/document_detail/98818.html) (not the snapshot backup cycle).
        # * For SQL Server instances: the log backup frequency.
        self.backup_interval = backup_interval
        # Indicates whether log backup is enabled. Valid values:
        # * **Enable**: enabled
        # * **Disabled**: disabled
        # 
        # **For SQL Server instances:**
        # 
        # - **Enable** is returned only when instance log backup frequency is **every 5 minutes**.
        # - When instance log backup frequency is **every 30 minutes** or **consistent with the data backup cycle**, this parameter returns **Disabled**. **Use the value of BackupInterval as the reference**.
        self.backup_log = backup_log
        # The backup method of the **SQL Server instance with cloud disks**. Valid values:
        # * **Physical**: physical backup
        # * **Snapshot**: snapshot backup
        self.backup_method = backup_method
        # The backup settings for the secondary instance of an **SQL Server Enterprise Cluster Edition** instance. Valid values:
        # - **1**: The secondary instance is preferred.
        # - **2**: The primary instance is forced.
        # 
        # > This parameter is returned only when SupportModifyBackupPriority is True.
        self.backup_priority = backup_priority
        # The number of days for which data backups are retained.
        self.backup_retention_period = backup_retention_period
        # Indicates whether backup within seconds is enabled for the **MySQL** or **PostgreSQL** instance. Valid values:
        # 
        # - **Flash**: enabled
        # - **Standard**: disabled
        # 
        # > This parameter takes effect only when the **BackupPolicyMode** parameter is set to **DataBackupPolicy**.
        self.category = category
        # The backup compression method. Valid values:
        # * **0**: no compression
        # * **1**: zlib compression
        # * **2**: parallel zlib compression
        # * **4**: QuickLZ compression with fast restoration for individual databases and tables enabled
        # * **8**: QuickLZ compression without fast restoration for individual databases and tables supported
        self.compress_type = compress_type
        # Indicates whether log backup is enabled. Valid values:
        # * **1**: enabled
        # * **0**: disabled
        # 
        # **For SQL Server instances:**
        # - **1** is returned only when instance log backup frequency is **every 5 minutes**.
        # - When instance log backup frequency is **every 30 minutes** or **consistent with the data backup cycle**, this parameter returns **0**. **Use the value of BackupInterval as the reference**.
        self.enable_backup_log = enable_backup_log
        # Indicates whether incremental backup is enabled for the **SQL Server** instance. Valid values:
        # * **True**: enabled
        # * **False**: disabled
        self.enable_increment_data_backup = enable_increment_data_backup
        # Indicates whether point-in-time recovery (PITR) is enabled for the **MySQL** instance. PITR is an upgraded version of log backup. Valid values:
        # - **True**: enabled
        # - **False**: disabled
        # 
        # > For more information, see [Configure a point-in-time recovery policy](https://help.aliyun.com/document_detail/2666046.html).
        self.enable_pitr_protection = enable_pitr_protection
        # Indicates whether binary logs are forcibly deleted when the storage usage of the **MySQL** instance exceeds 80% or the remaining storage is less than 5 GB. Valid values:
        # 
        # * **Disable**: Binary logs are not deleted.
        # * **Enable**: Binary logs are deleted.
        self.high_space_usage_protection = high_space_usage_protection
        self.inc_backup_interval = inc_backup_interval
        # The number of hours for which binary logs are retained on the **MySQL** instance.
        self.local_log_retention_hours = local_log_retention_hours
        # The maximum storage usage of binary logs on the **MySQL** instance, in percentage.
        self.local_log_retention_space = local_log_retention_space
        # The log backup frequency of the **SQL Server** instance. Valid values:
        # 
        # * **LogInterval**: every 30 minutes.
        # * Default: consistent with the data backup cycle specified by **PreferredBackupPeriod**.
        self.log_backup_frequency = log_backup_frequency
        # The number of binary logs retained on the **MySQL** instance.
        self.log_backup_local_retention_number = log_backup_local_retention_number
        # The number of days for which log backups are retained.
        self.log_backup_retention_period = log_backup_retention_period
        # The number of days for which point-in-time recovery is supported for the **MySQL** instance.
        self.pitr_retention_period = pitr_retention_period
        # The data backup cycle. Multiple values are separated by commas (,). Valid values:
        # * **Monday**
        # * **Tuesday**
        # * **Wednesday**
        # * **Thursday**
        # * **Friday**
        # * **Saturday**
        # * **Sunday**
        self.preferred_backup_period = preferred_backup_period
        # The data backup time. Format: <i>HH:mm</i>Z-<i>HH:mm</i>Z (UTC).
        self.preferred_backup_time = preferred_backup_time
        # The next backup time. Format: <i>yyyy-MM-dd</i>T<i>HH:mm</i>Z (UTC).
        self.preferred_next_backup_time = preferred_next_backup_time
        # The archived backup data retention policy for deleted **MySQL** instances. Valid values:
        # * **None**: No archived backups are retained.
        # * **Lastest**: Only the last archived backup is retained.
        # * **All**: All archived backups are retained.
        self.released_keep_policy = released_keep_policy
        # The request ID.
        self.request_id = request_id
        # Indicates whether the secondary instance backup option can be modified for the **SQL Server** instance. Valid values:
        # 
        # - **True**: The option can be modified.
        # - **False**: The option cannot be modified.
        self.support_modify_backup_priority = support_modify_backup_priority
        # A reserved parameter.
        self.support_released_keep = support_released_keep
        # Indicates whether snapshot backup is supported for the **SQL Server** instance. Valid values:
        # 
        # - **1**: supported
        # - **0**: not supported
        self.support_volume_shadow_copy = support_volume_shadow_copy
        # Indicates whether the [5-minute log backup feature](https://help.aliyun.com/document_detail/95717.html) is supported for the **SQL Server** instance. Valid values:
        # - **0**: not supported
        # - **1**: supported
        self.supports_high_frequency_backup = supports_high_frequency_backup

    def validate(self):
        if self.advanced_data_policies:
            self.advanced_data_policies.validate()
        if self.advanced_log_policies:
            self.advanced_log_policies.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_backup_policy_enabled is not None:
            result['AdvancedBackupPolicyEnabled'] = self.advanced_backup_policy_enabled

        if self.advanced_data_policies is not None:
            result['AdvancedDataPolicies'] = self.advanced_data_policies.to_map()

        if self.advanced_log_policies is not None:
            result['AdvancedLogPolicies'] = self.advanced_log_policies.to_map()

        if self.archive_backup_keep_count is not None:
            result['ArchiveBackupKeepCount'] = self.archive_backup_keep_count

        if self.archive_backup_keep_policy is not None:
            result['ArchiveBackupKeepPolicy'] = self.archive_backup_keep_policy

        if self.archive_backup_retention_period is not None:
            result['ArchiveBackupRetentionPeriod'] = self.archive_backup_retention_period

        if self.backup_interval is not None:
            result['BackupInterval'] = self.backup_interval

        if self.backup_log is not None:
            result['BackupLog'] = self.backup_log

        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method

        if self.backup_priority is not None:
            result['BackupPriority'] = self.backup_priority

        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period

        if self.category is not None:
            result['Category'] = self.category

        if self.compress_type is not None:
            result['CompressType'] = self.compress_type

        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log

        if self.enable_increment_data_backup is not None:
            result['EnableIncrementDataBackup'] = self.enable_increment_data_backup

        if self.enable_pitr_protection is not None:
            result['EnablePitrProtection'] = self.enable_pitr_protection

        if self.high_space_usage_protection is not None:
            result['HighSpaceUsageProtection'] = self.high_space_usage_protection

        if self.inc_backup_interval is not None:
            result['IncBackupInterval'] = self.inc_backup_interval

        if self.local_log_retention_hours is not None:
            result['LocalLogRetentionHours'] = self.local_log_retention_hours

        if self.local_log_retention_space is not None:
            result['LocalLogRetentionSpace'] = self.local_log_retention_space

        if self.log_backup_frequency is not None:
            result['LogBackupFrequency'] = self.log_backup_frequency

        if self.log_backup_local_retention_number is not None:
            result['LogBackupLocalRetentionNumber'] = self.log_backup_local_retention_number

        if self.log_backup_retention_period is not None:
            result['LogBackupRetentionPeriod'] = self.log_backup_retention_period

        if self.pitr_retention_period is not None:
            result['PitrRetentionPeriod'] = self.pitr_retention_period

        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period

        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time

        if self.preferred_next_backup_time is not None:
            result['PreferredNextBackupTime'] = self.preferred_next_backup_time

        if self.released_keep_policy is not None:
            result['ReleasedKeepPolicy'] = self.released_keep_policy

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.support_modify_backup_priority is not None:
            result['SupportModifyBackupPriority'] = self.support_modify_backup_priority

        if self.support_released_keep is not None:
            result['SupportReleasedKeep'] = self.support_released_keep

        if self.support_volume_shadow_copy is not None:
            result['SupportVolumeShadowCopy'] = self.support_volume_shadow_copy

        if self.supports_high_frequency_backup is not None:
            result['SupportsHighFrequencyBackup'] = self.supports_high_frequency_backup

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedBackupPolicyEnabled') is not None:
            self.advanced_backup_policy_enabled = m.get('AdvancedBackupPolicyEnabled')

        if m.get('AdvancedDataPolicies') is not None:
            temp_model = main_models.DescribeBackupPolicyResponseBodyAdvancedDataPolicies()
            self.advanced_data_policies = temp_model.from_map(m.get('AdvancedDataPolicies'))

        if m.get('AdvancedLogPolicies') is not None:
            temp_model = main_models.DescribeBackupPolicyResponseBodyAdvancedLogPolicies()
            self.advanced_log_policies = temp_model.from_map(m.get('AdvancedLogPolicies'))

        if m.get('ArchiveBackupKeepCount') is not None:
            self.archive_backup_keep_count = m.get('ArchiveBackupKeepCount')

        if m.get('ArchiveBackupKeepPolicy') is not None:
            self.archive_backup_keep_policy = m.get('ArchiveBackupKeepPolicy')

        if m.get('ArchiveBackupRetentionPeriod') is not None:
            self.archive_backup_retention_period = m.get('ArchiveBackupRetentionPeriod')

        if m.get('BackupInterval') is not None:
            self.backup_interval = m.get('BackupInterval')

        if m.get('BackupLog') is not None:
            self.backup_log = m.get('BackupLog')

        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')

        if m.get('BackupPriority') is not None:
            self.backup_priority = m.get('BackupPriority')

        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CompressType') is not None:
            self.compress_type = m.get('CompressType')

        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')

        if m.get('EnableIncrementDataBackup') is not None:
            self.enable_increment_data_backup = m.get('EnableIncrementDataBackup')

        if m.get('EnablePitrProtection') is not None:
            self.enable_pitr_protection = m.get('EnablePitrProtection')

        if m.get('HighSpaceUsageProtection') is not None:
            self.high_space_usage_protection = m.get('HighSpaceUsageProtection')

        if m.get('IncBackupInterval') is not None:
            self.inc_backup_interval = m.get('IncBackupInterval')

        if m.get('LocalLogRetentionHours') is not None:
            self.local_log_retention_hours = m.get('LocalLogRetentionHours')

        if m.get('LocalLogRetentionSpace') is not None:
            self.local_log_retention_space = m.get('LocalLogRetentionSpace')

        if m.get('LogBackupFrequency') is not None:
            self.log_backup_frequency = m.get('LogBackupFrequency')

        if m.get('LogBackupLocalRetentionNumber') is not None:
            self.log_backup_local_retention_number = m.get('LogBackupLocalRetentionNumber')

        if m.get('LogBackupRetentionPeriod') is not None:
            self.log_backup_retention_period = m.get('LogBackupRetentionPeriod')

        if m.get('PitrRetentionPeriod') is not None:
            self.pitr_retention_period = m.get('PitrRetentionPeriod')

        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')

        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')

        if m.get('PreferredNextBackupTime') is not None:
            self.preferred_next_backup_time = m.get('PreferredNextBackupTime')

        if m.get('ReleasedKeepPolicy') is not None:
            self.released_keep_policy = m.get('ReleasedKeepPolicy')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SupportModifyBackupPriority') is not None:
            self.support_modify_backup_priority = m.get('SupportModifyBackupPriority')

        if m.get('SupportReleasedKeep') is not None:
            self.support_released_keep = m.get('SupportReleasedKeep')

        if m.get('SupportVolumeShadowCopy') is not None:
            self.support_volume_shadow_copy = m.get('SupportVolumeShadowCopy')

        if m.get('SupportsHighFrequencyBackup') is not None:
            self.supports_high_frequency_backup = m.get('SupportsHighFrequencyBackup')

        return self

class DescribeBackupPolicyResponseBodyAdvancedLogPolicies(DaraModel):
    def __init__(
        self,
        advanced_log_policy: List[main_models.DescribeBackupPolicyResponseBodyAdvancedLogPoliciesAdvancedLogPolicy] = None,
    ):
        self.advanced_log_policy = advanced_log_policy

    def validate(self):
        if self.advanced_log_policy:
            for v1 in self.advanced_log_policy:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AdvancedLogPolicy'] = []
        if self.advanced_log_policy is not None:
            for k1 in self.advanced_log_policy:
                result['AdvancedLogPolicy'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.advanced_log_policy = []
        if m.get('AdvancedLogPolicy') is not None:
            for k1 in m.get('AdvancedLogPolicy'):
                temp_model = main_models.DescribeBackupPolicyResponseBodyAdvancedLogPoliciesAdvancedLogPolicy()
                self.advanced_log_policy.append(temp_model.from_map(k1))

        return self

class DescribeBackupPolicyResponseBodyAdvancedLogPoliciesAdvancedLogPolicy(DaraModel):
    def __init__(
        self,
        action_type: str = None,
        dest_region: str = None,
        dest_type: str = None,
        enable_log_backup: int = None,
        filter_key: str = None,
        filter_value: str = None,
        log_retention_type: str = None,
        log_retention_value: int = None,
        src_region: str = None,
        src_type: str = None,
        strategy_id: str = None,
    ):
        self.action_type = action_type
        self.dest_region = dest_region
        self.dest_type = dest_type
        self.enable_log_backup = enable_log_backup
        self.filter_key = filter_key
        self.filter_value = filter_value
        self.log_retention_type = log_retention_type
        self.log_retention_value = log_retention_value
        self.src_region = src_region
        self.src_type = src_type
        self.strategy_id = strategy_id

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

        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key

        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value

        if self.log_retention_type is not None:
            result['LogRetentionType'] = self.log_retention_type

        if self.log_retention_value is not None:
            result['LogRetentionValue'] = self.log_retention_value

        if self.src_region is not None:
            result['SrcRegion'] = self.src_region

        if self.src_type is not None:
            result['SrcType'] = self.src_type

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

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

        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')

        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')

        if m.get('LogRetentionType') is not None:
            self.log_retention_type = m.get('LogRetentionType')

        if m.get('LogRetentionValue') is not None:
            self.log_retention_value = m.get('LogRetentionValue')

        if m.get('SrcRegion') is not None:
            self.src_region = m.get('SrcRegion')

        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

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
        action_type: str = None,
        bak_type: str = None,
        dest_region: str = None,
        dest_type: str = None,
        filter_key: str = None,
        filter_type: str = None,
        filter_value: str = None,
        only_preserve_one_each_day: bool = None,
        only_preserve_one_each_hour: bool = None,
        retention_type: str = None,
        retention_value: int = None,
        src_region: str = None,
        src_type: str = None,
        strategy_id: str = None,
    ):
        self.action_type = action_type
        self.bak_type = bak_type
        self.dest_region = dest_region
        self.dest_type = dest_type
        self.filter_key = filter_key
        self.filter_type = filter_type
        self.filter_value = filter_value
        self.only_preserve_one_each_day = only_preserve_one_each_day
        self.only_preserve_one_each_hour = only_preserve_one_each_hour
        self.retention_type = retention_type
        self.retention_value = retention_value
        self.src_region = src_region
        self.src_type = src_type
        self.strategy_id = strategy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.bak_type is not None:
            result['BakType'] = self.bak_type

        if self.dest_region is not None:
            result['DestRegion'] = self.dest_region

        if self.dest_type is not None:
            result['DestType'] = self.dest_type

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

        if self.retention_type is not None:
            result['RetentionType'] = self.retention_type

        if self.retention_value is not None:
            result['RetentionValue'] = self.retention_value

        if self.src_region is not None:
            result['SrcRegion'] = self.src_region

        if self.src_type is not None:
            result['SrcType'] = self.src_type

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('BakType') is not None:
            self.bak_type = m.get('BakType')

        if m.get('DestRegion') is not None:
            self.dest_region = m.get('DestRegion')

        if m.get('DestType') is not None:
            self.dest_type = m.get('DestType')

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

        if m.get('RetentionType') is not None:
            self.retention_type = m.get('RetentionType')

        if m.get('RetentionValue') is not None:
            self.retention_value = m.get('RetentionValue')

        if m.get('SrcRegion') is not None:
            self.src_region = m.get('SrcRegion')

        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        return self

