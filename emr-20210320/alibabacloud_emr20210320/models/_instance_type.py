# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InstanceType(DaraModel):
    def __init__(
        self,
        cpu_architecture: str = None,
        cpu_core: int = None,
        instance_category: str = None,
        instance_type: str = None,
        instance_type_family: str = None,
        local_storage_amount: int = None,
        local_storage_capacity: int = None,
        modify_type: str = None,
        optimized: bool = None,
    ):
        # The CPU architecture. Valid values:
        # 
        # - `X86`: X86 architecture.
        # 
        # - `ARM`: ARM architecture.
        self.cpu_architecture = cpu_architecture
        # The number of vCPUs.
        self.cpu_core = cpu_core
        # The instance category. Valid values:
        # 
        # - `General-purpose`: A general-purpose instance type.
        # 
        # - `Compute-optimized`: A compute-optimized instance type.
        # 
        # - `Memory-optimized`: A memory-optimized instance type.
        # 
        # - `Big data`: A big data instance type.
        # 
        # - `Local SSDs`: A local SSD instance type.
        # 
        # - `High Clock Speed`: A high clock speed instance type.
        # 
        # - `Enhanced`: An enhanced instance type.
        # 
        # - `Shared`: A shared instance type.
        # 
        # - `Compute-optimized with GPU`: A compute-optimized instance type with GPUs.
        # 
        # - `Visual Compute-optimized`: A visual compute-optimized instance type.
        # 
        # - `Heterogeneous Service`: A heterogeneous service instance type.
        # 
        # - `Compute-optimized with FPGA`: A compute-optimized instance type with FPGAs.
        # 
        # - `Compute-optimized with NPU`: A compute-optimized instance type with NPUs.
        # 
        # - `ECS Bare Metal`: An ECS Bare Metal instance.
        # 
        # - `Super Computing Cluster`: A supercomputing cluster instance type.
        self.instance_category = instance_category
        # The ECS instance type. For more information, see [Instance type families](https://help.aliyun.com/document_detail/25378.html).
        self.instance_type = instance_type
        # The instance type family. For valid values, see the ECS documentation for [DescribeInstanceTypeFamilies](https://help.aliyun.com/document_detail/25621.html).
        self.instance_type_family = instance_type_family
        # The number of local disks attached to the instance.
        self.local_storage_amount = local_storage_amount
        # The capacity of each local disk attached to the instance, in GiB.
        self.local_storage_capacity = local_storage_capacity
        self.modify_type = modify_type
        # Specifies whether the instance type is I/O optimized. Valid values:
        # 
        # - `true`: The instance type is I/O optimized.
        # 
        # - `false`: The instance type is not I/O optimized.
        self.optimized = optimized

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_architecture is not None:
            result['CpuArchitecture'] = self.cpu_architecture

        if self.cpu_core is not None:
            result['CpuCore'] = self.cpu_core

        if self.instance_category is not None:
            result['InstanceCategory'] = self.instance_category

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family

        if self.local_storage_amount is not None:
            result['LocalStorageAmount'] = self.local_storage_amount

        if self.local_storage_capacity is not None:
            result['LocalStorageCapacity'] = self.local_storage_capacity

        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type

        if self.optimized is not None:
            result['Optimized'] = self.optimized

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuArchitecture') is not None:
            self.cpu_architecture = m.get('CpuArchitecture')

        if m.get('CpuCore') is not None:
            self.cpu_core = m.get('CpuCore')

        if m.get('InstanceCategory') is not None:
            self.instance_category = m.get('InstanceCategory')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')

        if m.get('LocalStorageAmount') is not None:
            self.local_storage_amount = m.get('LocalStorageAmount')

        if m.get('LocalStorageCapacity') is not None:
            self.local_storage_capacity = m.get('LocalStorageCapacity')

        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')

        if m.get('Optimized') is not None:
            self.optimized = m.get('Optimized')

        return self

