# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class NodeType(DaraModel):
    def __init__(
        self,
        accelerator_type: str = None,
        allocatable_cpu: str = None,
        allocatable_memory: str = None,
        cpu: str = None,
        gpu: str = None,
        gpumemory: str = None,
        gputype: str = None,
        memory: str = None,
        node_type: str = None,
        system_reserved_cpu: str = None,
        system_reserved_memory: str = None,
    ):
        self.accelerator_type = accelerator_type
        self.allocatable_cpu = allocatable_cpu
        self.allocatable_memory = allocatable_memory
        self.cpu = cpu
        self.gpu = gpu
        self.gpumemory = gpumemory
        self.gputype = gputype
        self.memory = memory
        self.node_type = node_type
        self.system_reserved_cpu = system_reserved_cpu
        self.system_reserved_memory = system_reserved_memory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type

        if self.allocatable_cpu is not None:
            result['AllocatableCPU'] = self.allocatable_cpu

        if self.allocatable_memory is not None:
            result['AllocatableMemory'] = self.allocatable_memory

        if self.cpu is not None:
            result['CPU'] = self.cpu

        if self.gpu is not None:
            result['GPU'] = self.gpu

        if self.gpumemory is not None:
            result['GPUMemory'] = self.gpumemory

        if self.gputype is not None:
            result['GPUType'] = self.gputype

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.system_reserved_cpu is not None:
            result['SystemReservedCPU'] = self.system_reserved_cpu

        if self.system_reserved_memory is not None:
            result['SystemReservedMemory'] = self.system_reserved_memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')

        if m.get('AllocatableCPU') is not None:
            self.allocatable_cpu = m.get('AllocatableCPU')

        if m.get('AllocatableMemory') is not None:
            self.allocatable_memory = m.get('AllocatableMemory')

        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')

        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')

        if m.get('GPUMemory') is not None:
            self.gpumemory = m.get('GPUMemory')

        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('SystemReservedCPU') is not None:
            self.system_reserved_cpu = m.get('SystemReservedCPU')

        if m.get('SystemReservedMemory') is not None:
            self.system_reserved_memory = m.get('SystemReservedMemory')

        return self

