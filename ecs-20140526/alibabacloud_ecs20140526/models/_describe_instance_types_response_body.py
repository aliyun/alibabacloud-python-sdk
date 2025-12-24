# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceTypesResponseBody(DaraModel):
    def __init__(
        self,
        instance_types: main_models.DescribeInstanceTypesResponseBodyInstanceTypes = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # Details about the instance types.
        self.instance_types = instance_types
        # The query token returned in this call.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.instance_types:
            self.instance_types.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types.to_map()

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceTypes') is not None:
            temp_model = main_models.DescribeInstanceTypesResponseBodyInstanceTypes()
            self.instance_types = temp_model.from_map(m.get('InstanceTypes'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceTypesResponseBodyInstanceTypes(DaraModel):
    def __init__(
        self,
        instance_type: List[main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceType] = None,
    ):
        self.instance_type = instance_type

    def validate(self):
        if self.instance_type:
            for v1 in self.instance_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceType'] = []
        if self.instance_type is not None:
            for k1 in self.instance_type:
                result['InstanceType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_type = []
        if m.get('InstanceType') is not None:
            for k1 in m.get('InstanceType'):
                temp_model = main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceType()
                self.instance_type.append(temp_model.from_map(k1))

        return self

class DescribeInstanceTypesResponseBodyInstanceTypesInstanceType(DaraModel):
    def __init__(
        self,
        attributes: main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeAttributes = None,
        baseline_credit: int = None,
        clock: main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeClock = None,
        cpu_architecture: str = None,
        cpu_core_count: int = None,
        cpu_options: main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeCpuOptions = None,
        cpu_speed_frequency: float = None,
        cpu_turbo_frequency: float = None,
        disk_quantity: int = None,
        enhanced_network: main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeEnhancedNetwork = None,
        eni_ipv_6address_quantity: int = None,
        eni_private_ip_address_quantity: int = None,
        eni_quantity: int = None,
        eni_total_quantity: int = None,
        eni_trunk_supported: bool = None,
        eri_quantity: int = None,
        gpuamount: int = None,
        gpumemory_size: float = None,
        gpuspec: str = None,
        initial_credit: int = None,
        instance_bandwidth_rx: int = None,
        instance_bandwidth_tx: int = None,
        instance_category: str = None,
        instance_family_level: str = None,
        instance_pps_rx: int = None,
        instance_pps_tx: int = None,
        instance_type_family: str = None,
        instance_type_id: str = None,
        jumbo_frame_support: bool = None,
        local_storage_amount: int = None,
        local_storage_capacity: int = None,
        local_storage_category: str = None,
        maximum_queue_number_per_eni: int = None,
        memory_size: float = None,
        network_card_quantity: int = None,
        network_cards: main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeNetworkCards = None,
        network_encryption_support: bool = None,
        network_info: main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeNetworkInfo = None,
        nvme_support: str = None,
        physical_processor_model: str = None,
        primary_eni_queue_number: int = None,
        queue_pair_number: int = None,
        secondary_eni_queue_number: int = None,
        supported_boot_modes: main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeSupportedBootModes = None,
        total_eni_queue_quantity: int = None,
    ):
        # The list of specification attributes.
        self.attributes = attributes
        # The baseline vCPU computing performance (overall baseline performance of all vCPUs) per t5 or t6 burstable instance.
        self.baseline_credit = baseline_credit
        # The clock supported by the specification.
        self.clock = clock
        # The CPU architecture. Valid values:
        # 
        # *   X86
        # *   ARM
        self.cpu_architecture = cpu_architecture
        # The number of vCPUs.
        self.cpu_core_count = cpu_core_count
        # The CPU options.
        self.cpu_options = cpu_options
        # The CPU base frequency. Unit: GHz.
        self.cpu_speed_frequency = cpu_speed_frequency
        # The CPU turbo frequency. Unit: GHz.
        self.cpu_turbo_frequency = cpu_turbo_frequency
        # The maximum number of cloud disks per instance.
        self.disk_quantity = disk_quantity
        # >  This parameter is not publicly available.
        self.enhanced_network = enhanced_network
        # The maximum number of IPv6 addresses per ENI.
        self.eni_ipv_6address_quantity = eni_ipv_6address_quantity
        # The maximum number of IPv4 addresses per ENI.
        self.eni_private_ip_address_quantity = eni_private_ip_address_quantity
        # The maximum number of ENIs per instance.
        self.eni_quantity = eni_quantity
        # The maximum number of ENIs, including primary, secondary, and trunk ENIs.
        # 
        # >  This parameter is in invitational preview and is not publicly available.
        self.eni_total_quantity = eni_total_quantity
        # Indicates whether trunk ENIs are supported.
        # 
        # >  This parameter is in invitational preview and is not publicly available.
        self.eni_trunk_supported = eni_trunk_supported
        # The number of ERIs.
        # 
        # >  This parameter is in invitational preview and is not publicly available.
        self.eri_quantity = eri_quantity
        # The number of GPUs.
        self.gpuamount = gpuamount
        # The amount of GPU memory per GPU. Unit: GiB
        self.gpumemory_size = gpumemory_size
        # The GPU model.
        self.gpuspec = gpuspec
        # The initial vCPU credits per t5 or t6 burstable instance.
        self.initial_credit = initial_credit
        # The maximum inbound internal bandwidth. Unit: Kbit/s.
        self.instance_bandwidth_rx = instance_bandwidth_rx
        # The maximum outbound internal bandwidth. Unit: Kbit/s.
        self.instance_bandwidth_tx = instance_bandwidth_tx
        # The category of the instance type. Valid values:
        # 
        # *   General-purpose
        # *   Compute-optimized
        # *   Memory-optimized
        # *   Big data
        # *   Local SSDs
        # *   High Clock Speed
        # *   Enhanced
        # *   Shared
        # *   Compute-optimized with GPU
        # *   Visual Compute-optimized
        # *   Heterogeneous Service
        # *   Compute-optimized with FPGA
        # *   Compute-optimized with NPU
        # *   ECS Bare Metal
        # *   Super Computing Cluster
        # *   High Performance Compute
        self.instance_category = instance_category
        # The level of the instance family. Valid values:
        # 
        # *   EntryLevel: entry level (shared).
        # *   EnterpriseLevel: enterprise level.
        # *   CreditEntryLevel: credit-based entry level. For more information, see [Overview](https://help.aliyun.com/document_detail/59977.html).
        self.instance_family_level = instance_family_level
        # The inbound packet forwarding rate over the internal network. Unit: pps.
        self.instance_pps_rx = instance_pps_rx
        # The outbound packet forwarding rate over the internal network. Unit: pps.
        self.instance_pps_tx = instance_pps_tx
        # The instance family.
        self.instance_type_family = instance_type_family
        # The ID of the instance type.
        self.instance_type_id = instance_type_id
        # Indicates whether jumbo frames are supported.
        self.jumbo_frame_support = jumbo_frame_support
        # The number of local disks per instance.
        self.local_storage_amount = local_storage_amount
        # The capacity of each local disk. Unit: GiB
        self.local_storage_capacity = local_storage_capacity
        # The category of local disks. For more information, see [Local disks](https://help.aliyun.com/document_detail/63138.html). Valid values:
        # 
        # *   local_hdd_pro: local SATA HDDs, which are attached to d1ne or d1 instances
        # *   local_ssd_pro: local NVMe SSDs, which are attached to i2, i2g, i1, ga1, or gn5 instances
        self.local_storage_category = local_storage_category
        # The maximum number of queues per ENI, including primary and secondary ENIs.
        self.maximum_queue_number_per_eni = maximum_queue_number_per_eni
        # The memory size. Unit: GiB
        self.memory_size = memory_size
        # The maximum number of network cards that the instance type supports.
        self.network_card_quantity = network_card_quantity
        # The information about the network cards.
        self.network_cards = network_cards
        # Indicates whether to allow network traffic transmitted over virtual private clouds (VPCs) to be encrypted. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >  This parameter is in invitational preview and is not publicly available.
        self.network_encryption_support = network_encryption_support
        self.network_info = network_info
        # Indicates whether cloud disks can be attached by using the NVMe protocol. Valid values:
        # 
        # *   required: Cloud disks can be attached by using the NVMe protocol.
        # *   unsupported: Cloud disks cannot be attached by using the NVMe protocol.
        self.nvme_support = nvme_support
        # The CPU model.
        self.physical_processor_model = physical_processor_model
        # The default number of queues per primary ENI.
        self.primary_eni_queue_number = primary_eni_queue_number
        # The maximum number of QPs per instance, which varies based on the instance type.
        # 
        # *   For enterprise-level CPU-based instance types, the value of `QueuePairNumber` is the maximum number of QPs per instance.
        # *   For GPU-accelerated instance types, the maximum number of QPs per instance is calculated by using the following formula: Value of `QueuePairNumber` × Value of NetworkCardQuantity.
        self.queue_pair_number = queue_pair_number
        # The default number of queues per secondary ENI.
        self.secondary_eni_queue_number = secondary_eni_queue_number
        # The boot modes supported by the instance type.
        self.supported_boot_modes = supported_boot_modes
        # The maximum number of queues on ENIs that the instance type supports.
        self.total_eni_queue_quantity = total_eni_queue_quantity

    def validate(self):
        if self.attributes:
            self.attributes.validate()
        if self.clock:
            self.clock.validate()
        if self.cpu_options:
            self.cpu_options.validate()
        if self.enhanced_network:
            self.enhanced_network.validate()
        if self.network_cards:
            self.network_cards.validate()
        if self.network_info:
            self.network_info.validate()
        if self.supported_boot_modes:
            self.supported_boot_modes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes.to_map()

        if self.baseline_credit is not None:
            result['BaselineCredit'] = self.baseline_credit

        if self.clock is not None:
            result['Clock'] = self.clock.to_map()

        if self.cpu_architecture is not None:
            result['CpuArchitecture'] = self.cpu_architecture

        if self.cpu_core_count is not None:
            result['CpuCoreCount'] = self.cpu_core_count

        if self.cpu_options is not None:
            result['CpuOptions'] = self.cpu_options.to_map()

        if self.cpu_speed_frequency is not None:
            result['CpuSpeedFrequency'] = self.cpu_speed_frequency

        if self.cpu_turbo_frequency is not None:
            result['CpuTurboFrequency'] = self.cpu_turbo_frequency

        if self.disk_quantity is not None:
            result['DiskQuantity'] = self.disk_quantity

        if self.enhanced_network is not None:
            result['EnhancedNetwork'] = self.enhanced_network.to_map()

        if self.eni_ipv_6address_quantity is not None:
            result['EniIpv6AddressQuantity'] = self.eni_ipv_6address_quantity

        if self.eni_private_ip_address_quantity is not None:
            result['EniPrivateIpAddressQuantity'] = self.eni_private_ip_address_quantity

        if self.eni_quantity is not None:
            result['EniQuantity'] = self.eni_quantity

        if self.eni_total_quantity is not None:
            result['EniTotalQuantity'] = self.eni_total_quantity

        if self.eni_trunk_supported is not None:
            result['EniTrunkSupported'] = self.eni_trunk_supported

        if self.eri_quantity is not None:
            result['EriQuantity'] = self.eri_quantity

        if self.gpuamount is not None:
            result['GPUAmount'] = self.gpuamount

        if self.gpumemory_size is not None:
            result['GPUMemorySize'] = self.gpumemory_size

        if self.gpuspec is not None:
            result['GPUSpec'] = self.gpuspec

        if self.initial_credit is not None:
            result['InitialCredit'] = self.initial_credit

        if self.instance_bandwidth_rx is not None:
            result['InstanceBandwidthRx'] = self.instance_bandwidth_rx

        if self.instance_bandwidth_tx is not None:
            result['InstanceBandwidthTx'] = self.instance_bandwidth_tx

        if self.instance_category is not None:
            result['InstanceCategory'] = self.instance_category

        if self.instance_family_level is not None:
            result['InstanceFamilyLevel'] = self.instance_family_level

        if self.instance_pps_rx is not None:
            result['InstancePpsRx'] = self.instance_pps_rx

        if self.instance_pps_tx is not None:
            result['InstancePpsTx'] = self.instance_pps_tx

        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family

        if self.instance_type_id is not None:
            result['InstanceTypeId'] = self.instance_type_id

        if self.jumbo_frame_support is not None:
            result['JumboFrameSupport'] = self.jumbo_frame_support

        if self.local_storage_amount is not None:
            result['LocalStorageAmount'] = self.local_storage_amount

        if self.local_storage_capacity is not None:
            result['LocalStorageCapacity'] = self.local_storage_capacity

        if self.local_storage_category is not None:
            result['LocalStorageCategory'] = self.local_storage_category

        if self.maximum_queue_number_per_eni is not None:
            result['MaximumQueueNumberPerEni'] = self.maximum_queue_number_per_eni

        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size

        if self.network_card_quantity is not None:
            result['NetworkCardQuantity'] = self.network_card_quantity

        if self.network_cards is not None:
            result['NetworkCards'] = self.network_cards.to_map()

        if self.network_encryption_support is not None:
            result['NetworkEncryptionSupport'] = self.network_encryption_support

        if self.network_info is not None:
            result['NetworkInfo'] = self.network_info.to_map()

        if self.nvme_support is not None:
            result['NvmeSupport'] = self.nvme_support

        if self.physical_processor_model is not None:
            result['PhysicalProcessorModel'] = self.physical_processor_model

        if self.primary_eni_queue_number is not None:
            result['PrimaryEniQueueNumber'] = self.primary_eni_queue_number

        if self.queue_pair_number is not None:
            result['QueuePairNumber'] = self.queue_pair_number

        if self.secondary_eni_queue_number is not None:
            result['SecondaryEniQueueNumber'] = self.secondary_eni_queue_number

        if self.supported_boot_modes is not None:
            result['SupportedBootModes'] = self.supported_boot_modes.to_map()

        if self.total_eni_queue_quantity is not None:
            result['TotalEniQueueQuantity'] = self.total_eni_queue_quantity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            temp_model = main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeAttributes()
            self.attributes = temp_model.from_map(m.get('Attributes'))

        if m.get('BaselineCredit') is not None:
            self.baseline_credit = m.get('BaselineCredit')

        if m.get('Clock') is not None:
            temp_model = main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeClock()
            self.clock = temp_model.from_map(m.get('Clock'))

        if m.get('CpuArchitecture') is not None:
            self.cpu_architecture = m.get('CpuArchitecture')

        if m.get('CpuCoreCount') is not None:
            self.cpu_core_count = m.get('CpuCoreCount')

        if m.get('CpuOptions') is not None:
            temp_model = main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeCpuOptions()
            self.cpu_options = temp_model.from_map(m.get('CpuOptions'))

        if m.get('CpuSpeedFrequency') is not None:
            self.cpu_speed_frequency = m.get('CpuSpeedFrequency')

        if m.get('CpuTurboFrequency') is not None:
            self.cpu_turbo_frequency = m.get('CpuTurboFrequency')

        if m.get('DiskQuantity') is not None:
            self.disk_quantity = m.get('DiskQuantity')

        if m.get('EnhancedNetwork') is not None:
            temp_model = main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeEnhancedNetwork()
            self.enhanced_network = temp_model.from_map(m.get('EnhancedNetwork'))

        if m.get('EniIpv6AddressQuantity') is not None:
            self.eni_ipv_6address_quantity = m.get('EniIpv6AddressQuantity')

        if m.get('EniPrivateIpAddressQuantity') is not None:
            self.eni_private_ip_address_quantity = m.get('EniPrivateIpAddressQuantity')

        if m.get('EniQuantity') is not None:
            self.eni_quantity = m.get('EniQuantity')

        if m.get('EniTotalQuantity') is not None:
            self.eni_total_quantity = m.get('EniTotalQuantity')

        if m.get('EniTrunkSupported') is not None:
            self.eni_trunk_supported = m.get('EniTrunkSupported')

        if m.get('EriQuantity') is not None:
            self.eri_quantity = m.get('EriQuantity')

        if m.get('GPUAmount') is not None:
            self.gpuamount = m.get('GPUAmount')

        if m.get('GPUMemorySize') is not None:
            self.gpumemory_size = m.get('GPUMemorySize')

        if m.get('GPUSpec') is not None:
            self.gpuspec = m.get('GPUSpec')

        if m.get('InitialCredit') is not None:
            self.initial_credit = m.get('InitialCredit')

        if m.get('InstanceBandwidthRx') is not None:
            self.instance_bandwidth_rx = m.get('InstanceBandwidthRx')

        if m.get('InstanceBandwidthTx') is not None:
            self.instance_bandwidth_tx = m.get('InstanceBandwidthTx')

        if m.get('InstanceCategory') is not None:
            self.instance_category = m.get('InstanceCategory')

        if m.get('InstanceFamilyLevel') is not None:
            self.instance_family_level = m.get('InstanceFamilyLevel')

        if m.get('InstancePpsRx') is not None:
            self.instance_pps_rx = m.get('InstancePpsRx')

        if m.get('InstancePpsTx') is not None:
            self.instance_pps_tx = m.get('InstancePpsTx')

        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')

        if m.get('InstanceTypeId') is not None:
            self.instance_type_id = m.get('InstanceTypeId')

        if m.get('JumboFrameSupport') is not None:
            self.jumbo_frame_support = m.get('JumboFrameSupport')

        if m.get('LocalStorageAmount') is not None:
            self.local_storage_amount = m.get('LocalStorageAmount')

        if m.get('LocalStorageCapacity') is not None:
            self.local_storage_capacity = m.get('LocalStorageCapacity')

        if m.get('LocalStorageCategory') is not None:
            self.local_storage_category = m.get('LocalStorageCategory')

        if m.get('MaximumQueueNumberPerEni') is not None:
            self.maximum_queue_number_per_eni = m.get('MaximumQueueNumberPerEni')

        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')

        if m.get('NetworkCardQuantity') is not None:
            self.network_card_quantity = m.get('NetworkCardQuantity')

        if m.get('NetworkCards') is not None:
            temp_model = main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeNetworkCards()
            self.network_cards = temp_model.from_map(m.get('NetworkCards'))

        if m.get('NetworkEncryptionSupport') is not None:
            self.network_encryption_support = m.get('NetworkEncryptionSupport')

        if m.get('NetworkInfo') is not None:
            temp_model = main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeNetworkInfo()
            self.network_info = temp_model.from_map(m.get('NetworkInfo'))

        if m.get('NvmeSupport') is not None:
            self.nvme_support = m.get('NvmeSupport')

        if m.get('PhysicalProcessorModel') is not None:
            self.physical_processor_model = m.get('PhysicalProcessorModel')

        if m.get('PrimaryEniQueueNumber') is not None:
            self.primary_eni_queue_number = m.get('PrimaryEniQueueNumber')

        if m.get('QueuePairNumber') is not None:
            self.queue_pair_number = m.get('QueuePairNumber')

        if m.get('SecondaryEniQueueNumber') is not None:
            self.secondary_eni_queue_number = m.get('SecondaryEniQueueNumber')

        if m.get('SupportedBootModes') is not None:
            temp_model = main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeSupportedBootModes()
            self.supported_boot_modes = temp_model.from_map(m.get('SupportedBootModes'))

        if m.get('TotalEniQueueQuantity') is not None:
            self.total_eni_queue_quantity = m.get('TotalEniQueueQuantity')

        return self

class DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeSupportedBootModes(DaraModel):
    def __init__(
        self,
        supported_boot_mode: List[str] = None,
    ):
        self.supported_boot_mode = supported_boot_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.supported_boot_mode is not None:
            result['SupportedBootMode'] = self.supported_boot_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedBootMode') is not None:
            self.supported_boot_mode = m.get('SupportedBootMode')

        return self

class DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeNetworkInfo(DaraModel):
    def __init__(
        self,
        bandwidth_weighting: main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeNetworkInfoBandwidthWeighting = None,
    ):
        self.bandwidth_weighting = bandwidth_weighting

    def validate(self):
        if self.bandwidth_weighting:
            self.bandwidth_weighting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_weighting is not None:
            result['BandwidthWeighting'] = self.bandwidth_weighting.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthWeighting') is not None:
            temp_model = main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeNetworkInfoBandwidthWeighting()
            self.bandwidth_weighting = temp_model.from_map(m.get('BandwidthWeighting'))

        return self

class DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeNetworkInfoBandwidthWeighting(DaraModel):
    def __init__(
        self,
        weighting_infos: main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeNetworkInfoBandwidthWeightingWeightingInfos = None,
    ):
        self.weighting_infos = weighting_infos

    def validate(self):
        if self.weighting_infos:
            self.weighting_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.weighting_infos is not None:
            result['WeightingInfos'] = self.weighting_infos.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WeightingInfos') is not None:
            temp_model = main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeNetworkInfoBandwidthWeightingWeightingInfos()
            self.weighting_infos = temp_model.from_map(m.get('WeightingInfos'))

        return self

class DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeNetworkInfoBandwidthWeightingWeightingInfos(DaraModel):
    def __init__(
        self,
        weighting_info: List[main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeNetworkInfoBandwidthWeightingWeightingInfosWeightingInfo] = None,
    ):
        self.weighting_info = weighting_info

    def validate(self):
        if self.weighting_info:
            for v1 in self.weighting_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['WeightingInfo'] = []
        if self.weighting_info is not None:
            for k1 in self.weighting_info:
                result['WeightingInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.weighting_info = []
        if m.get('WeightingInfo') is not None:
            for k1 in m.get('WeightingInfo'):
                temp_model = main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeNetworkInfoBandwidthWeightingWeightingInfosWeightingInfo()
                self.weighting_info.append(temp_model.from_map(k1))

        return self

class DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeNetworkInfoBandwidthWeightingWeightingInfosWeightingInfo(DaraModel):
    def __init__(
        self,
        ebs_bandwidth: int = None,
        ebs_burst_bandwidth: int = None,
        name: str = None,
        vpc_bandwidth: int = None,
        vpc_burst_bandwidth: int = None,
    ):
        self.ebs_bandwidth = ebs_bandwidth
        self.ebs_burst_bandwidth = ebs_burst_bandwidth
        self.name = name
        self.vpc_bandwidth = vpc_bandwidth
        self.vpc_burst_bandwidth = vpc_burst_bandwidth

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ebs_bandwidth is not None:
            result['EbsBandwidth'] = self.ebs_bandwidth

        if self.ebs_burst_bandwidth is not None:
            result['EbsBurstBandwidth'] = self.ebs_burst_bandwidth

        if self.name is not None:
            result['Name'] = self.name

        if self.vpc_bandwidth is not None:
            result['VpcBandwidth'] = self.vpc_bandwidth

        if self.vpc_burst_bandwidth is not None:
            result['VpcBurstBandwidth'] = self.vpc_burst_bandwidth

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EbsBandwidth') is not None:
            self.ebs_bandwidth = m.get('EbsBandwidth')

        if m.get('EbsBurstBandwidth') is not None:
            self.ebs_burst_bandwidth = m.get('EbsBurstBandwidth')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('VpcBandwidth') is not None:
            self.vpc_bandwidth = m.get('VpcBandwidth')

        if m.get('VpcBurstBandwidth') is not None:
            self.vpc_burst_bandwidth = m.get('VpcBurstBandwidth')

        return self

class DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeNetworkCards(DaraModel):
    def __init__(
        self,
        network_card_info: List[main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeNetworkCardsNetworkCardInfo] = None,
    ):
        self.network_card_info = network_card_info

    def validate(self):
        if self.network_card_info:
            for v1 in self.network_card_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkCardInfo'] = []
        if self.network_card_info is not None:
            for k1 in self.network_card_info:
                result['NetworkCardInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_card_info = []
        if m.get('NetworkCardInfo') is not None:
            for k1 in m.get('NetworkCardInfo'):
                temp_model = main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeNetworkCardsNetworkCardInfo()
                self.network_card_info.append(temp_model.from_map(k1))

        return self

class DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeNetworkCardsNetworkCardInfo(DaraModel):
    def __init__(
        self,
        network_card_index: int = None,
    ):
        # The index of the network card.
        self.network_card_index = network_card_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_card_index is not None:
            result['NetworkCardIndex'] = self.network_card_index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkCardIndex') is not None:
            self.network_card_index = m.get('NetworkCardIndex')

        return self

class DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeEnhancedNetwork(DaraModel):
    def __init__(
        self,
        rss_support: bool = None,
        sriov_support: bool = None,
        vf_queue_number_per_eni: int = None,
    ):
        # >  This parameter is not publicly available.
        self.rss_support = rss_support
        # >  This parameter is not publicly available.
        self.sriov_support = sriov_support
        # >  This parameter is not publicly available.
        self.vf_queue_number_per_eni = vf_queue_number_per_eni

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rss_support is not None:
            result['RssSupport'] = self.rss_support

        if self.sriov_support is not None:
            result['SriovSupport'] = self.sriov_support

        if self.vf_queue_number_per_eni is not None:
            result['VfQueueNumberPerEni'] = self.vf_queue_number_per_eni

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RssSupport') is not None:
            self.rss_support = m.get('RssSupport')

        if m.get('SriovSupport') is not None:
            self.sriov_support = m.get('SriovSupport')

        if m.get('VfQueueNumberPerEni') is not None:
            self.vf_queue_number_per_eni = m.get('VfQueueNumberPerEni')

        return self

class DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeCpuOptions(DaraModel):
    def __init__(
        self,
        core: int = None,
        core_factor: int = None,
        hyper_threading_adjustable: bool = None,
        supported_topology_types: main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeCpuOptionsSupportedTopologyTypes = None,
        threads_per_core: int = None,
    ):
        # The number of CPU cores.
        self.core = core
        # The CPU option step size.
        self.core_factor = core_factor
        # Indicates whether HT can be enabled or disabled.
        self.hyper_threading_adjustable = hyper_threading_adjustable
        # The CPU topology types of the instance type.
        self.supported_topology_types = supported_topology_types
        # The number of threads per CPU core.
        # 
        # >  `If the value of CpuOptions.ThreadPerCore is 1, Hyper-Threading (HT) is disabled.`
        self.threads_per_core = threads_per_core

    def validate(self):
        if self.supported_topology_types:
            self.supported_topology_types.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.core is not None:
            result['Core'] = self.core

        if self.core_factor is not None:
            result['CoreFactor'] = self.core_factor

        if self.hyper_threading_adjustable is not None:
            result['HyperThreadingAdjustable'] = self.hyper_threading_adjustable

        if self.supported_topology_types is not None:
            result['SupportedTopologyTypes'] = self.supported_topology_types.to_map()

        if self.threads_per_core is not None:
            result['ThreadsPerCore'] = self.threads_per_core

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Core') is not None:
            self.core = m.get('Core')

        if m.get('CoreFactor') is not None:
            self.core_factor = m.get('CoreFactor')

        if m.get('HyperThreadingAdjustable') is not None:
            self.hyper_threading_adjustable = m.get('HyperThreadingAdjustable')

        if m.get('SupportedTopologyTypes') is not None:
            temp_model = main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeCpuOptionsSupportedTopologyTypes()
            self.supported_topology_types = temp_model.from_map(m.get('SupportedTopologyTypes'))

        if m.get('ThreadsPerCore') is not None:
            self.threads_per_core = m.get('ThreadsPerCore')

        return self

class DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeCpuOptionsSupportedTopologyTypes(DaraModel):
    def __init__(
        self,
        supported_topology_type: List[str] = None,
    ):
        self.supported_topology_type = supported_topology_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.supported_topology_type is not None:
            result['SupportedTopologyType'] = self.supported_topology_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedTopologyType') is not None:
            self.supported_topology_type = m.get('SupportedTopologyType')

        return self

class DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeClock(DaraModel):
    def __init__(
        self,
        ptp_support: str = None,
    ):
        # Whether PTP is supported. Possible values:
        # 
        # *   supported
        # *   unsupported
        self.ptp_support = ptp_support

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ptp_support is not None:
            result['PtpSupport'] = self.ptp_support

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PtpSupport') is not None:
            self.ptp_support = m.get('PtpSupport')

        return self

class DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeAttributes(DaraModel):
    def __init__(
        self,
        attribute: List[main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeAttributesAttribute] = None,
    ):
        self.attribute = attribute

    def validate(self):
        if self.attribute:
            for v1 in self.attribute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Attribute'] = []
        if self.attribute is not None:
            for k1 in self.attribute:
                result['Attribute'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attribute = []
        if m.get('Attribute') is not None:
            for k1 in m.get('Attribute'):
                temp_model = main_models.DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeAttributesAttribute()
                self.attribute.append(temp_model.from_map(k1))

        return self

class DescribeInstanceTypesResponseBodyInstanceTypesInstanceTypeAttributesAttribute(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the attribute.
        self.name = name
        # The attribute value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

