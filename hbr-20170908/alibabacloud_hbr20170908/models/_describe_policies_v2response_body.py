# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribePoliciesV2ResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        policies: List[main_models.DescribePoliciesV2ResponseBodyPolicies] = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The response code. 200 indicates success.
        self.code = code
        # The number of results per query.
        # 
        # Valid values: 10 to 100. Default value: 10.
        self.max_results = max_results
        # The returned message. The value "successful" is returned for a successful request. An error message is returned for a failed request.
        self.message = message
        # The token required to retrieve the next page of policies.
        self.next_token = next_token
        # The list of policies.
        self.policies = policies
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - true: Successful.
        # - false: Failed.
        self.success = success
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.policies:
            for v1 in self.policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Policies'] = []
        if self.policies is not None:
            for k1 in self.policies:
                result['Policies'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.policies = []
        if m.get('Policies') is not None:
            for k1 in m.get('Policies'):
                temp_model = main_models.DescribePoliciesV2ResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribePoliciesV2ResponseBodyPolicies(DaraModel):
    def __init__(
        self,
        business_status: str = None,
        created_time: int = None,
        policy_binding_count: int = None,
        policy_description: str = None,
        policy_id: str = None,
        policy_name: str = None,
        policy_type: str = None,
        rules: List[main_models.DescribePoliciesV2ResponseBodyPoliciesRules] = None,
        updated_time: int = None,
    ):
        # The user business status.
        self.business_status = business_status
        # The creation time. UNIX timestamp, in seconds.
        self.created_time = created_time
        # The number of data sources bound to the policy.
        self.policy_binding_count = policy_binding_count
        # The policy description.
        self.policy_description = policy_description
        # The policy ID.
        self.policy_id = policy_id
        # The policy name.
        self.policy_name = policy_name
        # The policy type. Valid values:
        # - **STANDARD**: general backup policy. Supports backing up data sources other than ECS instance backup.
        # - **UDM_ECS_ONLY**: ECS instance backup policy. Supports backing up only ECS instances.
        self.policy_type = policy_type
        # The list of policy rules.
        self.rules = rules
        # The update time. UNIX timestamp, in seconds.
        self.updated_time = updated_time

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
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.policy_binding_count is not None:
            result['PolicyBindingCount'] = self.policy_binding_count

        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('PolicyBindingCount') is not None:
            self.policy_binding_count = m.get('PolicyBindingCount')

        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribePoliciesV2ResponseBodyPoliciesRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        return self

class DescribePoliciesV2ResponseBodyPoliciesRules(DaraModel):
    def __init__(
        self,
        archive_days: int = None,
        backup_type: str = None,
        data_source_filters: List[main_models.DescribePoliciesV2ResponseBodyPoliciesRulesDataSourceFilters] = None,
        immutable: bool = None,
        keep_latest_snapshots: int = None,
        replication_region_id: str = None,
        retention: int = None,
        retention_rules: List[main_models.DescribePoliciesV2ResponseBodyPoliciesRulesRetentionRules] = None,
        rule_id: str = None,
        rule_type: str = None,
        schedule: str = None,
        tag_filters: List[main_models.DescribePoliciesV2ResponseBodyPoliciesRulesTagFilters] = None,
        vault_id: str = None,
    ):
        # This parameter is required only when **RuleType** is set to **TRANSITION**. The number of days after which the backup is converted to archive storage. Unit: days.
        self.archive_days = archive_days
        # This parameter is required only when **RuleType** is set to **BACKUP**. The backup type. The value is **COMPLETE**, which indicates a full backup.
        self.backup_type = backup_type
        # This parameter is required only when **RuleType** is set to **TAG**. The data source filter rules.
        self.data_source_filters = data_source_filters
        # This parameter is valid only when **PolicyType** is set to **UDM_ECS_ONLY**. Specifies whether to enable backup locking.
        self.immutable = immutable
        # Specifies whether to retain at least one backup version. Valid values:
        # - **0**: Do not retain.
        # - **1**: Retain.
        self.keep_latest_snapshots = keep_latest_snapshots
        # This parameter is required only when **RuleType** is set to **REPLICATION**. The destination region ID for replication.
        self.replication_region_id = replication_region_id
        # This parameter is required only when **RuleType** is set to **TRANSITION** or **REPLICATION**.
        # - **RuleType** is set to **TRANSITION**: the retention period of the backup. Minimum value: 1. Unit: days.
        # - **RuleType** is set to **REPLICATION**: the retention period of the geo-redundancy backup. Minimum value: 1. Unit: days.
        self.retention = retention
        # This parameter is required only when **RuleType** is set to **TRANSITION**. The list of special retention rules.
        self.retention_rules = retention_rules
        # The rule ID.
        self.rule_id = rule_id
        # The rule type. Each policy must have at least one **BACKUP** rule and exactly one **TRANSITION** rule. Valid values:
        # - **BACKUP**: backup rule.
        # - **TRANSITION**: lifecycle rule.
        # - **REPLICATION**: replication rule.
        self.rule_type = rule_type
        # This parameter is required only when **RuleType** is set to **BACKUP**. The backup schedule. Optional format: `I|{startTime}|{interval}`. This indicates that a backup job is executed at every {interval} starting from {startTime}. Backup jobs for past time periods are not compensated. If the previous backup job is not completed, the next backup job is not triggered. For example, `I|1631685600|P1D` indicates that a backup is performed once a day starting from 2021-09-15 14:00:00.
        # 
        # * startTime: the start time of the backup. UNIX timestamp, in seconds.
        # * interval: the ISO 8601 time interval. For example, PT1H indicates an interval of one hour. P1D indicates an interval of one day.
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

        self.data_source_filters = []
        if m.get('DataSourceFilters') is not None:
            for k1 in m.get('DataSourceFilters'):
                temp_model = main_models.DescribePoliciesV2ResponseBodyPoliciesRulesDataSourceFilters()
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
                temp_model = main_models.DescribePoliciesV2ResponseBodyPoliciesRulesRetentionRules()
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
                temp_model = main_models.DescribePoliciesV2ResponseBodyPoliciesRulesTagFilters()
                self.tag_filters.append(temp_model.from_map(k1))

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

class DescribePoliciesV2ResponseBodyPoliciesRulesTagFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag matching rule. Valid values:
        # - **EQUAL**: matches both the tag key and the tag value.
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

class DescribePoliciesV2ResponseBodyPoliciesRulesRetentionRules(DaraModel):
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
        # The backup to which the rule applies. Currently, only the first backup is supported. The value is 1.
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

class DescribePoliciesV2ResponseBodyPoliciesRulesDataSourceFilters(DaraModel):
    def __init__(
        self,
        account_scope: str = None,
        accounts: List[main_models.DescribePoliciesV2ResponseBodyPoliciesRulesDataSourceFiltersAccounts] = None,
        data_source_ids: List[str] = None,
        source_type: str = None,
    ):
        self.account_scope = account_scope
        self.accounts = accounts
        # Deprecated.
        self.data_source_ids = data_source_ids
        # The data source type. Valid values:
        # - **UDM_ECS**: ECS instance backup.
        # - **OSS**: OSS backup.
        # - **NAS**: Alibaba Cloud NAS backup.
        # - **ECS_FILE**: ECS File Backup Essential Edition.
        # - **OTS**: Tablestore backup.
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
                temp_model = main_models.DescribePoliciesV2ResponseBodyPoliciesRulesDataSourceFiltersAccounts()
                self.accounts.append(temp_model.from_map(k1))

        if m.get('DataSourceIds') is not None:
            self.data_source_ids = m.get('DataSourceIds')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

class DescribePoliciesV2ResponseBodyPoliciesRulesDataSourceFiltersAccounts(DaraModel):
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

