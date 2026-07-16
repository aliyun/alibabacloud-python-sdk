# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class CreateCapacityReservationRequest(DaraModel):
    def __init__(
        self,
        private_pool_options: main_models.CreateCapacityReservationRequestPrivatePoolOptions = None,
        client_token: str = None,
        description: str = None,
        end_time: str = None,
        end_time_type: str = None,
        instance_amount: int = None,
        instance_charge_type: str = None,
        instance_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        platform: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
        tag: List[main_models.CreateCapacityReservationRequestTag] = None,
        zone_id: List[str] = None,
    ):
        self.private_pool_options = private_pool_options
        # A client-generated token that ensures the request is idempotent. You can use the same token to retry a request. The `ClientToken` value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The description of the capacity reservation. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        # 
        # Default value: empty string.
        self.description = description
        # The end time of the capacity reservation. Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC. For more information, see [ISO 8601](https://help.aliyun.com/document_detail/25696.html).
        self.end_time = end_time
        # The release mode of the capacity reservation. Valid values:
        # 
        # - Limited: The capacity reservation is automatically released at a specific time. You must also specify the `EndTime` parameter.
        # 
        # - Unlimited: The capacity reservation must be released manually.
        self.end_time_type = end_time_type
        # The number of instances of the specified instance type for which to reserve capacity.
        # 
        # This parameter is required.
        self.instance_amount = instance_amount
        self.instance_charge_type = instance_charge_type
        # The instance type for which to reserve capacity. You can call [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) to view the instance types that ECS provides.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The operating system of the image used by the instance. This parameter corresponds to the `Platform` parameter of a regional reserved instance. If this platform matches the platform of a regional reserved instance, the regional reserved instance can be used to offset the costs of unused capacity in the reservation. Valid values:
        # 
        # - Windows: Windows Server operating systems.
        # 
        # - Linux: Linux and Unix-like operating systems.
        # 
        # Default value: Linux.
        # 
        # > This parameter is not yet available for use.
        self.platform = platform
        # The ID of the region in which to create the capacity reservation. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the latest list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the capacity reservation belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The time when the capacity reservation takes effect. The capacity reservation takes effect immediately after it is created.
        # 
        # > If you do not specify this parameter, the capacity reservation takes effect immediately.
        self.start_time = start_time
        # The tags to add to the capacity reservation.
        self.tag = tag
        # The ID of the zone in which you want to create the capacity reservation. A capacity reservation can reserve resources within only one zone.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        if self.private_pool_options:
            self.private_pool_options.validate()
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.end_time_type is not None:
            result['EndTimeType'] = self.end_time_type

        if self.instance_amount is not None:
            result['InstanceAmount'] = self.instance_amount

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.platform is not None:
            result['Platform'] = self.platform

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
            temp_model = main_models.CreateCapacityReservationRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m.get('PrivatePoolOptions'))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EndTimeType') is not None:
            self.end_time_type = m.get('EndTimeType')

        if m.get('InstanceAmount') is not None:
            self.instance_amount = m.get('InstanceAmount')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

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
                temp_model = main_models.CreateCapacityReservationRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateCapacityReservationRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the capacity reservation. Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the capacity reservation. Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot start with `acs:`. It cannot contain `http://` or `https://`.
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

class CreateCapacityReservationRequestPrivatePoolOptions(DaraModel):
    def __init__(
        self,
        match_criteria: str = None,
        name: str = None,
    ):
        # The type of the private pool that is generated after the capacity reservation takes effect. Valid values:
        # 
        # - Open: open mode. When you launch an instance, it is automatically matched with the capacity of an open private pool. If no suitable private pool capacity is available, the instance is launched by using public pool resources.
        # 
        # - Target: targeted mode. The instance is launched by using the capacity of a specified private pool. If the capacity is unavailable, the instance fails to launch.
        # 
        # Default value: Open.
        self.match_criteria = match_criteria
        # The name of the capacity reservation. The name must be 2 to 128 characters in length. It must start with a letter or a Chinese character and cannot start with `http://` or `https://`. It can contain digits, colons (:), underscores (_), and hyphens (-).
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

