# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class NodeGPUMetric(DaraModel):
    def __init__(
        self,
        accelerator_type: str = None,
        gpucount: int = None,
        gpumetrics: List[main_models.GPUMetric] = None,
        gputype: str = None,
        memory_util: float = None,
        node_id: str = None,
        node_type: str = None,
        total_memory: float = None,
        used_memory: float = None,
    ):
        self.accelerator_type = accelerator_type
        self.gpucount = gpucount
        self.gpumetrics = gpumetrics
        self.gputype = gputype
        self.memory_util = memory_util
        self.node_id = node_id
        self.node_type = node_type
        self.total_memory = total_memory
        self.used_memory = used_memory

    def validate(self):
        if self.gpumetrics:
            for v1 in self.gpumetrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type

        if self.gpucount is not None:
            result['GPUCount'] = self.gpucount

        result['GPUMetrics'] = []
        if self.gpumetrics is not None:
            for k1 in self.gpumetrics:
                result['GPUMetrics'].append(k1.to_map() if k1 else None)

        if self.gputype is not None:
            result['GPUType'] = self.gputype

        if self.memory_util is not None:
            result['MemoryUtil'] = self.memory_util

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.total_memory is not None:
            result['TotalMemory'] = self.total_memory

        if self.used_memory is not None:
            result['UsedMemory'] = self.used_memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')

        if m.get('GPUCount') is not None:
            self.gpucount = m.get('GPUCount')

        self.gpumetrics = []
        if m.get('GPUMetrics') is not None:
            for k1 in m.get('GPUMetrics'):
                temp_model = main_models.GPUMetric()
                self.gpumetrics.append(temp_model.from_map(k1))

        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')

        if m.get('MemoryUtil') is not None:
            self.memory_util = m.get('MemoryUtil')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('TotalMemory') is not None:
            self.total_memory = m.get('TotalMemory')

        if m.get('UsedMemory') is not None:
            self.used_memory = m.get('UsedMemory')

        return self

