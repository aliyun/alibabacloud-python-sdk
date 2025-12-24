# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class PurchaseReservedInstancesOfferingRequest(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        client_token: str = None,
        description: str = None,
        instance_amount: int = None,
        instance_type: str = None,
        offering_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        period_unit: str = None,
        platform: str = None,
        region_id: str = None,
        reserved_instance_name: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scope: str = None,
        start_time: str = None,
        tag: List[main_models.PurchaseReservedInstancesOfferingRequestTag] = None,
        zone_id: str = None,
    ):
        # Specifies whether to enable auto-renewal for the reserved instance. Valid values:
        # 
        # *   true
        # *   false (default)
        self.auto_renew = auto_renew
        # The auto-renewal term of the reserved instance. Unit: months. This parameter takes effect only when AutoRenew is set to true.
        # 
        # Valid values: 12 and 36.
        # 
        # Default value when PeriodUnit is set to Year: 12.
        self.auto_renew_period = auto_renew_period
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The **ClientToken** value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The description of the reserved instance. The description can be 2 to 256 characters in length and cannot start with [http:// or https://](http://https://。).
        # 
        # This parameter is left empty by default.
        self.description = description
        # The number of pay-as-you-go instances of the same instance type that the reserved instance can match. Valid values: 1 to 50.
        # 
        # Default value: 1.
        self.instance_amount = instance_amount
        # The instance type that the reserved instance can match.
        # 
        # >  The instance types that support reserved instances are subject to updates. For more information, see [Reserved instance overview](~~100370#3c1b682051vt4~~).
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The payment option of the reserved instance. Valid values:
        # 
        # *   No Upfront
        # *   Partial Upfront
        # *   All Upfront
        # 
        # Default value: All Upfront.
        self.offering_type = offering_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The validity period of the reserved instance.
        # 
        # Valid values: 1 and 3.
        # 
        # Default value: 1.
        self.period = period
        # The unit of the validity period of the reserved instance.
        # 
        # Valid value: Year.
        # 
        # Default value: Year.
        self.period_unit = period_unit
        # The operating system of the image used by the instance. Valid values:
        # 
        # *   Windows: Windows Server operating system
        # *   Linux: Linux and UNIX-like operating system
        # 
        # Default value: Linux.
        self.platform = platform
        # The ID of the region in which to purchase a reserved instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the reserved instance. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with http:// or https://. The name can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.reserved_instance_name = reserved_instance_name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The scope of reserved instance N. Valid values:
        # 
        # *   Region: regional
        # *   Zone: zonal
        # 
        # Default value: Region.
        self.scope = scope
        # The time when you want the reserved instance to take effect. Specify the time in the [ISO 8601 standard](https://help.aliyun.com/document_detail/25696.html) in the `yyyy-MM-ddTHHZ` format. The time must be in UTC.
        # 
        # >  If you do not specify this parameter, the reserved instance takes effect starting on the hour when the reserved instance is purchased. For example, if you purchase a reserved instance at 13:45:35 on November 1, 2024, the reserved instance takes effect starting 13:00:00 on November 1, 2024.
        self.start_time = start_time
        # The tags to add to the reserved instance. You can add up to 20 tags.
        self.tag = tag
        # The ID of the zone in which to purchase the reserved instance. This parameter takes effect and is required only if you set `Scope` to `Zone`. You can call the [DescribeZones](https://help.aliyun.com/document_detail/25610.html) operation to query the most recent zone list.
        self.zone_id = zone_id

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

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.offering_type is not None:
            result['OfferingType'] = self.offering_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reserved_instance_name is not None:
            result['ReservedInstanceName'] = self.reserved_instance_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scope is not None:
            result['Scope'] = self.scope

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

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('OfferingType') is not None:
            self.offering_type = m.get('OfferingType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReservedInstanceName') is not None:
            self.reserved_instance_name = m.get('ReservedInstanceName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.PurchaseReservedInstancesOfferingRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class PurchaseReservedInstancesOfferingRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key to add to the reserved instance. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        self.key = key
        # The tag value to add to the reserved instance. The tag value cannot be an empty string. The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag value cannot start with `acs:` or `aliyun`.
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

