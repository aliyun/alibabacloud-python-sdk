# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDedicatedHostGroupsResponseBody(DaraModel):
    def __init__(
        self,
        dedicated_host_groups: main_models.DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroups = None,
        request_id: str = None,
    ):
        # The information about dedicated clusters returned.
        self.dedicated_host_groups = dedicated_host_groups
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dedicated_host_groups:
            self.dedicated_host_groups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_host_groups is not None:
            result['DedicatedHostGroups'] = self.dedicated_host_groups.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostGroups') is not None:
            temp_model = main_models.DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroups()
            self.dedicated_host_groups = temp_model.from_map(m.get('DedicatedHostGroups'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroups(DaraModel):
    def __init__(
        self,
        dedicated_host_groups: List[main_models.DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroups] = None,
    ):
        self.dedicated_host_groups = dedicated_host_groups

    def validate(self):
        if self.dedicated_host_groups:
            for v1 in self.dedicated_host_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DedicatedHostGroups'] = []
        if self.dedicated_host_groups is not None:
            for k1 in self.dedicated_host_groups:
                result['DedicatedHostGroups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dedicated_host_groups = []
        if m.get('DedicatedHostGroups') is not None:
            for k1 in m.get('DedicatedHostGroups'):
                temp_model = main_models.DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroups()
                self.dedicated_host_groups.append(temp_model.from_map(k1))

        return self

class DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroups(DaraModel):
    def __init__(
        self,
        allocation_policy: str = None,
        bastion_instance_id: str = None,
        cpu_allocate_ration: float = None,
        cpu_allocated_amount: float = None,
        cpu_allocation_ratio: int = None,
        create_time: str = None,
        dedicated_host_count_group_by_host_type: Dict[str, Any] = None,
        dedicated_host_group_desc: str = None,
        dedicated_host_group_id: str = None,
        disk_allocate_ration: float = None,
        disk_allocated_amount: float = None,
        disk_allocation_ratio: int = None,
        disk_used_amount: float = None,
        disk_utility: float = None,
        engine: str = None,
        host_number: int = None,
        host_replace_policy: str = None,
        instance_number: int = None,
        mem_allocate_ration: float = None,
        mem_allocated_amount: float = None,
        mem_allocation_ratio: int = None,
        mem_used_amount: float = None,
        mem_utility: float = None,
        open_permission: str = None,
        text: str = None,
        vpcid: str = None,
        zone_idlist: main_models.DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroupsZoneIDList = None,
    ):
        # The policy based on which the system allocates resources in the dedicated cluster. Valid values:
        # 
        # *   **Evenly**: The system evenly allocates the resources to all the hosts in the dedicated cluster.
        # *   **Intensively**: The system preferentially allocates the resources to the heavily loaded hosts in the dedicated cluster.
        self.allocation_policy = allocation_policy
        # The ID of the bastion host.
        self.bastion_instance_id = bastion_instance_id
        # The percentage of allocated cores in the dedicated cluster. Unit: %.
        self.cpu_allocate_ration = cpu_allocate_ration
        # The number of allocated cores in the dedicated cluster.
        self.cpu_allocated_amount = cpu_allocated_amount
        # The core overcommitment ratio of the dedicated cluster. Unit: %. For more information about the core overcommitment ratio, see [Manage a dedicated cluster](https://help.aliyun.com/document_detail/182328.html).
        self.cpu_allocation_ratio = cpu_allocation_ratio
        # The timestamp when the dedicated cluster was created.
        self.create_time = create_time
        # The type of storage media that is used for the hosts in the dedicated cluster. Valid values:
        # 
        # *   **dhg_cloud_ssd**: cloud disks
        # *   **dhg_local_ssd**: local disks
        self.dedicated_host_count_group_by_host_type = dedicated_host_count_group_by_host_type
        # The name of the dedicated cluster.
        self.dedicated_host_group_desc = dedicated_host_group_desc
        # The ID of the dedicated cluster.
        self.dedicated_host_group_id = dedicated_host_group_id
        # The percentage of allocated disk space in the dedicated cluster. Unit: %.
        self.disk_allocate_ration = disk_allocate_ration
        # The amount of allocated disk space in the dedicated cluster. Unit: GB.
        self.disk_allocated_amount = disk_allocated_amount
        # The disk overcommitment ratio of the dedicated cluster. Unit: %. For more information about the core overcommitment ratio, see [Manage a dedicated cluster](https://help.aliyun.com/document_detail/182328.html).
        self.disk_allocation_ratio = disk_allocation_ratio
        # The amount of used disk space in the dedicated cluster. Unit: GB.
        self.disk_used_amount = disk_used_amount
        # The disk usage of the dedicated cluster. Unit: %.
        self.disk_utility = disk_utility
        # The database engine of the instances in the dedicated cluster.
        self.engine = engine
        # The total number of hosts in the dedicated cluster.
        self.host_number = host_number
        # The policy that is used to handle host failures. Valid values:
        # 
        # *   **Auto**: The system automatically replaces faulty hosts.
        # *   **Manual**: You must manually replace faulty hosts.
        self.host_replace_policy = host_replace_policy
        # The total number of instances in the dedicated cluster.
        self.instance_number = instance_number
        # The percentage of allocated memory space in the dedicated cluster. Unit: %.
        self.mem_allocate_ration = mem_allocate_ration
        # The amount of allocated memory space in the dedicated cluster.
        self.mem_allocated_amount = mem_allocated_amount
        # The memory overcommitment ratio of the dedicated cluster. Unit: %. For more information about the core overcommitment ratio, see [Manage a dedicated cluster](https://help.aliyun.com/document_detail/182328.html).
        self.mem_allocation_ratio = mem_allocation_ratio
        # The amount of used memory space in the dedicated cluster. Unit: MB.
        self.mem_used_amount = mem_used_amount
        # The memory usage of the dedicated cluster. Unit: %.
        self.mem_utility = mem_utility
        # Indicates whether the feature that allows you to have the OS permissions on the host is enabled. Valid values:
        # 
        # *   **0** or **null**: The permissions cannot be granted.
        # *   **1**: The permissions can be granted.
        # *   **3**: The permissions have been granted.
        self.open_permission = open_permission
        # The name and ID of the dedicated cluster. The value consists of **DedicatedHostGroupDesc** and **DedicatedHostGroupId**. Format: DedicatedHostGroupDesc/DedicatedHostGroupId.
        self.text = text
        # The ID of the virtual private cloud (VPC) to which the dedicated cluster belongs.
        self.vpcid = vpcid
        # The zones to which the hosts of the dedicated cluster belong.
        self.zone_idlist = zone_idlist

    def validate(self):
        if self.zone_idlist:
            self.zone_idlist.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_policy is not None:
            result['AllocationPolicy'] = self.allocation_policy

        if self.bastion_instance_id is not None:
            result['BastionInstanceId'] = self.bastion_instance_id

        if self.cpu_allocate_ration is not None:
            result['CpuAllocateRation'] = self.cpu_allocate_ration

        if self.cpu_allocated_amount is not None:
            result['CpuAllocatedAmount'] = self.cpu_allocated_amount

        if self.cpu_allocation_ratio is not None:
            result['CpuAllocationRatio'] = self.cpu_allocation_ratio

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dedicated_host_count_group_by_host_type is not None:
            result['DedicatedHostCountGroupByHostType'] = self.dedicated_host_count_group_by_host_type

        if self.dedicated_host_group_desc is not None:
            result['DedicatedHostGroupDesc'] = self.dedicated_host_group_desc

        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id

        if self.disk_allocate_ration is not None:
            result['DiskAllocateRation'] = self.disk_allocate_ration

        if self.disk_allocated_amount is not None:
            result['DiskAllocatedAmount'] = self.disk_allocated_amount

        if self.disk_allocation_ratio is not None:
            result['DiskAllocationRatio'] = self.disk_allocation_ratio

        if self.disk_used_amount is not None:
            result['DiskUsedAmount'] = self.disk_used_amount

        if self.disk_utility is not None:
            result['DiskUtility'] = self.disk_utility

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.host_number is not None:
            result['HostNumber'] = self.host_number

        if self.host_replace_policy is not None:
            result['HostReplacePolicy'] = self.host_replace_policy

        if self.instance_number is not None:
            result['InstanceNumber'] = self.instance_number

        if self.mem_allocate_ration is not None:
            result['MemAllocateRation'] = self.mem_allocate_ration

        if self.mem_allocated_amount is not None:
            result['MemAllocatedAmount'] = self.mem_allocated_amount

        if self.mem_allocation_ratio is not None:
            result['MemAllocationRatio'] = self.mem_allocation_ratio

        if self.mem_used_amount is not None:
            result['MemUsedAmount'] = self.mem_used_amount

        if self.mem_utility is not None:
            result['MemUtility'] = self.mem_utility

        if self.open_permission is not None:
            result['OpenPermission'] = self.open_permission

        if self.text is not None:
            result['Text'] = self.text

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.zone_idlist is not None:
            result['ZoneIDList'] = self.zone_idlist.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationPolicy') is not None:
            self.allocation_policy = m.get('AllocationPolicy')

        if m.get('BastionInstanceId') is not None:
            self.bastion_instance_id = m.get('BastionInstanceId')

        if m.get('CpuAllocateRation') is not None:
            self.cpu_allocate_ration = m.get('CpuAllocateRation')

        if m.get('CpuAllocatedAmount') is not None:
            self.cpu_allocated_amount = m.get('CpuAllocatedAmount')

        if m.get('CpuAllocationRatio') is not None:
            self.cpu_allocation_ratio = m.get('CpuAllocationRatio')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DedicatedHostCountGroupByHostType') is not None:
            self.dedicated_host_count_group_by_host_type = m.get('DedicatedHostCountGroupByHostType')

        if m.get('DedicatedHostGroupDesc') is not None:
            self.dedicated_host_group_desc = m.get('DedicatedHostGroupDesc')

        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')

        if m.get('DiskAllocateRation') is not None:
            self.disk_allocate_ration = m.get('DiskAllocateRation')

        if m.get('DiskAllocatedAmount') is not None:
            self.disk_allocated_amount = m.get('DiskAllocatedAmount')

        if m.get('DiskAllocationRatio') is not None:
            self.disk_allocation_ratio = m.get('DiskAllocationRatio')

        if m.get('DiskUsedAmount') is not None:
            self.disk_used_amount = m.get('DiskUsedAmount')

        if m.get('DiskUtility') is not None:
            self.disk_utility = m.get('DiskUtility')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('HostNumber') is not None:
            self.host_number = m.get('HostNumber')

        if m.get('HostReplacePolicy') is not None:
            self.host_replace_policy = m.get('HostReplacePolicy')

        if m.get('InstanceNumber') is not None:
            self.instance_number = m.get('InstanceNumber')

        if m.get('MemAllocateRation') is not None:
            self.mem_allocate_ration = m.get('MemAllocateRation')

        if m.get('MemAllocatedAmount') is not None:
            self.mem_allocated_amount = m.get('MemAllocatedAmount')

        if m.get('MemAllocationRatio') is not None:
            self.mem_allocation_ratio = m.get('MemAllocationRatio')

        if m.get('MemUsedAmount') is not None:
            self.mem_used_amount = m.get('MemUsedAmount')

        if m.get('MemUtility') is not None:
            self.mem_utility = m.get('MemUtility')

        if m.get('OpenPermission') is not None:
            self.open_permission = m.get('OpenPermission')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('ZoneIDList') is not None:
            temp_model = main_models.DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroupsZoneIDList()
            self.zone_idlist = temp_model.from_map(m.get('ZoneIDList'))

        return self

class DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroupsZoneIDList(DaraModel):
    def __init__(
        self,
        zone_idlist: List[str] = None,
    ):
        self.zone_idlist = zone_idlist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.zone_idlist is not None:
            result['ZoneIDList'] = self.zone_idlist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneIDList') is not None:
            self.zone_idlist = m.get('ZoneIDList')

        return self

