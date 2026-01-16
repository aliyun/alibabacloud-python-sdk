# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResidentResourceCapacity(DaraModel):
    def __init__(
        self,
        gpu_type: str = None,
        total_cpu_cores: int = None,
        total_disk_size: int = None,
        total_gpu_cards: int = None,
        total_gpu_memory_size: int = None,
        total_memory_size: int = None,
    ):
        # GPU 卡型
        self.gpu_type = gpu_type
        # CPU 总核数
        self.total_cpu_cores = total_cpu_cores
        # 总磁盘大小，单位 GB
        self.total_disk_size = total_disk_size
        # GPU总卡数
        self.total_gpu_cards = total_gpu_cards
        # 总显存大小，单位 GB
        self.total_gpu_memory_size = total_gpu_memory_size
        # 总内存大小，单位 GB
        self.total_memory_size = total_memory_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gpu_type is not None:
            result['gpuType'] = self.gpu_type

        if self.total_cpu_cores is not None:
            result['totalCpuCores'] = self.total_cpu_cores

        if self.total_disk_size is not None:
            result['totalDiskSize'] = self.total_disk_size

        if self.total_gpu_cards is not None:
            result['totalGpuCards'] = self.total_gpu_cards

        if self.total_gpu_memory_size is not None:
            result['totalGpuMemorySize'] = self.total_gpu_memory_size

        if self.total_memory_size is not None:
            result['totalMemorySize'] = self.total_memory_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gpuType') is not None:
            self.gpu_type = m.get('gpuType')

        if m.get('totalCpuCores') is not None:
            self.total_cpu_cores = m.get('totalCpuCores')

        if m.get('totalDiskSize') is not None:
            self.total_disk_size = m.get('totalDiskSize')

        if m.get('totalGpuCards') is not None:
            self.total_gpu_cards = m.get('totalGpuCards')

        if m.get('totalGpuMemorySize') is not None:
            self.total_gpu_memory_size = m.get('totalGpuMemorySize')

        if m.get('totalMemorySize') is not None:
            self.total_memory_size = m.get('totalMemorySize')

        return self

