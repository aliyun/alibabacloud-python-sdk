# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeConfigurationPriceRequest(DaraModel):
    def __init__(
        self,
        best_effort_type: str = None,
        cpu: int = None,
        gpu_a10: str = None,
        gpu_ppu_810e: str = None,
        memory: int = None,
        new_sae_version: str = None,
        resource_type: str = None,
        workload: str = None,
    ):
        # The BestEffort policy. Valid values:
        # 
        # - besteffort: BestEffort.
        # - try-besteffort: BestEffort preferred.
        # - default: Default.
        self.best_effort_type = best_effort_type
        # The required CPU for each instance, in millicores. The value cannot be 0. Only the following defined specifications are supported:
        # - **500**
        # - **1000**
        # - **2000**
        # - **4000**
        # - **8000**
        # - **12000**
        # - **16000**
        # - **32000**
        # 
        # This parameter is required.
        self.cpu = cpu
        # The number of A10 GPUs.
        self.gpu_a10 = gpu_a10
        # The number of PPU 810E units.
        self.gpu_ppu_810e = gpu_ppu_810e
        # The required memory for each instance, in MB. The value cannot be 0. Memory has a one-to-one mapping with CPU. Only the following defined specifications are supported:
        # - **1024**: Corresponds to 500 and 1000 millicores.
        # - **2048**: Corresponds to 500, 1000, and 2000 millicores.
        # - **4096**: Corresponds to 1000, 2000, and 4000 millicores.
        # - **8192**: Corresponds to 2000, 4000, and 8000 millicores.
        # - **12288**: Corresponds to 12000 millicores.
        # - **16384**: Corresponds to 4000, 8000, and 16000 millicores.
        # - **24576**: Corresponds to 12000 millicores.
        # - **32768**: Corresponds to 16000 millicores.
        # - **65536**: Corresponds to 8000, 16000, and 32000 millicores.
        # - **131072**: Corresponds to 32000 millicores.
        # 
        # This parameter is required.
        self.memory = memory
        # The application edition. Valid values:
        # 
        # - lite: Lite Edition.
        # - std: Standard Edition.
        # - pro: Professional Edition.
        self.new_sae_version = new_sae_version
        # The resource type. Valid values: NULL (default), default (default), and haiguang (Hygon server).
        self.resource_type = resource_type
        # Common scenarios. Valid values:
        # 
        # - web
        # 
        # - micro_service
        self.workload = workload

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.best_effort_type is not None:
            result['BestEffortType'] = self.best_effort_type

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.gpu_a10 is not None:
            result['GpuA10'] = self.gpu_a10

        if self.gpu_ppu_810e is not None:
            result['GpuPpu810e'] = self.gpu_ppu_810e

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.new_sae_version is not None:
            result['NewSaeVersion'] = self.new_sae_version

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.workload is not None:
            result['Workload'] = self.workload

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BestEffortType') is not None:
            self.best_effort_type = m.get('BestEffortType')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('GpuA10') is not None:
            self.gpu_a10 = m.get('GpuA10')

        if m.get('GpuPpu810e') is not None:
            self.gpu_ppu_810e = m.get('GpuPpu810e')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NewSaeVersion') is not None:
            self.new_sae_version = m.get('NewSaeVersion')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Workload') is not None:
            self.workload = m.get('Workload')

        return self

