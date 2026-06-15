# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribePriceRequest(DaraModel):
    def __init__(
        self,
        data_disk: List[main_models.DescribePriceRequestDataDisk] = None,
        scheduler_options: main_models.DescribePriceRequestSchedulerOptions = None,
        system_disk: main_models.DescribePriceRequestSystemDisk = None,
        amount: int = None,
        assurance_times: str = None,
        capacity: int = None,
        dedicated_host_type: str = None,
        image_id: str = None,
        instance_amount: int = None,
        instance_cpu_core_count: int = None,
        instance_network_type: str = None,
        instance_type: str = None,
        instance_type_list: List[str] = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_out: int = None,
        io_optimized: str = None,
        isp: str = None,
        offering_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        platform: str = None,
        price_unit: str = None,
        recurrence_rules: List[main_models.DescribePriceRequestRecurrenceRules] = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        scope: str = None,
        spot_duration: int = None,
        spot_strategy: str = None,
        start_time: str = None,
        zone_id: str = None,
    ):
        self.data_disk = data_disk
        self.scheduler_options = scheduler_options
        self.system_disk = system_disk
        # The number of resources for which to query prices. Valid values: 1–1000.
        # 
        # Default value: 1.
        self.amount = amount
        # The number of times the elasticity assurance can be used. Set this to `Unlimited`, which allows the assurance to be used any number of times during its effective period.
        # 
        # Default value: `Unlimited`.
        self.assurance_times = assurance_times
        # The memory capacity for the elasticity assurance. Unit: GiB.
        self.capacity = capacity
        # The dedicated host type. You can call the [DescribeDedicatedHostTypes](https://help.aliyun.com/document_detail/134240.html) operation to query dedicated host types.
        self.dedicated_host_type = dedicated_host_type
        # This parameter is valid only when `ResourceType` is set to `instance`.
        # 
        # The ID of the image. The image provides the runtime environment for the instance. You can call the [DescribeImages](https://help.aliyun.com/document_detail/25534.html) operation to query available images. If you do not specify this parameter, the system queries prices for Linux instances by default.
        self.image_id = image_id
        # The number of instances to include in the reserved instance offering.
        # 
        # Valid values: 1–1000.
        self.instance_amount = instance_amount
        # The total number of vCPUs for instances that are covered by the elasticity assurance. When you call this operation, the system calculates the number of supported instances based on the specified `InstanceType` and rounds the value up to the nearest integer.
        # 
        # > When you query the price of an elasticity assurance, you can specify only one of the `InstanceCpuCoreCount` and `InstanceAmount` parameters.
        self.instance_cpu_core_count = instance_cpu_core_count
        # The network type of the instance. Valid values:
        # 
        # - `classic`: classic network
        # 
        # - `vpc`: VPC
        # 
        # Default value: `vpc`.
        self.instance_network_type = instance_network_type
        # The instance type. This parameter is required when `ResourceType` is set to `instance`. For more information, see [Instance type families](https://help.aliyun.com/document_detail/25378.html) or call the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) operation to query the instance types.
        self.instance_type = instance_type
        # The instance type. You can specify only one instance type for an elasticity assurance of the `Unlimited` type.
        self.instance_type_list = instance_type_list
        # The billing method for network usage. Valid values:
        # 
        # - `PayByBandwidth`: pay-by-bandwidth
        # 
        # - `PayByTraffic`: pay-by-traffic
        # 
        # Default value: `PayByTraffic`.
        self.internet_charge_type = internet_charge_type
        # The maximum outbound public bandwidth. Unit: Mbit/s. Valid values: 0–100.
        # 
        # Default value: 0.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # Specifies whether the instance is I/O optimized. Valid values:
        # 
        # - `none`: non-I/O-optimized.
        # 
        # - `optimized`: I/O-optimized.
        # 
        # For [generation I](https://help.aliyun.com/document_detail/55263.html) instances, the default value is `none`.
        # 
        # For other instance types, the default value is `optimized`.
        self.io_optimized = io_optimized
        # The Internet service provider (ISP). Valid values:
        # 
        # - `cmcc`: China Mobile
        # 
        # - `telecom`: China Telecom
        # 
        # - `unicom`: China Unicom
        # 
        # - `multiCarrier`: BGP (Multi-ISP)
        self.isp = isp
        # The payment option for the reserved instance. Valid values:
        # 
        # - `No Upfront`
        # 
        # - `Partial Upfront`
        # 
        # - `All Upfront`
        self.offering_type = offering_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The billing duration of the resource. This parameter is used with `PriceUnit`. Valid values:
        # 
        # <props="china">
        # 
        # - If `PriceUnit` is set to `Month`: 1–9.
        # 
        # - If `PriceUnit` is set to `Year`: 1–5.
        # 
        # - If `PriceUnit` is set to `Hour`: 1.
        # 
        # - If `PriceUnit` is set to `Week`: 1–4.
        # 
        # 
        # 
        # <props="intl">
        # 
        # - If `PriceUnit` is set to `Month`: 1–9.
        # 
        # - If `PriceUnit` is set to `Year`: 1–5.
        # 
        # - If `PriceUnit` is set to `Hour`: 1.
        # 
        # 
        # 
        # Default value: 1.
        self.period = period
        # The operating system of the instance. Valid values:
        # 
        # - `Windows`: Windows Server
        # 
        # - `Linux`: Linux
        self.platform = platform
        # The billing cycle of the resource. Valid values:
        # 
        # <props="china">
        # 
        # - `Month`: For monthly pricing.
        # 
        # - `Year`: For yearly pricing.
        # 
        # - `Hour` (Default): For hourly pricing.
        # 
        # - `Week`: For weekly pricing.
        # 
        # 
        # 
        # <props="intl">
        # 
        # - `Month`: For monthly pricing.
        # 
        # - `Year`: For yearly pricing.
        # 
        # - `Hour` (Default): For hourly pricing.
        self.price_unit = price_unit
        # The list of recurrence rules for the time-based elasticity assurance.
        # 
        # <props="china">
        # 
        # > The time-based elasticity assurance feature is available only in specific regions and to specific users. To use this feature, [submit a ticket](https://selfservice.console.aliyun.com/ticket/createIndex).
        # 
        # 
        # 
        # <props="intl">
        # 
        # > The time-based elasticity assurance feature is available only in specific regions and to specific users. To use this feature, [submit a ticket](https://smartservice.console.aliyun.com/service/create-ticket-intl).
        self.recurrence_rules = recurrence_rules
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the resource for which you want to query the price. Valid values:
        # 
        # - `instance`: Query the prices of ECS instances. If you set this parameter to `instance`, you must also specify the `InstanceType` parameter.
        # 
        # - `disk`: Query the prices of cloud disks. If you set this parameter to `disk`, you must also specify the `DataDisk.1.Category` and `DataDisk.1.Size` parameters.
        # 
        # - `diskperformance`: Query the prices of the provisioned performance of an ESSD AutoPL cloud disk. You must also specify the `DataDisk.1.Category` and `DataDisk.1.ProvisionedIops` parameters.
        # 
        # - `bandwidth`: Query the prices of network bandwidth.
        # 
        # - `ddh`: Query the prices of dedicated hosts.
        # 
        # - `ElasticityAssurance`: Query the prices of Elasticity Assurance. If you set this parameter to `ElasticityAssurance`, you must also specify the `InstanceType` parameter.
        # 
        # - `CapacityReservation`: Query the prices of Capacity Reservation. If you set this parameter to `CapacityReservation`, you must also specify the `InstanceType` parameter.
        # 
        # Default value: `instance`.
        self.resource_type = resource_type
        # The scope of the reserved instance. Valid values:
        # 
        # - `Region`: region-scoped
        # 
        # - `Zone`: zone-scoped
        # 
        # Default value: `Region`.
        self.scope = scope
        # The protection period of the spot instance. Unit: hours. Default value: 1. Valid values:
        # 
        # - `1`: Alibaba Cloud does not automatically release the instance within 1 hour. After the 1-hour protection period ends, the system checks the market price and resource inventory to determine whether to retain or release the instance.
        # 
        # - `0`: The instance has no protection period. The system checks the market price and resource inventory to determine whether to retain or release the instance.
        # 
        # Alibaba Cloud sends you an ECS system event five minutes before the instance is released. Spot instances are billed by the second. Select a protection period based on the time required to complete your task.
        # 
        # > This parameter is valid only when `SpotStrategy` is set to `SpotWithPriceLimit` or `SpotAsPriceGo`.
        self.spot_duration = spot_duration
        # The preemption policy for the pay-as-you-go instance. Valid values:
        # 
        # - `NoSpot`: A regular pay-as-you-go instance.
        # 
        # - `SpotWithPriceLimit`: A spot instance for which you specify a maximum hourly price.
        # 
        # - `SpotAsPriceGo`: A spot instance where the system automatically bids up to the pay-as-you-go price.
        # 
        # Default value: `NoSpot`.
        # 
        # > This parameter applies only when you query hourly prices, where `PriceUnit` is `Hour` and `Period` is `1`. Because these are the default values, you do not need to set them when you use `SpotStrategy`.
        self.spot_strategy = spot_strategy
        # The time when the time-based elasticity assurance takes effect. The time must be specified in UTC and formatted as `yyyy-MM-ddTHH:mm:ssZ` in accordance with the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard.
        self.start_time = start_time
        # The ID of the availability zone.
        # 
        # > The prices of spot instances may vary by availability zone. When you query the price of a spot instance, specify `ZoneId` to query the price for a specific availability zone.
        self.zone_id = zone_id

    def validate(self):
        if self.data_disk:
            for v1 in self.data_disk:
                 if v1:
                    v1.validate()
        if self.scheduler_options:
            self.scheduler_options.validate()
        if self.system_disk:
            self.system_disk.validate()
        if self.recurrence_rules:
            for v1 in self.recurrence_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k1 in self.data_disk:
                result['DataDisk'].append(k1.to_map() if k1 else None)

        if self.scheduler_options is not None:
            result['SchedulerOptions'] = self.scheduler_options.to_map()

        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        if self.amount is not None:
            result['Amount'] = self.amount

        if self.assurance_times is not None:
            result['AssuranceTimes'] = self.assurance_times

        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.dedicated_host_type is not None:
            result['DedicatedHostType'] = self.dedicated_host_type

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_amount is not None:
            result['InstanceAmount'] = self.instance_amount

        if self.instance_cpu_core_count is not None:
            result['InstanceCpuCoreCount'] = self.instance_cpu_core_count

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.instance_type_list is not None:
            result['InstanceTypeList'] = self.instance_type_list

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out

        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.offering_type is not None:
            result['OfferingType'] = self.offering_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit

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

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k1 in m.get('DataDisk'):
                temp_model = main_models.DescribePriceRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k1))

        if m.get('SchedulerOptions') is not None:
            temp_model = main_models.DescribePriceRequestSchedulerOptions()
            self.scheduler_options = temp_model.from_map(m.get('SchedulerOptions'))

        if m.get('SystemDisk') is not None:
            temp_model = main_models.DescribePriceRequestSystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('AssuranceTimes') is not None:
            self.assurance_times = m.get('AssuranceTimes')

        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('DedicatedHostType') is not None:
            self.dedicated_host_type = m.get('DedicatedHostType')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceAmount') is not None:
            self.instance_amount = m.get('InstanceAmount')

        if m.get('InstanceCpuCoreCount') is not None:
            self.instance_cpu_core_count = m.get('InstanceCpuCoreCount')

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InstanceTypeList') is not None:
            self.instance_type_list = m.get('InstanceTypeList')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')

        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('OfferingType') is not None:
            self.offering_type = m.get('OfferingType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')

        self.recurrence_rules = []
        if m.get('RecurrenceRules') is not None:
            for k1 in m.get('RecurrenceRules'):
                temp_model = main_models.DescribePriceRequestRecurrenceRules()
                self.recurrence_rules.append(temp_model.from_map(k1))

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

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribePriceRequestRecurrenceRules(DaraModel):
    def __init__(
        self,
        end_hour: int = None,
        recurrence_type: str = None,
        recurrence_value: str = None,
        start_hour: int = None,
    ):
        # The end time of the time-based assurance. The value must be on the hour.
        self.end_hour = end_hour
        # The recurrence type of the rule. Valid values:
        # 
        # - `Daily`: repeats on a daily basis.
        # 
        # - `Weekly`: repeats on a weekly basis.
        # 
        # - `Monthly`: repeats on a monthly basis.
        # 
        # > You must specify both `RecurrenceType` and `RecurrenceValue`.
        self.recurrence_type = recurrence_type
        # The recurrence value.
        # 
        # - If `RecurrenceType` is set to `Daily`, this parameter takes a single value that specifies the recurrence interval in days. Valid values: 1–31.
        # 
        # - If `RecurrenceType` is set to `Weekly`, this parameter can have multiple values separated by commas (,). The values 0, 1, 2, 3, 4, 5, and 6 correspond to Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, and Saturday. For example, `1,2` specifies Monday and Tuesday.
        # 
        # - If `RecurrenceType` is set to `Monthly`, the value must be in the `A–B` format. The values of A and B must be between 1 and 31, and B must be greater than or equal to A. For example, `1–5` specifies the first to the fifth day of each month.
        # 
        # > You must specify both `RecurrenceType` and `RecurrenceValue`.
        self.recurrence_value = recurrence_value
        # The start time of the time-based assurance. The value must be on the hour.
        # 
        # > Both `StartHour` and `EndHour` are required. The interval between them must be at least 4 hours.
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

class DescribePriceRequestSystemDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
        performance_level: str = None,
        size: int = None,
    ):
        # The category of the system disk. You must specify `ImageId` when you query the price of a system disk. Valid values:
        # 
        # - `cloud`: basic cloud disk
        # 
        # - `cloud_efficiency`: efficiency cloud disk
        # 
        # - `cloud_ssd`: SSD cloud disk
        # 
        # - `ephemeral_ssd`: local SSD
        # 
        # - `cloud_essd`: ESSD
        # 
        # - `cloud_auto`: ESSD AutoPL
        # 
        # <props="china">
        # 
        # - `cloud_essd_entry`: ESSD Entry
        # 
        # 
        # 
        # 
        # * For retired instance types where `IoOptimized` is `none`, the default value is `cloud`.
        # 
        # * In other cases, the default value is `cloud_efficiency`.<props="china">After January 30, 2026, for instance types that support only ESSDs, the default value will be changed from `cloud_efficiency` to `cloud_essd` at PL0. For more information, see the [change announcement](https://www.aliyun.com/notice/117844).
        self.category = category
        # The performance level of the ESSD when used as a system disk. This parameter is valid only when `SystemDisk.Category` is set to `cloud_essd`. Valid values:
        # 
        # `PL0`<br>`PL1` (Default)<br>`PL2`<br>`PL3`<br><br><br>
        self.performance_level = performance_level
        # The size of the system disk. Unit: GiB. Valid values:
        # 
        # - Basic cloud disk: 20–500.
        # 
        # - ESSD cloud disk:
        # 
        #   - PL0: 1–2048.
        # 
        #   - PL1: 20–2048.
        # 
        #   - PL2: 461–2048.
        # 
        #   - PL3: 1261–2048.
        # 
        # - ESSD AutoPL cloud disk: 1–2048.
        # 
        # - Other cloud disk categories: 20–2048.
        # 
        # Default value: `max{20, ImageSize}`, which is the greater of 20 and the size of the specified image (`ImageId`).
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

class DescribePriceRequestSchedulerOptions(DaraModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        deployment_set_strategy: str = None,
    ):
        # This parameter is valid only when `ResourceType` is set to `instance`.
        # 
        # The ID of the dedicated host. You can call the [DescribeDedicatedHosts](https://help.aliyun.com/document_detail/134242.html) operation to query dedicated host IDs.
        self.dedicated_host_id = dedicated_host_id
        # The deployment set strategy. Valid values:
        # 
        # - `Availability`: high availability
        # 
        # - `AvailabilityGroup`: high availability for deployment set groups
        # 
        # - `LowLatency`: low latency
        # 
        # - `ProximityLooseDispersion`: proximity loose dispersion
        # 
        # > Only the `ProximityLooseDispersion` strategy incurs a fee. The API response includes price details for the deployment set (where `Resource` is `deploymentSet`) only when this strategy is used. Other deployment set strategies are free of charge.
        self.deployment_set_strategy = deployment_set_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id

        if self.deployment_set_strategy is not None:
            result['DeploymentSetStrategy'] = self.deployment_set_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')

        if m.get('DeploymentSetStrategy') is not None:
            self.deployment_set_strategy = m.get('DeploymentSetStrategy')

        return self

class DescribePriceRequestDataDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
        performance_level: str = None,
        size: int = None,
        provisioned_iops: int = None,
    ):
        # The category of data disk N. Valid values:
        # 
        # - `cloud`: basic cloud disk
        # 
        # - `cloud_efficiency`: efficiency cloud disk
        # 
        # - `cloud_ssd`: SSD cloud disk
        # 
        # - `ephemeral_ssd`: local SSD
        # 
        # - `cloud_essd`: ESSD
        # 
        # - `cloud_auto`: ESSD AutoPL
        # 
        # <props="china">
        # 
        # - `cloud_essd_entry`: ESSD Entry
        # 
        # 
        # 
        # 
        # The value of N can be 1–16.
        self.category = category
        # The performance level of data disk N when it is an ESSD. This parameter is valid only when `DataDisk.N.Category` is set to `cloud_essd`. Valid values:
        # 
        # - `PL0`
        # 
        # - `PL1` (Default)
        # 
        # - `PL2`
        # 
        # - `PL3`
        # 
        # The value of N can be 1–16.
        self.performance_level = performance_level
        # The size of data disk N. Unit: GiB. Valid values:
        # 
        # - `cloud`: 5–2000
        # 
        # - `cloud_efficiency`: 20–32768
        # 
        # - `cloud_ssd`: 20–32768
        # 
        # - `cloud_auto`: 1–32768
        # 
        # <props="china">
        # 
        # - `cloud_essd_entry`: 10–32768
        # 
        # 
        # 
        # 
        # - `cloud_essd`: The value range depends on the `DataDisk.N.PerformanceLevel`.
        # 
        #   - PL0: 1–32768
        # 
        #   - PL1: 20–32768
        # 
        #   - PL2: 461–32768
        # 
        #   - PL3: 1261–32768
        # 
        # - `ephemeral_ssd`: 5–800
        # 
        # The value of N can be 1–16.
        self.size = size
        # The provisioned read/write IOPS for the ESSD AutoPL cloud disk. Valid values: 0–`min{50000, 1000 * Capacity - Baseline IOPS}`.
        # 
        # `Baseline IOPS = min{1800 + 50 * Capacity, 50000}`.
        # 
        # > This parameter is valid only when `DataDisk.N.Category` is set to `cloud_auto`. For more information, see [ESSD AutoPL cloud disks](https://help.aliyun.com/document_detail/368372.html).
        self.provisioned_iops = provisioned_iops

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.size is not None:
            result['Size'] = self.size

        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')

        return self

