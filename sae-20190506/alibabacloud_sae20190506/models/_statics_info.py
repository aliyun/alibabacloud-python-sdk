# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StaticsInfo(DaraModel):
    def __init__(
        self,
        active_cpuusage: int = None,
        cost: float = None,
        disk_usage: int = None,
        function_name: str = None,
        gpu_usage: int = None,
        idle_cpuusage: int = None,
        instance_traffic_out: int = None,
        invocations: int = None,
        invoke_cdnout: int = None,
        invoke_internet_out: int = None,
        memory_usage: int = None,
        region: str = None,
        service_name: str = None,
    ):
        self.active_cpuusage = active_cpuusage
        self.cost = cost
        self.disk_usage = disk_usage
        self.function_name = function_name
        self.gpu_usage = gpu_usage
        self.idle_cpuusage = idle_cpuusage
        self.instance_traffic_out = instance_traffic_out
        self.invocations = invocations
        self.invoke_cdnout = invoke_cdnout
        self.invoke_internet_out = invoke_internet_out
        self.memory_usage = memory_usage
        self.region = region
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_cpuusage is not None:
            result['activeCPUUsage'] = self.active_cpuusage

        if self.cost is not None:
            result['cost'] = self.cost

        if self.disk_usage is not None:
            result['diskUsage'] = self.disk_usage

        if self.function_name is not None:
            result['functionName'] = self.function_name

        if self.gpu_usage is not None:
            result['gpuUsage'] = self.gpu_usage

        if self.idle_cpuusage is not None:
            result['idleCPUUsage'] = self.idle_cpuusage

        if self.instance_traffic_out is not None:
            result['instanceTrafficOut'] = self.instance_traffic_out

        if self.invocations is not None:
            result['invocations'] = self.invocations

        if self.invoke_cdnout is not None:
            result['invokeCDNOut'] = self.invoke_cdnout

        if self.invoke_internet_out is not None:
            result['invokeInternetOut'] = self.invoke_internet_out

        if self.memory_usage is not None:
            result['memoryUsage'] = self.memory_usage

        if self.region is not None:
            result['region'] = self.region

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activeCPUUsage') is not None:
            self.active_cpuusage = m.get('activeCPUUsage')

        if m.get('cost') is not None:
            self.cost = m.get('cost')

        if m.get('diskUsage') is not None:
            self.disk_usage = m.get('diskUsage')

        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')

        if m.get('gpuUsage') is not None:
            self.gpu_usage = m.get('gpuUsage')

        if m.get('idleCPUUsage') is not None:
            self.idle_cpuusage = m.get('idleCPUUsage')

        if m.get('instanceTrafficOut') is not None:
            self.instance_traffic_out = m.get('instanceTrafficOut')

        if m.get('invocations') is not None:
            self.invocations = m.get('invocations')

        if m.get('invokeCDNOut') is not None:
            self.invoke_cdnout = m.get('invokeCDNOut')

        if m.get('invokeInternetOut') is not None:
            self.invoke_internet_out = m.get('invokeInternetOut')

        if m.get('memoryUsage') is not None:
            self.memory_usage = m.get('memoryUsage')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        return self

