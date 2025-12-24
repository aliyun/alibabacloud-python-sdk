# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class ModifyReservedInstancesRequest(DaraModel):
    def __init__(
        self,
        configuration: List[main_models.ModifyReservedInstancesRequestConfiguration] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        reserved_instance_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The configurations of the new reserved instances. You can specify up to 100 new reserved instances.
        self.configuration = configuration
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the reserved instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IDs of reserved instances that you want to modify. You can specify up to 20 reserved instance IDs.
        # 
        # This parameter is required.
        self.reserved_instance_id = reserved_instance_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.configuration:
            for v1 in self.configuration:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Configuration'] = []
        if self.configuration is not None:
            for k1 in self.configuration:
                result['Configuration'].append(k1.to_map() if k1 else None)

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reserved_instance_id is not None:
            result['ReservedInstanceId'] = self.reserved_instance_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configuration = []
        if m.get('Configuration') is not None:
            for k1 in m.get('Configuration'):
                temp_model = main_models.ModifyReservedInstancesRequestConfiguration()
                self.configuration.append(temp_model.from_map(k1))

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReservedInstanceId') is not None:
            self.reserved_instance_id = m.get('ReservedInstanceId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

class ModifyReservedInstancesRequestConfiguration(DaraModel):
    def __init__(
        self,
        instance_amount: int = None,
        instance_type: str = None,
        reserved_instance_name: str = None,
        scope: str = None,
        zone_id: str = None,
    ):
        # The number of pay-as-you-go instances of the specified instance type that the new reserved instance can match. The value of this parameter must be greater than or equal to 1.
        self.instance_amount = instance_amount
        # The instance types that the new reserved instance can match.
        # 
        # >  The supported instance types are continuously updated. For information about the instance types supported by reserved instances, see [Overview of reserved instances](~~100370#3c1b682051vt4~~).
        self.instance_type = instance_type
        # The name of the new reserved instance.
        # 
        # The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with http:// or https://. The name can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.reserved_instance_name = reserved_instance_name
        # The scope level of the new reserved instance. Valid values:
        # 
        # *   Region
        # *   Zone
        # 
        # Default value: Region.
        self.scope = scope
        # The zone ID of the new reserved instance.
        # 
        # This parameter is required when you set `Scope` to `Zone`.
        # 
        # You can call the [DescribeZones](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent zone list.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_amount is not None:
            result['InstanceAmount'] = self.instance_amount

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.reserved_instance_name is not None:
            result['ReservedInstanceName'] = self.reserved_instance_name

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceAmount') is not None:
            self.instance_amount = m.get('InstanceAmount')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('ReservedInstanceName') is not None:
            self.reserved_instance_name = m.get('ReservedInstanceName')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

