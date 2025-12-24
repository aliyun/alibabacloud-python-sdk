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
        # The total number of times that the elasticity assurance can be used. Set the value to Unlimited. This value specifies that the elasticity assurance can be used for an unlimited number of times within its validity period.
        # 
        # Default value: Unlimited.
        self.assurance_times = assurance_times
        # Specifies whether to enable auto-renewal for the elasticity assurance. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.auto_renew = auto_renew
        # The auto-renewal period. Unit: month. Valid values: 1, 2, 3, 6, 12, 24, and 36.
        # 
        # *   Default value when `PeriodUnit` is set to Month: 1.
        # *   Default value when `PeriodUnit` is set to Year: 12.
        # 
        # >  If you set `AutoRenew` to `true`, you must specify this parameter.
        self.auto_renew_period = auto_renew_period
        # The client token that you want to use to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The `token` can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The description of the elasticity assurance. The description must be 2 to 256 characters in length. It cannot start with `http://` or `https://`.
        # 
        # This parameter is empty by default.
        self.description = description
        # The total number of instances of an instance type for which you want to reserve capacity.
        # 
        # Valid values: 1 to 1000.
        # 
        # >  You must specify this parameter.
        self.instance_amount = instance_amount
        # > This parameter is no longer used.
        self.instance_cpu_core_count = instance_cpu_core_count
        # The instance type. An elasticity assurance can be created to reserve the capacity of a single instance type.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The validity period of the elasticity assurance. The unit of the validity period is determined by the value of `PeriodUnit`. Specifies whether to check the image used by the instance supports hot migration. Valid values:
        # 
        # *   When the value of `PeriodUnit` is `Month`, the valid values are 1, 2, 3, 4, 5, 6, 7, 8, and 9.
        # *   When the value of `PeriodUnit` is `Year`, the valid values are 1, 2, 3, 4, and 5.
        # *   When the value of `PeriodUnit` is `Day`, the valid values are 1 to 365.
        # 
        # Default value: 1
        self.period = period
        # The unit of the validity period of the elasticity assurance. Valid values:
        # 
        # *   Month
        # 
        # *   Year
        # 
        # *   Day
        # 
        #     **
        # 
        #     **Note** If you set `PeriodUnit` to `Day`, you must specify RecurrenceRules to create a time-segmented elasticity assurance.
        # 
        # Default value: Year.
        self.period_unit = period_unit
        # The assurance schedules based on which the capacity reservation takes effect.
        # 
        # >  Time-segmented elasticity assurances are available only in specific regions and to specific users. To use time-segmented elasticity assurances, [submit a ticket](https://smartservice.console.aliyun.com/service/create-ticket-intl).
        self.recurrence_rules = recurrence_rules
        # The ID of the region in which to create the elasticity assurance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which to assign the elasticity assurance.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The time when the elasticity assurance takes effect. The default value is the time when the CreateElasticityAssurance operation is called to create the elasticity assurance. Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC. For more information, see [ISO 8601](https://help.aliyun.com/document_detail/25696.html).
        self.start_time = start_time
        # The tags to add to the elasticity assurance.
        self.tag = tag
        # The ID of the zone in which to create the elasticity assurance. An elasticity assurance can be used to reserve resources within a single zone.
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
        # The key of tag N to add to the elasticity assurance. Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        self.key = key
        # The value of tag N to add to the elasticity assurance. Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot start with `acs:`. The tag value cannot contain `http://` or `https://`.
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
        # The end time of the assurance period for the capacity reservation. Specify an on-the-hour point in time.
        self.end_hour = end_hour
        # The type of the assurance schedule. Valid values:
        # 
        # *   Daily
        # *   Weekly
        # *   Monthly
        # 
        # >  You must specify both `RecurrenceType` and `RecurrenceValue`.
        self.recurrence_type = recurrence_type
        # The days of the week or month on which the capacity reservation takes effect or the interval, in number of days, at which the capacity reservation takes effect.
        # 
        # *   If you set `RecurrenceType` to `Daily`, you can specify only one value for this parameter. Valid values: 1 to 31. The value specifies that the capacity reservation takes effect every few days.
        # *   If you set `RecurrenceType` to `Weekly`, you can specify multiple values for this parameter. Separate the values with commas (,). Valid values: 0, 1, 2, 3, 4, 5, and 6, which specify Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, and Saturday, respectively. Example: `1,2`, which specifies that the capacity reservation takes effect on Monday and Tuesday.
        # *   If you set `RecurrenceType` to `Monthly`, you can specify two values in the `A-B` format for this parameter. Valid values of A and B: 1 to 31. B must be greater than or equal to A. For example, `1-5` indicates that the execution is repeated from the 1st to 5th of each month.
        # 
        # > You must specify both `RecurrenceType` and `RecurrenceValue`.
        self.recurrence_value = recurrence_value
        # The start time of the assurance period for the capacity reservation. Specify an on-the-hour point in time.
        # 
        # >  You must specify both `StartHour` and `EndHour`. EndHour must be at least four hours later than StartHour.
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
        # The type of the private pool with which you want to associate the elasticity assurance. Valid values:
        # 
        # *   Open: open private pool. If you use the elasticity assurance to create ECS instances, the open private pool that is associated with the elasticity assurance is automatically matched. If no capacity is available in the open private pool, resources in the public pool are automatically used to create the ECS instances.
        # *   Target: targeted private pool. If you use the elasticity assurance to create ECS instances, the specified private pool that is associated with the elasticity assurance is automatically matched. If no capacity is available in the private pool, the ECS instances fail to be created.
        # 
        # Default value: Open.
        self.match_criteria = match_criteria
        # The name of the elasticity assurance. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with `http://` or `https://`. It can contain letters, digits, colons (:), underscores (_), and hyphens (-).
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

