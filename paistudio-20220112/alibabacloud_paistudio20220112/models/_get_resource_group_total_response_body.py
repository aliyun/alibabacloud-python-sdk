# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class GetResourceGroupTotalResponseBody(DaraModel):
    def __init__(
        self,
        total_cpu: int = None,
        total_gpu: int = None,
        total_gpuinfos: List[main_models.GPUInfo] = None,
        total_memory: int = None,
    ):
        self.total_cpu = total_cpu
        self.total_gpu = total_gpu
        self.total_gpuinfos = total_gpuinfos
        self.total_memory = total_memory

    def validate(self):
        if self.total_gpuinfos:
            for v1 in self.total_gpuinfos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.total_cpu is not None:
            result['totalCPU'] = self.total_cpu

        if self.total_gpu is not None:
            result['totalGPU'] = self.total_gpu

        result['totalGPUInfos'] = []
        if self.total_gpuinfos is not None:
            for k1 in self.total_gpuinfos:
                result['totalGPUInfos'].append(k1.to_map() if k1 else None)

        if self.total_memory is not None:
            result['totalMemory'] = self.total_memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('totalCPU') is not None:
            self.total_cpu = m.get('totalCPU')

        if m.get('totalGPU') is not None:
            self.total_gpu = m.get('totalGPU')

        self.total_gpuinfos = []
        if m.get('totalGPUInfos') is not None:
            for k1 in m.get('totalGPUInfos'):
                temp_model = main_models.GPUInfo()
                self.total_gpuinfos.append(temp_model.from_map(k1))

        if m.get('totalMemory') is not None:
            self.total_memory = m.get('totalMemory')

        return self

