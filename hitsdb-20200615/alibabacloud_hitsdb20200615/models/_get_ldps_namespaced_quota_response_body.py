# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hitsdb20200615 import models as main_models
from darabonba.model import DaraModel

class GetLdpsNamespacedQuotaResponseBody(DaraModel):
    def __init__(
        self,
        namespaced_quotas: List[main_models.GetLdpsNamespacedQuotaResponseBodyNamespacedQuotas] = None,
        request_id: str = None,
    ):
        self.namespaced_quotas = namespaced_quotas
        self.request_id = request_id

    def validate(self):
        if self.namespaced_quotas:
            for v1 in self.namespaced_quotas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NamespacedQuotas'] = []
        if self.namespaced_quotas is not None:
            for k1 in self.namespaced_quotas:
                result['NamespacedQuotas'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.namespaced_quotas = []
        if m.get('NamespacedQuotas') is not None:
            for k1 in m.get('NamespacedQuotas'):
                temp_model = main_models.GetLdpsNamespacedQuotaResponseBodyNamespacedQuotas()
                self.namespaced_quotas.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetLdpsNamespacedQuotaResponseBodyNamespacedQuotas(DaraModel):
    def __init__(
        self,
        cpu_amount: str = None,
        memory_amount: str = None,
        name: str = None,
        used_cpu: str = None,
        used_memory: str = None,
    ):
        self.cpu_amount = cpu_amount
        self.memory_amount = memory_amount
        self.name = name
        self.used_cpu = used_cpu
        self.used_memory = used_memory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_amount is not None:
            result['CpuAmount'] = self.cpu_amount

        if self.memory_amount is not None:
            result['MemoryAmount'] = self.memory_amount

        if self.name is not None:
            result['Name'] = self.name

        if self.used_cpu is not None:
            result['UsedCpu'] = self.used_cpu

        if self.used_memory is not None:
            result['UsedMemory'] = self.used_memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuAmount') is not None:
            self.cpu_amount = m.get('CpuAmount')

        if m.get('MemoryAmount') is not None:
            self.memory_amount = m.get('MemoryAmount')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UsedCpu') is not None:
            self.used_cpu = m.get('UsedCpu')

        if m.get('UsedMemory') is not None:
            self.used_memory = m.get('UsedMemory')

        return self

