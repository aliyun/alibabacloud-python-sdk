# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WebStaticsInfo(DaraModel):
    def __init__(
        self,
        cpu_usage: int = None,
        internet_traffic_out: int = None,
        invocations: int = None,
        memory_usage: int = None,
    ):
        self.cpu_usage = cpu_usage
        self.internet_traffic_out = internet_traffic_out
        self.invocations = invocations
        self.memory_usage = memory_usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_usage is not None:
            result['CpuUsage'] = self.cpu_usage

        if self.internet_traffic_out is not None:
            result['InternetTrafficOut'] = self.internet_traffic_out

        if self.invocations is not None:
            result['Invocations'] = self.invocations

        if self.memory_usage is not None:
            result['MemoryUsage'] = self.memory_usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuUsage') is not None:
            self.cpu_usage = m.get('CpuUsage')

        if m.get('InternetTrafficOut') is not None:
            self.internet_traffic_out = m.get('InternetTrafficOut')

        if m.get('Invocations') is not None:
            self.invocations = m.get('Invocations')

        if m.get('MemoryUsage') is not None:
            self.memory_usage = m.get('MemoryUsage')

        return self

