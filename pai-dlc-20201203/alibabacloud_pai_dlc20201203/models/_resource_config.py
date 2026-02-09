# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResourceConfig(DaraModel):
    def __init__(
        self,
        cpu: str = None,
        gpu: str = None,
        gputype: str = None,
        memory: str = None,
        shared_memory: str = None,
    ):
        # The number of vCPUs.
        self.cpu = cpu
        # The number of GPUs.
        self.gpu = gpu
        # The GPU type.
        self.gputype = gputype
        # The memory size.
        self.memory = memory
        # The shared memory capacity.
        self.shared_memory = shared_memory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['CPU'] = self.cpu

        if self.gpu is not None:
            result['GPU'] = self.gpu

        if self.gputype is not None:
            result['GPUType'] = self.gputype

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.shared_memory is not None:
            result['SharedMemory'] = self.shared_memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')

        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')

        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('SharedMemory') is not None:
            self.shared_memory = m.get('SharedMemory')

        return self

