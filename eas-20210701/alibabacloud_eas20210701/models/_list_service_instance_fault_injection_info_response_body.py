# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class ListServiceInstanceFaultInjectionInfoResponseBody(DaraModel):
    def __init__(
        self,
        fault_info_list: List[main_models.ListServiceInstanceFaultInjectionInfoResponseBodyFaultInfoList] = None,
        request_id: str = None,
    ):
        # A list of injected faults.
        self.fault_info_list = fault_info_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.fault_info_list:
            for v1 in self.fault_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FaultInfoList'] = []
        if self.fault_info_list is not None:
            for k1 in self.fault_info_list:
                result['FaultInfoList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fault_info_list = []
        if m.get('FaultInfoList') is not None:
            for k1 in m.get('FaultInfoList'):
                temp_model = main_models.ListServiceInstanceFaultInjectionInfoResponseBodyFaultInfoList()
                self.fault_info_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListServiceInstanceFaultInjectionInfoResponseBodyFaultInfoList(DaraModel):
    def __init__(
        self,
        fault_args: Any = None,
        fault_status: main_models.ListServiceInstanceFaultInjectionInfoResponseBodyFaultInfoListFaultStatus = None,
        fault_type: str = None,
    ):
        # The parameters for each fault type.
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
        # The fault status.
        self.fault_status = fault_status
        # The fault type. Valid values:CpuFullloadTask: a CPU full load fault.MemLoadTask: a memory load fault.NetworkTask: a network fault.DiskBurnTask: a disk read/write fault.DiskFillTask: a disk fill fault.
        self.fault_type = fault_type

    def validate(self):
        if self.fault_status:
            self.fault_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fault_args is not None:
            result['FaultArgs'] = self.fault_args

        if self.fault_status is not None:
            result['FaultStatus'] = self.fault_status.to_map()

        if self.fault_type is not None:
            result['FaultType'] = self.fault_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaultArgs') is not None:
            self.fault_args = m.get('FaultArgs')

        if m.get('FaultStatus') is not None:
            temp_model = main_models.ListServiceInstanceFaultInjectionInfoResponseBodyFaultInfoListFaultStatus()
            self.fault_status = temp_model.from_map(m.get('FaultStatus'))

        if m.get('FaultType') is not None:
            self.fault_type = m.get('FaultType')

        return self

class ListServiceInstanceFaultInjectionInfoResponseBodyFaultInfoListFaultStatus(DaraModel):
    def __init__(
        self,
        fault_status: str = None,
        fault_status_message: str = None,
    ):
        # The status of the fault. Valid values:
        # 
        # 1. FaultNotInjected: The task was created, but the fault was not successfully injected.
        # 
        # 2. FaultInjectedSuccess: The fault was successfully injected.
        # 
        # 3. FaultInjectedFailure: The fault injection failed. The failure may be caused by parameter errors or system issues.
        self.fault_status = fault_status
        # The description of the fault injection.
        self.fault_status_message = fault_status_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fault_status is not None:
            result['FaultStatus'] = self.fault_status

        if self.fault_status_message is not None:
            result['FaultStatusMessage'] = self.fault_status_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaultStatus') is not None:
            self.fault_status = m.get('FaultStatus')

        if m.get('FaultStatusMessage') is not None:
            self.fault_status_message = m.get('FaultStatusMessage')

        return self

