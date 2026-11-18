# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResourceSpec(DaraModel):
    def __init__(
        self,
        cu: int = None,
        gpu: int = None,
        gpu_machine_num: int = None,
        instance_type_id: str = None,
        max_cu: int = None,
    ):
        # The number of CUs. Currently, 1 CU is equivalent to 1 vCPU and 4 GB of memory.
        self.cu = cu
        # The number of GPUs.
        self.gpu = gpu
        # The number of GPU machines.
        self.gpu_machine_num = gpu_machine_num
        # The instance type ID.
        self.instance_type_id = instance_type_id
        # The upper limit of the absolute value for the queue quota. If not specified, the backend falls back to the number of CUs.
        self.max_cu = max_cu

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['cu'] = self.cu

        if self.gpu is not None:
            result['gpu'] = self.gpu

        if self.gpu_machine_num is not None:
            result['gpuMachineNum'] = self.gpu_machine_num

        if self.instance_type_id is not None:
            result['instanceTypeId'] = self.instance_type_id

        if self.max_cu is not None:
            result['maxCu'] = self.max_cu

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cu') is not None:
            self.cu = m.get('cu')

        if m.get('gpu') is not None:
            self.gpu = m.get('gpu')

        if m.get('gpuMachineNum') is not None:
            self.gpu_machine_num = m.get('gpuMachineNum')

        if m.get('instanceTypeId') is not None:
            self.instance_type_id = m.get('instanceTypeId')

        if m.get('maxCu') is not None:
            self.max_cu = m.get('maxCu')

        return self

