# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class GetResourceGroupRequestResponseBody(DaraModel):
    def __init__(
        self,
        request_cpu: int = None,
        request_gpu: int = None,
        request_gpuinfos: List[main_models.GPUInfo] = None,
        request_memory: int = None,
    ):
        self.request_cpu = request_cpu
        self.request_gpu = request_gpu
        self.request_gpuinfos = request_gpuinfos
        self.request_memory = request_memory

    def validate(self):
        if self.request_gpuinfos:
            for v1 in self.request_gpuinfos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_cpu is not None:
            result['requestCPU'] = self.request_cpu

        if self.request_gpu is not None:
            result['requestGPU'] = self.request_gpu

        result['requestGPUInfos'] = []
        if self.request_gpuinfos is not None:
            for k1 in self.request_gpuinfos:
                result['requestGPUInfos'].append(k1.to_map() if k1 else None)

        if self.request_memory is not None:
            result['requestMemory'] = self.request_memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestCPU') is not None:
            self.request_cpu = m.get('requestCPU')

        if m.get('requestGPU') is not None:
            self.request_gpu = m.get('requestGPU')

        self.request_gpuinfos = []
        if m.get('requestGPUInfos') is not None:
            for k1 in m.get('requestGPUInfos'):
                temp_model = main_models.GPUInfo()
                self.request_gpuinfos.append(temp_model.from_map(k1))

        if m.get('requestMemory') is not None:
            self.request_memory = m.get('requestMemory')

        return self

