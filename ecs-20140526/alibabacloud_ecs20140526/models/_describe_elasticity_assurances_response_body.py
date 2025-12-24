# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeElasticityAssurancesResponseBody(DaraModel):
    def __init__(
        self,
        elasticity_assurance_set: main_models.DescribeElasticityAssurancesResponseBodyElasticityAssuranceSet = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the elasticity assurances.
        self.elasticity_assurance_set = elasticity_assurance_set
        # The maximum number of entries returned per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.elasticity_assurance_set:
            self.elasticity_assurance_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elasticity_assurance_set is not None:
            result['ElasticityAssuranceSet'] = self.elasticity_assurance_set.to_map()

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticityAssuranceSet') is not None:
            temp_model = main_models.DescribeElasticityAssurancesResponseBodyElasticityAssuranceSet()
            self.elasticity_assurance_set = temp_model.from_map(m.get('ElasticityAssuranceSet'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeElasticityAssurancesResponseBodyElasticityAssuranceSet(DaraModel):
    def __init__(
        self,
        elasticity_assurance_item: List[main_models.DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItem] = None,
    ):
        self.elasticity_assurance_item = elasticity_assurance_item

    def validate(self):
        if self.elasticity_assurance_item:
            for v1 in self.elasticity_assurance_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ElasticityAssuranceItem'] = []
        if self.elasticity_assurance_item is not None:
            for k1 in self.elasticity_assurance_item:
                result['ElasticityAssuranceItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elasticity_assurance_item = []
        if m.get('ElasticityAssuranceItem') is not None:
            for k1 in m.get('ElasticityAssuranceItem'):
                temp_model = main_models.DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItem()
                self.elasticity_assurance_item.append(temp_model.from_map(k1))

        return self

class DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItem(DaraModel):
    def __init__(
        self,
        allocated_resources: main_models.DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItemAllocatedResources = None,
        description: str = None,
        elasticity_assurance_owner_id: str = None,
        end_time: str = None,
        instance_charge_type: str = None,
        latest_start_time: str = None,
        package_type: str = None,
        private_pool_options_id: str = None,
        private_pool_options_match_criteria: str = None,
        private_pool_options_name: str = None,
        recurrence_rules: main_models.DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItemRecurrenceRules = None,
        region_id: str = None,
        resource_group_id: str = None,
        start_time: str = None,
        start_time_type: str = None,
        status: str = None,
        tags: main_models.DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItemTags = None,
        total_assurance_times: str = None,
        used_assurance_times: int = None,
    ):
        # Details of the allocated resources.
        self.allocated_resources = allocated_resources
        # The description of the elasticity assurance.
        self.description = description
        # >  This parameter is not publicly available.
        self.elasticity_assurance_owner_id = elasticity_assurance_owner_id
        # The time when the elasticity assurance expires.
        self.end_time = end_time
        # The billing method of the instance. The value can be only PostPaid. Only pay-as-you-go instances can be created by using elasticity assurances.
        self.instance_charge_type = instance_charge_type
        # > This parameter is not publicly available.
        self.latest_start_time = latest_start_time
        # The type of the elasticity assurance. Valid values:
        # 
        # *   ElasticityAssurance: the general-purpose elasticity assurance.
        # *   TimeDivisionElasticityAssurance: the time-segmented assurance of the elasticity assurance.
        self.package_type = package_type
        # The ID of the elasticity assurance.
        self.private_pool_options_id = private_pool_options_id
        # The type of the private pool associated with the elasticity assurance. Valid values:
        # 
        # *   Open: open private pool
        # *   Target: specific private pool
        self.private_pool_options_match_criteria = private_pool_options_match_criteria
        # The name of the elasticity assurance.
        self.private_pool_options_name = private_pool_options_name
        # The recurrence rules of the time-segmented assurances.
        self.recurrence_rules = recurrence_rules
        # The region ID of the elasticity assurance.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The time when the elasticity assurance takes effect.
        self.start_time = start_time
        # Indicates when the elasticity assurance takes effect. Valid values:
        # 
        # *   Now: The elasticity assurance takes effect immediately after it is created.
        # *   Later: The elasticity assurance takes effect at a specified time.
        self.start_time_type = start_time_type
        # The status of the elasticity assurance. Valid values:
        # 
        # *   Preparing
        # *   Prepared
        # *   Active
        # *   Released
        self.status = status
        # The tags of the elasticity assurance.
        self.tags = tags
        # The total number of times that the elasticity assurance is applied.
        self.total_assurance_times = total_assurance_times
        # > This parameter is not publicly available.
        self.used_assurance_times = used_assurance_times

    def validate(self):
        if self.allocated_resources:
            self.allocated_resources.validate()
        if self.recurrence_rules:
            self.recurrence_rules.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocated_resources is not None:
            result['AllocatedResources'] = self.allocated_resources.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.elasticity_assurance_owner_id is not None:
            result['ElasticityAssuranceOwnerId'] = self.elasticity_assurance_owner_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.latest_start_time is not None:
            result['LatestStartTime'] = self.latest_start_time

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.private_pool_options_id is not None:
            result['PrivatePoolOptionsId'] = self.private_pool_options_id

        if self.private_pool_options_match_criteria is not None:
            result['PrivatePoolOptionsMatchCriteria'] = self.private_pool_options_match_criteria

        if self.private_pool_options_name is not None:
            result['PrivatePoolOptionsName'] = self.private_pool_options_name

        if self.recurrence_rules is not None:
            result['RecurrenceRules'] = self.recurrence_rules.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.start_time_type is not None:
            result['StartTimeType'] = self.start_time_type

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.total_assurance_times is not None:
            result['TotalAssuranceTimes'] = self.total_assurance_times

        if self.used_assurance_times is not None:
            result['UsedAssuranceTimes'] = self.used_assurance_times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocatedResources') is not None:
            temp_model = main_models.DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItemAllocatedResources()
            self.allocated_resources = temp_model.from_map(m.get('AllocatedResources'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ElasticityAssuranceOwnerId') is not None:
            self.elasticity_assurance_owner_id = m.get('ElasticityAssuranceOwnerId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('LatestStartTime') is not None:
            self.latest_start_time = m.get('LatestStartTime')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('PrivatePoolOptionsId') is not None:
            self.private_pool_options_id = m.get('PrivatePoolOptionsId')

        if m.get('PrivatePoolOptionsMatchCriteria') is not None:
            self.private_pool_options_match_criteria = m.get('PrivatePoolOptionsMatchCriteria')

        if m.get('PrivatePoolOptionsName') is not None:
            self.private_pool_options_name = m.get('PrivatePoolOptionsName')

        if m.get('RecurrenceRules') is not None:
            temp_model = main_models.DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItemRecurrenceRules()
            self.recurrence_rules = temp_model.from_map(m.get('RecurrenceRules'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StartTimeType') is not None:
            self.start_time_type = m.get('StartTimeType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItemTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('TotalAssuranceTimes') is not None:
            self.total_assurance_times = m.get('TotalAssuranceTimes')

        if m.get('UsedAssuranceTimes') is not None:
            self.used_assurance_times = m.get('UsedAssuranceTimes')

        return self

class DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItemTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItemTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItemTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItemTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
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

class DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItemRecurrenceRules(DaraModel):
    def __init__(
        self,
        recurrence_rule: List[main_models.DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItemRecurrenceRulesRecurrenceRule] = None,
    ):
        self.recurrence_rule = recurrence_rule

    def validate(self):
        if self.recurrence_rule:
            for v1 in self.recurrence_rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RecurrenceRule'] = []
        if self.recurrence_rule is not None:
            for k1 in self.recurrence_rule:
                result['RecurrenceRule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.recurrence_rule = []
        if m.get('RecurrenceRule') is not None:
            for k1 in m.get('RecurrenceRule'):
                temp_model = main_models.DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItemRecurrenceRulesRecurrenceRule()
                self.recurrence_rule.append(temp_model.from_map(k1))

        return self

class DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItemRecurrenceRulesRecurrenceRule(DaraModel):
    def __init__(
        self,
        end_hour: int = None,
        recurrence_type: str = None,
        recurrence_value: str = None,
        start_hour: int = None,
    ):
        # The time when the time-segmented assurance ends.
        self.end_hour = end_hour
        # The type of the recurrence rule. Valid values:
        # 
        # *   Daily
        # *   Weekly
        # *   Monthly
        self.recurrence_type = recurrence_type
        # The recurrence value of the time-segmented assurance. Valid values:
        # 
        # *   If you set `RecurrenceType` to `Daily`, you can set RecurrenceValue to only one value. Valid values: 1 to 31. The time-segmented assurance is performed every few days.
        # *   If you set `RecurrenceType` to `Weekly`, you can set RecurrenceValue to one or more values. Separate the values with commas (,). The values that correspond to Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, and Saturday are 0, 1, 2, 3, 4, 5, and 6. For example, `1,2` indicates that the time-segmented assurance is performed on Monday and Tuesday of every week.
        # *   If you set `RecurrenceType` to `Monthly`, you can set RecurrenceValue to two values in the `A-B` format. Valid values of A and B: 1 to 31. B must be greater than or equal to A. For example, `1-5` indicates that the time-segmented assurance is performed from the 1st to the 5th of each month.
        self.recurrence_value = recurrence_value
        # The time when the time-segmented assurance takes effect.
        self.start_hour = start_hour

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_hour is not None:
            result['EndHour'] = self.end_hour

        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type

        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value

        if self.start_hour is not None:
            result['StartHour'] = self.start_hour

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndHour') is not None:
            self.end_hour = m.get('EndHour')

        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')

        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')

        if m.get('StartHour') is not None:
            self.start_hour = m.get('StartHour')

        return self

class DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItemAllocatedResources(DaraModel):
    def __init__(
        self,
        allocated_resource: List[main_models.DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItemAllocatedResourcesAllocatedResource] = None,
    ):
        self.allocated_resource = allocated_resource

    def validate(self):
        if self.allocated_resource:
            for v1 in self.allocated_resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AllocatedResource'] = []
        if self.allocated_resource is not None:
            for k1 in self.allocated_resource:
                result['AllocatedResource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.allocated_resource = []
        if m.get('AllocatedResource') is not None:
            for k1 in m.get('AllocatedResource'):
                temp_model = main_models.DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItemAllocatedResourcesAllocatedResource()
                self.allocated_resource.append(temp_model.from_map(k1))

        return self

class DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItemAllocatedResourcesAllocatedResource(DaraModel):
    def __init__(
        self,
        available_amount: int = None,
        elasticity_assurance_usages: main_models.DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItemAllocatedResourcesAllocatedResourceElasticityAssuranceUsages = None,
        instance_type: str = None,
        total_amount: int = None,
        used_amount: int = None,
        zone_id: str = None,
    ):
        # >  This parameter is not publicly available.
        self.available_amount = available_amount
        # >  This parameter is not publicly available.
        self.elasticity_assurance_usages = elasticity_assurance_usages
        # The instance type.
        self.instance_type = instance_type
        # The total number of instances for which capacity of an instance type is reserved.
        self.total_amount = total_amount
        # The number of instances that have used the elasticity assurance.
        self.used_amount = used_amount
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.elasticity_assurance_usages:
            self.elasticity_assurance_usages.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_amount is not None:
            result['AvailableAmount'] = self.available_amount

        if self.elasticity_assurance_usages is not None:
            result['ElasticityAssuranceUsages'] = self.elasticity_assurance_usages.to_map()

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.total_amount is not None:
            result['TotalAmount'] = self.total_amount

        if self.used_amount is not None:
            result['UsedAmount'] = self.used_amount

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableAmount') is not None:
            self.available_amount = m.get('AvailableAmount')

        if m.get('ElasticityAssuranceUsages') is not None:
            temp_model = main_models.DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItemAllocatedResourcesAllocatedResourceElasticityAssuranceUsages()
            self.elasticity_assurance_usages = temp_model.from_map(m.get('ElasticityAssuranceUsages'))

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('TotalAmount') is not None:
            self.total_amount = m.get('TotalAmount')

        if m.get('UsedAmount') is not None:
            self.used_amount = m.get('UsedAmount')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

class DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItemAllocatedResourcesAllocatedResourceElasticityAssuranceUsages(DaraModel):
    def __init__(
        self,
        elasticity_assurance_usage: List[main_models.DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItemAllocatedResourcesAllocatedResourceElasticityAssuranceUsagesElasticityAssuranceUsage] = None,
    ):
        self.elasticity_assurance_usage = elasticity_assurance_usage

    def validate(self):
        if self.elasticity_assurance_usage:
            for v1 in self.elasticity_assurance_usage:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ElasticityAssuranceUsage'] = []
        if self.elasticity_assurance_usage is not None:
            for k1 in self.elasticity_assurance_usage:
                result['ElasticityAssuranceUsage'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elasticity_assurance_usage = []
        if m.get('ElasticityAssuranceUsage') is not None:
            for k1 in m.get('ElasticityAssuranceUsage'):
                temp_model = main_models.DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItemAllocatedResourcesAllocatedResourceElasticityAssuranceUsagesElasticityAssuranceUsage()
                self.elasticity_assurance_usage.append(temp_model.from_map(k1))

        return self

class DescribeElasticityAssurancesResponseBodyElasticityAssuranceSetElasticityAssuranceItemAllocatedResourcesAllocatedResourceElasticityAssuranceUsagesElasticityAssuranceUsage(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        service_name: str = None,
        used_amount: int = None,
    ):
        # >  This parameter is not publicly available.
        self.account_id = account_id
        # >  This parameter is not publicly available.
        self.service_name = service_name
        # >  This parameter is not publicly available.
        self.used_amount = used_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.used_amount is not None:
            result['UsedAmount'] = self.used_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('UsedAmount') is not None:
            self.used_amount = m.get('UsedAmount')

        return self

