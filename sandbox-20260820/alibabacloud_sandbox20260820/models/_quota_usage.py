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
        scaling_cpu_cores_per_minute: float = None,
    ):
        # The consumed CPU quota in vCPUs, which does not represent CPU utilization.
        self.cpu_cores = cpu_cores
        # The number of unreleased instance authorizations.
        self.instance_count = instance_count
        # The consumed memory quota in GB, which does not represent the actual memory used by processes.
        self.memory_gb = memory_gb
        # The number of cores consumed from the team\\"s exclusive CPU creation quota that have not yet been naturally replenished. This is not the cumulative creation volume over the last minute. This field is omitted when no valid exclusive bucket snapshot is available, and actual zeros and decimals are retained.
        self.scaling_cpu_cores_per_minute = scaling_cpu_cores_per_minute

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

        if self.scaling_cpu_cores_per_minute is not None:
            result['scalingCpuCoresPerMinute'] = self.scaling_cpu_cores_per_minute

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuCores') is not None:
            self.cpu_cores = m.get('cpuCores')

        if m.get('instanceCount') is not None:
            self.instance_count = m.get('instanceCount')

        if m.get('memoryGB') is not None:
            self.memory_gb = m.get('memoryGB')

        if m.get('scalingCpuCoresPerMinute') is not None:
            self.scaling_cpu_cores_per_minute = m.get('scalingCpuCoresPerMinute')

        return self

