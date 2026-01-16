# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResidentResourceAllocation(DaraModel):
    def __init__(
        self,
        function_name: str = None,
        instance_count: int = None,
        instance_type: str = None,
        qualifier: str = None,
        total_cpu_cores: float = None,
        total_disk_size: float = None,
        total_gpu_memory_size: float = None,
        total_memory_size: float = None,
    ):
        # 使用该资源池的函数名
        self.function_name = function_name
        # 实例数
        self.instance_count = instance_count
        self.instance_type = instance_type
        # 函数的别名
        self.qualifier = qualifier
        # CPU 占用总核数
        self.total_cpu_cores = total_cpu_cores
        # 占用磁盘大小，单位 GB
        self.total_disk_size = total_disk_size
        # 占用显存大小，单位 GB
        self.total_gpu_memory_size = total_gpu_memory_size
        # 内存占用大小，单位 GB
        self.total_memory_size = total_memory_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function_name is not None:
            result['functionName'] = self.function_name

        if self.instance_count is not None:
            result['instanceCount'] = self.instance_count

        if self.instance_type is not None:
            result['instanceType'] = self.instance_type

        if self.qualifier is not None:
            result['qualifier'] = self.qualifier

        if self.total_cpu_cores is not None:
            result['totalCpuCores'] = self.total_cpu_cores

        if self.total_disk_size is not None:
            result['totalDiskSize'] = self.total_disk_size

        if self.total_gpu_memory_size is not None:
            result['totalGpuMemorySize'] = self.total_gpu_memory_size

        if self.total_memory_size is not None:
            result['totalMemorySize'] = self.total_memory_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')

        if m.get('instanceCount') is not None:
            self.instance_count = m.get('instanceCount')

        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')

        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')

        if m.get('totalCpuCores') is not None:
            self.total_cpu_cores = m.get('totalCpuCores')

        if m.get('totalDiskSize') is not None:
            self.total_disk_size = m.get('totalDiskSize')

        if m.get('totalGpuMemorySize') is not None:
            self.total_gpu_memory_size = m.get('totalGpuMemorySize')

        if m.get('totalMemorySize') is not None:
            self.total_memory_size = m.get('totalMemorySize')

        return self

