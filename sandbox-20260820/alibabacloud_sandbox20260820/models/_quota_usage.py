# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuotaUsage(DaraModel):
    def __init__(
        self,
        cpu_cores: float = None,
        instance_count: int = None,
        memory_gb: float = None,
    ):
        # 已占用的 CPU 配额，单位为 vCPU，不是 CPU 使用率。
        self.cpu_cores = cpu_cores
        # 尚未释放的实例授权数量。
        self.instance_count = instance_count
        # 已占用的内存配额，单位为 GB，不是进程实际内存。
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_cores is not None:
            result['cpuCores'] = self.cpu_cores

        if self.instance_count is not None:
            result['instanceCount'] = self.instance_count

        if self.memory_gb is not None:
            result['memoryGB'] = self.memory_gb

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuCores') is not None:
            self.cpu_cores = m.get('cpuCores')

        if m.get('instanceCount') is not None:
            self.instance_count = m.get('instanceCount')

        if m.get('memoryGB') is not None:
            self.memory_gb = m.get('memoryGB')

        return self

