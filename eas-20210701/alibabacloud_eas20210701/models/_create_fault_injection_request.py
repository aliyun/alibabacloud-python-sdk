# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class CreateFaultInjectionRequest(DaraModel):
    def __init__(
        self,
        fault_args: Any = None,
        fault_type: str = None,
    ):
        # The parameters for each fault type are described as follows:
        # 
        # 1. CpuFullloadTask (CPU full load fault)
        #    `{ "FaultType": "CpuFullloadTask", "FaultArgs": { "FaultAction": "fullload", "CpuPercent": 50 } }`
        # 
        # 2. MemLoadTask (Memory load fault)
        #    `{ "FaultType": "MemLoadTask", "FaultArgs": { "FaultAction": "load", "MemPercent": 80 } }`
        # 
        # 3. NetworkTask (Network fault)
        #    3.a. NetworkDelayAction (Network delay)
        #    `{ "FaultType": "NetworkTask", "FaultArgs": { "FaultAction": "delay", "Time": 3000, "Offset": 100 } }`
        #    3.b. NetworkCorruptAction (Network packet corruption)
        #    `{ "FaultType": "NetworkTask", "FaultArgs": { "FaultAction": "corrupt", "Percent": 50 } }`
        #    3.c. NetworkLossAction (Network packet loss)
        #    `{ "FaultType": "NetworkTask", "FaultArgs": { "FaultAction": "loss", "Percent": 30 } }`
        # 
        # 4. DiskBurnTask (Disk read/write fault)
        #    `{ "FaultType": "DiskBurnTask", "FaultArgs": { "FaultAction": "burn", "Read": true, "Write": true, "Size": 100 } }`
        # 
        # 5. DiskFillTask (Disk fill fault)
        #    `{ "FaultType": "DiskFillTask", "FaultArgs": { "FaultAction": "fill", "Percent": 80 } }`
        self.fault_args = fault_args
        # The fault type.
        # Device faults: 1. CPU full load fault. 2. Memory load fault. 3. Network fault. 4. Disk read/write fault. 5. Disk fill fault.
        self.fault_type = fault_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fault_args is not None:
            result['FaultArgs'] = self.fault_args

        if self.fault_type is not None:
            result['FaultType'] = self.fault_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaultArgs') is not None:
            self.fault_args = m.get('FaultArgs')

        if m.get('FaultType') is not None:
            self.fault_type = m.get('FaultType')

        return self

