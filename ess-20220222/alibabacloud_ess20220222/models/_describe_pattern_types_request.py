# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribePatternTypesRequest(DaraModel):
    def __init__(
        self,
        architecture: List[str] = None,
        burstable_performance: str = None,
        channel_id: int = None,
        cores: int = None,
        cores_list: List[int] = None,
        cpu_architectures: List[str] = None,
        excluded_instance_type: List[str] = None,
        gpu_specs: List[str] = None,
        instance_categories: List[str] = None,
        instance_family_level: str = None,
        instance_type_families: List[str] = None,
        max_price: float = None,
        maximum_cpu_core_count: int = None,
        maximum_gpu_amount: int = None,
        maximum_memory_size: float = None,
        memory: float = None,
        memory_list: List[float] = None,
        minimum_baseline_credit: int = None,
        minimum_cpu_core_count: int = None,
        minimum_eni_ipv_6address_quantity: int = None,
        minimum_eni_private_ip_address_quantity: int = None,
        minimum_eni_quantity: int = None,
        minimum_gpu_amount: int = None,
        minimum_initial_credit: int = None,
        minimum_memory_size: float = None,
        physical_processor_models: List[str] = None,
        region_id: str = None,
        spot_strategy: str = None,
        v_switch_id: List[str] = None,
        zone_id: List[str] = None,
    ):
        # The architecture types of the instance types. Valid values:
        # 
        # *   X86: x86 architecture.
        # *   Heterogeneous: heterogeneous computing, such as GPU-accelerated or FPGA-accelerated.
        # *   BareMetal: ECS Bare Metal Instance.
        # *   Arm: Arm.
        # 
        # By default, all values are selected.
        self.architecture = architecture
        # Specifies whether to include burstable instance types. Valid values:
        # 
        # *   Exclude: does not include burstable instance types.
        # *   Include: includes burstable instance types.
        # *   Required: includes only burstable instance types.
        # 
        # Default value: Include.
        self.burstable_performance = burstable_performance
        # The channel ID. This parameter is not for public use.
        self.channel_id = channel_id
        # The number of vCPUs that you want to assign to the instance type.
        self.cores = cores
        # The number of vCPUs that you want to assign to the instance type. You can specify multiple vCPUs.
        self.cores_list = cores_list
        # The CPU architectures of the instance types. Valid values:
        # 
        # >  You can specify 1 to 2 CPU architectures.
        # 
        # *   x86
        # *   Arm
        self.cpu_architectures = cpu_architectures
        self.excluded_instance_type = excluded_instance_type
        # The GPU models.
        self.gpu_specs = gpu_specs
        # The classifications of the instance types. Valid values:
        # 
        # *   General-purpose: general-purpose instance type.
        # *   Compute-optimized: compute-optimized instance type.
        # *   Memory-optimized: memory-optimized instance type.
        # *   Big data: big data instance type.
        # *   Local SSDs: instance type with local SSDs.
        # *   High Clock Speed: instance type with high clock speeds.
        # *   Enhanced: enhanced instance type.
        # *   Shared: shared instance type.
        # *   Compute-optimized with GPU: GPU-accelerated compute-optimized instance type.
        # *   Visual Compute-optimized: visual compute-optimized instance type.
        # *   Heterogeneous Service: heterogeneous service instance type.
        # *   Compute-optimized with FPGA: FPGA-accelerated compute-optimized instance type.
        # *   Compute-optimized with NPU: NPU-accelerated compute-optimized instance type.
        # *   ECS Bare Metal: ECS Bare Metal Instance type.
        # *   High Performance Compute: HPC-optimized instance type.
        self.instance_categories = instance_categories
        # The level of the instance family. Valid values:
        # 
        # *   EntryLevel: entry level
        # *   EnterpriseLevel: enterprise level
        # *   CreditEntryLevel: credit-based entry level For more information, see [Burstable instance families](https://help.aliyun.com/document_detail/59977.html).
        self.instance_family_level = instance_family_level
        # The instance families that you want to query. You can query 1 to 10 instance families in each call.
        self.instance_type_families = instance_type_families
        # The maximum hourly price for pay-as-you-go or preemptible instances.
        self.max_price = max_price
        # The maximum number of vCPUs per instance type.
        self.maximum_cpu_core_count = maximum_cpu_core_count
        # The maximum number of GPUs per instance. The value must be a positive integer.
        self.maximum_gpu_amount = maximum_gpu_amount
        # The maximum memory size per instance. Unit: GiB.
        self.maximum_memory_size = maximum_memory_size
        # The memory size that you want to assign to the instance type. Unit: GiB.
        self.memory = memory
        # The memory size that you want to assign to the instance type. Unit: GiB. You can specify multiple memory sizes.
        self.memory_list = memory_list
        # The baseline vCPU computing performance (overall baseline performance of all vCPUs) per t5 or t6 burstable instance.
        self.minimum_baseline_credit = minimum_baseline_credit
        # The minimum number of vCPUs per instance type.
        self.minimum_cpu_core_count = minimum_cpu_core_count
        # The minimum number of IPv6 addresses per ENI.
        self.minimum_eni_ipv_6address_quantity = minimum_eni_ipv_6address_quantity
        # The minimum number of IPv4 addresses per ENI.
        self.minimum_eni_private_ip_address_quantity = minimum_eni_private_ip_address_quantity
        # The minimum number of elastic network interfaces (ENIs) per instance.
        self.minimum_eni_quantity = minimum_eni_quantity
        # The minimum number of GPUs per instance. The value must be a positive integer.
        self.minimum_gpu_amount = minimum_gpu_amount
        # The initial vCPU credits per t5 or t6 burstable instance.
        self.minimum_initial_credit = minimum_initial_credit
        # The minimum memory size per instance. Unit: GiB.
        self.minimum_memory_size = minimum_memory_size
        # The processor models of the instance types. You can specify 1 to 10 processor models.
        self.physical_processor_models = physical_processor_models
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The preemption policy that you want to apply to pay-as-you-go instances. Valid values:
        # 
        # *   NoSpot: The instances are created as regular pay-as-you-go instances.
        # *   SpotWithPriceLimit: The instances are created as preemptible instances that have a user-defined maximum hourly price.
        # *   SpotAsPriceGo: The instances are created as preemptible instances for which the market price at the time of purchase is automatically used as the bidding price.
        # 
        # Default value: NoSpot.
        self.spot_strategy = spot_strategy
        # The IDs of the vSwitches.
        self.v_switch_id = v_switch_id
        # The zone IDs. If you pass vSwitch IDs to the system, this parameter does not take effect.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.architecture is not None:
            result['Architecture'] = self.architecture

        if self.burstable_performance is not None:
            result['BurstablePerformance'] = self.burstable_performance

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.cores is not None:
            result['Cores'] = self.cores

        if self.cores_list is not None:
            result['CoresList'] = self.cores_list

        if self.cpu_architectures is not None:
            result['CpuArchitectures'] = self.cpu_architectures

        if self.excluded_instance_type is not None:
            result['ExcludedInstanceType'] = self.excluded_instance_type

        if self.gpu_specs is not None:
            result['GpuSpecs'] = self.gpu_specs

        if self.instance_categories is not None:
            result['InstanceCategories'] = self.instance_categories

        if self.instance_family_level is not None:
            result['InstanceFamilyLevel'] = self.instance_family_level

        if self.instance_type_families is not None:
            result['InstanceTypeFamilies'] = self.instance_type_families

        if self.max_price is not None:
            result['MaxPrice'] = self.max_price

        if self.maximum_cpu_core_count is not None:
            result['MaximumCpuCoreCount'] = self.maximum_cpu_core_count

        if self.maximum_gpu_amount is not None:
            result['MaximumGpuAmount'] = self.maximum_gpu_amount

        if self.maximum_memory_size is not None:
            result['MaximumMemorySize'] = self.maximum_memory_size

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.memory_list is not None:
            result['MemoryList'] = self.memory_list

        if self.minimum_baseline_credit is not None:
            result['MinimumBaselineCredit'] = self.minimum_baseline_credit

        if self.minimum_cpu_core_count is not None:
            result['MinimumCpuCoreCount'] = self.minimum_cpu_core_count

        if self.minimum_eni_ipv_6address_quantity is not None:
            result['MinimumEniIpv6AddressQuantity'] = self.minimum_eni_ipv_6address_quantity

        if self.minimum_eni_private_ip_address_quantity is not None:
            result['MinimumEniPrivateIpAddressQuantity'] = self.minimum_eni_private_ip_address_quantity

        if self.minimum_eni_quantity is not None:
            result['MinimumEniQuantity'] = self.minimum_eni_quantity

        if self.minimum_gpu_amount is not None:
            result['MinimumGpuAmount'] = self.minimum_gpu_amount

        if self.minimum_initial_credit is not None:
            result['MinimumInitialCredit'] = self.minimum_initial_credit

        if self.minimum_memory_size is not None:
            result['MinimumMemorySize'] = self.minimum_memory_size

        if self.physical_processor_models is not None:
            result['PhysicalProcessorModels'] = self.physical_processor_models

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('BurstablePerformance') is not None:
            self.burstable_performance = m.get('BurstablePerformance')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('Cores') is not None:
            self.cores = m.get('Cores')

        if m.get('CoresList') is not None:
            self.cores_list = m.get('CoresList')

        if m.get('CpuArchitectures') is not None:
            self.cpu_architectures = m.get('CpuArchitectures')

        if m.get('ExcludedInstanceType') is not None:
            self.excluded_instance_type = m.get('ExcludedInstanceType')

        if m.get('GpuSpecs') is not None:
            self.gpu_specs = m.get('GpuSpecs')

        if m.get('InstanceCategories') is not None:
            self.instance_categories = m.get('InstanceCategories')

        if m.get('InstanceFamilyLevel') is not None:
            self.instance_family_level = m.get('InstanceFamilyLevel')

        if m.get('InstanceTypeFamilies') is not None:
            self.instance_type_families = m.get('InstanceTypeFamilies')

        if m.get('MaxPrice') is not None:
            self.max_price = m.get('MaxPrice')

        if m.get('MaximumCpuCoreCount') is not None:
            self.maximum_cpu_core_count = m.get('MaximumCpuCoreCount')

        if m.get('MaximumGpuAmount') is not None:
            self.maximum_gpu_amount = m.get('MaximumGpuAmount')

        if m.get('MaximumMemorySize') is not None:
            self.maximum_memory_size = m.get('MaximumMemorySize')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('MemoryList') is not None:
            self.memory_list = m.get('MemoryList')

        if m.get('MinimumBaselineCredit') is not None:
            self.minimum_baseline_credit = m.get('MinimumBaselineCredit')

        if m.get('MinimumCpuCoreCount') is not None:
            self.minimum_cpu_core_count = m.get('MinimumCpuCoreCount')

        if m.get('MinimumEniIpv6AddressQuantity') is not None:
            self.minimum_eni_ipv_6address_quantity = m.get('MinimumEniIpv6AddressQuantity')

        if m.get('MinimumEniPrivateIpAddressQuantity') is not None:
            self.minimum_eni_private_ip_address_quantity = m.get('MinimumEniPrivateIpAddressQuantity')

        if m.get('MinimumEniQuantity') is not None:
            self.minimum_eni_quantity = m.get('MinimumEniQuantity')

        if m.get('MinimumGpuAmount') is not None:
            self.minimum_gpu_amount = m.get('MinimumGpuAmount')

        if m.get('MinimumInitialCredit') is not None:
            self.minimum_initial_credit = m.get('MinimumInitialCredit')

        if m.get('MinimumMemorySize') is not None:
            self.minimum_memory_size = m.get('MinimumMemorySize')

        if m.get('PhysicalProcessorModels') is not None:
            self.physical_processor_models = m.get('PhysicalProcessorModels')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

