# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dbs20210101 import models as main_models
from darabonba.model import DaraModel

class ModifyBackupPolicyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ModifyBackupPolicyResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The response code.
        self.code = code
        # The details of the backup policy.
        self.data = data
        # The error code returned if the request failed.
        self.err_code = err_code
        # The error message returned if the request failed.
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
            temp_model = main_models.ModifyBackupPolicyResponseBodyData()
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

class ModifyBackupPolicyResponseBodyData(DaraModel):
    def __init__(
        self,
        advance_data_policies: List[main_models.ModifyBackupPolicyResponseBodyDataAdvanceDataPolicies] = None,
        advance_inc_policies: List[main_models.ModifyBackupPolicyResponseBodyDataAdvanceIncPolicies] = None,
        advance_log_policies: List[main_models.ModifyBackupPolicyResponseBodyDataAdvanceLogPolicies] = None,
        backup_method: str = None,
        backup_priority: int = None,
        backup_retention_policy_on_cluster_deletion: str = None,
        category: str = None,
        enable_inc_backup: bool = None,
        preferred_backup_window: str = None,
        preferred_backup_window_begin: str = None,
    ):
        # The details of data backup policies.
        self.advance_data_policies = advance_data_policies
        self.advance_inc_policies = advance_inc_policies
        self.advance_log_policies = advance_log_policies
        self.backup_method = backup_method
        self.backup_priority = backup_priority
        self.backup_retention_policy_on_cluster_deletion = backup_retention_policy_on_cluster_deletion
        self.category = category
        self.enable_inc_backup = enable_inc_backup
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

        if self.backup_retention_policy_on_cluster_deletion is not None:
            result['BackupRetentionPolicyOnClusterDeletion'] = self.backup_retention_policy_on_cluster_deletion

        if self.category is not None:
            result['Category'] = self.category

        if self.enable_inc_backup is not None:
            result['EnableIncBackup'] = self.enable_inc_backup

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
                temp_model = main_models.ModifyBackupPolicyResponseBodyDataAdvanceDataPolicies()
                self.advance_data_policies.append(temp_model.from_map(k1))

        self.advance_inc_policies = []
        if m.get('AdvanceIncPolicies') is not None:
            for k1 in m.get('AdvanceIncPolicies'):
                temp_model = main_models.ModifyBackupPolicyResponseBodyDataAdvanceIncPolicies()
                self.advance_inc_policies.append(temp_model.from_map(k1))

        self.advance_log_policies = []
        if m.get('AdvanceLogPolicies') is not None:
            for k1 in m.get('AdvanceLogPolicies'):
                temp_model = main_models.ModifyBackupPolicyResponseBodyDataAdvanceLogPolicies()
                self.advance_log_policies.append(temp_model.from_map(k1))

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

        if m.get('PreferredBackupWindow') is not None:
            self.preferred_backup_window = m.get('PreferredBackupWindow')

        if m.get('PreferredBackupWindowBegin') is not None:
            self.preferred_backup_window_begin = m.get('PreferredBackupWindowBegin')

        return self

class ModifyBackupPolicyResponseBodyDataAdvanceLogPolicies(DaraModel):
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
        self.dest_region = dest_region
        self.dest_type = dest_type
        self.enable_log_backup = enable_log_backup
        self.filter_key = filter_key
        self.filter_type = filter_type
        self.filter_value = filter_value
        self.log_retention_type = log_retention_type
        self.log_retention_value = log_retention_value
        self.policy_id = policy_id
        self.src_region = src_region
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

class ModifyBackupPolicyResponseBodyDataAdvanceIncPolicies(DaraModel):
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

class ModifyBackupPolicyResponseBodyDataAdvanceDataPolicies(DaraModel):
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
        # *   **F**: full backup.
        # *   **L**: log backup.
        self.bak_type = bak_type
        # The region in which backup files are stored.
        self.dest_region = dest_region
        # The storage method of backup files. Valid values:
        # 
        # *   **db**: database.
        # *   **level1**: level-1 backup.
        # *   **level2**: level-2 backup.
        # *   **level2Cross**: level-2 cross-region backup.
        self.dest_type = dest_type
        # The information about the dump policy. Valid values:
        # 
        # *   **copy**: The backup data is copied from the data source to the destination.
        # *   **move**: The backup data is moved from the data source to the destination.
        self.dump_action = dump_action
        # The scheduling cycle. Valid values:
        # 
        # *   **dayOfWeek**: scheduling by week.
        # *   **dayOfMonth**: scheduling by month.
        # *   **dayOfYear**: scheduling by year.
        # *   **backupInterval**: scheduling at a specific interval.
        # 
        # >  This parameter is returned only when FilterType is set to **crontab**.
        self.filter_key = filter_key
        # The scheduling mode of the advanced backup policy. Valid values:
        # 
        # *   **crontab**: periodic scheduling.
        # *   **event**: event-based scheduling.
        self.filter_type = filter_type
        # The backup cycle.
        self.filter_value = filter_value
        self.only_preserve_one_each_day = only_preserve_one_each_day
        # The ID of the advanced backup policy.
        self.policy_id = policy_id
        # The retention type of backup sets. Valid values:
        # 
        # *   **never**: Backup sets never expire.
        # *   **delay**: Backup sets are retained for a specific number of days.
        self.retention_type = retention_type
        # The retention period. Unit: day.
        self.retention_value = retention_value
        # The region in which the data source of the backup policy resides.
        self.src_region = src_region
        # The type of the data source of the backup policy. Valid values:
        # 
        # *   **db**: database.
        # *   **level1**: level-1 backup.
        # *   **level2**: level-2 backup.
        # *   **level2Cross**: level-2 cross-region backup.
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

