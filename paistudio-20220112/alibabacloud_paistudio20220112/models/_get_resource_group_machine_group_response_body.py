# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class GetResourceGroupMachineGroupResponseBody(DaraModel):
    def __init__(
        self,
        allocatable_cpu: str = None,
        allocatable_memory: str = None,
        cpu: str = None,
        default_driver: str = None,
        ecs_count: int = None,
        ecs_spec: str = None,
        gmt_created_time: str = None,
        gmt_expired_time: str = None,
        gmt_modified_time: str = None,
        gmt_started_time: str = None,
        gpu: str = None,
        gpu_type: str = None,
        machine_group_id: str = None,
        memory: str = None,
        name: str = None,
        payment_duration: str = None,
        payment_duration_unit: str = None,
        payment_type: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        supported_drivers: List[str] = None,
        system_reserved_cpu: str = None,
        system_reserved_memory: str = None,
        tags: List[main_models.GetResourceGroupMachineGroupResponseBodyTags] = None,
    ):
        self.allocatable_cpu = allocatable_cpu
        self.allocatable_memory = allocatable_memory
        self.cpu = cpu
        self.default_driver = default_driver
        self.ecs_count = ecs_count
        self.ecs_spec = ecs_spec
        self.gmt_created_time = gmt_created_time
        self.gmt_expired_time = gmt_expired_time
        self.gmt_modified_time = gmt_modified_time
        self.gmt_started_time = gmt_started_time
        self.gpu = gpu
        self.gpu_type = gpu_type
        self.machine_group_id = machine_group_id
        self.memory = memory
        self.name = name
        self.payment_duration = payment_duration
        self.payment_duration_unit = payment_duration_unit
        self.payment_type = payment_type
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.status = status
        self.supported_drivers = supported_drivers
        self.system_reserved_cpu = system_reserved_cpu
        self.system_reserved_memory = system_reserved_memory
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocatable_cpu is not None:
            result['AllocatableCpu'] = self.allocatable_cpu

        if self.allocatable_memory is not None:
            result['AllocatableMemory'] = self.allocatable_memory

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.default_driver is not None:
            result['DefaultDriver'] = self.default_driver

        if self.ecs_count is not None:
            result['EcsCount'] = self.ecs_count

        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec

        if self.gmt_created_time is not None:
            result['GmtCreatedTime'] = self.gmt_created_time

        if self.gmt_expired_time is not None:
            result['GmtExpiredTime'] = self.gmt_expired_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.gmt_started_time is not None:
            result['GmtStartedTime'] = self.gmt_started_time

        if self.gpu is not None:
            result['Gpu'] = self.gpu

        if self.gpu_type is not None:
            result['GpuType'] = self.gpu_type

        if self.machine_group_id is not None:
            result['MachineGroupID'] = self.machine_group_id

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.name is not None:
            result['Name'] = self.name

        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration

        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupID'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.supported_drivers is not None:
            result['SupportedDrivers'] = self.supported_drivers

        if self.system_reserved_cpu is not None:
            result['SystemReservedCpu'] = self.system_reserved_cpu

        if self.system_reserved_memory is not None:
            result['SystemReservedMemory'] = self.system_reserved_memory

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocatableCpu') is not None:
            self.allocatable_cpu = m.get('AllocatableCpu')

        if m.get('AllocatableMemory') is not None:
            self.allocatable_memory = m.get('AllocatableMemory')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('DefaultDriver') is not None:
            self.default_driver = m.get('DefaultDriver')

        if m.get('EcsCount') is not None:
            self.ecs_count = m.get('EcsCount')

        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')

        if m.get('GmtCreatedTime') is not None:
            self.gmt_created_time = m.get('GmtCreatedTime')

        if m.get('GmtExpiredTime') is not None:
            self.gmt_expired_time = m.get('GmtExpiredTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('GmtStartedTime') is not None:
            self.gmt_started_time = m.get('GmtStartedTime')

        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')

        if m.get('GpuType') is not None:
            self.gpu_type = m.get('GpuType')

        if m.get('MachineGroupID') is not None:
            self.machine_group_id = m.get('MachineGroupID')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')

        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupID') is not None:
            self.resource_group_id = m.get('ResourceGroupID')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupportedDrivers') is not None:
            self.supported_drivers = m.get('SupportedDrivers')

        if m.get('SystemReservedCpu') is not None:
            self.system_reserved_cpu = m.get('SystemReservedCpu')

        if m.get('SystemReservedMemory') is not None:
            self.system_reserved_memory = m.get('SystemReservedMemory')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetResourceGroupMachineGroupResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class GetResourceGroupMachineGroupResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
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

