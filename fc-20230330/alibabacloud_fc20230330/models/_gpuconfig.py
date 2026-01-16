# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GPUConfig(DaraModel):
    def __init__(
        self,
        gpu_memory_size: int = None,
        gpu_type: str = None,
    ):
        self.gpu_memory_size = gpu_memory_size
        self.gpu_type = gpu_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gpu_memory_size is not None:
            result['gpuMemorySize'] = self.gpu_memory_size

        if self.gpu_type is not None:
            result['gpuType'] = self.gpu_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gpuMemorySize') is not None:
            self.gpu_memory_size = m.get('gpuMemorySize')

        if m.get('gpuType') is not None:
            self.gpu_type = m.get('gpuType')

        return self

