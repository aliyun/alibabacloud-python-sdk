# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class JobMetric(DaraModel):
    def __init__(
        self,
        total_cpu: float = None,
        total_memory_byte: int = None,
    ):
        # The number of CPU cores.
        self.total_cpu = total_cpu
        # The memory size. Unit: bytes.
        self.total_memory_byte = total_memory_byte

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.total_cpu is not None:
            result['totalCpu'] = self.total_cpu

        if self.total_memory_byte is not None:
            result['totalMemoryByte'] = self.total_memory_byte

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('totalCpu') is not None:
            self.total_cpu = m.get('totalCpu')

        if m.get('totalMemoryByte') is not None:
            self.total_memory_byte = m.get('totalMemoryByte')

        return self

