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
        # The consumed CPU quota in vCPUs, not the CPU utilization.
        self.cpu_cores = cpu_cores
        # The number of unreleased instance authorizations.
        self.instance_count = instance_count
        # The consumed memory quota in GB, not the actual memory used by processes.
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

