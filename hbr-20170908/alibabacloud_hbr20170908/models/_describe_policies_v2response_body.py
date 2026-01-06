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
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The number of results for each query.
        # 
        # Valid values: 10 to 100. Default value: 10.
        self.max_results = max_results
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The token that is used to obtain the next page of backup policies.
        self.next_token = next_token
        # The backup policies.
        self.policies = policies
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success
        # The total number of returned entries.
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
        self.business_status = business_status
        # The time when the backup policy was created. The value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time
        # The number of data sources that are bound to the backup policy.
        self.policy_binding_count = policy_binding_count
        # The description of the backup policy.
        self.policy_description = policy_description
        # The ID of the backup policy.
        self.policy_id = policy_id
        # The name of the backup policy.
        self.policy_name = policy_name
        # The policy type. Valid values:
        # 
        # *   **STANDARD**: the general backup policy. This type of policy applies to backups other than Elastic Compute Service (ECS) instance backup.
        # *   **UDM_ECS_ONLY**: the ECS instance backup policy. This type of policy applies only to ECS instance backup.
        self.policy_type = policy_type
        # The rules in the backup policy.
        self.rules = rules
        # The time when the backup policy was updated. The value is a UNIX timestamp. Unit: seconds.
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
        # This parameter is returned only if the value of the **RuleType** parameter is **TRANSITION**. This parameter indicates the time when data is dumped from a backup vault to an archive vault. Unit: days.
        self.archive_days = archive_days
        # This parameter is returned only if the value of the **RuleType** parameter is **BACKUP**. This parameter indicates the backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type
        # This parameter is required only when **RuleType** is set to **TAG**. It defines the data source filtering rule.
        self.data_source_filters = data_source_filters
        # This parameter is returned only if the **PolicyType** is **UDM_ECS_ONLY**. This parameter indicates whether the immutable backup feature is enabled.
        self.immutable = immutable
        # Indicates whether the feature of keeping at least one backup version is enabled. Valid values:
        # 
        # *   **0**: The feature is disabled.
        # *   **1**: The feature is enabled.
        self.keep_latest_snapshots = keep_latest_snapshots
        # This parameter is returned only if the value of the **RuleType** parameter is **REPLICATION**. This parameter indicates the ID of the destination region.
        self.replication_region_id = replication_region_id
        # This parameter is returned only if the value of the **RuleType** parameter is **TRANSITION** or **REPLICATION**.
        # 
        # *   If the value of the **RuleType** parameter is **TRANSITION**, this parameter indicates the retention period of the backup data. Minimum value: 1. Unit: days.
        # *   If the value of the **RuleType** parameter is **REPLICATION**, this parameter indicates the retention period of remote backups. Minimum value: 1. Unit: days.
        self.retention = retention
        # This parameter is returned only if the value of the **RuleType** parameter is **TRANSITION**. This parameter indicates the special retention rules.
        self.retention_rules = retention_rules
        # The rule ID.
        self.rule_id = rule_id
        # The type of the rule. Each backup policy must have at least one rule of the **BACKUP** type and only one rule of the **TRANSITION** type. Valid values:
        # 
        # *   **BACKUP**: backup rule
        # *   **TRANSITION**: lifecycle rule
        # *   **REPLICATION**: replication rule
        self.rule_type = rule_type
        # This parameter is returned only if the value of the **RuleType** parameter is **BACKUP**. This parameter indicates the backup schedule settings. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified in the {startTime} parameter and the subsequent backup jobs at an interval that is specified in the {interval} parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, `I|1631685600|P1D` indicates that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   startTime: the time at which the system starts to run a backup job. The time follows the UNIX time format. Unit: seconds.
        # *   interval: the interval at which the system runs a backup job. The interval follows the ISO 8601 standard. For example, PT1H indicates an interval of 1 hour. P1D indicates an interval of one day.
        self.schedule = schedule
        # This parameter is required only when **RuleType** is set to **TAG**. It defines the resource tag filtering rule.
        self.tag_filters = tag_filters
        # This parameter is returned only if the value of the RuleType parameter is BACKUP. The ID of the backup vault.
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
        # Tag key
        self.key = key
        # Tag matching rules, supporting: - **EQUAL**: Matches both the tag key and tag value. - **NOT**: Matches the tag key but not the tag value.
        self.operator = operator
        # Tag value.
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
        # 
        # *   **WEEKLY**: weekly backups
        # *   **MONTHLY**: monthly backups
        # *   **YEARLY**: yearly backups
        self.advanced_retention_type = advanced_retention_type
        # The special retention period of backups. Minimum value: 1. Unit: days.
        self.retention = retention
        # Indicates which backup is retained based on the special retention rule. Only the first backup can be retained.
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
        data_source_ids: List[str] = None,
        source_type: str = None,
    ):
        # Deprecated.
        self.data_source_ids = data_source_ids
        # Data source type. The value range is as follows: 
        # - **UDM_ECS**: Indicates ECS server backup. 
        # - **OSS**: Indicates OSS backup. 
        # - **NAS**: Indicates Alibaba Cloud NAS backup. 
        # - **ECS_FILE**: Indicates ECS file backup. 
        # - **OTS**: Indicates Tablestore backup.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_ids is not None:
            result['DataSourceIds'] = self.data_source_ids

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceIds') is not None:
            self.data_source_ids = m.get('DataSourceIds')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

