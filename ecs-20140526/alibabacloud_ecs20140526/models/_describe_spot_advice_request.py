# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeSpotAdviceRequest(DaraModel):
    def __init__(
        self,
        cores: int = None,
        gpu_amount: int = None,
        gpu_spec: str = None,
        instance_family_level: str = None,
        instance_type_family: str = None,
        instance_types: List[str] = None,
        memory: float = None,
        min_cores: int = None,
        min_memory: float = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        zone_id: str = None,
    ):
        # The number of vCPUs of the instance type. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        self.cores = cores
        # The number of GPUs that a GPU-accelerated instance has. For information about the valid values, see [GPU-accelerated compute optimized instance types](https://help.aliyun.com/document_detail/108496.html).
        self.gpu_amount = gpu_amount
        # The GPU type. Valid values:
        # 
        # *   NVIDIA P4
        # *   NVIDIA T4
        # *   NVIDIA P100
        # *   NVIDIA V100
        # 
        # This parameter is left empty by default, which indicates that all GPU types are queried. For more information, see [GPU-accelerated compute-optimized and vGPU-accelerated instance families](https://help.aliyun.com/document_detail/108496.html).
        self.gpu_spec = gpu_spec
        # The level of the instance family. Valid values:
        # 
        # *   EntryLevel.
        # *   EnterpriseLevel.
        # *   CreditEntryLevel. For more information, see [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html).
        # 
        # This parameter is left empty by default, which indicates that instance families at all levels are queried.
        self.instance_family_level = instance_family_level
        # The instance family. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        self.instance_type_family = instance_type_family
        # The instance types. You can specify up to 10 instance types.
        self.instance_types = instance_types
        # The memory size of the instance type. Unit: GiB. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        self.memory = memory
        # The minimum number of vCPUs of the instance type. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        self.min_cores = min_cores
        # The minimum memory size of the instance type. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        self.min_memory = min_memory
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The zone ID.
        # 
        # This parameter is left empty by default, which indicates that all zones in the specified region are queried.
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

        if self.gpu_amount is not None:
            result['GpuAmount'] = self.gpu_amount

        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec

        if self.instance_family_level is not None:
            result['InstanceFamilyLevel'] = self.instance_family_level

        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family

        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.min_cores is not None:
            result['MinCores'] = self.min_cores

        if self.min_memory is not None:
            result['MinMemory'] = self.min_memory

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

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')

        if m.get('GpuAmount') is not None:
            self.gpu_amount = m.get('GpuAmount')

        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')

        if m.get('InstanceFamilyLevel') is not None:
            self.instance_family_level = m.get('InstanceFamilyLevel')

        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')

        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('MinCores') is not None:
            self.min_cores = m.get('MinCores')

        if m.get('MinMemory') is not None:
            self.min_memory = m.get('MinMemory')

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

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

