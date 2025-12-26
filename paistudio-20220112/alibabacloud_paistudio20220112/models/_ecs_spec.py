# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EcsSpec(DaraModel):
    def __init__(
        self,
        accelerator_type: str = None,
        cpu: int = None,
        ecs_image_id: str = None,
        eri_quantity: int = None,
        gpu: int = None,
        gpu_guspec: str = None,
        gpu_memory: int = None,
        gpu_type: str = None,
        gpu_type_alias: str = None,
        instance_type: str = None,
        machine_model: str = None,
        memory: int = None,
        network_mode: str = None,
        planned_cpu: int = None,
        planned_memory: int = None,
        resource_type: str = None,
        support_gpushare: bool = None,
        support_rdma: bool = None,
        support_set_network_card_index: bool = None,
    ):
        self.accelerator_type = accelerator_type
        self.cpu = cpu
        self.ecs_image_id = ecs_image_id
        self.eri_quantity = eri_quantity
        self.gpu = gpu
        self.gpu_guspec = gpu_guspec
        self.gpu_memory = gpu_memory
        self.gpu_type = gpu_type
        self.gpu_type_alias = gpu_type_alias
        self.instance_type = instance_type
        self.machine_model = machine_model
        self.memory = memory
        self.network_mode = network_mode
        self.planned_cpu = planned_cpu
        self.planned_memory = planned_memory
        self.resource_type = resource_type
        self.support_gpushare = support_gpushare
        self.support_rdma = support_rdma
        self.support_set_network_card_index = support_set_network_card_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.ecs_image_id is not None:
            result['EcsImageId'] = self.ecs_image_id

        if self.eri_quantity is not None:
            result['EriQuantity'] = self.eri_quantity

        if self.gpu is not None:
            result['Gpu'] = self.gpu

        if self.gpu_guspec is not None:
            result['GpuGUSpec'] = self.gpu_guspec

        if self.gpu_memory is not None:
            result['GpuMemory'] = self.gpu_memory

        if self.gpu_type is not None:
            result['GpuType'] = self.gpu_type

        if self.gpu_type_alias is not None:
            result['GpuTypeAlias'] = self.gpu_type_alias

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.machine_model is not None:
            result['MachineModel'] = self.machine_model

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.network_mode is not None:
            result['NetworkMode'] = self.network_mode

        if self.planned_cpu is not None:
            result['PlannedCpu'] = self.planned_cpu

        if self.planned_memory is not None:
            result['PlannedMemory'] = self.planned_memory

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.support_gpushare is not None:
            result['SupportGPUShare'] = self.support_gpushare

        if self.support_rdma is not None:
            result['SupportRDMA'] = self.support_rdma

        if self.support_set_network_card_index is not None:
            result['SupportSetNetworkCardIndex'] = self.support_set_network_card_index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('EcsImageId') is not None:
            self.ecs_image_id = m.get('EcsImageId')

        if m.get('EriQuantity') is not None:
            self.eri_quantity = m.get('EriQuantity')

        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')

        if m.get('GpuGUSpec') is not None:
            self.gpu_guspec = m.get('GpuGUSpec')

        if m.get('GpuMemory') is not None:
            self.gpu_memory = m.get('GpuMemory')

        if m.get('GpuType') is not None:
            self.gpu_type = m.get('GpuType')

        if m.get('GpuTypeAlias') is not None:
            self.gpu_type_alias = m.get('GpuTypeAlias')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('MachineModel') is not None:
            self.machine_model = m.get('MachineModel')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NetworkMode') is not None:
            self.network_mode = m.get('NetworkMode')

        if m.get('PlannedCpu') is not None:
            self.planned_cpu = m.get('PlannedCpu')

        if m.get('PlannedMemory') is not None:
            self.planned_memory = m.get('PlannedMemory')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SupportGPUShare') is not None:
            self.support_gpushare = m.get('SupportGPUShare')

        if m.get('SupportRDMA') is not None:
            self.support_rdma = m.get('SupportRDMA')

        if m.get('SupportSetNetworkCardIndex') is not None:
            self.support_set_network_card_index = m.get('SupportSetNetworkCardIndex')

        return self

