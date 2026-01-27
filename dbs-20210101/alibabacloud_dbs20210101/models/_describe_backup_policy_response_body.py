# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dbs20210101 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupPolicyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeBackupPolicyResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The status code.
        self.code = code
        # The details of the backup policy.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeBackupPolicyResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeBackupPolicyResponseBodyData(DaraModel):
    def __init__(
        self,
        advance_data_policies: List[main_models.DescribeBackupPolicyResponseBodyDataAdvanceDataPolicies] = None,
        advance_inc_policies: List[main_models.DescribeBackupPolicyResponseBodyDataAdvanceIncPolicies] = None,
        advance_log_policies: List[main_models.DescribeBackupPolicyResponseBodyDataAdvanceLogPolicies] = None,
        backup_method: str = None,
        backup_priority: int = None,
        backup_retention_period: int = None,
        backup_retention_policy_on_cluster_deletion: str = None,
        category: str = None,
        enable_backup: int = None,
        enable_inc_backup: int = None,
        enable_log_backup: int = None,
        high_frequency_bak_interval: int = None,
        high_space_usage_protection: str = None,
        inc_backup_interval: int = None,
        local_log_retention_space: int = None,
        log_backup_local_retention_number: str = None,
        log_backup_retention: int = None,
        preferred_backup_date: str = None,
        preferred_backup_window: str = None,
        preferred_backup_window_begin: str = None,
    ):
        # The details of data backup policies.
        self.advance_data_policies = advance_data_policies
        self.advance_inc_policies = advance_inc_policies
        # The details of log backup policies.
        self.advance_log_policies = advance_log_policies
        # The method that is used to generate backup files. Valid values:
        # 
        # *   **Physical**: physical backup
        # *   **Snapshot**: snapshot backup
        self.backup_method = backup_method
        # Indicates whether the secondary database is preferentially backed up. Valid values:
        # 
        # *   **1**: The secondary database is preferentially backed up.
        # *   **2**: Only the primary database is backed up.
        # 
        # >  This parameter is returned only for ApsaraDB RDS for SQL Server instances. If the instance runs a different database engine, **0** is returned.
        self.backup_priority = backup_priority
        # The retention period of basic backup files. If an advanced backup policy is enabled, the value indicates the retention period of the level-1 backup policy.
        self.backup_retention_period = backup_retention_period
        # The policy that is used to retain the archived backup files if the instance is deleted. Valid values:
        # 
        # *   **NONE**: No archived backup file is retained.
        # *   **LATEST**: Only the latest archived backup file is retained.
        # *   **ALL**: All archived backup files are retained.
        self.backup_retention_policy_on_cluster_deletion = backup_retention_policy_on_cluster_deletion
        # Indicates whether the second-granularity backup feature is enabled. Valid values:
        # 
        # *   **Flash**: The second-granularity backup feature is enabled.
        # *   **Standard**: The standard backup feature is enabled.
        # 
        # >  This parameter is returned only for MySQL instances.
        self.category = category
        # Indicates whether the backup feature is enabled.
        self.enable_backup = enable_backup
        # Indicates whether the incremental backup feature is enabled.
        self.enable_inc_backup = enable_inc_backup
        # Indicates whether the log backup feature is enabled. Valid values:
        # 
        # *   **1**: The log backup feature is enabled.
        # *   **0**: The log backup feature is disabled.
        self.enable_log_backup = enable_log_backup
        # The interval for high-frequency backups. Unit: minutes. For example, a value of 120 indicates that a backup is performed every two hours.
        self.high_frequency_bak_interval = high_frequency_bak_interval
        # Indicates whether logs are forcibly cleared if the storage usage of the instance is greater than 80% or the available storage space of the instance is smaller than 5 GB. Valid values:
        # 
        # *   **Disable**: Logs are not forcibly cleared.
        # *   **Enable**: Logs are forcibly cleared.
        self.high_space_usage_protection = high_space_usage_protection
        # The interval for high-frequency incremental backups.
        self.inc_backup_interval = inc_backup_interval
        # The maximum storage usage that is allowed for log files on the instance.
        self.local_log_retention_space = local_log_retention_space
        # The number of local binary log files that are retained.
        self.log_backup_local_retention_number = log_backup_local_retention_number
        # The retention period of log backups.
        self.log_backup_retention = log_backup_retention
        # The backup cycle of a basic backup. The backup cycle is represented by a seven-digit string, which corresponds to the days of the week from Monday to Sunday. A value of 1 indicates that a basic backup is performed on that day, and a value of 0 indicates that no basic backup is performed on that day.
        self.preferred_backup_date = preferred_backup_date
        # The time period during which a basic backup is performed.
        self.preferred_backup_window = preferred_backup_window
        # The start time of a basic backup.
        self.preferred_backup_window_begin = preferred_backup_window_begin

    def validate(self):
        if self.advance_data_policies:
            for v1 in self.advance_data_policies:
                 if v1:
                    v1.validate()
        if self.advance_inc_policies:
            for v1 in self.advance_inc_policies:
                 if v1:
                    v1.validate()
        if self.advance_log_policies:
            for v1 in self.advance_log_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AdvanceDataPolicies'] = []
        if self.advance_data_policies is not None:
            for k1 in self.advance_data_policies:
                result['AdvanceDataPolicies'].append(k1.to_map() if k1 else None)

        result['AdvanceIncPolicies'] = []
        if self.advance_inc_policies is not None:
            for k1 in self.advance_inc_policies:
                result['AdvanceIncPolicies'].append(k1.to_map() if k1 else None)

        result['AdvanceLogPolicies'] = []
        if self.advance_log_policies is not None:
            for k1 in self.advance_log_policies:
                result['AdvanceLogPolicies'].append(k1.to_map() if k1 else None)

        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method

        if self.backup_priority is not None:
            result['BackupPriority'] = self.backup_priority

        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period

        if self.backup_retention_policy_on_cluster_deletion is not None:
            result['BackupRetentionPolicyOnClusterDeletion'] = self.backup_retention_policy_on_cluster_deletion

        if self.category is not None:
            result['Category'] = self.category

        if self.enable_backup is not None:
            result['EnableBackup'] = self.enable_backup

        if self.enable_inc_backup is not None:
            result['EnableIncBackup'] = self.enable_inc_backup

        if self.enable_log_backup is not None:
            result['EnableLogBackup'] = self.enable_log_backup

        if self.high_frequency_bak_interval is not None:
            result['HighFrequencyBakInterval'] = self.high_frequency_bak_interval

        if self.high_space_usage_protection is not None:
            result['HighSpaceUsageProtection'] = self.high_space_usage_protection

        if self.inc_backup_interval is not None:
            result['IncBackupInterval'] = self.inc_backup_interval

        if self.local_log_retention_space is not None:
            result['LocalLogRetentionSpace'] = self.local_log_retention_space

        if self.log_backup_local_retention_number is not None:
            result['LogBackupLocalRetentionNumber'] = self.log_backup_local_retention_number

        if self.log_backup_retention is not None:
            result['LogBackupRetention'] = self.log_backup_retention

        if self.preferred_backup_date is not None:
            result['PreferredBackupDate'] = self.preferred_backup_date

        if self.preferred_backup_window is not None:
            result['PreferredBackupWindow'] = self.preferred_backup_window

        if self.preferred_backup_window_begin is not None:
            result['PreferredBackupWindowBegin'] = self.preferred_backup_window_begin

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.advance_data_policies = []
        if m.get('AdvanceDataPolicies') is not None:
            for k1 in m.get('AdvanceDataPolicies'):
                temp_model = main_models.DescribeBackupPolicyResponseBodyDataAdvanceDataPolicies()
                self.advance_data_policies.append(temp_model.from_map(k1))

        self.advance_inc_policies = []
        if m.get('AdvanceIncPolicies') is not None:
            for k1 in m.get('AdvanceIncPolicies'):
                temp_model = main_models.DescribeBackupPolicyResponseBodyDataAdvanceIncPolicies()
                self.advance_inc_policies.append(temp_model.from_map(k1))

        self.advance_log_policies = []
        if m.get('AdvanceLogPolicies') is not None:
            for k1 in m.get('AdvanceLogPolicies'):
                temp_model = main_models.DescribeBackupPolicyResponseBodyDataAdvanceLogPolicies()
                self.advance_log_policies.append(temp_model.from_map(k1))

        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')

        if m.get('BackupPriority') is not None:
            self.backup_priority = m.get('BackupPriority')

        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')

        if m.get('BackupRetentionPolicyOnClusterDeletion') is not None:
            self.backup_retention_policy_on_cluster_deletion = m.get('BackupRetentionPolicyOnClusterDeletion')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('EnableBackup') is not None:
            self.enable_backup = m.get('EnableBackup')

        if m.get('EnableIncBackup') is not None:
            self.enable_inc_backup = m.get('EnableIncBackup')

        if m.get('EnableLogBackup') is not None:
            self.enable_log_backup = m.get('EnableLogBackup')

        if m.get('HighFrequencyBakInterval') is not None:
            self.high_frequency_bak_interval = m.get('HighFrequencyBakInterval')

        if m.get('HighSpaceUsageProtection') is not None:
            self.high_space_usage_protection = m.get('HighSpaceUsageProtection')

        if m.get('IncBackupInterval') is not None:
            self.inc_backup_interval = m.get('IncBackupInterval')

        if m.get('LocalLogRetentionSpace') is not None:
            self.local_log_retention_space = m.get('LocalLogRetentionSpace')

        if m.get('LogBackupLocalRetentionNumber') is not None:
            self.log_backup_local_retention_number = m.get('LogBackupLocalRetentionNumber')

        if m.get('LogBackupRetention') is not None:
            self.log_backup_retention = m.get('LogBackupRetention')

        if m.get('PreferredBackupDate') is not None:
            self.preferred_backup_date = m.get('PreferredBackupDate')

        if m.get('PreferredBackupWindow') is not None:
            self.preferred_backup_window = m.get('PreferredBackupWindow')

        if m.get('PreferredBackupWindowBegin') is not None:
            self.preferred_backup_window_begin = m.get('PreferredBackupWindowBegin')

        return self

class DescribeBackupPolicyResponseBodyDataAdvanceLogPolicies(DaraModel):
    def __init__(
        self,
        dest_region: str = None,
        dest_type: str = None,
        enable_log_backup: int = None,
        filter_key: str = None,
        filter_type: str = None,
        filter_value: str = None,
        log_retention_type: str = None,
        log_retention_value: str = None,
        policy_id: str = None,
        src_region: str = None,
        src_type: str = None,
    ):
        # The region in which the backup files are stored.
        self.dest_region = dest_region
        # The storage method of backup files. Valid values:
        # 
        # *   **db**: database
        # *   **level1**: level-1 backup
        # *   **level2**: level-2 backup
        # *   **level2Cross**: level-2 cross-region backup
        self.dest_type = dest_type
        # A reserved parameter.
        self.enable_log_backup = enable_log_backup
        self.filter_key = filter_key
        self.filter_type = filter_type
        self.filter_value = filter_value
        # The retention type of log backups. Valid values:
        # 
        # *   **never**: Log backups never expire.
        # *   **delay**: Log backups are retained for a specific number of days.
        self.log_retention_type = log_retention_type
        # The retention period of log backups.
        self.log_retention_value = log_retention_value
        # The backup policy ID.
        self.policy_id = policy_id
        # The region in which the data source of the backup policy resides.
        self.src_region = src_region
        # The type of the data source of the backup policy. Valid values:
        # 
        # *   **db**: database
        # *   **level1**: level-1 backup
        # *   **level2**: level-2 backup
        # *   **level2Cross**: level-2 cross-region backup
        self.src_type = src_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dest_region is not None:
            result['DestRegion'] = self.dest_region

        if self.dest_type is not None:
            result['DestType'] = self.dest_type

        if self.enable_log_backup is not None:
            result['EnableLogBackup'] = self.enable_log_backup

        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key

        if self.filter_type is not None:
            result['FilterType'] = self.filter_type

        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value

        if self.log_retention_type is not None:
            result['LogRetentionType'] = self.log_retention_type

        if self.log_retention_value is not None:
            result['LogRetentionValue'] = self.log_retention_value

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.src_region is not None:
            result['SrcRegion'] = self.src_region

        if self.src_type is not None:
            result['SrcType'] = self.src_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestRegion') is not None:
            self.dest_region = m.get('DestRegion')

        if m.get('DestType') is not None:
            self.dest_type = m.get('DestType')

        if m.get('EnableLogBackup') is not None:
            self.enable_log_backup = m.get('EnableLogBackup')

        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')

        if m.get('FilterType') is not None:
            self.filter_type = m.get('FilterType')

        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')

        if m.get('LogRetentionType') is not None:
            self.log_retention_type = m.get('LogRetentionType')

        if m.get('LogRetentionValue') is not None:
            self.log_retention_value = m.get('LogRetentionValue')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('SrcRegion') is not None:
            self.src_region = m.get('SrcRegion')

        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')

        return self

class DescribeBackupPolicyResponseBodyDataAdvanceIncPolicies(DaraModel):
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

class DescribeBackupPolicyResponseBodyDataAdvanceDataPolicies(DaraModel):
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
        policy_id: str = None,
        retention_type: str = None,
        retention_value: str = None,
        src_region: str = None,
        src_type: str = None,
        storage_class: str = None,
    ):
        # Indicates whether the backup policy is generated by the system. Valid values:
        # 
        # *   **true**: The backup policy is generated by the system.
        # *   **false**: The backup policy is a custom one.
        self.auto_created = auto_created
        # The backup type. Valid values:
        # 
        # *   **F**: full backup
        # *   **L**: log backup
        self.bak_type = bak_type
        # The region in which the backup files are stored.
        self.dest_region = dest_region
        # The storage method of backup files. Valid values:
        # 
        # *   **db**: database
        # *   **level1**: level-1 backup
        # *   **level2**: level-2 backup
        # *   **level2Cross**: level-2 cross-region backup
        self.dest_type = dest_type
        # The information about the dump policy. Valid values:
        # 
        # *   **copy**: The backup data is copied from the data source to the destination.
        # *   **move**: The backup data is moved from the data source to the destination.
        self.dump_action = dump_action
        # The scheduling frequency. Valid values:
        # 
        # *   **dayOfWeek**: scheduling by week
        # *   **dayOfMonth**: scheduling by month
        # *   **dayOfYear**: scheduling by year
        # *   **backupInterval**: scheduling at a specific interval
        # 
        # >  This parameter is returned only if the value of FilterType is **crontab**.
        self.filter_key = filter_key
        # The scheduling mode of the advanced backup policy. Valid values:
        # 
        # *   **crontab**: periodic scheduling
        # *   **event**: event-based scheduling
        self.filter_type = filter_type
        # The day of a week on which you want to back up data.
        self.filter_value = filter_value
        # The ID of the advanced backup policy.
        self.policy_id = policy_id
        # The retention type of backup sets. Valid values:
        # 
        # *   **never**: Backup sets never expire.
        # *   **delay**: Backup sets are retained for a specific number of days.
        self.retention_type = retention_type
        # The validity period, in days.
        self.retention_value = retention_value
        # The region in which the data source of the backup policy resides.
        self.src_region = src_region
        # The type of the data source of the backup policy. Valid values:
        # 
        # *   **db**: database
        # *   **level1**: level-1 backup
        # *   **level2**: level-2 backup
        # *   **level2Cross**: level-2 cross-region backup
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

