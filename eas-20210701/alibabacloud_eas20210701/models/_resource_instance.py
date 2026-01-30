# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class ResourceInstance(DaraModel):
    def __init__(
        self,
        arch: str = None,
        auto_renewal: bool = None,
        charge_type: str = None,
        create_time: str = None,
        expired_time: str = None,
        instance_cpu_count: int = None,
        instance_gpu_count: int = None,
        instance_gpu_memory: str = None,
        instance_id: str = None,
        instance_ip: str = None,
        instance_memory: str = None,
        instance_name: str = None,
        instance_phase: str = None,
        instance_status: str = None,
        instance_system_disk_size: int = None,
        instance_tenant_ip: str = None,
        instance_type: str = None,
        instance_used_cpu: float = None,
        instance_used_gpu: float = None,
        instance_used_gpu_memory: str = None,
        instance_used_memory: str = None,
        labels: List[main_models.ResourceInstanceLabels] = None,
        last_cordon_operator: str = None,
        last_cordon_reason: str = None,
        region: str = None,
        resource_id: str = None,
        zone: str = None,
    ):
        self.arch = arch
        self.auto_renewal = auto_renewal
        self.charge_type = charge_type
        self.create_time = create_time
        self.expired_time = expired_time
        self.instance_cpu_count = instance_cpu_count
        self.instance_gpu_count = instance_gpu_count
        self.instance_gpu_memory = instance_gpu_memory
        self.instance_id = instance_id
        self.instance_ip = instance_ip
        self.instance_memory = instance_memory
        self.instance_name = instance_name
        self.instance_phase = instance_phase
        self.instance_status = instance_status
        self.instance_system_disk_size = instance_system_disk_size
        self.instance_tenant_ip = instance_tenant_ip
        self.instance_type = instance_type
        self.instance_used_cpu = instance_used_cpu
        self.instance_used_gpu = instance_used_gpu
        self.instance_used_gpu_memory = instance_used_gpu_memory
        self.instance_used_memory = instance_used_memory
        self.labels = labels
        self.last_cordon_operator = last_cordon_operator
        self.last_cordon_reason = last_cordon_reason
        self.region = region
        self.resource_id = resource_id
        self.zone = zone

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arch is not None:
            result['Arch'] = self.arch

        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.instance_cpu_count is not None:
            result['InstanceCpuCount'] = self.instance_cpu_count

        if self.instance_gpu_count is not None:
            result['InstanceGpuCount'] = self.instance_gpu_count

        if self.instance_gpu_memory is not None:
            result['InstanceGpuMemory'] = self.instance_gpu_memory

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_ip is not None:
            result['InstanceIp'] = self.instance_ip

        if self.instance_memory is not None:
            result['InstanceMemory'] = self.instance_memory

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_phase is not None:
            result['InstancePhase'] = self.instance_phase

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.instance_system_disk_size is not None:
            result['InstanceSystemDiskSize'] = self.instance_system_disk_size

        if self.instance_tenant_ip is not None:
            result['InstanceTenantIp'] = self.instance_tenant_ip

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.instance_used_cpu is not None:
            result['InstanceUsedCpu'] = self.instance_used_cpu

        if self.instance_used_gpu is not None:
            result['InstanceUsedGpu'] = self.instance_used_gpu

        if self.instance_used_gpu_memory is not None:
            result['InstanceUsedGpuMemory'] = self.instance_used_gpu_memory

        if self.instance_used_memory is not None:
            result['InstanceUsedMemory'] = self.instance_used_memory

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.last_cordon_operator is not None:
            result['LastCordonOperator'] = self.last_cordon_operator

        if self.last_cordon_reason is not None:
            result['LastCordonReason'] = self.last_cordon_reason

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.zone is not None:
            result['Zone'] = self.zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arch') is not None:
            self.arch = m.get('Arch')

        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('InstanceCpuCount') is not None:
            self.instance_cpu_count = m.get('InstanceCpuCount')

        if m.get('InstanceGpuCount') is not None:
            self.instance_gpu_count = m.get('InstanceGpuCount')

        if m.get('InstanceGpuMemory') is not None:
            self.instance_gpu_memory = m.get('InstanceGpuMemory')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceIp') is not None:
            self.instance_ip = m.get('InstanceIp')

        if m.get('InstanceMemory') is not None:
            self.instance_memory = m.get('InstanceMemory')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstancePhase') is not None:
            self.instance_phase = m.get('InstancePhase')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InstanceSystemDiskSize') is not None:
            self.instance_system_disk_size = m.get('InstanceSystemDiskSize')

        if m.get('InstanceTenantIp') is not None:
            self.instance_tenant_ip = m.get('InstanceTenantIp')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InstanceUsedCpu') is not None:
            self.instance_used_cpu = m.get('InstanceUsedCpu')

        if m.get('InstanceUsedGpu') is not None:
            self.instance_used_gpu = m.get('InstanceUsedGpu')

        if m.get('InstanceUsedGpuMemory') is not None:
            self.instance_used_gpu_memory = m.get('InstanceUsedGpuMemory')

        if m.get('InstanceUsedMemory') is not None:
            self.instance_used_memory = m.get('InstanceUsedMemory')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.ResourceInstanceLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('LastCordonOperator') is not None:
            self.last_cordon_operator = m.get('LastCordonOperator')

        if m.get('LastCordonReason') is not None:
            self.last_cordon_reason = m.get('LastCordonReason')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Zone') is not None:
            self.zone = m.get('Zone')

        return self



class ResourceInstanceLabels(DaraModel):
    def __init__(
        self,
        label_key: str = None,
        label_value: str = None,
    ):
        self.label_key = label_key
        self.label_value = label_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label_key is not None:
            result['LabelKey'] = self.label_key

        if self.label_value is not None:
            result['LabelValue'] = self.label_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelKey') is not None:
            self.label_key = m.get('LabelKey')

        if m.get('LabelValue') is not None:
            self.label_value = m.get('LabelValue')

        return self

