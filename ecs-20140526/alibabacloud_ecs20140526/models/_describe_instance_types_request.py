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
        # The list of advanced features to return for instance types.
        self.additional_attributes = additional_attributes
        # The CPU architecture. Valid values:
        self.cpu_architecture = cpu_architecture
        # The CPU architectures to query. Array length: 1 to 2.
        self.cpu_architectures = cpu_architectures
        # The GPU type.
        self.gpuspec = gpuspec
        # The GPU types to query. Array length: 1 to 10.
        self.gpu_specs = gpu_specs
        # The instance type categories to query. Array length: 1 to 10.
        self.instance_categories = instance_categories
        # The instance type category. Valid values:
        self.instance_category = instance_category
        # The level of the instance family. Valid values:
        self.instance_family_level = instance_family_level
        # The instance families to query. Array length: 1 to 10.
        self.instance_type_families = instance_type_families
        # The instance family to which the instance type belongs. For more information, see [DescribeInstanceTypeFamilies](https://help.aliyun.com/document_detail/25621.html).
        self.instance_type_family = instance_type_family
        # The specified instance types. Array length: 1 to 10. If this parameter is not specified, information about all instance types is queried by default.
        self.instance_types = instance_types
        # The local disk types to query. Array length: 1 to 2.
        self.local_storage_categories = local_storage_categories
        # The local disk type. For more information, see [Local disks](~~63138#section_n2w_8yc_5u1~~). Valid values:
        self.local_storage_category = local_storage_category
        # The maximum number of entries per page for paging query. Maximum value: 1600.
        self.max_results = max_results
        # The expected maximum number of vCPU cores when querying instance types. Valid values: positive integers.
        self.maximum_cpu_core_count = maximum_cpu_core_count
        # The expected maximum clock speed when querying instance types.
        self.maximum_cpu_speed_frequency = maximum_cpu_speed_frequency
        # The expected maximum turbo frequency when querying instance types.
        self.maximum_cpu_turbo_frequency = maximum_cpu_turbo_frequency
        # The expected maximum number of GPUs when querying instance types. Valid values: positive integers.
        self.maximum_gpuamount = maximum_gpuamount
        # The expected maximum memory size when querying instance types. Unit: GiB.
        self.maximum_memory_size = maximum_memory_size
        # The expected minimum baseline vCPU computing performance (sum of all vCPUs) for burstable instances t5 and t6 when querying instance types.
        self.minimum_baseline_credit = minimum_baseline_credit
        # The expected minimum number of vCPU cores when querying instance types. Valid values: positive integers.
        self.minimum_cpu_core_count = minimum_cpu_core_count
        # The expected minimum clock speed when querying instance types.
        self.minimum_cpu_speed_frequency = minimum_cpu_speed_frequency
        # The expected minimum turbo frequency when querying instance types.
        self.minimum_cpu_turbo_frequency = minimum_cpu_turbo_frequency
        # The expected minimum number of cloud disks that can be attached when querying instance types.
        self.minimum_disk_quantity = minimum_disk_quantity
        # The expected minimum number of IPv6 addresses per Elastic Network Interface (ENI) network interface controller (NIC) when querying instance types.
        self.minimum_eni_ipv_6address_quantity = minimum_eni_ipv_6address_quantity
        # The expected minimum number of IPv4 addresses per Elastic Network Interface (ENI) network interface controller (NIC) when querying instance types.
        self.minimum_eni_private_ip_address_quantity = minimum_eni_private_ip_address_quantity
        # The expected minimum number of Elastic Network Interfaces (ENIs) that can be attached per network interface controller (NIC) when querying instance types.
        self.minimum_eni_quantity = minimum_eni_quantity
        # The expected minimum number of Elastic RDMA Interfaces (ERIs) per network interface controller (NIC) when querying instance types.
        self.minimum_eri_quantity = minimum_eri_quantity
        # The expected minimum number of GPUs when querying instance types. Valid values: positive integers.
        self.minimum_gpuamount = minimum_gpuamount
        # The expected minimum initial vCPU CPU credits for burstable instances t5 and t6 when querying instance types.
        self.minimum_initial_credit = minimum_initial_credit
        # The expected minimum inbound internal bandwidth when querying instance types. Unit: kbit/s.
        self.minimum_instance_bandwidth_rx = minimum_instance_bandwidth_rx
        # The expected minimum outbound internal bandwidth when querying instance types. Unit: kbit/s.
        self.minimum_instance_bandwidth_tx = minimum_instance_bandwidth_tx
        # The expected minimum inbound packet forwarding rate over the internal network when querying instance types. Unit: pps.
        self.minimum_instance_pps_rx = minimum_instance_pps_rx
        # The expected minimum outbound packet forwarding rate over the internal network when querying instance types. Unit: pps.
        self.minimum_instance_pps_tx = minimum_instance_pps_tx
        # The expected minimum number of local disks attached to the instance when querying instance types.
        self.minimum_local_storage_amount = minimum_local_storage_amount
        # The capacity of each local disk attached to the instance. Unit: GiB.
        self.minimum_local_storage_capacity = minimum_local_storage_capacity
        # The expected minimum memory size when querying instance types. Unit: GiB.
        self.minimum_memory_size = minimum_memory_size
        # The expected minimum number of default queues for the primary ENI when querying instance types.
        self.minimum_primary_eni_queue_number = minimum_primary_eni_queue_number
        # The expected minimum number of QueuePair (QP) queues per Elastic RDMA Interface (ERI) when querying instance types.
        self.minimum_queue_pair_number = minimum_queue_pair_number
        # The expected minimum number of default queues for secondary Elastic Network Interfaces (ENIs) per network interface controller (NIC) when querying instance types.
        self.minimum_secondary_eni_queue_number = minimum_secondary_eni_queue_number
        # The query token. Set this parameter to the NextToken value returned in the previous call. You do not need to set this parameter for the first call.
        self.next_token = next_token
        # Specifies whether the cloud disks attached to the instance type support NVMe. Valid values:
        self.nvme_support = nvme_support
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The processor model.
        self.physical_processor_model = physical_processor_model
        # The processor models to query. Array length: 1 to 10.
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

