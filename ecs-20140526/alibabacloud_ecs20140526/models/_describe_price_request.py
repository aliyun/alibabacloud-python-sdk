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
        # The number of Elastic Compute Service (ECS) instances that you want to purchase in batch. You can use this parameter to query the price of batch purchasing instances of a specific configuration. Valid values: 1 to 1000.
        # 
        # Default value: 1.
        self.amount = amount
        # The total number of times that the elasticity assurance can be applied. Set the value to Unlimited. Only the unlimited mode within the service effective period is supported.
        # 
        # Default value: Unlimited.
        self.assurance_times = assurance_times
        # The capacity, in GiB.
        self.capacity = capacity
        # The dedicated host type. You can call [DescribeDedicatedHostTypes](https://help.aliyun.com/document_detail/134240.html) to query the most recent list of dedicated host types.
        self.dedicated_host_type = dedicated_host_type
        # This parameter takes effect only when ResourceType is set to instance.
        # 
        # The image ID, which specifies the runtime environment to load when the instance starts. You can call [DescribeImages](https://help.aliyun.com/document_detail/25534.html) to query available image resources. If you do not specify this parameter, the price of a Linux image is queried by default.
        self.image_id = image_id
        # The total number of instances to reserve within an instance type.
        # 
        # Valid values: 1 to 1000.
        self.instance_amount = instance_amount
        # The total number of vCPUs supported by the elasticity assurance. When you call this operation, the system calculates the number of instances required by the elasticity assurance based on the specified InstanceType (rounded up).
        # 
        # > When you call this operation to query the price of an elasticity assurance, you can specify only one of InstanceCoreCpuCount and InstanceAmount.
        self.instance_cpu_core_count = instance_cpu_core_count
        # The network type of the instance. Valid values:
        # 
        # - vpc: Virtual Private Cloud (VPC).
        # - classic: classic network. The classic network is no longer available. For more information, see [Retirement notice](https://help.aliyun.com/document_detail/2833134.html).
        # 
        # Default value: vpc.
        self.instance_network_type = instance_network_type
        # The instance type. You must specify this parameter when `ResourceType` is set to `instance`. For more details, see [Instance family](https://help.aliyun.com/document_detail/25378.html). You can also invoke [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) to query the most recent instance type list.
        self.instance_type = instance_type
        # The instance type. Only a single instance type can be specified for the unlimited elasticity assurance service.
        self.instance_type_list = instance_type_list
        # The billing method for network bandwidth. Valid values:
        # 
        # - PayByBandwidth: pay-by-bandwidth.
        # - PayByTraffic: pay-by-traffic.
        # 
        # Default value: PayByTraffic.
        self.internet_charge_type = internet_charge_type
        # The maximum outbound public bandwidth, in Mbit/s. Valid values: 0 to 100.
        # 
        # Default value: 0.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # Specifies whether the queried instance is an I/O optimized instance. Valid values:
        # 
        # - none: non-I/O optimization.
        # - optimized: I/O optimized.
        # 
        # If InstanceType is a [Series I](https://help.aliyun.com/document_detail/55263.html) instance type, the default value is none.
        # 
        # If InstanceType is not a [Series I](https://help.aliyun.com/document_detail/55263.html) instance type, the default value is optimized.
        self.io_optimized = io_optimized
        # The Internet Service Provider (ISP). Valid values: 
        # - cmcc: China Mobile.
        # - telecom: China Telecom.
        # - unicom: China Unicom.
        # - multiCarrier: multi-ISP.
        self.isp = isp
        # The payment option of the reserved instance. Valid values:
        # 
        # - No Upfront: no upfront.
        # - Partial Upfront: partial upfront.
        # - All Upfront: all upfront.
        self.offering_type = offering_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The billing duration of Elastic Compute Service (ECS). Valid values:
        # 
        # <props="china">
        # - If the PriceUnit parameter is set to Month: 1 to 9.
        # - If the PriceUnit parameter is set to Year: 1 to 5.
        # - If the PriceUnit parameter is set to Hour: 1.
        # - If the PriceUnit parameter is set to Week: 1 to 4.
        # 
        # 
        # 
        # <props="intl">
        # - If the PriceUnit parameter is set to Month: 1 to 9.
        # - If the PriceUnit parameter is set to Year: 1 to 5.
        # - If the PriceUnit parameter is set to Hour: 1.
        # 
        # 
        # 
        # Default value: 1.
        self.period = period
        # The operating system type of the image used by the instance. Valid values: 
        # - Windows: Windows Server operating system.
        # - Linux: Linux and Unix-like operating systems.
        self.platform = platform
        # The pricing unit for querying Elastic Compute Service (ECS) prices across different billing cycles. Valid values:
        # 
        # <props="china">
        # - Month: monthly pricing unit.
        # - Year: yearly pricing unit.
        # - Hour (default): hourly pricing unit.
        # - Week: weekly pricing unit.
        # 
        # 
        # 
        # <props="intl">
        # - Month: monthly pricing unit.
        # - Year: yearly pricing unit.
        # - Hour (default): hourly pricing unit.
        self.price_unit = price_unit
        # The list of recurrence rules for the time-sharing elasticity assurance.
        # 
        # <props="china">
        # 
        # > The time-sharing elasticity assurance feature is available only in specific regions and for specific users. To use this feature, [submit a ticket](https://selfservice.console.aliyun.com/ticket/createIndex).
        # 
        # 
        # 
        # <props="intl">
        # 
        # > The time-sharing elasticity assurance feature is available only in specific regions and for specific users. To use this feature, [submit a ticket](https://smartservice.console.aliyun.com/service/create-ticket-intl).
        self.recurrence_rules = recurrence_rules
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the resource. Valid values:
        # - instance: queries the latest price list of ECS instances. When this parameter is set to `instance`, you must also specify `InstanceType`.
        # - disk: queries the latest price list of disks. When this parameter is set to `disk`, you must also specify `DataDisk.1.Category` and `DataDisk.1.Size`.
        # - diskperformance: queries the latest price list of provisioned performance for ESSD AutoPL disks. You must also specify `DataDisk.1.Category` and `DataDisk.1.ProvisionedIops`.
        # - bandwidth: queries the latest price list of bandwidth.
        # - ddh: queries the latest price list of dedicated hosts.
        # - ElasticityAssurance: queries the price of the elasticity assurance service. When this parameter is set to `ElasticityAssurance`, you must also specify `InstanceType`.
        # - CapacityReservation: queries the price of the capacity reservation service. When this parameter is set to `CapacityReservation`, you must also specify `InstanceType`.
        # 
        # Default value: instance.
        self.resource_type = resource_type
        # The scope of the reserved instance. Valid values: 
        #    
        # - Region: regional. 
        # - Zone: zonal.
        # 
        # Default value: Region.
        self.scope = scope
        # The protection period of the spot instance, in hours. Default value: 1. Valid values:
        # - 1: After a spot instance is created, Alibaba Cloud ensures that the instance is not automatically released for 1 hour. After 1 hour, the system automatically compares the bid price with the market price and checks resource availability to determine whether to retain automatic release the instance.
        # - 0: After a spot instance is created, Alibaba Cloud does not ensure that the instance runs for 1 hour. The system automatically compares the bid price with the market price and checks resource availability to determine whether to retain automatic release the instance.
        # 
        # Alibaba Cloud sends an ECS system event notification 5 minutes before the instance is released. Spot instances are billed by second. Select an appropriate protection period based on the expected task execution duration.
        # 
        # > This parameter takes effect only when SpotStrategy is set to SpotWithPriceLimit or SpotAsPriceGo.
        self.spot_duration = spot_duration
        # The bidding policy for pay-as-you-go instances. Valid values:
        # - NoSpot: a regular pay-as-you-go instance.
        # - SpotWithPriceLimit: a spot instance with a maximum price limit.
        # - SpotAsPriceGo: a spot instance priced at the market price with the pay-as-you-go price as the upper limit.
        # 
        # Default value: NoSpot.
        # 
        # > This parameter takes effect only when `PriceUnit=Hour` and `Period=1`. Because the default value of `PriceUnit` is `Hour` and the default value of `Period` is `1`, you do not need to set `PriceUnit` or `Period` when you specify this parameter.
        self.spot_strategy = spot_strategy
        # The effective period when the time-sharing elasticity assurance takes effect. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC+0. For more information, see [ISO 8601](https://help.aliyun.com/document_detail/25696.html).
        self.start_time = start_time
        # The zone ID.
        # 
        # > Spot instance prices may vary across zones. When you query spot instance prices, specify ZoneId to query the price in a specific zone.
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
        # The end hour of the time-sharing assurance. The value must be a whole hour.
        self.end_hour = end_hour
        # The type of the recurrence rule. Valid values:
        # - Daily: daily recurrence.
        # - Weekly: weekly recurrence.
        # - Monthly: monthly recurrence.
        # 
        # > You must specify both `RecurrenceType` and `RecurrenceValue`.
        self.recurrence_type = recurrence_type
        # The value of the recurrence rule.
        # 
        # - If `RecurrenceType` is set to `Daily`, you can specify only one value. Valid values: 1 to 31. This value indicates the interval in days between recurrences.
        # - If `RecurrenceType` is set to `Weekly`, you can specify multiple values separated by commas (,). The values for Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, and Saturday are 0, 1, 2, 3, 4, 5, and 6. For example, `1,2` indicates Monday and Tuesday.
        # - If `RecurrenceType` is set to `Monthly`, the format is `A-B`. Valid values of A and B: 1 to 31. B must be greater than or equal to A. For example, `1-5` indicates the 1st through 5th day of each month.
        # 
        # > You must specify both `RecurrenceType` and `RecurrenceValue`.
        self.recurrence_value = recurrence_value
        # The effective period start hour of the time-sharing assurance. The value must be a whole hour.
        # 
        # > You must specify both StartHour and EndHour, and the difference between them must be at least 4 hours.
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
        # The category of the system disk. You must also specify `ImageId` when querying the system disk price. Valid values:
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
        # - If InstanceType is a retired instance type and `IoOptimized` is set to `none`, the default value is `cloud`.
        # - In other cases, the default value is `cloud_efficiency`.<props="china">After January 30, 2026, for instance types that support only cloud_essd, the default value is changed from cloud_efficiency to cloud_essd PL0. For more information, see [Change notice](https://www.aliyun.com/notice/117844).
        self.category = category
        # The performance level of the system disk when the disk type is ESSD. This parameter is valid only when `SystemDiskCategory=cloud_essd`. Valid values:
        # 
        # PL0.
        # PL1 (default).
        # PL2.
        # PL3.
        self.performance_level = performance_level
        # The size of the system disk, in GiB. Valid values:
        # 
        # - Basic disk: 20 to 500.
        # - ESSD:
        #   - PL0: 1 to 2048.
        #   - PL1: 20 to 2048.
        #   - PL2: 461 to 2048.
        #   - PL3: 1261 to 2048.
        # - ESSD AutoPL disk: 1 to 2048.
        # - Other disk categories: 20 to 2048.
        # 
        # Default value: max{20, image size of the specified ImageId parameter}.
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
        # The dedicated host ID. You can call [DescribeDedicatedHosts](https://help.aliyun.com/document_detail/134242.html) to query the list of dedicated host IDs.
        self.dedicated_host_id = dedicated_host_id
        # The deployment set strategy. Valid values:
        # - Availability: high availability.
        # - AvailabilityGroup: deployment set group high availability.
        # - LowLatency: low network latency.
        # - ProximityLooseDispersion: proximity loose dispersion.
        # 
        # > Only when the strategy is set to ProximityLooseDispersion does the API response include the price details for "Resource": "deploymentSet". Other deployment set strategies are free of charge, so the API response does not include price information for "Resource": "deploymentSet".
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
        # Valid values of N: 1 to 16.
        self.category = category
        # The performance level of data disk N when the disk type is ESSD. This parameter is valid only when `DataDisk.N.Category=cloud_essd`. Valid values:
        # 
        # - PL0.
        # - PL1 (default).
        # - PL2.
        # - PL3.
        # 
        # Valid values of N: 1 to 16.
        self.performance_level = performance_level
        # The size of data disk N, in GiB. Valid values:
        # 
        # - cloud: 5 to 2000.
        # - cloud_efficiency: 20 to 32768.
        # - cloud_ssd: 20 to 32768.
        # - cloud_auto: 1 to 32768.
        # <props="china">
        # - cloud_essd_entry: 10 to 32768.
        # 
        # - cloud_essd: The valid values depend on the value of `DataDisk.N.PerformanceLevel`.	
        #     - PL0: 1 to 32768.
        #     - PL1: 20 to 32768.
        #     - PL2: 461 to 32768.
        #     - PL3: 1261 to 32768.
        # - ephemeral_ssd: 5 to 800.
        # 
        # Valid values of N: 1 to 16.
        self.size = size
        # The provisioned read/write IOPS of the ESSD AutoPL disk. Valid values: 0 to min{50,000, 1000 × capacity - baseline performance}.
        # 
        # Baseline performance = min{1,800 + 50 × capacity, 50000}.
        # 
        # > This parameter is supported only when `DiskCategory` is set to `cloud_auto`. For more information, see [ESSD AutoPL disk](https://help.aliyun.com/document_detail/368372.html).
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

