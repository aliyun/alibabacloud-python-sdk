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
        # - besteffort: BestEffort
        # 
        # - try-besteffort: BestEffort preferred
        # 
        # - default: default
        self.best_effort_type = best_effort_type
        # The number of CPU cores required for each instance. Unit: millicores. This value cannot be 0. Only the following defined specifications are supported:
        # 
        # - **500**
        # 
        # - **1000**
        # 
        # - **2000**
        # 
        # - **4000**
        # 
        # - **8000**
        # 
        # - **12000**
        # 
        # - **16000**
        # 
        # - **32000**
        # 
        # This parameter is required.
        self.cpu = cpu
        self.gpu_a10 = gpu_a10
        self.gpu_ppu_810e = gpu_ppu_810e
        # The amount of memory required for each instance. Unit: MB. This value cannot be 0. The memory size must correspond to the CPU specification. Only the following defined specifications are supported:
        # 
        # - **1024**: Corresponds to 500 millicores and 1,000 millicores of CPU.
        # 
        # - **2048**: Corresponds to 500, 1,000, and 2,000 millicores of CPU.
        # 
        # - **4096**: Corresponds to 1,000, 2,000, and 4,000 millicores of CPU.
        # 
        # - **8192**: Corresponds to 2,000, 4,000, and 8,000 millicores of CPU.
        # 
        # - **12288**: Corresponds to 12,000 millicores of CPU.
        # 
        # - **16384**: Corresponds to 4,000, 8,000, and 16,000 millicores of CPU.
        # 
        # - **24576**: Corresponds to 12,000 millicores of CPU.
        # 
        # - **32768**: Corresponds to 16,000 millicores of CPU.
        # 
        # - **65536**: Corresponds to 8,000, 16,000, and 32,000 millicores of CPU.
        # 
        # - **131072**: Corresponds to 32,000 millicores of CPU.
        # 
        # This parameter is required.
        self.memory = memory
        # The application version. Valid values:
        # 
        # - lite: Lightweight Edition
        # 
        # - std: Standard Edition
        # 
        # - pro: Professional Edition
        self.new_sae_version = new_sae_version
        # The resource type. Valid values: NULL (default), default, and haiguang (Haiguang server).
        self.resource_type = resource_type
        # The application scenario. Valid values:
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

