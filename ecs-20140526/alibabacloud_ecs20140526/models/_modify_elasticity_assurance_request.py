# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class ModifyElasticityAssuranceRequest(DaraModel):
    def __init__(
        self,
        private_pool_options: main_models.ModifyElasticityAssuranceRequestPrivatePoolOptions = None,
        client_token: str = None,
        description: str = None,
        instance_amount: int = None,
        owner_account: str = None,
        owner_id: int = None,
        recurrence_rules: List[main_models.ModifyElasticityAssuranceRequestRecurrenceRules] = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.private_pool_options = private_pool_options
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The description of the elasticity assurance. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The total number of instances to be reserved by the elasticity assurance. Valid values: number of used instances to 1000. This parameter cannot be modified together with other parameters.
        self.instance_amount = instance_amount
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The list of recurrence rules for the time-sharing elasticity assurance.
        self.recurrence_rules = recurrence_rules
        # The region ID of the elasticity assurance. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.private_pool_options:
            self.private_pool_options.validate()
        if self.recurrence_rules:
            for v1 in self.recurrence_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_amount is not None:
            result['InstanceAmount'] = self.instance_amount

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        result['RecurrenceRules'] = []
        if self.recurrence_rules is not None:
            for k1 in self.recurrence_rules:
                result['RecurrenceRules'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivatePoolOptions') is not None:
            temp_model = main_models.ModifyElasticityAssuranceRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m.get('PrivatePoolOptions'))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceAmount') is not None:
            self.instance_amount = m.get('InstanceAmount')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        self.recurrence_rules = []
        if m.get('RecurrenceRules') is not None:
            for k1 in m.get('RecurrenceRules'):
                temp_model = main_models.ModifyElasticityAssuranceRequestRecurrenceRules()
                self.recurrence_rules.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

class ModifyElasticityAssuranceRequestRecurrenceRules(DaraModel):
    def __init__(
        self,
        end_hour: int = None,
        recurrence_type: str = None,
        recurrence_value: str = None,
        start_hour: int = None,
    ):
        # The end time of the time-sharing assurance. The value must be on the hour.
        self.end_hour = end_hour
        # The policy type of the recurrence rule. Valid values:
        # - Daily: repeats on a daily basis.
        # - Weekly: repeats on a weekly basis.
        # - Monthly: repeats on a monthly basis.
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
        # The effective period start time of the time-sharing assurance. The value must be on the hour.
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

class ModifyElasticityAssuranceRequestPrivatePoolOptions(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # The ID of the elasticity assurance.
        # 
        # This parameter is required.
        self.id = id
        # The name of the elasticity assurance. The name must be 2 to 128 characters in length. It must start with a letter or a Chinese character and cannot start with http:// or https://. The name can contain digits, colons (:), underscores (_), or hyphens (-).
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

