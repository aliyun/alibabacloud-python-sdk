# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ebs20210730 import models as main_models
from darabonba.model import DaraModel

class DescribeEnterpriseSnapshotPolicyResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        policies: List[main_models.DescribeEnterpriseSnapshotPolicyResponseBodyPolicies] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The pagination token (Token) returned for the next query.
        self.next_token = next_token
        # The page number for paged queries.
        self.page_number = page_number
        # The number of entries per page for paged queries.
        self.page_size = page_size
        # The list of policies.
        self.policies = policies
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
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
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Policies'] = []
        if self.policies is not None:
            for k1 in self.policies:
                result['Policies'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.policies = []
        if m.get('Policies') is not None:
            for k1 in m.get('Policies'):
                temp_model = main_models.DescribeEnterpriseSnapshotPolicyResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeEnterpriseSnapshotPolicyResponseBodyPolicies(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        cross_region_copy_info: main_models.DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesCrossRegionCopyInfo = None,
        desc: str = None,
        disk_ids: List[str] = None,
        managed_for_ecs: bool = None,
        name: str = None,
        policy_id: str = None,
        resource_group_id: str = None,
        retain_rule: main_models.DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesRetainRule = None,
        schedule: main_models.DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesSchedule = None,
        special_retain_rules: main_models.DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesSpecialRetainRules = None,
        state: str = None,
        storage_rule: main_models.DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesStorageRule = None,
        tags: List[main_models.DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesTags] = None,
        target_count: int = None,
        target_type: str = None,
    ):
        # The creation time in UTC ISO 8601 format.
        self.create_time = create_time
        # The snapshot cross-region copy information.
        self.cross_region_copy_info = cross_region_copy_info
        # The snapshot policy description.
        self.desc = desc
        # The list of bound cloud disk IDs.
        self.disk_ids = disk_ids
        # The snapshot managed status.
        self.managed_for_ecs = managed_for_ecs
        # The snapshot policy name.
        self.name = name
        # The snapshot policy ID.
        self.policy_id = policy_id
        # the resource group
        self.resource_group_id = resource_group_id
        # The snapshot policy retention rule.
        self.retain_rule = retain_rule
        # The snapshot policy schedule rule.
        self.schedule = schedule
        # The special retention rules for the snapshot policy.
        self.special_retain_rules = special_retain_rules
        # The status. Valid values:
        # 
        # - DISABLED
        # - ENABLED
        self.state = state
        # The snapshot policy storage rule.
        self.storage_rule = storage_rule
        # the pair tags
        self.tags = tags
        # The number of bound targets.
        self.target_count = target_count
        # The type. Valid values:
        # 
        # - DISK
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
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cross_region_copy_info is not None:
            result['CrossRegionCopyInfo'] = self.cross_region_copy_info.to_map()

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.disk_ids is not None:
            result['DiskIds'] = self.disk_ids

        if self.managed_for_ecs is not None:
            result['ManagedForEcs'] = self.managed_for_ecs

        if self.name is not None:
            result['Name'] = self.name

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

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

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.target_count is not None:
            result['TargetCount'] = self.target_count

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CrossRegionCopyInfo') is not None:
            temp_model = main_models.DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesCrossRegionCopyInfo()
            self.cross_region_copy_info = temp_model.from_map(m.get('CrossRegionCopyInfo'))

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('DiskIds') is not None:
            self.disk_ids = m.get('DiskIds')

        if m.get('ManagedForEcs') is not None:
            self.managed_for_ecs = m.get('ManagedForEcs')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RetainRule') is not None:
            temp_model = main_models.DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesRetainRule()
            self.retain_rule = temp_model.from_map(m.get('RetainRule'))

        if m.get('Schedule') is not None:
            temp_model = main_models.DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesSchedule()
            self.schedule = temp_model.from_map(m.get('Schedule'))

        if m.get('SpecialRetainRules') is not None:
            temp_model = main_models.DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesSpecialRetainRules()
            self.special_retain_rules = temp_model.from_map(m.get('SpecialRetainRules'))

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('StorageRule') is not None:
            temp_model = main_models.DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesStorageRule()
            self.storage_rule = temp_model.from_map(m.get('StorageRule'))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TargetCount') is not None:
            self.target_count = m.get('TargetCount')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

class DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key of the resource.
        self.tag_key = tag_key
        # The tag value of the resource.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesStorageRule(DaraModel):
    def __init__(
        self,
        enable_immediate_access: bool = None,
    ):
        # Indicates whether instant access is enabled for snapshots.
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

class DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesSpecialRetainRules(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        rules: List[main_models.DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesSpecialRetainRulesRules] = None,
    ):
        # Indicates whether special retention is enabled.
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
                temp_model = main_models.DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesSpecialRetainRulesRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesSpecialRetainRulesRules(DaraModel):
    def __init__(
        self,
        special_period_unit: str = None,
        time_interval: int = None,
        time_unit: str = None,
    ):
        # The special period unit.
        self.special_period_unit = special_period_unit
        # The time interval of the retention rule. The unit is specified by the TimeUnit parameter. The value must be greater than 1.
        self.time_interval = time_interval
        # The retention time unit.
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

class DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesSchedule(DaraModel):
    def __init__(
        self,
        cron_expression: str = None,
    ):
        # The cron expression.
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

class DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesRetainRule(DaraModel):
    def __init__(
        self,
        number: int = None,
        time_interval: int = None,
        time_unit: str = None,
    ):
        # The retention count.
        self.number = number
        # The time interval of the retention rule. The unit is specified by the TimeUnit parameter. The value must be greater than 1.
        self.time_interval = time_interval
        # The retention time unit.
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

class DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesCrossRegionCopyInfo(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        regions: List[main_models.DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesCrossRegionCopyInfoRegions] = None,
    ):
        # Indicates whether cross-region copy is enabled.
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
                temp_model = main_models.DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesCrossRegionCopyInfoRegions()
                self.regions.append(temp_model.from_map(k1))

        return self

class DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesCrossRegionCopyInfoRegions(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        retain_days: int = None,
    ):
        # The snapshot copy destination region.
        self.region_id = region_id
        # The number of days to retain snapshots at the destination region.
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

