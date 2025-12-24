# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeRecommendInstanceTypeRequest(DaraModel):
    def __init__(
        self,
        cores: int = None,
        instance_charge_type: str = None,
        instance_family_level: str = None,
        instance_type: str = None,
        instance_type_family: List[str] = None,
        io_optimized: str = None,
        max_price: float = None,
        memory: float = None,
        network_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        priority_strategy: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scene: str = None,
        spot_strategy: str = None,
        system_disk_category: str = None,
        zone_id: str = None,
        zone_match_mode: str = None,
    ):
        # The number of vCPU cores of the instance type.
        # 
        # >  If you specify both `Cores` and `Memory`, the system returns all instance types that match the values of the parameters.
        self.cores = cores
        # The billing method of the ECS instance. For more information, see [Billing overview](https://help.aliyun.com/document_detail/25398.html). Valid values:
        # 
        # *   PrePaid: subscription.
        # *   PostPaid: pay-as-you-go
        # 
        # Default value: PostPaid
        self.instance_charge_type = instance_charge_type
        # The level of the instance family. Valid values:
        # 
        # *   EntryLevel: entry level.
        # *   EnterpriseLevel: enterprise level.
        # *   CreditEntryLevel: credit-based entry level. For more information, see [Burstable instance families](https://help.aliyun.com/document_detail/59977.html).
        self.instance_family_level = instance_family_level
        # The instance type. For more information, see [Overview of instance families](https://help.aliyun.com/document_detail/25378.html) or call the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) operation to query the most recent instance type list.
        # 
        # >  If you specify `InstanceType`, you cannot specify `Cores` or `Memory`.
        self.instance_type = instance_type
        # The instance families from which the alternative instance types are selected. You can specify up to 10 instance families.
        self.instance_type_family = instance_type_family
        # Specifies whether instances of the instance type are I/O optimized. You cannot specify IoOptimized if the instance type supports only non-I/O optimized instances. Valid values:
        # 
        # *   optimized: The instances are I/O optimized.
        # *   none: The instances are non-I/O optimized.
        # 
        # Default value: optimized.
        # 
        # If you query alternative instance types for retired instance types, this parameter is set to none by default.
        self.io_optimized = io_optimized
        # The maximum hourly price for pay-as-you-go instances or spot instances.
        # 
        # >  This parameter takes effect only when `SpotStrategy` is set to `SpotWithPriceLimit`.
        self.max_price = max_price
        # The memory size of the instance type. Unit: GiB.
        # 
        # >  If you specify both `Cores` and `Memory`, the system returns all instance types that match the values of the parameters.
        self.memory = memory
        # The network type of ECS instances. Valid values:
        # 
        # *   classic
        # *   vpc
        # 
        # Default value: vpc.
        # 
        # This parameter is required.
        self.network_type = network_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The policy for recommending instance types. Valid values:
        # 
        # *   InventoryFirst: recommends instance types in descending order of resource availability.
        # *   PriceFirst: recommends the most cost-effective instance types. Recommended instance types appear based on the hourly prices of vCPUs in ascending order.
        # *   NewProductFirst: recommends the latest instance types first.
        # 
        # Default value: InventoryFirst.
        self.priority_strategy = priority_strategy
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies the scenarios in which instance types are recommended. Valid values:
        # 
        # *   UPGRADE: instance type upgrade or downgrade
        # *   CREATE: instance creation
        # 
        # Default value: CREATE.
        self.scene = scene
        # The bidding policy of the spot instance. Valid values:
        # 
        # *   NoSpot: The instance is created as a pay-as-you-go instance.
        # *   SpotWithPriceLimit: The instance is a spot instance that has a user-defined maximum hourly price.
        # *   SpotAsPriceGo: The instance is a spot instance for which the market price at the time of purchase is automatically used as the bid price. The market price can be up to the pay-as-you-go price.
        # 
        # >  If you specify `SpotStrategy`, you must set `InstanceChargeType` to `PostPaid`.
        # 
        # Default value: NoSpot.
        self.spot_strategy = spot_strategy
        # The category of the system disk. Valid values:
        # 
        # *   cloud_efficiency: ultra disk
        # *   cloud_ssd: standard SSD
        # *   cloud_essd: Enterprise SSD (ESSD)
        # *   cloud: basic disk
        # 
        # For non-I/O optimized instances, the default value is cloud.
        # 
        # For I/O optimized instances, the default value is cloud_efficiency.
        self.system_disk_category = system_disk_category
        # The zone ID. You can call the [DescribeZones](https://help.aliyun.com/document_detail/25610.html) operation to query the most recent zone list.
        # 
        # We recommend that you set ZoneMatchMode to Include, which is the default value. This way, the system recommends instance types that are available in the zone specified by ZoneId based on the priority policy. The system also recommends instance types that are available in other zones within the same region.
        self.zone_id = zone_id
        # Specifies whether to recommend only instance types in the zone specified by ZoneId. Valid values:
        # 
        # *   Strict: recommends only instance types that are available in the zone specified by ZoneId.
        # *   Include: recommends instance types that are available in the zone specified by ZoneId and instance types that are available in other zones within the same region.
        # 
        # If `ZoneId` is specified, the default value of this parameter is Strict, which indicates that only instance types in the zone specified by ZoneId are recommended.
        self.zone_match_mode = zone_match_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cores is not None:
            result['Cores'] = self.cores

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_family_level is not None:
            result['InstanceFamilyLevel'] = self.instance_family_level

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family

        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized

        if self.max_price is not None:
            result['MaxPrice'] = self.max_price

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.priority_strategy is not None:
            result['PriorityStrategy'] = self.priority_strategy

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_match_mode is not None:
            result['ZoneMatchMode'] = self.zone_match_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceFamilyLevel') is not None:
            self.instance_family_level = m.get('InstanceFamilyLevel')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')

        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')

        if m.get('MaxPrice') is not None:
            self.max_price = m.get('MaxPrice')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PriorityStrategy') is not None:
            self.priority_strategy = m.get('PriorityStrategy')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneMatchMode') is not None:
            self.zone_match_mode = m.get('ZoneMatchMode')

        return self

