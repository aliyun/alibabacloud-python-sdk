# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResourceInstanceWorker(DaraModel):
    def __init__(
        self,
        cpu_limit: int = None,
        cpu_request: int = None,
        gpu_limit: int = None,
        gpu_request: int = None,
        memory_limit: int = None,
        memory_rquest: int = None,
        name: str = None,
        ready: bool = None,
        restart_count: int = None,
        service_name: str = None,
        start_time: str = None,
        status: str = None,
    ):
        self.cpu_limit = cpu_limit
        self.cpu_request = cpu_request
        self.gpu_limit = gpu_limit
        self.gpu_request = gpu_request
        self.memory_limit = memory_limit
        self.memory_rquest = memory_rquest
        self.name = name
        self.ready = ready
        self.restart_count = restart_count
        self.service_name = service_name
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_limit is not None:
            result['CpuLimit'] = self.cpu_limit

        if self.cpu_request is not None:
            result['CpuRequest'] = self.cpu_request

        if self.gpu_limit is not None:
            result['GpuLimit'] = self.gpu_limit

        if self.gpu_request is not None:
            result['GpuRequest'] = self.gpu_request

        if self.memory_limit is not None:
            result['MemoryLimit'] = self.memory_limit

        if self.memory_rquest is not None:
            result['MemoryRquest'] = self.memory_rquest

        if self.name is not None:
            result['Name'] = self.name

        if self.ready is not None:
            result['Ready'] = self.ready

        if self.restart_count is not None:
            result['RestartCount'] = self.restart_count

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuLimit') is not None:
            self.cpu_limit = m.get('CpuLimit')

        if m.get('CpuRequest') is not None:
            self.cpu_request = m.get('CpuRequest')

        if m.get('GpuLimit') is not None:
            self.gpu_limit = m.get('GpuLimit')

        if m.get('GpuRequest') is not None:
            self.gpu_request = m.get('GpuRequest')

        if m.get('MemoryLimit') is not None:
            self.memory_limit = m.get('MemoryLimit')

        if m.get('MemoryRquest') is not None:
            self.memory_rquest = m.get('MemoryRquest')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Ready') is not None:
            self.ready = m.get('Ready')

        if m.get('RestartCount') is not None:
            self.restart_count = m.get('RestartCount')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

