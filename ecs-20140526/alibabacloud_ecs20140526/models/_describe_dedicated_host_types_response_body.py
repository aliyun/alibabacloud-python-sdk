# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeDedicatedHostTypesResponseBody(DaraModel):
    def __init__(
        self,
        dedicated_host_types: main_models.DescribeDedicatedHostTypesResponseBodyDedicatedHostTypes = None,
        request_id: str = None,
    ):
        # Details about the dedicated host types.
        self.dedicated_host_types = dedicated_host_types
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dedicated_host_types:
            self.dedicated_host_types.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_host_types is not None:
            result['DedicatedHostTypes'] = self.dedicated_host_types.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostTypes') is not None:
            temp_model = main_models.DescribeDedicatedHostTypesResponseBodyDedicatedHostTypes()
            self.dedicated_host_types = temp_model.from_map(m.get('DedicatedHostTypes'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDedicatedHostTypesResponseBodyDedicatedHostTypes(DaraModel):
    def __init__(
        self,
        dedicated_host_type: List[main_models.DescribeDedicatedHostTypesResponseBodyDedicatedHostTypesDedicatedHostType] = None,
    ):
        self.dedicated_host_type = dedicated_host_type

    def validate(self):
        if self.dedicated_host_type:
            for v1 in self.dedicated_host_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DedicatedHostType'] = []
        if self.dedicated_host_type is not None:
            for k1 in self.dedicated_host_type:
                result['DedicatedHostType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dedicated_host_type = []
        if m.get('DedicatedHostType') is not None:
            for k1 in m.get('DedicatedHostType'):
                temp_model = main_models.DescribeDedicatedHostTypesResponseBodyDedicatedHostTypesDedicatedHostType()
                self.dedicated_host_type.append(temp_model.from_map(k1))

        return self

class DescribeDedicatedHostTypesResponseBodyDedicatedHostTypesDedicatedHostType(DaraModel):
    def __init__(
        self,
        cores: int = None,
        cpu_over_commit_ratio_range: str = None,
        dedicated_host_type: str = None,
        gpuspec: str = None,
        local_storage_amount: int = None,
        local_storage_capacity: int = None,
        local_storage_category: str = None,
        memory_size: float = None,
        physical_gpus: int = None,
        sockets: int = None,
        support_cpu_over_commit_ratio: bool = None,
        supported_instance_type_families: main_models.DescribeDedicatedHostTypesResponseBodyDedicatedHostTypesDedicatedHostTypeSupportedInstanceTypeFamilies = None,
        supported_instance_types_list: main_models.DescribeDedicatedHostTypesResponseBodyDedicatedHostTypesDedicatedHostTypeSupportedInstanceTypesList = None,
        total_vcpus: int = None,
        total_vgpus: int = None,
    ):
        # The number of cores per physical CPU.
        self.cores = cores
        # The supported CPU overcommit ratio range.
        self.cpu_over_commit_ratio_range = cpu_over_commit_ratio_range
        # The dedicated host type.
        self.dedicated_host_type = dedicated_host_type
        # The GPU model.
        self.gpuspec = gpuspec
        # The number of local disks on a dedicated host.
        self.local_storage_amount = local_storage_amount
        # The capacity of a local disk. Unit: GiB.
        self.local_storage_capacity = local_storage_capacity
        # The category of local disks.
        self.local_storage_category = local_storage_category
        # The memory size. Unit: GiB.
        self.memory_size = memory_size
        # The number of physical GPUs.
        self.physical_gpus = physical_gpus
        # The number of physical CPUs.
        self.sockets = sockets
        # Indicates whether the CPU overcommit ratio settings are supported.
        self.support_cpu_over_commit_ratio = support_cpu_over_commit_ratio
        # The ECS instance families supported by the dedicated host type.
        self.supported_instance_type_families = supported_instance_type_families
        # The ECS instance types supported by the dedicated host type.
        self.supported_instance_types_list = supported_instance_types_list
        # The total number of vCPUs.
        self.total_vcpus = total_vcpus
        # The total number of vGPUs.
        self.total_vgpus = total_vgpus

    def validate(self):
        if self.supported_instance_type_families:
            self.supported_instance_type_families.validate()
        if self.supported_instance_types_list:
            self.supported_instance_types_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cores is not None:
            result['Cores'] = self.cores

        if self.cpu_over_commit_ratio_range is not None:
            result['CpuOverCommitRatioRange'] = self.cpu_over_commit_ratio_range

        if self.dedicated_host_type is not None:
            result['DedicatedHostType'] = self.dedicated_host_type

        if self.gpuspec is not None:
            result['GPUSpec'] = self.gpuspec

        if self.local_storage_amount is not None:
            result['LocalStorageAmount'] = self.local_storage_amount

        if self.local_storage_capacity is not None:
            result['LocalStorageCapacity'] = self.local_storage_capacity

        if self.local_storage_category is not None:
            result['LocalStorageCategory'] = self.local_storage_category

        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size

        if self.physical_gpus is not None:
            result['PhysicalGpus'] = self.physical_gpus

        if self.sockets is not None:
            result['Sockets'] = self.sockets

        if self.support_cpu_over_commit_ratio is not None:
            result['SupportCpuOverCommitRatio'] = self.support_cpu_over_commit_ratio

        if self.supported_instance_type_families is not None:
            result['SupportedInstanceTypeFamilies'] = self.supported_instance_type_families.to_map()

        if self.supported_instance_types_list is not None:
            result['SupportedInstanceTypesList'] = self.supported_instance_types_list.to_map()

        if self.total_vcpus is not None:
            result['TotalVcpus'] = self.total_vcpus

        if self.total_vgpus is not None:
            result['TotalVgpus'] = self.total_vgpus

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')

        if m.get('CpuOverCommitRatioRange') is not None:
            self.cpu_over_commit_ratio_range = m.get('CpuOverCommitRatioRange')

        if m.get('DedicatedHostType') is not None:
            self.dedicated_host_type = m.get('DedicatedHostType')

        if m.get('GPUSpec') is not None:
            self.gpuspec = m.get('GPUSpec')

        if m.get('LocalStorageAmount') is not None:
            self.local_storage_amount = m.get('LocalStorageAmount')

        if m.get('LocalStorageCapacity') is not None:
            self.local_storage_capacity = m.get('LocalStorageCapacity')

        if m.get('LocalStorageCategory') is not None:
            self.local_storage_category = m.get('LocalStorageCategory')

        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')

        if m.get('PhysicalGpus') is not None:
            self.physical_gpus = m.get('PhysicalGpus')

        if m.get('Sockets') is not None:
            self.sockets = m.get('Sockets')

        if m.get('SupportCpuOverCommitRatio') is not None:
            self.support_cpu_over_commit_ratio = m.get('SupportCpuOverCommitRatio')

        if m.get('SupportedInstanceTypeFamilies') is not None:
            temp_model = main_models.DescribeDedicatedHostTypesResponseBodyDedicatedHostTypesDedicatedHostTypeSupportedInstanceTypeFamilies()
            self.supported_instance_type_families = temp_model.from_map(m.get('SupportedInstanceTypeFamilies'))

        if m.get('SupportedInstanceTypesList') is not None:
            temp_model = main_models.DescribeDedicatedHostTypesResponseBodyDedicatedHostTypesDedicatedHostTypeSupportedInstanceTypesList()
            self.supported_instance_types_list = temp_model.from_map(m.get('SupportedInstanceTypesList'))

        if m.get('TotalVcpus') is not None:
            self.total_vcpus = m.get('TotalVcpus')

        if m.get('TotalVgpus') is not None:
            self.total_vgpus = m.get('TotalVgpus')

        return self

class DescribeDedicatedHostTypesResponseBodyDedicatedHostTypesDedicatedHostTypeSupportedInstanceTypesList(DaraModel):
    def __init__(
        self,
        supported_instance_types_list: List[str] = None,
    ):
        self.supported_instance_types_list = supported_instance_types_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.supported_instance_types_list is not None:
            result['SupportedInstanceTypesList'] = self.supported_instance_types_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedInstanceTypesList') is not None:
            self.supported_instance_types_list = m.get('SupportedInstanceTypesList')

        return self

class DescribeDedicatedHostTypesResponseBodyDedicatedHostTypesDedicatedHostTypeSupportedInstanceTypeFamilies(DaraModel):
    def __init__(
        self,
        supported_instance_type_family: List[str] = None,
    ):
        self.supported_instance_type_family = supported_instance_type_family

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.supported_instance_type_family is not None:
            result['SupportedInstanceTypeFamily'] = self.supported_instance_type_family

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedInstanceTypeFamily') is not None:
            self.supported_instance_type_family = m.get('SupportedInstanceTypeFamily')

        return self

