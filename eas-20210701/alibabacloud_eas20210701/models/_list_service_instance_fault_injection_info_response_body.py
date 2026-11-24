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
        # The list of injected faults.
        self.fault_info_list = fault_info_list
        # Id of the request
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
        # Detailed parameters for each fault type:
        # 1. CpuFullloadTask (CPU full load fault)
        # `
        # {
        #   "FaultType": "CpuFullloadTask",
        #   "FaultArgs": {
        #     "FaultAction": "fullload",
        #     "CpuPercent": 50
        #   }
        # }
        # `
        # 2. MemLoadTask (memory load fault)
        # `
        # {
        #   "FaultType": "MemLoadTask",
        #   "FaultArgs": {
        #     "FaultAction": "load",
        #     "MemPercent": 80
        #   }
        # }
        # `
        # 3. NetworkTask (network fault)
        # 3.a. NetworkDelayAction (network delay)
        # `
        # {
        #   "FaultType": "NetworkTask",
        #   "FaultArgs": {
        #     "FaultAction": "delay",
        #     "Time": 3000,
        #     "Offset": 100
        #   }
        # }
        # `
        # 3.b. NetworkCorruptAction (network packet corruption)
        # `
        # {
        #   "FaultType": "NetworkTask",
        #   "FaultArgs": {
        #     "FaultAction": "corrupt",
        #     "Percent": 50
        #   }
        # }
        # `
        # 3.c. NetworkLossAction (network packet loss)
        # `
        # {
        #   "FaultType": "NetworkTask",
        #   "FaultArgs": {
        #     "FaultAction": "loss",
        #     "Percent": 30
        #   }
        # }
        # `
        # 4. DiskBurnTask (disk read/write fault)
        # `
        # {
        #   "FaultType": "DiskBurnTask",
        #   "FaultArgs": {
        #     "FaultAction": "burn",
        #     "Read": true,
        #     "Write": true,
        #     "Size": 100
        #   }
        # }
        # `
        # 5. DiskFillTask (disk fill fault)
        # `
        # {
        #   "FaultType": "DiskFillTask",
        #   "FaultArgs": {
        #     "FaultAction": "fill",
        #     "Percent": 80
        #   }
        # }
        # `
        self.fault_args = fault_args
        # The fault status.
        self.fault_status = fault_status
        # The fault type. Valid values:
        # - CpuFullloadTask: CPU full load fault.
        # - MemLoadTask: memory load fault.
        # - NetworkTask: network fault.
        # - DiskBurnTask: disk read/write fault.
        # - DiskFillTask: disk fill fault.
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
        # The fault status. Valid values:
        # - FaultNotInjected: The task is created but the fault is not injected.
        # - FaultInjectedSuccess: The fault is successfully injected.
        # - FaultInjectedFailure: The fault injection failed, which may be caused by parameter errors or system issues.
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

