# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class UpdatePolicyV2Request(DaraModel):
    def __init__(
        self,
        policy_description: str = None,
        policy_id: str = None,
        policy_name: str = None,
        rules: List[main_models.UpdatePolicyV2RequestRules] = None,
    ):
        # The policy description.
        self.policy_description = policy_description
        # The policy ID.
        self.policy_id = policy_id
        # The policy name.
        self.policy_name = policy_name
        # The list of policy rules.
        self.rules = rules

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.UpdatePolicyV2RequestRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class UpdatePolicyV2RequestRules(DaraModel):
    def __init__(
        self,
        archive_days: int = None,
        backup_type: str = None,
        cold_archive_days: int = None,
        data_source_filters: List[main_models.UpdatePolicyV2RequestRulesDataSourceFilters] = None,
        immutable: bool = None,
        keep_latest_snapshots: int = None,
        replication_region_id: str = None,
        retention: int = None,
        retention_rules: List[main_models.UpdatePolicyV2RequestRulesRetentionRules] = None,
        rule_id: str = None,
        rule_type: str = None,
        schedule: str = None,
        tag_filters: List[main_models.UpdatePolicyV2RequestRulesTagFilters] = None,
        vault_id: str = None,
    ):
        # This parameter is required only when **RuleType** is set to **TRANSITION**. The number of days after which the backup is converted to archive storage. Unit: days.
        self.archive_days = archive_days
        # This parameter is required only when **RuleType** is set to **BACKUP**. The backup type. Set the value to **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type
        # This parameter is required only when **RuleType** is set to **TRANSITION**. The number of days after which the backup is converted to cold archive storage. Unit: days.
        self.cold_archive_days = cold_archive_days
        # This parameter is required only when **RuleType** is set to **TAG**. The data source filter rules.
        self.data_source_filters = data_source_filters
        # This parameter is required only when **PolicyType** is set to **UDM_ECS_ONLY** and **RuleType** is set to **SECURITY**. Specifies whether to enable backup locking.
        self.immutable = immutable
        # Specifies whether to retain at least one backup version. Valid values:
        # - 0: do not retain.
        # - 1: retain.
        self.keep_latest_snapshots = keep_latest_snapshots
        # This parameter is required only when **RuleType** is set to **REPLICATION**. The ID of the destination region for replication.
        self.replication_region_id = replication_region_id
        # This parameter is required only when **RuleType** is set to **TRANSITION** or **REPLICATION**.
        # - If **RuleType** is set to **TRANSITION**: the retention period of the backup. Minimum value: 1. Unit: days.
        # - If **RuleType** is set to **REPLICATION**: the retention period of the cross-region backup. Minimum value: 1. Unit: days.
        self.retention = retention
        # This parameter is required only when **RuleType** is set to **TRANSITION**. The special retention rules.
        self.retention_rules = retention_rules
        # The rule ID.
        self.rule_id = rule_id
        # The rule type. Each policy must have at least one **BACKUP** rule and exactly one **TRANSITION** rule. Valid values:
        # - **BACKUP**: backup rule.
        # - **TRANSITION**: lifecycle rule.
        # - **REPLICATION**: replication rule.
        self.rule_type = rule_type
        # This parameter is required only when **RuleType** is set to **BACKUP**. The backup schedule settings. Supported formats:
        # - `I|{startTime}|{interval}`: specifies that a backup job is run at the {interval} from the {startTime}. Example: `I|1631685600|P1D` specifies that a backup job is run once a day starting from 2021-09-15 14:00:00.
        # 
        #   * startTime: the start time of the backup. This value is a UNIX timestamp. Unit: seconds.
        #   * interval: the ISO 8601 time interval. Example: `PT1H` specifies an interval of one hour. `P1D` specifies an interval of one day.
        # - `C|{startTime}|{crontab}`: specifies that a backup job is run based on the {crontab} expression from the {startTime}. Example: `C|1631685600|0 0 2 ? * 3,5,7` specifies that a backup job is run at 02:00:00 every Tuesday, Thursday, and Saturday starting from 2021-09-15 14:00:00.
        #   * startTime: the start time of the backup. This value is a UNIX timestamp. Unit: seconds.
        #   * crontab: the crontab expression. Example: `0 0 2 ? * 3,5,7` specifies every Tuesday, Thursday, and Saturday at 02:00:00.
        # 
        # Backup jobs for elapsed time periods are not compensated. If the previous backup job is not completed, the next backup job is not triggered.
        self.schedule = schedule
        # This parameter is required only when **RuleType** is set to **TAG**. The resource tag filter rules.
        self.tag_filters = tag_filters
        # This parameter is required only when RuleType is set to BACKUP. The backup vault ID.
        self.vault_id = vault_id

    def validate(self):
        if self.data_source_filters:
            for v1 in self.data_source_filters:
                 if v1:
                    v1.validate()
        if self.retention_rules:
            for v1 in self.retention_rules:
                 if v1:
                    v1.validate()
        if self.tag_filters:
            for v1 in self.tag_filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.archive_days is not None:
            result['ArchiveDays'] = self.archive_days

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.cold_archive_days is not None:
            result['ColdArchiveDays'] = self.cold_archive_days

        result['DataSourceFilters'] = []
        if self.data_source_filters is not None:
            for k1 in self.data_source_filters:
                result['DataSourceFilters'].append(k1.to_map() if k1 else None)

        if self.immutable is not None:
            result['Immutable'] = self.immutable

        if self.keep_latest_snapshots is not None:
            result['KeepLatestSnapshots'] = self.keep_latest_snapshots

        if self.replication_region_id is not None:
            result['ReplicationRegionId'] = self.replication_region_id

        if self.retention is not None:
            result['Retention'] = self.retention

        result['RetentionRules'] = []
        if self.retention_rules is not None:
            for k1 in self.retention_rules:
                result['RetentionRules'].append(k1.to_map() if k1 else None)

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.schedule is not None:
            result['Schedule'] = self.schedule

        result['TagFilters'] = []
        if self.tag_filters is not None:
            for k1 in self.tag_filters:
                result['TagFilters'].append(k1.to_map() if k1 else None)

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveDays') is not None:
            self.archive_days = m.get('ArchiveDays')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('ColdArchiveDays') is not None:
            self.cold_archive_days = m.get('ColdArchiveDays')

        self.data_source_filters = []
        if m.get('DataSourceFilters') is not None:
            for k1 in m.get('DataSourceFilters'):
                temp_model = main_models.UpdatePolicyV2RequestRulesDataSourceFilters()
                self.data_source_filters.append(temp_model.from_map(k1))

        if m.get('Immutable') is not None:
            self.immutable = m.get('Immutable')

        if m.get('KeepLatestSnapshots') is not None:
            self.keep_latest_snapshots = m.get('KeepLatestSnapshots')

        if m.get('ReplicationRegionId') is not None:
            self.replication_region_id = m.get('ReplicationRegionId')

        if m.get('Retention') is not None:
            self.retention = m.get('Retention')

        self.retention_rules = []
        if m.get('RetentionRules') is not None:
            for k1 in m.get('RetentionRules'):
                temp_model = main_models.UpdatePolicyV2RequestRulesRetentionRules()
                self.retention_rules.append(temp_model.from_map(k1))

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')

        self.tag_filters = []
        if m.get('TagFilters') is not None:
            for k1 in m.get('TagFilters'):
                temp_model = main_models.UpdatePolicyV2RequestRulesTagFilters()
                self.tag_filters.append(temp_model.from_map(k1))

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

class UpdatePolicyV2RequestRulesTagFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag matching rule. Valid values:
        # - **EQUAL**: matches both the tag key and tag value.
        # - **NOT**: matches the tag key but not the tag value.
        self.operator = operator
        # The tag value. An empty value indicates any value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class UpdatePolicyV2RequestRulesRetentionRules(DaraModel):
    def __init__(
        self,
        advanced_retention_type: str = None,
        retention: int = None,
        which_snapshot: int = None,
    ):
        # The type of the special retention rule. Valid values:
        # - **WEEKLY**: weekly backup.
        # - **MONTHLY**: monthly backup.
        # - **YEARLY**: yearly backup.
        self.advanced_retention_type = advanced_retention_type
        # The special retention period of the backup. Minimum value: 1. Unit: days.
        self.retention = retention
        # The backup to which the rule applies. Currently, only the first backup is supported. Set the value to 1.
        self.which_snapshot = which_snapshot

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_retention_type is not None:
            result['AdvancedRetentionType'] = self.advanced_retention_type

        if self.retention is not None:
            result['Retention'] = self.retention

        if self.which_snapshot is not None:
            result['WhichSnapshot'] = self.which_snapshot

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedRetentionType') is not None:
            self.advanced_retention_type = m.get('AdvancedRetentionType')

        if m.get('Retention') is not None:
            self.retention = m.get('Retention')

        if m.get('WhichSnapshot') is not None:
            self.which_snapshot = m.get('WhichSnapshot')

        return self

class UpdatePolicyV2RequestRulesDataSourceFilters(DaraModel):
    def __init__(
        self,
        account_scope: str = None,
        accounts: List[main_models.UpdatePolicyV2RequestRulesDataSourceFiltersAccounts] = None,
        data_source_ids: List[str] = None,
        source_type: str = None,
    ):
        self.account_scope = account_scope
        self.accounts = accounts
        # Deprecated.
        self.data_source_ids = data_source_ids
        # The data source type. Valid values:
        # - **UDM_ECS**: ECS instance backup. This data source type is supported only when **RuleType** is set to **UDM_ECS_ONLY**.
        # - **OSS**: OSS backup. This data source type is supported only when **RuleType** is set to **STANDARD**.
        # - **NAS**: Alibaba Cloud NAS backup. This data source type is supported only when **RuleType** is set to **STANDARD**.
        # - **ECS_FILE**: ECS File Backup Essential Edition. This data source type is supported only when **RuleType** is set to **STANDARD**.
        # - **OTS**: Tablestore backup. This data source type is supported only when **RuleType** is set to **STANDARD**.
        self.source_type = source_type

    def validate(self):
        if self.accounts:
            for v1 in self.accounts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_scope is not None:
            result['AccountScope'] = self.account_scope

        result['Accounts'] = []
        if self.accounts is not None:
            for k1 in self.accounts:
                result['Accounts'].append(k1.to_map() if k1 else None)

        if self.data_source_ids is not None:
            result['DataSourceIds'] = self.data_source_ids

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountScope') is not None:
            self.account_scope = m.get('AccountScope')

        self.accounts = []
        if m.get('Accounts') is not None:
            for k1 in m.get('Accounts'):
                temp_model = main_models.UpdatePolicyV2RequestRulesDataSourceFiltersAccounts()
                self.accounts.append(temp_model.from_map(k1))

        if m.get('DataSourceIds') is not None:
            self.data_source_ids = m.get('DataSourceIds')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

class UpdatePolicyV2RequestRulesDataSourceFiltersAccounts(DaraModel):
    def __init__(
        self,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
    ):
        self.cross_account_role_name = cross_account_role_name
        self.cross_account_type = cross_account_type
        self.cross_account_user_id = cross_account_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name

        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type

        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')

        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')

        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')

        return self

