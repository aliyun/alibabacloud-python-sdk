# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResourceAmount(DaraModel):
    def __init__(
        self,
        cpu: str = None,
        gpu: str = None,
        gpumemory: str = None,
        gpumemory_bytes: int = None,
        gputype: str = None,
        memory: str = None,
    ):
        # Total CPU
        self.cpu = cpu
        # Total GPU cards
        self.gpu = gpu
        self.gpumemory = gpumemory
        self.gpumemory_bytes = gpumemory_bytes
        # GPU card type
        self.gputype = gputype
        # Total memory
        self.memory = memory

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

        if self.gpumemory is not None:
            result['GPUMemory'] = self.gpumemory

        if self.gpumemory_bytes is not None:
            result['GPUMemoryBytes'] = self.gpumemory_bytes

        if self.gputype is not None:
            result['GPUType'] = self.gputype

        if self.memory is not None:
            result['Memory'] = self.memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')

        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')

        if m.get('GPUMemory') is not None:
            self.gpumemory = m.get('GPUMemory')

        if m.get('GPUMemoryBytes') is not None:
            self.gpumemory_bytes = m.get('GPUMemoryBytes')

        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        return self

