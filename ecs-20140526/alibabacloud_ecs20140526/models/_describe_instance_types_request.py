# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeInstanceTypesRequest(DaraModel):
    def __init__(
        self,
        additional_attributes: List[str] = None,
        cpu_architecture: str = None,
        cpu_architectures: List[str] = None,
        gpuspec: str = None,
        gpu_specs: List[str] = None,
        instance_categories: List[str] = None,
        instance_category: str = None,
        instance_family_level: str = None,
        instance_type_families: List[str] = None,
        instance_type_family: str = None,
        instance_types: List[str] = None,
        local_storage_categories: List[str] = None,
        local_storage_category: str = None,
        max_results: int = None,
        maximum_cpu_core_count: int = None,
        maximum_cpu_speed_frequency: float = None,
        maximum_cpu_turbo_frequency: float = None,
        maximum_gpuamount: int = None,
        maximum_memory_size: float = None,
        minimum_baseline_credit: int = None,
        minimum_cpu_core_count: int = None,
        minimum_cpu_speed_frequency: float = None,
        minimum_cpu_turbo_frequency: float = None,
        minimum_disk_quantity: int = None,
        minimum_eni_ipv_6address_quantity: int = None,
        minimum_eni_private_ip_address_quantity: int = None,
        minimum_eni_quantity: int = None,
        minimum_eri_quantity: int = None,
        minimum_gpuamount: int = None,
        minimum_initial_credit: int = None,
        minimum_instance_bandwidth_rx: int = None,
        minimum_instance_bandwidth_tx: int = None,
        minimum_instance_pps_rx: int = None,
        minimum_instance_pps_tx: int = None,
        minimum_local_storage_amount: int = None,
        minimum_local_storage_capacity: int = None,
        minimum_memory_size: float = None,
        minimum_primary_eni_queue_number: int = None,
        minimum_queue_pair_number: int = None,
        minimum_secondary_eni_queue_number: int = None,
        next_token: str = None,
        nvme_support: str = None,
        owner_account: str = None,
        owner_id: int = None,
        physical_processor_model: str = None,
        physical_processor_models: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.additional_attributes = additional_attributes
        # The CPU architecture. Valid values:
        # 
        # *   X86
        # *   ARM
        self.cpu_architecture = cpu_architecture
        # The CPU architectures of instance types. You can specify 1 or 2 CPU architectures.
        self.cpu_architectures = cpu_architectures
        # The GPU model.
        # 
        # >  Fuzzy match is supported. For example, if an instance type provides NVIDIA V100 GPUs and you set this parameter to NVIDIA, information about the instance type is queried.
        self.gpuspec = gpuspec
        # The GPU models of instance types. You can specify 1 to 10 GPU models.
        self.gpu_specs = gpu_specs
        # The categories of instance types. You can specify 1 to 10 categories of instance types.
        self.instance_categories = instance_categories
        # The category of the instance type. Valid values:
        # 
        # *   General-purpose: general-purpose instance type
        # *   Compute-optimized: compute-optimized instance type
        # *   Memory-optimized: memory-optimized instance type
        # *   Big data: big data instance type
        # *   Local SSDs: instance type with local SSDs
        # *   High Clock Speed: instance type with high clock speeds
        # *   Enhanced: enhanced instance type
        # *   Shared: shared instance type
        # *   Compute-optimized with GPU: GPU-accelerated compute-optimized instance type
        # *   Visual Compute-optimized: visual compute-optimized instance type
        # *   Heterogeneous Service: heterogeneous service instance type
        # *   Compute-optimized with FPGA: FPGA-accelerated compute-optimized instance type
        # *   Compute-optimized with NPU: NPU-accelerated compute-optimized instance type
        # *   ECS Bare Metal: ECS Bare Metal Instance type
        # *   Super Computing Cluster: Super Computing Cluster (SCC) instance type
        # *   High Performance Compute: high-performance computing instance type
        self.instance_category = instance_category
        # The level of the instance family. Valid values:
        # 
        # *   EntryLevel: entry level (shared)
        # *   EnterpriseLevel: enterprise level
        # *   CreditEntryLevel: credit-based entry level
        self.instance_family_level = instance_family_level
        # The instance families. You can specify 1 to 10 instance families.
        self.instance_type_families = instance_type_families
        # The instance family to which the instance type belongs. For information about the valid values of this parameter, see [DescribeInstanceTypeFamilies](https://help.aliyun.com/document_detail/25621.html).
        # 
        # For more information about instance families, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        self.instance_type_family = instance_type_family
        # The instance types. You can specify 1 to 10 instance types. If this parameter is empty, information about all instance types is queried.
        self.instance_types = instance_types
        # The categories of local disks used by instance types. You can specify 1 or 2 categories of local disks.
        self.local_storage_categories = local_storage_categories
        # The category of local disks. For more information, see [Local disks](~~63138#section_n2w_8yc_5u1~~). Valid values:
        # 
        # *   local_hdd_pro: local Serial Advanced Technology Attachment (SATA) HDDs, which are attached to d1ne or d1 instances.
        # *   local_ssd_pro: local Non-Volatile Memory Express (NVMe) SSDs, which are attached to i2, i2g, i1, ga1, or gn5 instances.
        # 
        # Valid values:
        # 
        # *   local_hdd_pro
        # *   local_ssd_pro
        self.local_storage_category = local_storage_category
        # The maximum number of entries per page. Valid values: 1 to 1600.
        # 
        # Default value: 1600.
        self.max_results = max_results
        # The maximum number of vCPUs. The value must be a positive integer.
        # 
        # >  If an instance type has more vCPUs than the specified value, information about the instance type is not queried.
        self.maximum_cpu_core_count = maximum_cpu_core_count
        # The maximum clock speed.
        # 
        # >  If an instance type uses processors that have a higher clock speed than the specified value, information about the instance type is not queried.
        self.maximum_cpu_speed_frequency = maximum_cpu_speed_frequency
        # The maximum turbo frequency.
        # 
        # >  If an instance type uses processors that deliver a higher turbo frequency than the specified value, information about the instance type is not queried.
        self.maximum_cpu_turbo_frequency = maximum_cpu_turbo_frequency
        # The maximum number of GPUs. The value must be a positive integer.
        # 
        # >  If an instance type provides more GPUs than the specified value, information about the instance type is not queried.
        self.maximum_gpuamount = maximum_gpuamount
        # The maximum memory size. Unit: GiB.
        # 
        # >  If the memory size of an instance type is larger than the specified value, information about the instance type is not queried.
        self.maximum_memory_size = maximum_memory_size
        # The minimum baseline CPU performance (overall baseline performance of all vCPUs) of a t5 or t6 burstable instance.
        # 
        # >  If a t5 or t6 instance type provides baseline CPU performance lower than the specified value, information about the instance type is not queried.
        self.minimum_baseline_credit = minimum_baseline_credit
        # The minimum number of vCPUs. The value must be a positive integer.
        # 
        # >  If an instance type has fewer vCPUs than the specified value, information about the instance type is not queried.
        self.minimum_cpu_core_count = minimum_cpu_core_count
        # The minimum clock speed.
        # 
        # >  If an instance type uses processors that have a lower clock speed than the specified value, information about the instance type is not queried.
        self.minimum_cpu_speed_frequency = minimum_cpu_speed_frequency
        # The minimum turbo frequency.
        # 
        # >  If an instance type uses processors that deliver a lower turbo frequency than the specified value, information about the instance type is not queried.
        self.minimum_cpu_turbo_frequency = minimum_cpu_turbo_frequency
        # The minimum number of cloud disks per instance.
        # 
        # >  If an instance type supports fewer cloud disks than the specified value, information about the instance type is not queried.
        self.minimum_disk_quantity = minimum_disk_quantity
        # The minimum number of IPv6 addresses per ENI.
        # 
        # >  If an instance type supports fewer IPv6 addresses per ENI than the specified value, information about the instance type is not queried.
        self.minimum_eni_ipv_6address_quantity = minimum_eni_ipv_6address_quantity
        # The minimum number of IPv4 addresses per ENI.
        # 
        # >  If an instance type supports fewer IPv4 addresses per ENI than the specified value, information about the instance type is not queried.
        self.minimum_eni_private_ip_address_quantity = minimum_eni_private_ip_address_quantity
        # The minimum number of elastic network interfaces (ENIs) per instance.
        # 
        # >  If an instance type supports fewer ENIs than the specified value, information about the instance type is not queried.
        self.minimum_eni_quantity = minimum_eni_quantity
        # The minimum number of ERIs per instance.
        # 
        # >  If an instance type supports fewer ERIs than the specified value, information about the instance type is not queried.
        self.minimum_eri_quantity = minimum_eri_quantity
        # The minimum number of GPUs. The value must be a positive integer.
        # 
        # >  If an instance type provides fewer GPUs than the specified value, information about the instance type is not queried.
        self.minimum_gpuamount = minimum_gpuamount
        # The minimum initial CPU credits of a t5 or t6 burstable instance.
        # 
        # >  If a t5 or t6 instance type provides less initial vCPU credits than the specified value, information about the instance type is not queried.
        self.minimum_initial_credit = minimum_initial_credit
        # The minimum inbound internal bandwidth. Unit: Kbit/s.
        # 
        # >  If an instance type provides an inbound internal bandwidth that is lower than the specified value, information about the instance type is not queried.
        self.minimum_instance_bandwidth_rx = minimum_instance_bandwidth_rx
        # The minimum outbound internal bandwidth. Unit: Kbit/s.
        # 
        # >  If an instance type provides an outbound internal bandwidth that is lower than the specified value, information about the instance type is not queried.
        self.minimum_instance_bandwidth_tx = minimum_instance_bandwidth_tx
        # The minimum inbound packet forwarding rate over the internal network. Unit: pps.
        # 
        # >  If an instance type provides an inbound packet forwarding rate over the internal network that is lower than the specified value, information about the instance type is not queried.
        self.minimum_instance_pps_rx = minimum_instance_pps_rx
        # The minimum outbound packet forwarding rate over the internal network. Unit: pps.
        # 
        # >  If an instance type provides an outbound packet forwarding rate over the internal network that is lower than the specified value, information about the instance type is not queried.
        self.minimum_instance_pps_tx = minimum_instance_pps_tx
        # The minimum number of local disks per instance.
        # 
        # >  If an instance type supports fewer local disks than the specified value, information about the instance type is not queried.
        self.minimum_local_storage_amount = minimum_local_storage_amount
        # The capacity of each local disk attached per instance. Unit: GiB.
        self.minimum_local_storage_capacity = minimum_local_storage_capacity
        # The minimum memory size. Unit: GiB.
        # 
        # >  If the memory size of an instance type is smaller than the specified value, information about the instance type is not queried.
        self.minimum_memory_size = minimum_memory_size
        # The minimum default number of queues per primary network interface controller (NIC).
        # 
        # >  If an instance type supports fewer queues per primary NIC than the specified value, information about the instance type is not queried.
        self.minimum_primary_eni_queue_number = minimum_primary_eni_queue_number
        # The minimum number of queue pair (QP) queues per elastic RDMA interface (ERI).
        # 
        # >  If an instance type supports fewer QP queues per ERI than the specified value, information about the instance type is not queried.
        self.minimum_queue_pair_number = minimum_queue_pair_number
        # The minimum default number of queues per secondary NIC.
        # 
        # >  If an instance type supports fewer queues per secondary NIC than the specified value, information about the instance type is not queried.
        self.minimum_secondary_eni_queue_number = minimum_secondary_eni_queue_number
        # The query token. Set the value to the NextToken value returned in the previous call to the DescribeInstanceTypes operation. You do not need to specify this parameter for the first request.
        self.next_token = next_token
        # Specifies whether cloud disks can be attached by using the NVMe protocol. Valid values:
        # 
        # *   required: Cloud disks can be attached by using the NVMe protocol.
        # *   unsupported: Cloud disks cannot be attached by using the NVMe protocol.
        self.nvme_support = nvme_support
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The CPU model.
        # 
        # >  Fuzzy match is supported. For example, if an instance type uses Intel Xeon (Ice Lake) Platinum 8369B processors and you set this parameter to Intel, information about the instance type is queried.
        self.physical_processor_model = physical_processor_model
        # The CPU models of instance types. You can specify 1 to 10 CPU models.
        self.physical_processor_models = physical_processor_models
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_attributes is not None:
            result['AdditionalAttributes'] = self.additional_attributes

        if self.cpu_architecture is not None:
            result['CpuArchitecture'] = self.cpu_architecture

        if self.cpu_architectures is not None:
            result['CpuArchitectures'] = self.cpu_architectures

        if self.gpuspec is not None:
            result['GPUSpec'] = self.gpuspec

        if self.gpu_specs is not None:
            result['GpuSpecs'] = self.gpu_specs

        if self.instance_categories is not None:
            result['InstanceCategories'] = self.instance_categories

        if self.instance_category is not None:
            result['InstanceCategory'] = self.instance_category

        if self.instance_family_level is not None:
            result['InstanceFamilyLevel'] = self.instance_family_level

        if self.instance_type_families is not None:
            result['InstanceTypeFamilies'] = self.instance_type_families

        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family

        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types

        if self.local_storage_categories is not None:
            result['LocalStorageCategories'] = self.local_storage_categories

        if self.local_storage_category is not None:
            result['LocalStorageCategory'] = self.local_storage_category

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.maximum_cpu_core_count is not None:
            result['MaximumCpuCoreCount'] = self.maximum_cpu_core_count

        if self.maximum_cpu_speed_frequency is not None:
            result['MaximumCpuSpeedFrequency'] = self.maximum_cpu_speed_frequency

        if self.maximum_cpu_turbo_frequency is not None:
            result['MaximumCpuTurboFrequency'] = self.maximum_cpu_turbo_frequency

        if self.maximum_gpuamount is not None:
            result['MaximumGPUAmount'] = self.maximum_gpuamount

        if self.maximum_memory_size is not None:
            result['MaximumMemorySize'] = self.maximum_memory_size

        if self.minimum_baseline_credit is not None:
            result['MinimumBaselineCredit'] = self.minimum_baseline_credit

        if self.minimum_cpu_core_count is not None:
            result['MinimumCpuCoreCount'] = self.minimum_cpu_core_count

        if self.minimum_cpu_speed_frequency is not None:
            result['MinimumCpuSpeedFrequency'] = self.minimum_cpu_speed_frequency

        if self.minimum_cpu_turbo_frequency is not None:
            result['MinimumCpuTurboFrequency'] = self.minimum_cpu_turbo_frequency

        if self.minimum_disk_quantity is not None:
            result['MinimumDiskQuantity'] = self.minimum_disk_quantity

        if self.minimum_eni_ipv_6address_quantity is not None:
            result['MinimumEniIpv6AddressQuantity'] = self.minimum_eni_ipv_6address_quantity

        if self.minimum_eni_private_ip_address_quantity is not None:
            result['MinimumEniPrivateIpAddressQuantity'] = self.minimum_eni_private_ip_address_quantity

        if self.minimum_eni_quantity is not None:
            result['MinimumEniQuantity'] = self.minimum_eni_quantity

        if self.minimum_eri_quantity is not None:
            result['MinimumEriQuantity'] = self.minimum_eri_quantity

        if self.minimum_gpuamount is not None:
            result['MinimumGPUAmount'] = self.minimum_gpuamount

        if self.minimum_initial_credit is not None:
            result['MinimumInitialCredit'] = self.minimum_initial_credit

        if self.minimum_instance_bandwidth_rx is not None:
            result['MinimumInstanceBandwidthRx'] = self.minimum_instance_bandwidth_rx

        if self.minimum_instance_bandwidth_tx is not None:
            result['MinimumInstanceBandwidthTx'] = self.minimum_instance_bandwidth_tx

        if self.minimum_instance_pps_rx is not None:
            result['MinimumInstancePpsRx'] = self.minimum_instance_pps_rx

        if self.minimum_instance_pps_tx is not None:
            result['MinimumInstancePpsTx'] = self.minimum_instance_pps_tx

        if self.minimum_local_storage_amount is not None:
            result['MinimumLocalStorageAmount'] = self.minimum_local_storage_amount

        if self.minimum_local_storage_capacity is not None:
            result['MinimumLocalStorageCapacity'] = self.minimum_local_storage_capacity

        if self.minimum_memory_size is not None:
            result['MinimumMemorySize'] = self.minimum_memory_size

        if self.minimum_primary_eni_queue_number is not None:
            result['MinimumPrimaryEniQueueNumber'] = self.minimum_primary_eni_queue_number

        if self.minimum_queue_pair_number is not None:
            result['MinimumQueuePairNumber'] = self.minimum_queue_pair_number

        if self.minimum_secondary_eni_queue_number is not None:
            result['MinimumSecondaryEniQueueNumber'] = self.minimum_secondary_eni_queue_number

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.nvme_support is not None:
            result['NvmeSupport'] = self.nvme_support

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.physical_processor_model is not None:
            result['PhysicalProcessorModel'] = self.physical_processor_model

        if self.physical_processor_models is not None:
            result['PhysicalProcessorModels'] = self.physical_processor_models

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalAttributes') is not None:
            self.additional_attributes = m.get('AdditionalAttributes')

        if m.get('CpuArchitecture') is not None:
            self.cpu_architecture = m.get('CpuArchitecture')

        if m.get('CpuArchitectures') is not None:
            self.cpu_architectures = m.get('CpuArchitectures')

        if m.get('GPUSpec') is not None:
            self.gpuspec = m.get('GPUSpec')

        if m.get('GpuSpecs') is not None:
            self.gpu_specs = m.get('GpuSpecs')

        if m.get('InstanceCategories') is not None:
            self.instance_categories = m.get('InstanceCategories')

        if m.get('InstanceCategory') is not None:
            self.instance_category = m.get('InstanceCategory')

        if m.get('InstanceFamilyLevel') is not None:
            self.instance_family_level = m.get('InstanceFamilyLevel')

        if m.get('InstanceTypeFamilies') is not None:
            self.instance_type_families = m.get('InstanceTypeFamilies')

        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')

        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')

        if m.get('LocalStorageCategories') is not None:
            self.local_storage_categories = m.get('LocalStorageCategories')

        if m.get('LocalStorageCategory') is not None:
            self.local_storage_category = m.get('LocalStorageCategory')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('MaximumCpuCoreCount') is not None:
            self.maximum_cpu_core_count = m.get('MaximumCpuCoreCount')

        if m.get('MaximumCpuSpeedFrequency') is not None:
            self.maximum_cpu_speed_frequency = m.get('MaximumCpuSpeedFrequency')

        if m.get('MaximumCpuTurboFrequency') is not None:
            self.maximum_cpu_turbo_frequency = m.get('MaximumCpuTurboFrequency')

        if m.get('MaximumGPUAmount') is not None:
            self.maximum_gpuamount = m.get('MaximumGPUAmount')

        if m.get('MaximumMemorySize') is not None:
            self.maximum_memory_size = m.get('MaximumMemorySize')

        if m.get('MinimumBaselineCredit') is not None:
            self.minimum_baseline_credit = m.get('MinimumBaselineCredit')

        if m.get('MinimumCpuCoreCount') is not None:
            self.minimum_cpu_core_count = m.get('MinimumCpuCoreCount')

        if m.get('MinimumCpuSpeedFrequency') is not None:
            self.minimum_cpu_speed_frequency = m.get('MinimumCpuSpeedFrequency')

        if m.get('MinimumCpuTurboFrequency') is not None:
            self.minimum_cpu_turbo_frequency = m.get('MinimumCpuTurboFrequency')

        if m.get('MinimumDiskQuantity') is not None:
            self.minimum_disk_quantity = m.get('MinimumDiskQuantity')

        if m.get('MinimumEniIpv6AddressQuantity') is not None:
            self.minimum_eni_ipv_6address_quantity = m.get('MinimumEniIpv6AddressQuantity')

        if m.get('MinimumEniPrivateIpAddressQuantity') is not None:
            self.minimum_eni_private_ip_address_quantity = m.get('MinimumEniPrivateIpAddressQuantity')

        if m.get('MinimumEniQuantity') is not None:
            self.minimum_eni_quantity = m.get('MinimumEniQuantity')

        if m.get('MinimumEriQuantity') is not None:
            self.minimum_eri_quantity = m.get('MinimumEriQuantity')

        if m.get('MinimumGPUAmount') is not None:
            self.minimum_gpuamount = m.get('MinimumGPUAmount')

        if m.get('MinimumInitialCredit') is not None:
            self.minimum_initial_credit = m.get('MinimumInitialCredit')

        if m.get('MinimumInstanceBandwidthRx') is not None:
            self.minimum_instance_bandwidth_rx = m.get('MinimumInstanceBandwidthRx')

        if m.get('MinimumInstanceBandwidthTx') is not None:
            self.minimum_instance_bandwidth_tx = m.get('MinimumInstanceBandwidthTx')

        if m.get('MinimumInstancePpsRx') is not None:
            self.minimum_instance_pps_rx = m.get('MinimumInstancePpsRx')

        if m.get('MinimumInstancePpsTx') is not None:
            self.minimum_instance_pps_tx = m.get('MinimumInstancePpsTx')

        if m.get('MinimumLocalStorageAmount') is not None:
            self.minimum_local_storage_amount = m.get('MinimumLocalStorageAmount')

        if m.get('MinimumLocalStorageCapacity') is not None:
            self.minimum_local_storage_capacity = m.get('MinimumLocalStorageCapacity')

        if m.get('MinimumMemorySize') is not None:
            self.minimum_memory_size = m.get('MinimumMemorySize')

        if m.get('MinimumPrimaryEniQueueNumber') is not None:
            self.minimum_primary_eni_queue_number = m.get('MinimumPrimaryEniQueueNumber')

        if m.get('MinimumQueuePairNumber') is not None:
            self.minimum_queue_pair_number = m.get('MinimumQueuePairNumber')

        if m.get('MinimumSecondaryEniQueueNumber') is not None:
            self.minimum_secondary_eni_queue_number = m.get('MinimumSecondaryEniQueueNumber')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('NvmeSupport') is not None:
            self.nvme_support = m.get('NvmeSupport')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhysicalProcessorModel') is not None:
            self.physical_processor_model = m.get('PhysicalProcessorModel')

        if m.get('PhysicalProcessorModels') is not None:
            self.physical_processor_models = m.get('PhysicalProcessorModels')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

