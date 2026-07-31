# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class CreateElasticityAssuranceRequest(DaraModel):
    def __init__(
        self,
        private_pool_options: main_models.CreateElasticityAssuranceRequestPrivatePoolOptions = None,
        assurance_times: str = None,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        client_token: str = None,
        description: str = None,
        instance_amount: int = None,
        instance_cpu_core_count: int = None,
        instance_type: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        period_unit: str = None,
        recurrence_rules: List[main_models.CreateElasticityAssuranceRequestRecurrenceRules] = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
        tag: List[main_models.CreateElasticityAssuranceRequestTag] = None,
        zone_id: List[str] = None,
    ):
        self.private_pool_options = private_pool_options
        # The total number of times that the elasticity assurance can be applied. Valid values: Unlimited. Currently, only the unlimited mode is supported within the service validity period.
        # 
        # Default value: Unlimited.
        self.assurance_times = assurance_times
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # - true: Auto-renewal is enabled.
        # - false: Auto-renewal is disabled.
        # 
        # Default value: false.
        self.auto_renew = auto_renew
        # The auto-renewal period. Unit: months. Valid values: 1, 2, 3, 6, 12, 24, and 36.
        # 
        # 
        # 
        # - If `PeriodUnit=Month`, the default value is 1.
        # 
        # - If `PeriodUnit=Year`, the default value is 12.
        # 
        # 
        # > This parameter is required when `AutoRenew` is set to `True`.
        self.auto_renew_period = auto_renew_period
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. The `ClientToken` value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The description of the elasticity assurance service. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        # 
        # Default value: empty.
        self.description = description
        # The total number of instances to be reserved for a single instance type.
        # 
        # Valid values: 1 to 1000.
        # 
        # >Notice: This parameter is required.
        self.instance_amount = instance_amount
        # > This parameter is deprecated.
        self.instance_cpu_core_count = instance_cpu_core_count
        # The instance type. Currently, you can configure an elasticity assurance service for only one instance type.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The purchase duration. The unit of the duration is determined by the `PeriodUnit` parameter. Valid values:
        # 
        # - If `PeriodUnit` is set to `Month`: 1, 2, 3, 4, 5, 6, 7, 8, and 9.
        # - If `PeriodUnit` is set to `Year`: 1, 2, 3, 4, and 5.
        # - If `PeriodUnit` is set to `Day`: 1 to 365.
        # 
        # Default value: 1.
        self.period = period
        # The unit of the purchase duration. Valid values:
        # 
        # - Month: month.
        # - Year: year.
        # - Day: day.
        #   > When `PeriodUnit` is set to `Day`, you must also specify RecurrenceRules to create a time-sharing elasticity assurance.
        # 
        # Default value: Year.
        self.period_unit = period_unit
        # The recurrence rules for the time-sharing elasticity assurance.
        self.recurrence_rules = recurrence_rules
        # The region ID of the elasticity assurance service. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the elasticity assurance service belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The effective period start time of the elasticity assurance service. By default, the service takes effect when the operation is invoked. Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC. For more information, see [ISO 8601](https://help.aliyun.com/document_detail/25696.html).
        self.start_time = start_time
        # The tags of the elasticity assurance service.
        self.tag = tag
        # The zone ID within the region of the elasticity assurance service. Currently, you can create an elasticity assurance service in only one zone.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        if self.private_pool_options:
            self.private_pool_options.validate()
        if self.recurrence_rules:
            for v1 in self.recurrence_rules:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()

        if self.assurance_times is not None:
            result['AssuranceTimes'] = self.assurance_times

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_amount is not None:
            result['InstanceAmount'] = self.instance_amount

        if self.instance_cpu_core_count is not None:
            result['InstanceCpuCoreCount'] = self.instance_cpu_core_count

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        result['RecurrenceRules'] = []
        if self.recurrence_rules is not None:
            for k1 in self.recurrence_rules:
                result['RecurrenceRules'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivatePoolOptions') is not None:
            temp_model = main_models.CreateElasticityAssuranceRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m.get('PrivatePoolOptions'))

        if m.get('AssuranceTimes') is not None:
            self.assurance_times = m.get('AssuranceTimes')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceAmount') is not None:
            self.instance_amount = m.get('InstanceAmount')

        if m.get('InstanceCpuCoreCount') is not None:
            self.instance_cpu_core_count = m.get('InstanceCpuCoreCount')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        self.recurrence_rules = []
        if m.get('RecurrenceRules') is not None:
            for k1 in m.get('RecurrenceRules'):
                temp_model = main_models.CreateElasticityAssuranceRequestRecurrenceRules()
                self.recurrence_rules.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateElasticityAssuranceRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateElasticityAssuranceRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the elasticity assurance service. Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot start with `aliyun` or `acs:` or contain `http://` or `https://`.
        self.key = key
        # The tag value of the elasticity assurance service. Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot start with `acs:` or contain `http://` or `https://`.
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

class CreateElasticityAssuranceRequestRecurrenceRules(DaraModel):
    def __init__(
        self,
        end_hour: int = None,
        recurrence_type: str = None,
        recurrence_value: str = None,
        start_hour: int = None,
    ):
        # The end time of the time-sharing assurance. The value must be on the hour.
        self.end_hour = end_hour
        # The type of the recurrence rule. Valid values:
        # - Daily: daily recurrence.
        # - Weekly: weekly recurrence.
        # - Monthly: monthly recurrence.
        # 
        # > You must specify both `RecurrenceType` and `RecurrenceValue`.
        self.recurrence_type = recurrence_type
        # The value of the recurrence rule.
        # 
        # - If `RecurrenceType` is set to `Daily`, you can specify only one value. Valid values: 1 to 31. The value specifies the interval in days between recurrences.
        # - If `RecurrenceType` is set to `Weekly`, you can specify multiple values separated by commas (,). The values for Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, and Saturday are 0, 1, 2, 3, 4, 5, and 6. For example, `1,2` specifies Monday and Tuesday.
        # - If `RecurrenceType` is set to `Monthly`, the format is `A-B`. Valid values of A and B: 1 to 31. B must be greater than or equal to A. For example, `1-5` specifies the 1st to 5th day of each month.
        # 
        # > You must specify both `RecurrenceType` and `RecurrenceValue`.
        self.recurrence_value = recurrence_value
        # The effective period start hour of the time-sharing assurance. The value must be on the hour.
        # 
        # > You must specify both `StartHour` and `EndHour`, and the difference between them must be at least 4 hours.
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

class CreateElasticityAssuranceRequestPrivatePoolOptions(DaraModel):
    def __init__(
        self,
        match_criteria: str = None,
        name: str = None,
    ):
        # The match mode of the elasticity assurance service. Valid values:
        # 
        # - Open: open mode. The system automatically matches the capacity of open private pools when instances are started. If no matching private pool capacity is available, public pool resources are used to start the instances.
        # - Target: targeted mode. Instances are started by using the capacity of the specified private pool. If the specified private pool capacity is unavailable, the instances fail to start.
        # 
        # Default value: Open.
        self.match_criteria = match_criteria
        # The name of the elasticity assurance service. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with `http://` or `https://`. The name can contain digits, colons (:), underscores (_), and hyphens (-).
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.match_criteria is not None:
            result['MatchCriteria'] = self.match_criteria

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchCriteria') is not None:
            self.match_criteria = m.get('MatchCriteria')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

