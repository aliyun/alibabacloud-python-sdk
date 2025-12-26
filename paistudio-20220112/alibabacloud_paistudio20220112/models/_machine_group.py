# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class MachineGroup(DaraModel):
    def __init__(
        self,
        allocatable_cpu: int = None,
        allocatable_memory: int = None,
        cpu: int = None,
        creator_id: str = None,
        default_driver: str = None,
        disk_capacity: int = None,
        disk_pl: str = None,
        ecs_count: int = None,
        ecs_spec: str = None,
        gmt_created_time: str = None,
        gmt_expired_time: str = None,
        gmt_modified_time: str = None,
        gmt_started_time: str = None,
        gpu: int = None,
        gpu_memory: int = None,
        gpu_type: str = None,
        machine_group_id: str = None,
        memory: int = None,
        order_instance_id: str = None,
        payment_duration: str = None,
        payment_duration_unit: str = None,
        payment_type: str = None,
        reason_code: str = None,
        reason_message: str = None,
        resource_group_id: str = None,
        resource_type: str = None,
        status: str = None,
        supported_drivers: List[str] = None,
        system_reserved_cpu: int = None,
        system_reserved_memory: int = None,
    ):
        self.allocatable_cpu = allocatable_cpu
        self.allocatable_memory = allocatable_memory
        self.cpu = cpu
        self.creator_id = creator_id
        self.default_driver = default_driver
        self.disk_capacity = disk_capacity
        self.disk_pl = disk_pl
        self.ecs_count = ecs_count
        self.ecs_spec = ecs_spec
        self.gmt_created_time = gmt_created_time
        self.gmt_expired_time = gmt_expired_time
        self.gmt_modified_time = gmt_modified_time
        self.gmt_started_time = gmt_started_time
        self.gpu = gpu
        self.gpu_memory = gpu_memory
        self.gpu_type = gpu_type
        self.machine_group_id = machine_group_id
        self.memory = memory
        self.order_instance_id = order_instance_id
        self.payment_duration = payment_duration
        self.payment_duration_unit = payment_duration_unit
        self.payment_type = payment_type
        self.reason_code = reason_code
        self.reason_message = reason_message
        self.resource_group_id = resource_group_id
        self.resource_type = resource_type
        self.status = status
        self.supported_drivers = supported_drivers
        self.system_reserved_cpu = system_reserved_cpu
        self.system_reserved_memory = system_reserved_memory

    def validate(self):
        pass

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

        if self.creator_id is not None:
            result['CreatorID'] = self.creator_id

        if self.default_driver is not None:
            result['DefaultDriver'] = self.default_driver

        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity

        if self.disk_pl is not None:
            result['DiskPL'] = self.disk_pl

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

        if self.gpu_memory is not None:
            result['GpuMemory'] = self.gpu_memory

        if self.gpu_type is not None:
            result['GpuType'] = self.gpu_type

        if self.machine_group_id is not None:
            result['MachineGroupID'] = self.machine_group_id

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.order_instance_id is not None:
            result['OrderInstanceId'] = self.order_instance_id

        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration

        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message

        if self.resource_group_id is not None:
            result['ResourceGroupID'] = self.resource_group_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.status is not None:
            result['Status'] = self.status

        if self.supported_drivers is not None:
            result['SupportedDrivers'] = self.supported_drivers

        if self.system_reserved_cpu is not None:
            result['SystemReservedCpu'] = self.system_reserved_cpu

        if self.system_reserved_memory is not None:
            result['SystemReservedMemory'] = self.system_reserved_memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocatableCpu') is not None:
            self.allocatable_cpu = m.get('AllocatableCpu')

        if m.get('AllocatableMemory') is not None:
            self.allocatable_memory = m.get('AllocatableMemory')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CreatorID') is not None:
            self.creator_id = m.get('CreatorID')

        if m.get('DefaultDriver') is not None:
            self.default_driver = m.get('DefaultDriver')

        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')

        if m.get('DiskPL') is not None:
            self.disk_pl = m.get('DiskPL')

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

        if m.get('GpuMemory') is not None:
            self.gpu_memory = m.get('GpuMemory')

        if m.get('GpuType') is not None:
            self.gpu_type = m.get('GpuType')

        if m.get('MachineGroupID') is not None:
            self.machine_group_id = m.get('MachineGroupID')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('OrderInstanceId') is not None:
            self.order_instance_id = m.get('OrderInstanceId')

        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')

        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')

        if m.get('ResourceGroupID') is not None:
            self.resource_group_id = m.get('ResourceGroupID')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupportedDrivers') is not None:
            self.supported_drivers = m.get('SupportedDrivers')

        if m.get('SystemReservedCpu') is not None:
            self.system_reserved_cpu = m.get('SystemReservedCpu')

        if m.get('SystemReservedMemory') is not None:
            self.system_reserved_memory = m.get('SystemReservedMemory')

        return self

