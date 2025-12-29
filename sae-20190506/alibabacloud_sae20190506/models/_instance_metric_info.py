# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InstanceMetricInfo(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        cpu_percent: float = None,
        cpu_quota_percent: float = None,
        instance_id: str = None,
        memory_limit_mb: float = None,
        memory_usage_mb: float = None,
        timestamp: int = None,
    ):
        self.application_id = application_id
        self.cpu_percent = cpu_percent
        self.cpu_quota_percent = cpu_quota_percent
        self.instance_id = instance_id
        self.memory_limit_mb = memory_limit_mb
        self.memory_usage_mb = memory_usage_mb
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['applicationID'] = self.application_id

        if self.cpu_percent is not None:
            result['cpuPercent'] = self.cpu_percent

        if self.cpu_quota_percent is not None:
            result['cpuQuotaPercent'] = self.cpu_quota_percent

        if self.instance_id is not None:
            result['instanceID'] = self.instance_id

        if self.memory_limit_mb is not None:
            result['memoryLimitMB'] = self.memory_limit_mb

        if self.memory_usage_mb is not None:
            result['memoryUsageMB'] = self.memory_usage_mb

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationID') is not None:
            self.application_id = m.get('applicationID')

        if m.get('cpuPercent') is not None:
            self.cpu_percent = m.get('cpuPercent')

        if m.get('cpuQuotaPercent') is not None:
            self.cpu_quota_percent = m.get('cpuQuotaPercent')

        if m.get('instanceID') is not None:
            self.instance_id = m.get('instanceID')

        if m.get('memoryLimitMB') is not None:
            self.memory_limit_mb = m.get('memoryLimitMB')

        if m.get('memoryUsageMB') is not None:
            self.memory_usage_mb = m.get('memoryUsageMB')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        return self

