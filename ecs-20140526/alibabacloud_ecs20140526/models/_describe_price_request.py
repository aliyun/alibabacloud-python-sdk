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
        # The number of ECS instances. You can specify this parameter when you want to query the prices of multiple instances that have specific specifications. Valid values: 1 to 1000.
        # 
        # Default value: 1.
        self.amount = amount
        # The total number of times that the elasticity assurance can be applied. Set the value to Unlimited. This value indicates that the elasticity assurance can be applied an unlimited number of times within its effective period.
        # 
        # Default value: Unlimited.
        self.assurance_times = assurance_times
        # The storage capacity. Unit: GiB.
        self.capacity = capacity
        # The type of the dedicated host. You can call the [DescribeDedicatedHostTypes](https://help.aliyun.com/document_detail/134240.html) operation to query the most recent list of dedicated host types.
        self.dedicated_host_type = dedicated_host_type
        # This parameter takes effect only when ResourceType is set to instance.
        # 
        # The image ID. Images contain the runtime environments to load when instances start. You can call the [DescribeImages](https://help.aliyun.com/document_detail/25534.html) operation to query available images. If you do not specify this parameter, the system queries the prices of Linux images.
        self.image_id = image_id
        # The total number of reserved instances for an instance type.
        # 
        # Valid values: 1 to 1000.
        self.instance_amount = instance_amount
        # The total number of vCPUs supported by the elasticity assurance. When you call this API operation, the system calculates the number of instances that an elasticity assurance must support based on the specified value of InstanceType. The calculated value is rounded up to the nearest integer.
        # 
        # > When you call this API operation to query the price of an elasticity assurance, you can only specify either InstanceCoreCpuCount or InstanceAmount.
        self.instance_cpu_core_count = instance_cpu_core_count
        # The network type of the instance. Valid values:
        # 
        # *   classic: classic network
        # *   vpc: Virtual Private Cloud (VPC)
        # 
        # Default value: vpc.
        self.instance_network_type = instance_network_type
        # The instance type. When `ResourceType` is set to `instance`, you must specify this parameter. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html) or call the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) operation to query the most recent list of instance types.
        self.instance_type = instance_type
        # The instance types. You can select only a single instance type when you configure an elasticity assurance in unlimited mode.
        self.instance_type_list = instance_type_list
        # The billing method for network usage. Valid values:
        # 
        # *   PayByBandwidth: pay-by-bandwidth
        # *   PayByTraffic: pay-by-traffic
        # 
        # Default value: PayByTraffic
        self.internet_charge_type = internet_charge_type
        # The maximum outbound public bandwidth. Unit: Mbit/s. Valid values: 0 to 100.
        # 
        # Default value: 0.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # Specifies whether the instance is I/O optimized. Valid values:
        # 
        # *   none: The instance is not I/O optimized.
        # *   optimized: The instance is I/O optimized.
        # 
        # When the instance type specified by the InstanceType parameter belongs to [Generation I instance families](https://help.aliyun.com/document_detail/55263.html), the default value of this parameter is none.
        # 
        # When the instance type specified by the InstanceType parameter does not belong to [Generation I instance families](https://help.aliyun.com/document_detail/55263.html), the default value of this parameter is optimized.
        self.io_optimized = io_optimized
        # The Internet service provider (ISP). Valid values:
        # 
        # *   cmcc: China Mobile
        # *   telecom: China Telecom
        # *   unicom: China Unicom
        # *   multiCarrier: multi-line ISP
        self.isp = isp
        # The payment option of the reserved instance. Valid values:
        # 
        # *   No Upfront
        # *   Partial Upfront
        # *   All Upfront
        self.offering_type = offering_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The billing cycle of the ECS instance. Valid values:
        # 
        # *   Valid values when PriceUnit is set to Month: 1, 2, 3, 4, 5, 6, 7, 8, and 9.
        # *   Valid values when PriceUnit is set to Year: 1, 2, 3, 4, and 5.
        # *   Set the value to 1 when PriceUnit is set to Hour.
        # 
        # Default value: 1.
        self.period = period
        # The operating system of the image that is used by the instance. Valid values:
        # 
        # *   Windows: Windows Server operating system
        # *   Linux: Linux and UNIX-like operating system
        self.platform = platform
        # The pricing unit of the ECS resource. Valid values:
        # 
        # *   Month
        # *   Year
        # *   Hour (default)
        self.price_unit = price_unit
        # The assurance schedules of the time-segmented elasticity assurance.
        # 
        # >  Time-segmented elasticity assurances are available only in specific regions and to specific users. To use time-segmented elasticity assurances, [submit a ticket](https://smartservice.console.aliyun.com/service/create-ticket-intl).
        self.recurrence_rules = recurrence_rules
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent list of regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the resource. Valid values:
        # 
        # *   instance: queries the most recent prices of ECS instances. If you set this parameter to `instance`, specify `InstanceType`.
        # *   disk: queries the most recent prices of cloud disks. If you set this parameter to `disk`, specify `DataDisk.1.Category` and `DataDisk.1.Size`.
        # *   diskperformance: Queries the most recent prices of the provioned performance of the Enterprise SSD (ESSD) AutoPL disk. You must also specify `DataDisk.1.Category` and `DataDisk.1.ProvisionedIops`.
        # *   bandwidth: queries the most recent prices for network usage.
        # *   ddh: queries the most recent prices of dedicated hosts.
        # *   ElasticityAssurance: queries the most recent prices of elasticity assurances. If you set this parameter to `ElasticityAssurance`, specify `InstanceType`.
        # *   CapacityReservation: queries the most recent prices of capacity reservations. If you set this parameter to `CapacityReservation`, specify `InstanceType`.
        # 
        # Default value: instance.
        self.resource_type = resource_type
        # The scope of the reserved instance. Valid values:
        # 
        # *   Region: regional
        # *   Zone: zonal
        # 
        # Default value: Region.
        self.scope = scope
        # The protection period of the spot instance. Unit: hours. Default value: 1. Valid values:
        # 
        # *   1: After a spot instance is created, Alibaba Cloud ensures that the instance is not automatically released within 1 hour. After the 1-hour protection period ends, the system compares the bid price with the market price and checks the resource inventory to determine whether to retain or release the instance.
        # *   0: After a spot instance is created, Alibaba Cloud does not ensure that the instance runs for 1 hour. The system compares the bid price with the market price and checks the resource inventory to determine whether to retain or release the instance.
        # 
        # Alibaba Cloud sends an ECS system event to notify you 5 minutes before the instance is released. Spot instances are billed by second. We recommend that you specify a protection period based on your business requirements.
        # 
        # >  This parameter takes effect only when SpotStrategy is set to SpotWithPriceLimit or SpotAsPriceGo.
        self.spot_duration = spot_duration
        # The bidding policy for the pay-as-you-go instance. Valid values:
        # 
        # *   NoSpot: The instance is a regular pay-as-you-go instance.
        # *   SpotWithPriceLimit: The instance is created as a spot instance that has a user-defined maximum hourly price.
        # *   SpotAsPriceGo: The instance is created as a spot instance whose bid price is based on the market price at the time of purchase. The market price can be up to the pay-as-you-go price.
        # 
        # Default value: NoSpot.
        # 
        # >  This parameter takes effect only when `PriceUnit` is set to Hour and `Period` is set to 1. The default value of `PriceUnit` is `Hour` and the default value of `Period` is `1`. Therefore, you do not need to set `PriceUnit` or `Period` when you set SpotStrategy.
        self.spot_strategy = spot_strategy
        # The time when the time-segmented assurance of the elasticity assurance takes effect. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. For more information, see [ISO 8601](https://help.aliyun.com/document_detail/25696.html).
        self.start_time = start_time
        # The zone ID.
        # 
        # > Prices of spot instances vary based on zones. When you query the price of a spot instance, specify ZoneId.
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
        # The end time of the assurance period for the capacity reservation of the time-segmented elasticity assurance. Specify an on-the-hour point in time.
        self.end_hour = end_hour
        # The type of the assurance schedule. Valid values:
        # 
        # *   Daily
        # *   Weekly
        # *   Monthly
        # 
        # >  If you specify this parameter, you must specify `RecurrenceType` and `RecurrenceValue`.
        self.recurrence_type = recurrence_type
        # The days of the week or month on which the capacity reservation of the time-segmented elasticity assurance takes effect or the interval, in number of days, at which the capacity reservation takes effect.
        # 
        # *   If you set `RecurrenceType` to `Daily`, you can specify only one value. Valid values: 1 to 31. The value specifies that the capacity reservation takes effect every few days.
        # *   If you set `RecurrenceType` to `Weekly`, you can specify multiple values. Separate the values with commas (,). Valid values: 0, 1, 2, 3, 4, 5, and 6, which specify Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, and Saturday, respectively. Example: `1,2`, which specifies that the capacity reservation takes effect on Monday and Tuesday.
        # *   If you set `RecurrenceType` to `Monthly`, you can specify two values in the `A-B` format. Valid values of A and B: 1 to 31. B must be greater than or equal to A. Example: `1-5`, which specifies that the capacity reservation takes effect every day from the first day up to the fifth day of each month.
        # 
        # >  If you specify this parameter, you must specify `RecurrenceType` and `RecurrenceValue`.
        self.recurrence_value = recurrence_value
        # The start time of the assurance period for the capacity reservation of the time-segmented elasticity assurance. Specify an on-the-hour point in time.
        # 
        # >  You must specify both StartHour and EndHour. The EndHour value must be at least 4 hours later than the StartHour value.
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
        # The category of the system disk. Valid values:
        # 
        # *   cloud: basic disk
        # *   cloud_efficiency: ultra disk
        # *   cloud_ssd: standard SSD
        # *   ephemeral_ssd: local SSD
        # *   cloud_essd: Enterprise SSD (ESSD)
        # *   cloud_auto: ESSD AutoPL disk
        # 
        # Default value:
        # 
        # *   When InstanceType is set to a retired instance type and `IoOptimized` is set to `none`, the default value is `cloud`.
        # *   In other cases, the default value is `cloud_efficiency`.
        # 
        # >  If you want to query the price of a system disk, you must also specify `ImageId`.
        self.category = category
        # The performance level of the system disk when the disk is an ESSD. This parameter is valid only when `SystemDiskCategory` is set to cloud_essd. Valid values:
        # 
        # PL0, PL1 (default), PL2, PL3.
        self.performance_level = performance_level
        # The size of the system disk. Unit: GiB. Valid values:
        # 
        # *   Basic disk (cloud): 20 to 500.
        # 
        # *   ESSD (cloud_essd): Valid values vary based on the SystemDisk.PerformanceLevel value.
        # 
        #     *   Valid values when SystemDisk.PerformanceLevel is set to PL0: 1 to 2048.
        #     *   Valid values when SystemDisk.PerformanceLevel is set to PL1: 20 to 2048.
        #     *   Valid values when SystemDisk.PerformanceLevel is set to PL2: 461 to 2048.
        #     *   Valid values when SystemDisk.PerformanceLevel is set to PL3: 1261 to 2048.
        # 
        # *   ESSD AutoPL disk (cloud_auto): 1 to 2048.
        # 
        # *   Other disk categories: 20 to 2048.
        # 
        # Default value: 20 or the size of the image specified by ImageId, whichever is greater.
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
        # This parameter takes effect only when ResourceType is set to instance.
        # 
        # The ID of the dedicated host. You can call the [DescribeDedicatedHosts](https://help.aliyun.com/document_detail/134242.html) operation to query the dedicated host list.
        self.dedicated_host_id = dedicated_host_id
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
        # *   cloud: basic disk.
        # *   cloud_efficiency: ultra disk.
        # *   cloud_ssd: standard SSD.
        # *   ephemeral_ssd: local SSD.
        # *   cloud_essd: ESSD.
        # *   cloud_auto: ESSD AutoPL disk.
        # 
        # Valid values of N: 1 to 16.
        self.category = category
        # The performance level of data disk N when the disk is an ESSD. This parameter takes effect only when `DataDisk.N.Category` is set to cloud_essd. Valid values:
        # 
        # *   PL0
        # *   PL1 (default)
        # *   PL2
        # *   PL3
        # 
        # Valid values of N: 1 to 16.
        self.performance_level = performance_level
        # The size of data disk N. Unit: GiB. Valid values:
        # 
        # *   Valid values if DataDisk.N.Category is set to cloud: 5 to 2000.
        # 
        # *   Valid values if DataDisk.N.Category is set to cloud_efficiency: 20 to 32768.
        # 
        # *   Valid values if DataDisk.N.Category is set to cloud_ssd: 20 to 32768.
        # 
        # *   Valid values if DataDisk.N.Category is set to cloud_auto: 1 to 32768.
        # 
        # *   Valid values if DataDisk.N.Category is set to cloud_essd: vary based on the `DataDisk.N.PerformanceLevel` value.
        # 
        #     *   Valid values if DataDisk.N.PerformanceLevel is set to PL0: 1 to 32768.
        #     *   Valid values if DataDisk.N.PerformanceLevel is set to PL1: 20 to 32768.
        #     *   Valid values if DataDisk.N.PerformanceLevel is set to PL2: 461 to 32768.
        #     *   Valid values if DataDisk.N.PerformanceLevel is set to PL3: 1261 to 32768.
        # 
        # *   Valid values if DataDisk.N.Category is set to ephemeral_ssd: 5 to 800.
        # 
        # Valid values of N: 1 to 16.
        self.size = size
        # The provisioned read/write IOPS of the ESSD AutoPL disk to use as data disk N. Valid values: 0 to min{50,000, 1,000 × Capacity - Baseline IOPS}.
        # 
        # Baseline IOPS = min{1,800 + 50 × Capacity, 50,000}.
        # 
        # >  This parameter is available only if you set `DataDisk.N.Category` to `cloud_auto`. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
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

