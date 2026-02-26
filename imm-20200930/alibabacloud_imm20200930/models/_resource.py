# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Resource(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        ecsinstance: str = None,
        gpumodel: str = None,
        gpunum: int = None,
        name: str = None,
        ram: int = None,
    ):
        # The number of CPU cores. Valid values: 4 to 96.
        self.cpu = cpu
        # The Elastic Compute Service (ECS) instance.
        self.ecsinstance = ecsinstance
        # The GPU.
        self.gpumodel = gpumodel
        # The number of GPUs.
        self.gpunum = gpunum
        # The displayed name of the resource.
        self.name = name
        # The RAM size. Unit: GB. Valid values: 30 to 736.
        self.ram = ram

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['CPU'] = self.cpu

        if self.ecsinstance is not None:
            result['ECSInstance'] = self.ecsinstance

        if self.gpumodel is not None:
            result['GPUModel'] = self.gpumodel

        if self.gpunum is not None:
            result['GPUNum'] = self.gpunum

        if self.name is not None:
            result['Name'] = self.name

        if self.ram is not None:
            result['RAM'] = self.ram

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')

        if m.get('ECSInstance') is not None:
            self.ecsinstance = m.get('ECSInstance')

        if m.get('GPUModel') is not None:
            self.gpumodel = m.get('GPUModel')

        if m.get('GPUNum') is not None:
            self.gpunum = m.get('GPUNum')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RAM') is not None:
            self.ram = m.get('RAM')

        return self

