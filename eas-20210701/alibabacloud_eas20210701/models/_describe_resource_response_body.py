# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeResourceResponseBody(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cpu_count: int = None,
        cpu_used: int = None,
        create_time: str = None,
        extra_data: str = None,
        features: List[str] = None,
        gpu_count: int = None,
        gpu_used: float = None,
        instance_count: int = None,
        instance_max_allocatable_cpu: int = None,
        instance_max_allocatable_gpu: float = None,
        instance_max_allocatable_memory: int = None,
        memory: int = None,
        memory_used: int = None,
        message: str = None,
        owner_uid: str = None,
        post_paid_instance_count: int = None,
        pre_paid_instance_count: int = None,
        request_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        status: str = None,
        update_time: str = None,
    ):
        # The ID of the cluster to which the resource group belongs.
        self.cluster_id = cluster_id
        # The total number of CPU cores.
        self.cpu_count = cpu_count
        # The number of vCPUs that is used.
        self.cpu_used = cpu_used
        # The time when the resource group was created.
        self.create_time = create_time
        # The additional information, such as the connection status of a virtual private cloud (VPC) and the log status of Log Service.
        self.extra_data = extra_data
        self.features = features
        # The total number of GPUs.
        self.gpu_count = gpu_count
        # The number of GPUs that is used.
        self.gpu_used = gpu_used
        # The total number of instances in the resource group.
        self.instance_count = instance_count
        self.instance_max_allocatable_cpu = instance_max_allocatable_cpu
        self.instance_max_allocatable_gpu = instance_max_allocatable_gpu
        self.instance_max_allocatable_memory = instance_max_allocatable_memory
        # The total memory size. Unit: MB.
        self.memory = memory
        # The size of memory that is used. Unit: MB.
        self.memory_used = memory_used
        # The returned message.
        self.message = message
        # The ID of the resource group owner.
        self.owner_uid = owner_uid
        # The total number of pay-as-you-go instances in the resource group.
        self.post_paid_instance_count = post_paid_instance_count
        # The total number of subscription instances in the resource group.
        self.pre_paid_instance_count = pre_paid_instance_count
        # The request ID.
        self.request_id = request_id
        # The ID of the Elastic Algorithm Service (EAS) resource.
        self.resource_id = resource_id
        # The name of the EAS resource.
        self.resource_name = resource_name
        # The type of the resource group. Valid values:
        # 
        # *   Dedicated: the dedicated resource group.
        # *   SelfManaged: the self-managed resource group.
        self.resource_type = resource_type
        # The state of the resource group.
        self.status = status
        # The time when the resource group was last updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count

        if self.cpu_used is not None:
            result['CpuUsed'] = self.cpu_used

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data

        if self.features is not None:
            result['Features'] = self.features

        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count

        if self.gpu_used is not None:
            result['GpuUsed'] = self.gpu_used

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.instance_max_allocatable_cpu is not None:
            result['InstanceMaxAllocatableCPU'] = self.instance_max_allocatable_cpu

        if self.instance_max_allocatable_gpu is not None:
            result['InstanceMaxAllocatableGPU'] = self.instance_max_allocatable_gpu

        if self.instance_max_allocatable_memory is not None:
            result['InstanceMaxAllocatableMemory'] = self.instance_max_allocatable_memory

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.memory_used is not None:
            result['MemoryUsed'] = self.memory_used

        if self.message is not None:
            result['Message'] = self.message

        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid

        if self.post_paid_instance_count is not None:
            result['PostPaidInstanceCount'] = self.post_paid_instance_count

        if self.pre_paid_instance_count is not None:
            result['PrePaidInstanceCount'] = self.pre_paid_instance_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')

        if m.get('CpuUsed') is not None:
            self.cpu_used = m.get('CpuUsed')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')

        if m.get('Features') is not None:
            self.features = m.get('Features')

        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')

        if m.get('GpuUsed') is not None:
            self.gpu_used = m.get('GpuUsed')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('InstanceMaxAllocatableCPU') is not None:
            self.instance_max_allocatable_cpu = m.get('InstanceMaxAllocatableCPU')

        if m.get('InstanceMaxAllocatableGPU') is not None:
            self.instance_max_allocatable_gpu = m.get('InstanceMaxAllocatableGPU')

        if m.get('InstanceMaxAllocatableMemory') is not None:
            self.instance_max_allocatable_memory = m.get('InstanceMaxAllocatableMemory')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('MemoryUsed') is not None:
            self.memory_used = m.get('MemoryUsed')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')

        if m.get('PostPaidInstanceCount') is not None:
            self.post_paid_instance_count = m.get('PostPaidInstanceCount')

        if m.get('PrePaidInstanceCount') is not None:
            self.pre_paid_instance_count = m.get('PrePaidInstanceCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

