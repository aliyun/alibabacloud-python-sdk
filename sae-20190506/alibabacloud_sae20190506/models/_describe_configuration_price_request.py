# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeConfigurationPriceRequest(DaraModel):
    def __init__(
        self,
        best_effort_type: str = None,
        cpu: int = None,
        memory: int = None,
        new_sae_version: str = None,
        resource_type: str = None,
        workload: str = None,
    ):
        self.best_effort_type = best_effort_type
        # The CPU specifications that are required for each instance. Unit: millicores. This parameter cannot be set to 0. Valid values:
        # 
        # *   **500**
        # *   **1000**
        # *   **2000**
        # *   **4000**
        # *   **8000**
        # *   **12000**
        # *   **16000**
        # *   **32000**
        # 
        # This parameter is required.
        self.cpu = cpu
        # The memory size that is required by each instance. Unit: MB. This parameter cannot be set to 0. The values of this parameter correspond to the values of the Cpu parameter:
        # 
        # *   This parameter is set to **1024** if the Cpu parameter is set to 500 or 1000.
        # *   This parameter is set to **2048** if the Cpu parameter is set to 500, 1000, or 2000.
        # *   This parameter is set to **4096** if the Cpu parameter is set to 1000, 2000, or 4000.
        # *   This parameter is set to **8192** if the Cpu parameter is set to 2000, 4000, or 8,000.
        # *   This parameter is set to **12288** if the Cpu parameter is set to 12000.
        # *   This parameter is set to **16384** if the Cpu parameter is set to 4000, 8000, or 16000.
        # *   This parameter is set to **24576** if the Cpu parameter is set to 12000.
        # *   This parameter is set to **32768** if the Cpu parameter is set to 16000.
        # *   This parameter is set to **65536** if the Cpu parameter is set to 8000, 16000, or 32000.
        # *   This parameter is set to **131072** if the Cpu parameter is set to 32000.
        # 
        # This parameter is required.
        self.memory = memory
        self.new_sae_version = new_sae_version
        self.resource_type = resource_type
        # Scenarios:
        # 
        # *   Web
        # *   micro_service
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

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NewSaeVersion') is not None:
            self.new_sae_version = m.get('NewSaeVersion')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Workload') is not None:
            self.workload = m.get('Workload')

        return self

