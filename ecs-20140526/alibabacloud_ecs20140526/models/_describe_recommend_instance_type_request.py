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
        # The number of vCPUs of the ECS instance.
        # 
        # >If you specify both the Cores and Memory parameters, the system matches all instance types that meet the specified vCPU and memory requirements.
        self.cores = cores
        # The billing method of the ECS instance. For details, see [Billing overview](https://help.aliyun.com/document_detail/25398.html). Valid values:
        # 
        # - PrePaid: subscription.
        # - PostPaid: pay-as-you-go.
        # 
        # Default value: PostPaid.
        self.instance_charge_type = instance_charge_type
        # The level of the instance family. Valid values:
        # 
        # - EntryLevel: entry level.
        # - EnterpriseLevel: enterprise level.
        # - CreditEntryLevel: credit-based entry level. For details, see [Burstable instances](https://help.aliyun.com/document_detail/59977.html).
        self.instance_family_level = instance_family_level
        # The specified instance type. For details, see [Instance families](https://help.aliyun.com/document_detail/25378.html). You can also call the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) operation to query the most recent instance type list.
        # 
        # > If you specify InstanceType, you cannot specify Cores or Memory.
        self.instance_type = instance_type
        # The collection of alternative instance families from which alternative instance types are selected. You can set up to 10 instance families in this parameter.
        self.instance_type_family = instance_type_family
        # Specifies whether the instance is I/O optimized. If the instance type supports only non-I/O optimized instances, you cannot set the IoOptimized parameter. Valid values:
        # 
        # - optimized: I/O optimized.
        # - none: non-I/O optimized.
        # 
        # Default value: optimized.
        # 
        # If you specify a retired instance type, the default value is none.
        self.io_optimized = io_optimized
        # The maximum acceptable hourly price for pay-as-you-go or spot instances.
        # 
        # >To set the maximum hourly price for a spot instance, set SpotStrategy to SpotWithPriceLimit.
        self.max_price = max_price
        # The memory size of the ECS instance. Unit: GiB.
        # 
        # >If you specify both the Cores and Memory parameters, the system matches all instance types that meet the specified vCPU and memory requirements.
        self.memory = memory
        # The network type of the ECS instance. Valid values:
        # 
        # - vpc: virtual private cloud (VPC).
        # - classic: classic network. The classic network is no longer available. For more information, see [Retirement notice](https://help.aliyun.com/document_detail/2833134.html).
        # 
        # Default value: vpc.
        # 
        # This parameter is required.
        self.network_type = network_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The priority recommendation strategy. Valid values:
        # 
        # - InventoryFirst: inventory first.
        # - PriceFirst: price first. Instance types are sorted by the hourly vCPU unit price in ascending order.
        # - NewProductFirst: newest product first.
        # 
        # Default value: InventoryFirst.
        self.priority_strategy = priority_strategy
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The scenario in which instance types are recommended. Valid values:
        # 
        # - UPGRADE: upgrade or downgrade an instance type.
        # - CREATE: create an instance.
        # 
        # Default value: CREATE.
        self.scene = scene
        # The bidding policy for the spot instance. Valid values:
        # 
        # - NoSpot: a pay-as-you-go instance.
        # - SpotWithPriceLimit: a spot instance with a maximum hourly price.
        # - SpotAsPriceGo: a spot instance for which the system automatically bids at up to the pay-as-you-go price.
        # 
        # > When you use SpotStrategy, set InstanceChargeType to PostPaid.
        # 
        # Default value: NoSpot.
        self.spot_strategy = spot_strategy
        # The category of the system disk. Valid values:
        # 
        # - cloud_efficiency: ultra disk.
        # - cloud_ssd: standard SSD.
        # - cloud_essd: enterprise SSD (ESSD).
        # - cloud: basic disk.
        # 
        # Default value for non-I/O optimized instances: cloud.
        # 
        # Default value for I/O optimized instances: cloud_efficiency.
        self.system_disk_category = system_disk_category
        # The zone ID. You can call [DescribeZones](https://help.aliyun.com/document_detail/25610.html) to query the most recent zone list.
        # 
        # Set ZoneMatchMode to Include (default value) to preferentially recommend instance types in the zone specified by ZoneId and also list instance types in other zones within the same region.
        self.zone_id = zone_id
        # Specifies whether to recommend only instance types in the zone specified by ZoneId. Valid values:
        # 
        # - Strict: recommends only instance types in the zone specified by ZoneId.
        # 
        # - Include: recommends instance types in other zones within the same region.
        # 
        # 
        # When ZoneId is specified, the default value of this parameter is Strict, which indicates that only instance types in the zone specified by ZoneId are recommended.
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

