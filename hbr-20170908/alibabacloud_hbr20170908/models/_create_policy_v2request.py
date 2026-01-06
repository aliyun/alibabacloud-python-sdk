# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class CreatePolicyV2Request(DaraModel):
    def __init__(
        self,
        policy_description: str = None,
        policy_name: str = None,
        policy_type: str = None,
        rules: List[main_models.CreatePolicyV2RequestRules] = None,
    ):
        # The description of the backup policy.
        self.policy_description = policy_description
        # The name of the backup policy.
        self.policy_name = policy_name
        # The policy type. Valid values:
        # 
        # *   **STANDARD**: the general backup policy. This type of policy applies to backups other than Elastic Compute Service (ECS) instance backup.
        # *   **UDM_ECS_ONLY**: This type of policy applies only to ECS instance backup.
        # 
        # If the policy type is not specified, Cloud Backup automatically sets the policy type based on whether the backup vault is specified in the rules of the policy:
        # 
        # *   If the backup vault is specified, Cloud Backup sets the policy type to **STANDARD**.
        # *   If the backup vault is not specified, Cloud Backup sets the policy type to **UDM_ECS_ONLY**.
        self.policy_type = policy_type
        # The rules in the backup policy.
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

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.CreatePolicyV2RequestRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class CreatePolicyV2RequestRules(DaraModel):
    def __init__(
        self,
        backup_type: str = None,
        data_source_filters: List[main_models.CreatePolicyV2RequestRulesDataSourceFilters] = None,
        immutable: bool = None,
        keep_latest_snapshots: int = None,
        replication_region_id: str = None,
        retention: int = None,
        retention_rules: List[main_models.CreatePolicyV2RequestRulesRetentionRules] = None,
        rule_type: str = None,
        schedule: str = None,
        tag_filters: List[main_models.CreatePolicyV2RequestRulesTagFilters] = None,
        vault_id: str = None,
    ):
        # This parameter is required only if the **RuleType** parameter is set to **BACKUP**. This parameter specifies the backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type
        # This parameter is required only if the **RuleType** parameter is set to **TAG**. This parameter specifies the data source filter rule.
        self.data_source_filters = data_source_filters
        # This parameter is required only if the **PolicyType** parameter is set to **UDM_ECS_ONLY**. This parameter specifies whether to enable the immutable backup feature.
        self.immutable = immutable
        # Specifies whether to enable the feature of keeping at least one backup version. Valid values:
        # 
        # *   0: The feature is disabled.
        # *   1: The feature is enabled.
        self.keep_latest_snapshots = keep_latest_snapshots
        # This parameter is required only if the **RuleType** parameter is set to **REPLICATION**. This parameter specifies the ID of the destination region.
        self.replication_region_id = replication_region_id
        # This parameter is required only if the **RuleType** parameter is set to **BACKUP**, **TRANSITION**, or **REPLICATION**.
        # 
        # *   If the **RuleType** parameter is set to **BACKUP**, this parameter specifies the retention period of the backup data. The priority is lower than the retention period when the **RuleType** parameter is set to **TRANSITION**. Minimum value: 1. Maximum value: 364635. Unit: days.
        # *   If the **RuleType** parameter is set to **TRANSITION**, this parameter specifies the retention period of the backup data. Minimum value: 1. Maximum value: 364635. Unit: days.
        # *   If the **RuleType** parameter is set to **REPLICATION**, this parameter specifies the retention period of remote backups. Minimum value: 1. Maximum value: 364635. Unit: days.
        self.retention = retention
        # This parameter is required only if the **RuleType** parameter is set to **TRANSITION**. This parameter specifies the special retention rules.
        self.retention_rules = retention_rules
        # The type of the rule. Each backup policy must have at least one rule of the **BACKUP** type and only one rule of the **TRANSITION** type. Valid values:
        # 
        # *   **BACKUP**: backup rule
        # *   **TRANSITION**: lifecycle rule
        # *   **REPLICATION**: replication rule
        # *   **TAG**: tag-based resource association rule
        # 
        # This parameter is required.
        self.rule_type = rule_type
        # This parameter is required only if the **RuleType** parameter is set to **BACKUP**. This parameter specifies the backup schedule settings. Formats:
        # 
        # *   `I|{startTime}|{interval}`: The system runs the first backup job at a point in time that is specified in the {startTime} parameter and the subsequent backup jobs at an interval that is specified in the {interval} parameter. For example, `I|1631685600|P1D` indicates that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        #     *   startTime: the time at which the system starts to run a backup job. The time must follow the UNIX time format. Unit: seconds.
        #     *   interval: the interval at which the system runs a backup job. The interval must follow the ISO 8601 standard. For example, `PT1H` specifies an interval of 1 hour. `P1D` specifies an interval of one day.
        # 
        # *   `C|{startTime}|{crontab}`: The system runs backup jobs at a point in time that is specified in the {startTime} parameter based on the {crontab} expression. For example, C|1631685600|0 0 2 ?\\* 3,5,7 indicates that the system runs backup jobs at 02:00:00 every Tuesday, Thursday, and Saturday from14:00:00 on September 15, 2021.``
        # 
        #     *   startTime: the time at which the system starts to run a backup job. The time must follow the UNIX time format. Unit: seconds.
        #     *   crontab: the crontab expression. For example, 0 0 2 ?\\* 3,5,7 indicates 02:00:00 every Tuesday, Thursday, and Saturday.``
        # 
        # The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed.
        self.schedule = schedule
        # This parameter is required only if the **RuleType** parameter is set to **TAG**. This parameter specifies the resource tag filter rule.
        self.tag_filters = tag_filters
        # This parameter is required only if the RuleType parameter is set to BACKUP. The ID of the backup vault.
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
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        self.data_source_filters = []
        if m.get('DataSourceFilters') is not None:
            for k1 in m.get('DataSourceFilters'):
                temp_model = main_models.CreatePolicyV2RequestRulesDataSourceFilters()
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
                temp_model = main_models.CreatePolicyV2RequestRulesRetentionRules()
                self.retention_rules.append(temp_model.from_map(k1))

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')

        self.tag_filters = []
        if m.get('TagFilters') is not None:
            for k1 in m.get('TagFilters'):
                temp_model = main_models.CreatePolicyV2RequestRulesTagFilters()
                self.tag_filters.append(temp_model.from_map(k1))

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

class CreatePolicyV2RequestRulesTagFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag-based matching rule. Valid values:
        # 
        # *   **EQUAL**: Both the tag key and tag value are matched.
        # *   **NOT**: The tag key is matched and the tag value is not matched.
        self.operator = operator
        # The tag value. If you leave this parameter empty, the value is any value.
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

class CreatePolicyV2RequestRulesRetentionRules(DaraModel):
    def __init__(
        self,
        advanced_retention_type: str = None,
        retention: int = None,
        which_snapshot: int = None,
    ):
        # The type of the special retention rule. Valid values:
        # 
        # *   **DAILY**: retains daily backups
        # *   **WEEKLY**: retains weekly backups
        # *   **MONTHLY**: retains monthly backups
        # *   **YEARLY**: retains yearly backups
        self.advanced_retention_type = advanced_retention_type
        # The special retention period of backups. Minimum value: 1. Unit: days.
        self.retention = retention
        # Specifies which backup is retained based on the special retention rule. Only the first backup can be retained.
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

class CreatePolicyV2RequestRulesDataSourceFilters(DaraModel):
    def __init__(
        self,
        data_source_ids: List[str] = None,
        source_type: str = None,
    ):
        # This parameter is deprecated.
        self.data_source_ids = data_source_ids
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: Elastic Compute Service (ECS) instance This type of data source is supported only if the **PolicyType** parameter is set to **UDM_ECS_ONLY**.
        # *   **OSS**: Object Storage Service (OSS) bucket This type of data source is supported only if the **PolicyType** parameter is set to **STANDARD**.
        # *   **NAS**: File Storage NAS (NAS) file system This type of data source is supported only if the **PolicyType** parameter is set to **STANDARD**.
        # *   **ECS_FILE**: ECS file This type of data source is supported only if the **PolicyType** parameter is set to **STANDARD**.
        # *   **OTS**: Tablestore instance This type of data source is supported only if the **PolicyType** parameter is set to **STANDARD**.
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

