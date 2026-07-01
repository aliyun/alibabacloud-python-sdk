# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAvailableResourceRequest(DaraModel):
    def __init__(
        self,
        cores: int = None,
        data_disk_category: str = None,
        dedicated_host_id: str = None,
        destination_resource: str = None,
        instance_charge_type: str = None,
        instance_type: str = None,
        io_optimized: str = None,
        memory: float = None,
        network_category: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        scope: str = None,
        spot_duration: int = None,
        spot_strategy: str = None,
        system_disk_category: str = None,
        zone_id: str = None,
    ):
        # The number of vCPU cores of the instance type. For valid values, see [Instance family](https://help.aliyun.com/document_detail/25378.html).
        # 
        # This parameter takes effect only when DestinationResource is set to InstanceType.
        self.cores = cores
        # The category of the data disk. Valid values: 
        #          
        # - cloud: basic disk.
        # - cloud_efficiency: ultra disk.
        # - cloud_ssd: standard SSD.
        # - ephemeral_ssd: local SSD.
        # - cloud_essd: enterprise SSD (ESSD).
        # - cloud_auto: ESSD AutoPL disk.
        # <props="china">
        # - cloud_essd_entry: ESSD Entry disk.
        self.data_disk_category = data_disk_category
        # The ID of the dedicated host.
        self.dedicated_host_id = dedicated_host_id
        # The type of resource to query. Valid values: 
        #          
        # - Zone: zone.
        # - IoOptimized: I/O optimized.
        # - InstanceType: instance type.
        # - Network: network type.
        # - ddh: dedicated host.
        # - SystemDisk: system disk.
        # - DataDisk: data disk.
        # 
        # > When DestinationResource is set to `SystemDisk`, you must specify InstanceType because system disks are restricted by instance types.
        # 
        # For more information about how to set the DestinationResource parameter, see the **operation description** section of this topic.
        # 
        # This parameter is required.
        self.destination_resource = destination_resource
        # The billing method of the resource. For more information, see [Billing overview](https://help.aliyun.com/document_detail/25398.html). Valid values: 
        #        
        # - PrePaid: subscription.  
        # - PostPaid: pay-as-you-go.
        # 
        # Default value: PostPaid.
        self.instance_charge_type = instance_charge_type
        # The instance type. For more information, see [Instance family](https://help.aliyun.com/document_detail/25378.html). You can also invoke [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) to query the most recent instance type list.
        # 
        # For more information about how to set the InstanceType parameter, see the **operation description** section at the beginning of this topic.
        self.instance_type = instance_type
        # Specifies whether the instance is an I/O optimized instance. Valid values:
        # 
        # - none: non-I/O optimized instance.
        # - optimized: I/O optimized instance.
        # 
        # Default value: optimized.
        self.io_optimized = io_optimized
        # The memory size of the instance type. Unit: GiB. For valid values, see [Instance family](https://help.aliyun.com/document_detail/25378.html).
        # 
        # This parameter takes effect only when DestinationResource is set to InstanceType.
        self.memory = memory
        # The network type. Valid values: 
        #         
        # - vpc: virtual private cloud (VPC).
        # - classic: classic network. The classic network is deprecated. For more information, see [Deprecation notice](https://help.aliyun.com/document_detail/2833134.html).
        self.network_category = network_category
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the destination region. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the resource. Valid values:
        # 
        # - instance: ECS instance.
        # - disk: cloud disk.
        # - reservedinstance: reserved instance.
        # - ddh: dedicated host.
        self.resource_type = resource_type
        # The scope of the reserved instance. Valid values:
        #          
        # - Region: regional.
        # - Zone: zonal.
        self.scope = scope
        # The protection period of the spot instance. Unit: hours. Default value: 1. Valid values:
        # - 1: After a spot instance is created, Alibaba Cloud ensures that the instance is not automatically released within 1 hour. After 1 hour, the system compares the bid price with the market price and checks the inventory to determine whether to retain automatic release the instance.
        # - 0: After a spot instance is created, Alibaba Cloud does not ensure that the instance runs for 1 hour. The system compares the bid price with the market price and checks the inventory to determine whether to retain automatic release the instance.
        # 
        # Alibaba Cloud sends an ECS system event notification 5 minutes before the instance is released. Spot instances are billed by second. Select an appropriate protection period based on the expected task execution duration.
        # 
        # > This parameter takes effect only when `InstanceChargeType` is set to `PostPaid` and `SpotStrategy` is set to `SpotWithPriceLimit` or `SpotAsPriceGo`.
        self.spot_duration = spot_duration
        # The bidding policy for pay-as-you-go instances. Valid values: 
        #          
        # - NoSpot: a regular pay-as-you-go instance.
        # - SpotWithPriceLimit: a spot instance with a maximum price limit.
        # - SpotAsPriceGo: a spot instance priced at the market price with the pay-as-you-go price as the upper limit.
        # 
        # Default value: NoSpot.
        # 
        # This parameter takes effect only when InstanceChargeType is set to `PostPaid`.
        self.spot_strategy = spot_strategy
        # The category of the system disk. Valid values: 
        #          
        # - cloud: basic disk.
        # - cloud_efficiency: ultra disk.
        # - cloud_ssd: standard SSD.
        # - ephemeral_ssd: local SSD.
        # - cloud_essd: enterprise SSD (ESSD).
        # - cloud_auto: ESSD AutoPL disk.
        # <props="china">
        # - cloud_essd_entry: ESSD Entry disk.
        # 
        # 
        # Default value description:
        # 
        # - If InstanceType is set to a retired instance type, the default value is `cloud`.
        # - In other cases, the default value is `cloud_efficiency`.<props="china">After January 30, 2026, for instance types that support only cloud_essd, the default value is changed from cloud_efficiency to cloud_essd PL0. For more information, see [Change notice](https://www.aliyun.com/notice/117844).
        # 
        # > When ResourceType is set to instance and DestinationResource is set to DataDisk, the SystemDiskCategory parameter is required. If you do not specify this parameter, the default value takes effect.
        self.system_disk_category = system_disk_category
        # The zone ID.
        # 
        # Default value: null. The operation returns resources that match the query conditions across all zones in the specified region (RegionId).
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cores is not None:
            result['Cores'] = self.cores

        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category

        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id

        if self.destination_resource is not None:
            result['DestinationResource'] = self.destination_resource

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.network_category is not None:
            result['NetworkCategory'] = self.network_category

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')

        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')

        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')

        if m.get('DestinationResource') is not None:
            self.destination_resource = m.get('DestinationResource')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NetworkCategory') is not None:
            self.network_category = m.get('NetworkCategory')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

