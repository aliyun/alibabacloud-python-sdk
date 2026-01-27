# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ebs20210730 import models as main_models
from darabonba.model import DaraModel

class UpdateEnterpriseSnapshotPolicyRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        cross_region_copy_info: main_models.UpdateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfo = None,
        desc: str = None,
        name: str = None,
        policy_id: str = None,
        region_id: str = None,
        retain_rule: main_models.UpdateEnterpriseSnapshotPolicyRequestRetainRule = None,
        schedule: main_models.UpdateEnterpriseSnapshotPolicyRequestSchedule = None,
        special_retain_rules: main_models.UpdateEnterpriseSnapshotPolicyRequestSpecialRetainRules = None,
        state: str = None,
        storage_rule: main_models.UpdateEnterpriseSnapshotPolicyRequestStorageRule = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # Snapshot replication destination information.
        self.cross_region_copy_info = cross_region_copy_info
        # The description of the policy.
        self.desc = desc
        # The name of the policy.
        self.name = name
        # The id of the policy.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The region ID . You can call the [DescribeRegions](https://help.aliyun.com/document_detail/354276.html) operation to query the most recent list of regions in which snapshot policy is supported.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Snapshot retention rule.
        self.retain_rule = retain_rule
        # The rule for scheduling.
        self.schedule = schedule
        # The special snapshot retention rules.
        self.special_retain_rules = special_retain_rules
        # The status of the policy. Valid values:
        # 
        # *   **ENABLED**: Enable snapshot policy execution.
        # *   **DISABLED**: Disable snapshot policy execution.
        self.state = state
        # Advanced snapshot features.
        self.storage_rule = storage_rule

    def validate(self):
        if self.cross_region_copy_info:
            self.cross_region_copy_info.validate()
        if self.retain_rule:
            self.retain_rule.validate()
        if self.schedule:
            self.schedule.validate()
        if self.special_retain_rules:
            self.special_retain_rules.validate()
        if self.storage_rule:
            self.storage_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cross_region_copy_info is not None:
            result['CrossRegionCopyInfo'] = self.cross_region_copy_info.to_map()

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.name is not None:
            result['Name'] = self.name

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.retain_rule is not None:
            result['RetainRule'] = self.retain_rule.to_map()

        if self.schedule is not None:
            result['Schedule'] = self.schedule.to_map()

        if self.special_retain_rules is not None:
            result['SpecialRetainRules'] = self.special_retain_rules.to_map()

        if self.state is not None:
            result['State'] = self.state

        if self.storage_rule is not None:
            result['StorageRule'] = self.storage_rule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CrossRegionCopyInfo') is not None:
            temp_model = main_models.UpdateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfo()
            self.cross_region_copy_info = temp_model.from_map(m.get('CrossRegionCopyInfo'))

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RetainRule') is not None:
            temp_model = main_models.UpdateEnterpriseSnapshotPolicyRequestRetainRule()
            self.retain_rule = temp_model.from_map(m.get('RetainRule'))

        if m.get('Schedule') is not None:
            temp_model = main_models.UpdateEnterpriseSnapshotPolicyRequestSchedule()
            self.schedule = temp_model.from_map(m.get('Schedule'))

        if m.get('SpecialRetainRules') is not None:
            temp_model = main_models.UpdateEnterpriseSnapshotPolicyRequestSpecialRetainRules()
            self.special_retain_rules = temp_model.from_map(m.get('SpecialRetainRules'))

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('StorageRule') is not None:
            temp_model = main_models.UpdateEnterpriseSnapshotPolicyRequestStorageRule()
            self.storage_rule = temp_model.from_map(m.get('StorageRule'))

        return self

class UpdateEnterpriseSnapshotPolicyRequestStorageRule(DaraModel):
    def __init__(
        self,
        enable_immediate_access: bool = None,
    ):
        # Whether to enable the rapid availability of snapshots. The range of values:
        # 
        # - true
        # 
        # - false
        self.enable_immediate_access = enable_immediate_access

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_immediate_access is not None:
            result['EnableImmediateAccess'] = self.enable_immediate_access

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableImmediateAccess') is not None:
            self.enable_immediate_access = m.get('EnableImmediateAccess')

        return self

class UpdateEnterpriseSnapshotPolicyRequestSpecialRetainRules(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        rules: List[main_models.UpdateEnterpriseSnapshotPolicyRequestSpecialRetainRulesRules] = None,
    ):
        # Indicates whether the special retention is enabled.
        # 
        # *   true: enable
        # *   false: disable
        self.enabled = enabled
        # The special retention rules.
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
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.UpdateEnterpriseSnapshotPolicyRequestSpecialRetainRulesRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class UpdateEnterpriseSnapshotPolicyRequestSpecialRetainRulesRules(DaraModel):
    def __init__(
        self,
        special_period_unit: str = None,
        time_interval: int = None,
        time_unit: str = None,
    ):
        # The periodic unit for specially retained snapshots. If configured to WEEKS, it provides special retention for the first snapshot of each week. The retention period is determined by TimeUnit and TimeInterval. The range of values are:
        # - WEEKS
        # - MONTHS
        # - YEARS"
        self.special_period_unit = special_period_unit
        # Retention Time Value. The range of values is greater than 1.
        self.time_interval = time_interval
        # Retention time unit for special snapshots. The range of values:
        # 
        # - DAYS
        # 
        # - WEEKS
        self.time_unit = time_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.special_period_unit is not None:
            result['SpecialPeriodUnit'] = self.special_period_unit

        if self.time_interval is not None:
            result['TimeInterval'] = self.time_interval

        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpecialPeriodUnit') is not None:
            self.special_period_unit = m.get('SpecialPeriodUnit')

        if m.get('TimeInterval') is not None:
            self.time_interval = m.get('TimeInterval')

        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')

        return self

class UpdateEnterpriseSnapshotPolicyRequestSchedule(DaraModel):
    def __init__(
        self,
        cron_expression: str = None,
    ):
        # The time when the policy will to be scheduled. Valid values: Set the parameter in a cron expression.
        # 
        # For example, you can use `0 0 4 1/1 * ?` to specify 04:00:00 (UTC+8) on the first day of each month.
        # 
        # This parameter is required.
        self.cron_expression = cron_expression

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        return self

class UpdateEnterpriseSnapshotPolicyRequestRetainRule(DaraModel):
    def __init__(
        self,
        number: int = None,
        time_interval: int = None,
        time_unit: str = None,
    ):
        # Maximum number of retained snapshots.
        self.number = number
        # The time interval , valid value greater than 1.
        self.time_interval = time_interval
        # The unit of time, valid values:
        # 
        # - DAYS
        # - WEEKS
        self.time_unit = time_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.number is not None:
            result['Number'] = self.number

        if self.time_interval is not None:
            result['TimeInterval'] = self.time_interval

        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('TimeInterval') is not None:
            self.time_interval = m.get('TimeInterval')

        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')

        return self

class UpdateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfo(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        regions: List[main_models.UpdateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfoRegions] = None,
    ):
        # Whether cross-region replication is enabled. The range of values:
        # 
        # - true
        # 
        # - false
        self.enabled = enabled
        # Destination region information.
        self.regions = regions

    def validate(self):
        if self.regions:
            for v1 in self.regions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        result['Regions'] = []
        if self.regions is not None:
            for k1 in self.regions:
                result['Regions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        self.regions = []
        if m.get('Regions') is not None:
            for k1 in m.get('Regions'):
                temp_model = main_models.UpdateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfoRegions()
                self.regions.append(temp_model.from_map(k1))

        return self

class UpdateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfoRegions(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        retain_days: int = None,
    ):
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/354276.html) operation to query the most recent list of regions in which async replication is supported.
        self.region_id = region_id
        # Number of days to retain the destination snapshot. The range of values is greater than 1.
        self.retain_days = retain_days

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.retain_days is not None:
            result['RetainDays'] = self.retain_days

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RetainDays') is not None:
            self.retain_days = m.get('RetainDays')

        return self

