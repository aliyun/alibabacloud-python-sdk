# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ebs20210730 import models as main_models
from darabonba.model import DaraModel

class CreateEnterpriseSnapshotPolicyRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        cross_region_copy_info: main_models.CreateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfo = None,
        desc: str = None,
        name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        retain_rule: main_models.CreateEnterpriseSnapshotPolicyRequestRetainRule = None,
        schedule: main_models.CreateEnterpriseSnapshotPolicyRequestSchedule = None,
        special_retain_rules: main_models.CreateEnterpriseSnapshotPolicyRequestSpecialRetainRules = None,
        state: str = None,
        storage_rule: main_models.CreateEnterpriseSnapshotPolicyRequestStorageRule = None,
        tag: List[main_models.CreateEnterpriseSnapshotPolicyRequestTag] = None,
        target_type: str = None,
    ):
        # Ensures the idempotence of the request. Generate a parameter value from your client that is unique across different requests. ClientToken supports only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The snapshot replication information.
        self.cross_region_copy_info = cross_region_copy_info
        # The description.
        self.desc = desc
        # The Policy Name.
        # 
        # This parameter is required.
        self.name = name
        # The region ID. You can call DescribeRegions to query the regions that support asynchronous replication.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The retention rule.
        # 
        # This parameter is required.
        self.retain_rule = retain_rule
        # The schedule rule.
        # 
        # This parameter is required.
        self.schedule = schedule
        # The special retention rules.
        self.special_retain_rules = special_retain_rules
        # The status. Valid values:
        # 
        # - DISABLED
        # - ENABLED
        self.state = state
        # The advanced snapshot feature.
        self.storage_rule = storage_rule
        # The tag key-value pairs. Valid values of n: 1 to 20.
        self.tag = tag
        # The type. Valid values:
        # 
        # - DISK
        # 
        # This parameter is required.
        self.target_type = target_type

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
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

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

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CrossRegionCopyInfo') is not None:
            temp_model = main_models.CreateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfo()
            self.cross_region_copy_info = temp_model.from_map(m.get('CrossRegionCopyInfo'))

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RetainRule') is not None:
            temp_model = main_models.CreateEnterpriseSnapshotPolicyRequestRetainRule()
            self.retain_rule = temp_model.from_map(m.get('RetainRule'))

        if m.get('Schedule') is not None:
            temp_model = main_models.CreateEnterpriseSnapshotPolicyRequestSchedule()
            self.schedule = temp_model.from_map(m.get('Schedule'))

        if m.get('SpecialRetainRules') is not None:
            temp_model = main_models.CreateEnterpriseSnapshotPolicyRequestSpecialRetainRules()
            self.special_retain_rules = temp_model.from_map(m.get('SpecialRetainRules'))

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('StorageRule') is not None:
            temp_model = main_models.CreateEnterpriseSnapshotPolicyRequestStorageRule()
            self.storage_rule = temp_model.from_map(m.get('StorageRule'))

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateEnterpriseSnapshotPolicyRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

class CreateEnterpriseSnapshotPolicyRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource.
        # 
        # This parameter is required.
        self.key = key
        # The tag value of the resource.
        # 
        # This parameter is required.
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

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEnterpriseSnapshotPolicyRequestStorageRule(DaraModel):
    def __init__(
        self,
        enable_immediate_access: bool = None,
    ):
        # Specifies whether to enable instant access for snapshots. Valid values:
        # 
        # - true
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

class CreateEnterpriseSnapshotPolicyRequestSpecialRetainRules(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        rules: List[main_models.CreateEnterpriseSnapshotPolicyRequestSpecialRetainRulesRules] = None,
    ):
        # Specifies whether to enable special retention. Valid values:
        # 
        # - true
        # - false
        self.enabled = enabled
        # The list of special retention rules.
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
                temp_model = main_models.CreateEnterpriseSnapshotPolicyRequestSpecialRetainRulesRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class CreateEnterpriseSnapshotPolicyRequestSpecialRetainRulesRules(DaraModel):
    def __init__(
        self,
        special_period_unit: str = None,
        time_interval: int = None,
        time_unit: str = None,
    ):
        # The period unit for specially retained snapshots. For example, if this parameter is set to WEEKS, the first snapshot of each week is specially retained. The retention duration is determined by TimeUnit and TimeInterval. Valid values:
        # 
        # - WEEKS
        # - MONTHS
        # - YEARS
        self.special_period_unit = special_period_unit
        # The time interval of the retention rule. The unit is specified by the TimeUnit parameter. The value must be greater than 1.
        self.time_interval = time_interval
        # The unit of the retention time for special snapshots. Valid values:
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

class CreateEnterpriseSnapshotPolicyRequestSchedule(DaraModel):
    def __init__(
        self,
        cron_expression: str = None,
    ):
        # The cycle and time at which the policy is executed. Specify the value in a cron expression.
        # 
        # For example, `0 0 4 1/1 * ?` specifies that the snapshot operation is performed at 4:00 AM every day, starting from the first day of each month.
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

class CreateEnterpriseSnapshotPolicyRequestRetainRule(DaraModel):
    def __init__(
        self,
        number: int = None,
        time_interval: int = None,
        time_unit: str = None,
    ):
        # The number of snapshots to retain. Valid values: 1 to 256.
        self.number = number
        # The time interval of the retention rule. The unit is specified by the TimeUnit parameter. The value must be greater than 1.
        self.time_interval = time_interval
        # The unit of the retention time. Valid values:
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

class CreateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfo(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        regions: List[main_models.CreateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfoRegions] = None,
    ):
        # Specifies whether to enable cross-region replication. Valid values:
        # 
        # - true
        # - false
        self.enabled = enabled
        # The destination region information.
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
                temp_model = main_models.CreateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfoRegions()
                self.regions.append(temp_model.from_map(k1))

        return self

class CreateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfoRegions(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        retain_days: int = None,
    ):
        # The ID of the destination region for snapshot replication. You can invoke [DescribeDiskReplicaPairs](https://help.aliyun.com/document_detail/354206.html) to query the region information of existing asynchronous replication relationships.
        self.region_id = region_id
        # The number of days to retain snapshots in the destination region. The value must be greater than 1.
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

