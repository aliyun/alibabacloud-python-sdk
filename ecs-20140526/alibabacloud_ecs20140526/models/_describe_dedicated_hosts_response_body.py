# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeDedicatedHostsResponseBody(DaraModel):
    def __init__(
        self,
        dedicated_hosts: main_models.DescribeDedicatedHostsResponseBodyDedicatedHosts = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the DDH.
        self.dedicated_hosts = dedicated_hosts
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists. If the return value of this parameter is empty when you specify MaxResults and NextToken for a paged query, no more results are to be returned.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of dedicated hosts.
        self.total_count = total_count

    def validate(self):
        if self.dedicated_hosts:
            self.dedicated_hosts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_hosts is not None:
            result['DedicatedHosts'] = self.dedicated_hosts.to_map()

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHosts') is not None:
            temp_model = main_models.DescribeDedicatedHostsResponseBodyDedicatedHosts()
            self.dedicated_hosts = temp_model.from_map(m.get('DedicatedHosts'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDedicatedHostsResponseBodyDedicatedHosts(DaraModel):
    def __init__(
        self,
        dedicated_host: List[main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHost] = None,
    ):
        self.dedicated_host = dedicated_host

    def validate(self):
        if self.dedicated_host:
            for v1 in self.dedicated_host:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DedicatedHost'] = []
        if self.dedicated_host is not None:
            for k1 in self.dedicated_host:
                result['DedicatedHost'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dedicated_host = []
        if m.get('DedicatedHost') is not None:
            for k1 in m.get('DedicatedHost'):
                temp_model = main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHost()
                self.dedicated_host.append(temp_model.from_map(k1))

        return self

class DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHost(DaraModel):
    def __init__(
        self,
        scheduler_options: main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostSchedulerOptions = None,
        action_on_maintenance: str = None,
        auto_placement: str = None,
        auto_release_time: str = None,
        capacity: main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostCapacity = None,
        charge_type: str = None,
        cores: int = None,
        cpu_over_commit_ratio: float = None,
        creation_time: str = None,
        dedicated_host_cluster_id: str = None,
        dedicated_host_id: str = None,
        dedicated_host_name: str = None,
        dedicated_host_owner_id: int = None,
        dedicated_host_type: str = None,
        description: str = None,
        expired_time: str = None,
        gpuspec: str = None,
        host_detail_info: main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostHostDetailInfo = None,
        instances: main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostInstances = None,
        machine_id: str = None,
        network_attributes: main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostNetworkAttributes = None,
        operation_locks: main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostOperationLocks = None,
        physical_gpus: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        sale_cycle: str = None,
        sockets: int = None,
        status: str = None,
        supported_custom_instance_type_families: main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostSupportedCustomInstanceTypeFamilies = None,
        supported_instance_type_families: main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostSupportedInstanceTypeFamilies = None,
        supported_instance_types_list: main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostSupportedInstanceTypesList = None,
        tags: main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostTags = None,
        zone_id: str = None,
    ):
        self.scheduler_options = scheduler_options
        # The policy used to migrate the ECS instances deployed on the dedicated host when the dedicated host fails. Valid values:
        # 
        # *   Migrate: The instances are migrated to another physical machine. Instances that are not in the Stopped state when the dedicated host fails are restarted.
        # *   Stop: The instances are stopped. If the dedicated host cannot be repaired, the instances are migrated to another physical machine and then restarted.
        # 
        # If the dedicated host has cloud disks attached, the default value is Migrate. If the dedicated host has local disks attached, the default value is Stop.
        self.action_on_maintenance = action_on_maintenance
        # Indicates whether the dedicated host is added to the resource pool for automatic deployment. Valid values:
        # 
        # *   on: The dedicated host is added to the resource pool for automatic deployment.
        # *   off: The dedicated host is not added to the resource pool for automatic deployment.
        # 
        # For information about automatic deployment, see the "Automatic deployment" section in [Functions and features](https://help.aliyun.com/document_detail/118938.html).
        self.auto_placement = auto_placement
        # The automatic release time of the dedicated host. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-MM-ddTHH:mmZ` format. The time is displayed in UTC.
        self.auto_release_time = auto_release_time
        # The performance specifications of the dedicated host.
        self.capacity = capacity
        # The billing method of the dedicated host.
        self.charge_type = charge_type
        # The number of physical cores per CPU.
        self.cores = cores
        # The CPU overcommit ratio. Valid values: 1 to 5.
        self.cpu_over_commit_ratio = cpu_over_commit_ratio
        # The time when the dedicated host was created. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-MM-ddTHH:mmZ` format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The ID of the dedicated host cluster to which the dedicated host belongs.
        self.dedicated_host_cluster_id = dedicated_host_cluster_id
        # The ID of the dedicated host.
        self.dedicated_host_id = dedicated_host_id
        # The name of the dedicated host.
        self.dedicated_host_name = dedicated_host_name
        # The ID of the dedicated host owner.
        self.dedicated_host_owner_id = dedicated_host_owner_id
        # The type of the dedicated host.
        self.dedicated_host_type = dedicated_host_type
        # The description of the dedicated host.
        self.description = description
        # The expiration time of the subscription dedicated host. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-MM-ddTHH:mmZ` format. The time is displayed in UTC.
        self.expired_time = expired_time
        # The GPU model.
        self.gpuspec = gpuspec
        # This parameter will be removed in the future. We recommend that you use other parameters to ensure future compatibility.
        self.host_detail_info = host_detail_info
        # The ECS instances that were created on the dedicated host.
        self.instances = instances
        # The machine code of the dedicated host.
        self.machine_id = machine_id
        # The network attributes of the dedicated host.
        self.network_attributes = network_attributes
        # The reasons why the resources of the dedicated host were locked.
        self.operation_locks = operation_locks
        # The number of physical GPUs.
        self.physical_gpus = physical_gpus
        # The region ID of the dedicated host.
        self.region_id = region_id
        # The ID of the resource group to which the dedicated host belongs.
        self.resource_group_id = resource_group_id
        # The unit of the subscription duration. Valid values:
        # 
        # *   Month
        # *   Year
        self.sale_cycle = sale_cycle
        # The number of physical CPUs.
        self.sockets = sockets
        # The status of the dedicated host. Valid values:
        # 
        # *   Available: The dedicated host is running as expected.
        # *   UnderAssessment: The dedicated host is available but has potential risks that may cause the ECS instances on the dedicated host to fail.
        # *   PermanentFailure: The dedicated host has permanent failures and is unavailable.
        self.status = status
        # The custom ECS instance families that are supported by the dedicated host.
        self.supported_custom_instance_type_families = supported_custom_instance_type_families
        # The ECS instance families that are supported by the dedicated host.
        self.supported_instance_type_families = supported_instance_type_families
        # The ECS instance types that are supported by the dedicated host.
        self.supported_instance_types_list = supported_instance_types_list
        # The tags of the dedicated host.
        self.tags = tags
        # The zone ID of the dedicated host.
        self.zone_id = zone_id

    def validate(self):
        if self.scheduler_options:
            self.scheduler_options.validate()
        if self.capacity:
            self.capacity.validate()
        if self.host_detail_info:
            self.host_detail_info.validate()
        if self.instances:
            self.instances.validate()
        if self.network_attributes:
            self.network_attributes.validate()
        if self.operation_locks:
            self.operation_locks.validate()
        if self.supported_custom_instance_type_families:
            self.supported_custom_instance_type_families.validate()
        if self.supported_instance_type_families:
            self.supported_instance_type_families.validate()
        if self.supported_instance_types_list:
            self.supported_instance_types_list.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scheduler_options is not None:
            result['SchedulerOptions'] = self.scheduler_options.to_map()

        if self.action_on_maintenance is not None:
            result['ActionOnMaintenance'] = self.action_on_maintenance

        if self.auto_placement is not None:
            result['AutoPlacement'] = self.auto_placement

        if self.auto_release_time is not None:
            result['AutoReleaseTime'] = self.auto_release_time

        if self.capacity is not None:
            result['Capacity'] = self.capacity.to_map()

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cores is not None:
            result['Cores'] = self.cores

        if self.cpu_over_commit_ratio is not None:
            result['CpuOverCommitRatio'] = self.cpu_over_commit_ratio

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.dedicated_host_cluster_id is not None:
            result['DedicatedHostClusterId'] = self.dedicated_host_cluster_id

        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id

        if self.dedicated_host_name is not None:
            result['DedicatedHostName'] = self.dedicated_host_name

        if self.dedicated_host_owner_id is not None:
            result['DedicatedHostOwnerId'] = self.dedicated_host_owner_id

        if self.dedicated_host_type is not None:
            result['DedicatedHostType'] = self.dedicated_host_type

        if self.description is not None:
            result['Description'] = self.description

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.gpuspec is not None:
            result['GPUSpec'] = self.gpuspec

        if self.host_detail_info is not None:
            result['HostDetailInfo'] = self.host_detail_info.to_map()

        if self.instances is not None:
            result['Instances'] = self.instances.to_map()

        if self.machine_id is not None:
            result['MachineId'] = self.machine_id

        if self.network_attributes is not None:
            result['NetworkAttributes'] = self.network_attributes.to_map()

        if self.operation_locks is not None:
            result['OperationLocks'] = self.operation_locks.to_map()

        if self.physical_gpus is not None:
            result['PhysicalGpus'] = self.physical_gpus

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sale_cycle is not None:
            result['SaleCycle'] = self.sale_cycle

        if self.sockets is not None:
            result['Sockets'] = self.sockets

        if self.status is not None:
            result['Status'] = self.status

        if self.supported_custom_instance_type_families is not None:
            result['SupportedCustomInstanceTypeFamilies'] = self.supported_custom_instance_type_families.to_map()

        if self.supported_instance_type_families is not None:
            result['SupportedInstanceTypeFamilies'] = self.supported_instance_type_families.to_map()

        if self.supported_instance_types_list is not None:
            result['SupportedInstanceTypesList'] = self.supported_instance_types_list.to_map()

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SchedulerOptions') is not None:
            temp_model = main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostSchedulerOptions()
            self.scheduler_options = temp_model.from_map(m.get('SchedulerOptions'))

        if m.get('ActionOnMaintenance') is not None:
            self.action_on_maintenance = m.get('ActionOnMaintenance')

        if m.get('AutoPlacement') is not None:
            self.auto_placement = m.get('AutoPlacement')

        if m.get('AutoReleaseTime') is not None:
            self.auto_release_time = m.get('AutoReleaseTime')

        if m.get('Capacity') is not None:
            temp_model = main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostCapacity()
            self.capacity = temp_model.from_map(m.get('Capacity'))

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Cores') is not None:
            self.cores = m.get('Cores')

        if m.get('CpuOverCommitRatio') is not None:
            self.cpu_over_commit_ratio = m.get('CpuOverCommitRatio')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DedicatedHostClusterId') is not None:
            self.dedicated_host_cluster_id = m.get('DedicatedHostClusterId')

        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')

        if m.get('DedicatedHostName') is not None:
            self.dedicated_host_name = m.get('DedicatedHostName')

        if m.get('DedicatedHostOwnerId') is not None:
            self.dedicated_host_owner_id = m.get('DedicatedHostOwnerId')

        if m.get('DedicatedHostType') is not None:
            self.dedicated_host_type = m.get('DedicatedHostType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('GPUSpec') is not None:
            self.gpuspec = m.get('GPUSpec')

        if m.get('HostDetailInfo') is not None:
            temp_model = main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostHostDetailInfo()
            self.host_detail_info = temp_model.from_map(m.get('HostDetailInfo'))

        if m.get('Instances') is not None:
            temp_model = main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostInstances()
            self.instances = temp_model.from_map(m.get('Instances'))

        if m.get('MachineId') is not None:
            self.machine_id = m.get('MachineId')

        if m.get('NetworkAttributes') is not None:
            temp_model = main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostNetworkAttributes()
            self.network_attributes = temp_model.from_map(m.get('NetworkAttributes'))

        if m.get('OperationLocks') is not None:
            temp_model = main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostOperationLocks()
            self.operation_locks = temp_model.from_map(m.get('OperationLocks'))

        if m.get('PhysicalGpus') is not None:
            self.physical_gpus = m.get('PhysicalGpus')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SaleCycle') is not None:
            self.sale_cycle = m.get('SaleCycle')

        if m.get('Sockets') is not None:
            self.sockets = m.get('Sockets')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupportedCustomInstanceTypeFamilies') is not None:
            temp_model = main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostSupportedCustomInstanceTypeFamilies()
            self.supported_custom_instance_type_families = temp_model.from_map(m.get('SupportedCustomInstanceTypeFamilies'))

        if m.get('SupportedInstanceTypeFamilies') is not None:
            temp_model = main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostSupportedInstanceTypeFamilies()
            self.supported_instance_type_families = temp_model.from_map(m.get('SupportedInstanceTypeFamilies'))

        if m.get('SupportedInstanceTypesList') is not None:
            temp_model = main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostSupportedInstanceTypesList()
            self.supported_instance_types_list = temp_model.from_map(m.get('SupportedInstanceTypesList'))

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key of the dedicated host.
        self.tag_key = tag_key
        # The tag value of the dedicated host.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostSupportedInstanceTypesList(DaraModel):
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

class DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostSupportedInstanceTypeFamilies(DaraModel):
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

class DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostSupportedCustomInstanceTypeFamilies(DaraModel):
    def __init__(
        self,
        supported_custom_instance_type_family: List[str] = None,
    ):
        self.supported_custom_instance_type_family = supported_custom_instance_type_family

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.supported_custom_instance_type_family is not None:
            result['SupportedCustomInstanceTypeFamily'] = self.supported_custom_instance_type_family

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedCustomInstanceTypeFamily') is not None:
            self.supported_custom_instance_type_family = m.get('SupportedCustomInstanceTypeFamily')

        return self

class DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostOperationLocks(DaraModel):
    def __init__(
        self,
        operation_lock: List[main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostOperationLocksOperationLock] = None,
    ):
        self.operation_lock = operation_lock

    def validate(self):
        if self.operation_lock:
            for v1 in self.operation_lock:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OperationLock'] = []
        if self.operation_lock is not None:
            for k1 in self.operation_lock:
                result['OperationLock'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operation_lock = []
        if m.get('OperationLock') is not None:
            for k1 in m.get('OperationLock'):
                temp_model = main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostOperationLocksOperationLock()
                self.operation_lock.append(temp_model.from_map(k1))

        return self

class DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostOperationLocksOperationLock(DaraModel):
    def __init__(
        self,
        lock_reason: str = None,
    ):
        # The reason why the dedicated host was locked. Valid values:
        # 
        # *   financial: The dedicated host was locked due to overdue payments.
        # *   security: The dedicated host was locked due to security reasons.
        self.lock_reason = lock_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        return self

class DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostNetworkAttributes(DaraModel):
    def __init__(
        self,
        slb_udp_timeout: int = None,
        udp_timeout: int = None,
    ):
        # The timeout period of the UDP session that is established between Server Load Balancer (SLB) and the dedicated host. Unit: seconds. Only 60 is returned.
        self.slb_udp_timeout = slb_udp_timeout
        # The timeout period of the UDP session that is established between a user and an Alibaba Cloud service on the dedicated host. Unit: seconds. Only 60 is returned.
        self.udp_timeout = udp_timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.slb_udp_timeout is not None:
            result['SlbUdpTimeout'] = self.slb_udp_timeout

        if self.udp_timeout is not None:
            result['UdpTimeout'] = self.udp_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlbUdpTimeout') is not None:
            self.slb_udp_timeout = m.get('SlbUdpTimeout')

        if m.get('UdpTimeout') is not None:
            self.udp_timeout = m.get('UdpTimeout')

        return self

class DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostInstances(DaraModel):
    def __init__(
        self,
        instance: List[main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostInstancesInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for v1 in self.instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instance'] = []
        if self.instance is not None:
            for k1 in self.instance:
                result['Instance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k1 in m.get('Instance'):
                temp_model = main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostInstancesInstance()
                self.instance.append(temp_model.from_map(k1))

        return self

class DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostInstancesInstance(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_owner_id: int = None,
        instance_type: str = None,
        socket_id: str = None,
    ):
        # The ID of the ECS instance.
        self.instance_id = instance_id
        # The ID of the ECS instance owner.
        self.instance_owner_id = instance_owner_id
        # The instance type of the ECS instance that was created on the dedicated host.
        self.instance_type = instance_type
        # The ID of the socket to which the ECS instance belongs.
        self.socket_id = socket_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_owner_id is not None:
            result['InstanceOwnerId'] = self.instance_owner_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.socket_id is not None:
            result['SocketId'] = self.socket_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceOwnerId') is not None:
            self.instance_owner_id = m.get('InstanceOwnerId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('SocketId') is not None:
            self.socket_id = m.get('SocketId')

        return self

class DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostHostDetailInfo(DaraModel):
    def __init__(
        self,
        serial_number: str = None,
    ):
        # This parameter will be removed in the future. We recommend that you use other parameters to ensure future compatibility.
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        return self

class DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostCapacity(DaraModel):
    def __init__(
        self,
        available_instance_types: main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostCapacityAvailableInstanceTypes = None,
        available_local_storage: int = None,
        available_memory: float = None,
        available_vcpus: int = None,
        available_vgpus: int = None,
        local_storage_category: str = None,
        socket_capacities: main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostCapacitySocketCapacities = None,
        total_local_storage: int = None,
        total_memory: float = None,
        total_vcpus: int = None,
        total_vgpus: int = None,
    ):
        self.available_instance_types = available_instance_types
        # The amount of available space on the local disks. Unit: GiB
        self.available_local_storage = available_local_storage
        # The amount of available memory. Unit: GiB.
        self.available_memory = available_memory
        # The number of available vCPUs.
        self.available_vcpus = available_vcpus
        # The number of available vGPUs.
        self.available_vgpus = available_vgpus
        # The category of local disks.
        self.local_storage_category = local_storage_category
        # The socket capacities.
        self.socket_capacities = socket_capacities
        # The total capacity of local disks. Unit: GiB.
        self.total_local_storage = total_local_storage
        # The total amount of memory. Unit: GiB.
        self.total_memory = total_memory
        # The total number of vCPUs.
        self.total_vcpus = total_vcpus
        # The total number of vGPUs.
        self.total_vgpus = total_vgpus

    def validate(self):
        if self.available_instance_types:
            self.available_instance_types.validate()
        if self.socket_capacities:
            self.socket_capacities.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_instance_types is not None:
            result['AvailableInstanceTypes'] = self.available_instance_types.to_map()

        if self.available_local_storage is not None:
            result['AvailableLocalStorage'] = self.available_local_storage

        if self.available_memory is not None:
            result['AvailableMemory'] = self.available_memory

        if self.available_vcpus is not None:
            result['AvailableVcpus'] = self.available_vcpus

        if self.available_vgpus is not None:
            result['AvailableVgpus'] = self.available_vgpus

        if self.local_storage_category is not None:
            result['LocalStorageCategory'] = self.local_storage_category

        if self.socket_capacities is not None:
            result['SocketCapacities'] = self.socket_capacities.to_map()

        if self.total_local_storage is not None:
            result['TotalLocalStorage'] = self.total_local_storage

        if self.total_memory is not None:
            result['TotalMemory'] = self.total_memory

        if self.total_vcpus is not None:
            result['TotalVcpus'] = self.total_vcpus

        if self.total_vgpus is not None:
            result['TotalVgpus'] = self.total_vgpus

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableInstanceTypes') is not None:
            temp_model = main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostCapacityAvailableInstanceTypes()
            self.available_instance_types = temp_model.from_map(m.get('AvailableInstanceTypes'))

        if m.get('AvailableLocalStorage') is not None:
            self.available_local_storage = m.get('AvailableLocalStorage')

        if m.get('AvailableMemory') is not None:
            self.available_memory = m.get('AvailableMemory')

        if m.get('AvailableVcpus') is not None:
            self.available_vcpus = m.get('AvailableVcpus')

        if m.get('AvailableVgpus') is not None:
            self.available_vgpus = m.get('AvailableVgpus')

        if m.get('LocalStorageCategory') is not None:
            self.local_storage_category = m.get('LocalStorageCategory')

        if m.get('SocketCapacities') is not None:
            temp_model = main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostCapacitySocketCapacities()
            self.socket_capacities = temp_model.from_map(m.get('SocketCapacities'))

        if m.get('TotalLocalStorage') is not None:
            self.total_local_storage = m.get('TotalLocalStorage')

        if m.get('TotalMemory') is not None:
            self.total_memory = m.get('TotalMemory')

        if m.get('TotalVcpus') is not None:
            self.total_vcpus = m.get('TotalVcpus')

        if m.get('TotalVgpus') is not None:
            self.total_vgpus = m.get('TotalVgpus')

        return self

class DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostCapacitySocketCapacities(DaraModel):
    def __init__(
        self,
        socket_capacity: List[main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostCapacitySocketCapacitiesSocketCapacity] = None,
    ):
        self.socket_capacity = socket_capacity

    def validate(self):
        if self.socket_capacity:
            for v1 in self.socket_capacity:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SocketCapacity'] = []
        if self.socket_capacity is not None:
            for k1 in self.socket_capacity:
                result['SocketCapacity'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.socket_capacity = []
        if m.get('SocketCapacity') is not None:
            for k1 in m.get('SocketCapacity'):
                temp_model = main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostCapacitySocketCapacitiesSocketCapacity()
                self.socket_capacity.append(temp_model.from_map(k1))

        return self

class DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostCapacitySocketCapacitiesSocketCapacity(DaraModel):
    def __init__(
        self,
        available_memory: float = None,
        available_vcpu: int = None,
        socket_id: int = None,
        total_memory: float = None,
        total_vcpu: int = None,
    ):
        # The amount of available memory. Unit: GiB.
        self.available_memory = available_memory
        # The number of available vCPUs.
        self.available_vcpu = available_vcpu
        # The socket ID.
        self.socket_id = socket_id
        # The total amount of memory. Unit: GiB.
        self.total_memory = total_memory
        # The total number of vCPUs.
        self.total_vcpu = total_vcpu

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_memory is not None:
            result['AvailableMemory'] = self.available_memory

        if self.available_vcpu is not None:
            result['AvailableVcpu'] = self.available_vcpu

        if self.socket_id is not None:
            result['SocketId'] = self.socket_id

        if self.total_memory is not None:
            result['TotalMemory'] = self.total_memory

        if self.total_vcpu is not None:
            result['TotalVcpu'] = self.total_vcpu

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableMemory') is not None:
            self.available_memory = m.get('AvailableMemory')

        if m.get('AvailableVcpu') is not None:
            self.available_vcpu = m.get('AvailableVcpu')

        if m.get('SocketId') is not None:
            self.socket_id = m.get('SocketId')

        if m.get('TotalMemory') is not None:
            self.total_memory = m.get('TotalMemory')

        if m.get('TotalVcpu') is not None:
            self.total_vcpu = m.get('TotalVcpu')

        return self

class DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostCapacityAvailableInstanceTypes(DaraModel):
    def __init__(
        self,
        available_instance_type: List[main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostCapacityAvailableInstanceTypesAvailableInstanceType] = None,
    ):
        self.available_instance_type = available_instance_type

    def validate(self):
        if self.available_instance_type:
            for v1 in self.available_instance_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableInstanceType'] = []
        if self.available_instance_type is not None:
            for k1 in self.available_instance_type:
                result['AvailableInstanceType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_instance_type = []
        if m.get('AvailableInstanceType') is not None:
            for k1 in m.get('AvailableInstanceType'):
                temp_model = main_models.DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostCapacityAvailableInstanceTypesAvailableInstanceType()
                self.available_instance_type.append(temp_model.from_map(k1))

        return self

class DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostCapacityAvailableInstanceTypesAvailableInstanceType(DaraModel):
    def __init__(
        self,
        available_instance_capacity: int = None,
        instance_type: str = None,
    ):
        self.available_instance_capacity = available_instance_capacity
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_instance_capacity is not None:
            result['AvailableInstanceCapacity'] = self.available_instance_capacity

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableInstanceCapacity') is not None:
            self.available_instance_capacity = m.get('AvailableInstanceCapacity')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        return self

class DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHostSchedulerOptions(DaraModel):
    def __init__(
        self,
        managed_private_space_id: str = None,
    ):
        self.managed_private_space_id = managed_private_space_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.managed_private_space_id is not None:
            result['ManagedPrivateSpaceId'] = self.managed_private_space_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ManagedPrivateSpaceId') is not None:
            self.managed_private_space_id = m.get('ManagedPrivateSpaceId')

        return self

