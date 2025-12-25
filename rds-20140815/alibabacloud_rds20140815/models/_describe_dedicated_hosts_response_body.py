# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDedicatedHostsResponseBody(DaraModel):
    def __init__(
        self,
        dedicated_host_group_id: str = None,
        dedicated_hosts: main_models.DescribeDedicatedHostsResponseBodyDedicatedHosts = None,
        request_id: str = None,
    ):
        # The host group ID.
        self.dedicated_host_group_id = dedicated_host_group_id
        # The host information.
        self.dedicated_hosts = dedicated_hosts
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dedicated_hosts:
            self.dedicated_hosts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id

        if self.dedicated_hosts is not None:
            result['DedicatedHosts'] = self.dedicated_hosts.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')

        if m.get('DedicatedHosts') is not None:
            temp_model = main_models.DescribeDedicatedHostsResponseBodyDedicatedHosts()
            self.dedicated_hosts = temp_model.from_map(m.get('DedicatedHosts'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDedicatedHostsResponseBodyDedicatedHosts(DaraModel):
    def __init__(
        self,
        dedicated_hosts: List[main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHosts] = None,
    ):
        self.dedicated_hosts = dedicated_hosts

    def validate(self):
        if self.dedicated_hosts:
            for v1 in self.dedicated_hosts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DedicatedHosts'] = []
        if self.dedicated_hosts is not None:
            for k1 in self.dedicated_hosts:
                result['DedicatedHosts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dedicated_hosts = []
        if m.get('DedicatedHosts') is not None:
            for k1 in m.get('DedicatedHosts'):
                temp_model = main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHosts()
                self.dedicated_hosts.append(temp_model.from_map(k1))

        return self

class DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHosts(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        allocation_status: str = None,
        bastion_instance_id: str = None,
        cpuallocation_ratio: str = None,
        cpu_used: str = None,
        created_time: str = None,
        dedicated_host_group_id: str = None,
        dedicated_host_id: str = None,
        disk_allocation_ratio: str = None,
        end_time: str = None,
        engine: str = None,
        host_cpu: str = None,
        host_class: str = None,
        host_mem: str = None,
        host_name: str = None,
        host_status: str = None,
        host_storage: str = None,
        host_type: str = None,
        ipaddress: str = None,
        image_category: str = None,
        instance_number: str = None,
        mem_allocation_ratio: str = None,
        memory_used: str = None,
        open_permission: str = None,
        storage_used: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The host account. You can call the [CreateDedicatedHostAccount](https://help.aliyun.com/document_detail/196877.html) operation to create a host account.
        self.account_name = account_name
        # Specifies whether instances can be deployed on the host. Valid values:
        # 
        # *   **0**: Instances cannot be deployed on the host.
        # *   **1**: Instances can be deployed on the host.
        self.allocation_status = allocation_status
        # The bastion host ID.
        self.bastion_instance_id = bastion_instance_id
        # The core overcommitment ratio of the dedicated cluster. Unit: percentage. For more information about the core overcommitment ratio, see [Manage a dedicated cluster](https://help.aliyun.com/document_detail/182328.html).
        self.cpuallocation_ratio = cpuallocation_ratio
        # The number of used CPU cores on the host. Unit: cores.
        self.cpu_used = cpu_used
        # The time when the host was created.
        self.created_time = created_time
        # The dedicated cluster ID.
        self.dedicated_host_group_id = dedicated_host_group_id
        # The host ID.
        self.dedicated_host_id = dedicated_host_id
        # The disk overcommitment ratio of the dedicated cluster. Unit: percentage. For more information about the core overcommitment ratio, see [Manage a dedicated cluster](https://help.aliyun.com/document_detail/182328.html).
        self.disk_allocation_ratio = disk_allocation_ratio
        # The time when the host expires.
        self.end_time = end_time
        # The database engine of instances that are created on the host.
        self.engine = engine
        # The total number of CPU cores that are configured for the host. Unit: cores.
        self.host_cpu = host_cpu
        # The instance type of the host.
        self.host_class = host_class
        # The total memory space of the host. Unit: MB.
        self.host_mem = host_mem
        # The host name.
        self.host_name = host_name
        # The status of the host. Valid values:
        # 
        # *   **0**: creating
        # *   **1**: running
        # *   **2**: faulty
        # *   **3**: being replaced
        # *   **4**: deprecated
        # *   **5**: deleting
        # *   **6**: restarting
        self.host_status = host_status
        # The storage capacity of the host. Unit: MB.
        self.host_storage = host_storage
        # The storage type of the host. Valid values:
        # 
        # *   **dhg_cloud_ssd**: ESSD
        # *   **dhg_local_ssd**: local SSD
        self.host_type = host_type
        # The internal IP address of the host.
        self.ipaddress = ipaddress
        # The host image. This parameter is returned only when the **Engine** parameter is set to **mssql**. Valid values:
        # 
        # *   **WindowsWithMssqlStdLicense**: a Windows image that contains the licenses of SQL Server Standard Edition
        # *   **WindowsWithMssqlEntLisence**: a Windows image that contains the licenses of SQL Server Enterprise Edition
        # *   **WindowsWithMssqlWebLisence**: a Windows image that contains the licenses of SQL Server Web Edition
        self.image_category = image_category
        # The total number of instances that are created on the host.
        self.instance_number = instance_number
        # The maximum memory usage per host in the dedicated cluster.
        self.mem_allocation_ratio = mem_allocation_ratio
        # The size of the used memory. Unit: MB.
        self.memory_used = memory_used
        # Indicates whether the feature that allows you to have the OS permissions on the host is enabled. Valid values:
        # 
        # *   **0** or **null**: The permissions cannot be granted.
        # *   **1**: The permissions can be granted.
        # *   **3**: The permissions have been granted.
        self.open_permission = open_permission
        # The amount of used storage space on the host.
        self.storage_used = storage_used
        # The ID of the virtual private cloud (VPC) to which the host belongs.
        self.vpcid = vpcid
        # The ID of the vSwitch associated with the specified VPC.
        self.v_switch_id = v_switch_id
        # The zone ID of the host.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status

        if self.bastion_instance_id is not None:
            result['BastionInstanceId'] = self.bastion_instance_id

        if self.cpuallocation_ratio is not None:
            result['CPUAllocationRatio'] = self.cpuallocation_ratio

        if self.cpu_used is not None:
            result['CpuUsed'] = self.cpu_used

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id

        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id

        if self.disk_allocation_ratio is not None:
            result['DiskAllocationRatio'] = self.disk_allocation_ratio

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.host_cpu is not None:
            result['HostCPU'] = self.host_cpu

        if self.host_class is not None:
            result['HostClass'] = self.host_class

        if self.host_mem is not None:
            result['HostMem'] = self.host_mem

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.host_status is not None:
            result['HostStatus'] = self.host_status

        if self.host_storage is not None:
            result['HostStorage'] = self.host_storage

        if self.host_type is not None:
            result['HostType'] = self.host_type

        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress

        if self.image_category is not None:
            result['ImageCategory'] = self.image_category

        if self.instance_number is not None:
            result['InstanceNumber'] = self.instance_number

        if self.mem_allocation_ratio is not None:
            result['MemAllocationRatio'] = self.mem_allocation_ratio

        if self.memory_used is not None:
            result['MemoryUsed'] = self.memory_used

        if self.open_permission is not None:
            result['OpenPermission'] = self.open_permission

        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')

        if m.get('BastionInstanceId') is not None:
            self.bastion_instance_id = m.get('BastionInstanceId')

        if m.get('CPUAllocationRatio') is not None:
            self.cpuallocation_ratio = m.get('CPUAllocationRatio')

        if m.get('CpuUsed') is not None:
            self.cpu_used = m.get('CpuUsed')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')

        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')

        if m.get('DiskAllocationRatio') is not None:
            self.disk_allocation_ratio = m.get('DiskAllocationRatio')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('HostCPU') is not None:
            self.host_cpu = m.get('HostCPU')

        if m.get('HostClass') is not None:
            self.host_class = m.get('HostClass')

        if m.get('HostMem') is not None:
            self.host_mem = m.get('HostMem')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('HostStatus') is not None:
            self.host_status = m.get('HostStatus')

        if m.get('HostStorage') is not None:
            self.host_storage = m.get('HostStorage')

        if m.get('HostType') is not None:
            self.host_type = m.get('HostType')

        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')

        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')

        if m.get('InstanceNumber') is not None:
            self.instance_number = m.get('InstanceNumber')

        if m.get('MemAllocationRatio') is not None:
            self.mem_allocation_ratio = m.get('MemAllocationRatio')

        if m.get('MemoryUsed') is not None:
            self.memory_used = m.get('MemoryUsed')

        if m.get('OpenPermission') is not None:
            self.open_permission = m.get('OpenPermission')

        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

