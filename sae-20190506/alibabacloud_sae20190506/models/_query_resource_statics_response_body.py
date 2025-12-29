# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class QueryResourceStaticsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryResourceStaticsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: indicates that the request was successful.
        # *   **3xx**: indicates that the request was redirected.
        # *   **4xx**: indicates that the request was invalid.
        # *   **5xx**: indicates that a server error occurred.
        self.code = code
        # The resource usage.
        self.data = data
        # The error code. 
        # 
        # - The **ErrorCode** parameter is not returned when the request succeeds.
        # - The **ErrorCode** parameter is returned when the request fails. For more information, see **Error codes** in this topic.
        self.error_code = error_code
        # The returned message.
        # 
        # *   **success** is returned when the request succeeds.
        # *   An error code is returned when the request fails.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the resource usage of an application was obtained. Valid values:
        # 
        # *   **true**: indicates that the resource usage was obtained.
        # *   **false**: indicates that the resource usage could not be obtained.
        self.success = success
        # The ID of the trace. It can be used to query the details of a request.
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryResourceStaticsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class QueryResourceStaticsResponseBodyData(DaraModel):
    def __init__(
        self,
        real_time_res: main_models.QueryResourceStaticsResponseBodyDataRealTimeRes = None,
        summary: main_models.QueryResourceStaticsResponseBodyDataSummary = None,
    ):
        # The real-time resource usage.
        self.real_time_res = real_time_res
        # The resource usage of the current month.
        self.summary = summary

    def validate(self):
        if self.real_time_res:
            self.real_time_res.validate()
        if self.summary:
            self.summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.real_time_res is not None:
            result['RealTimeRes'] = self.real_time_res.to_map()

        if self.summary is not None:
            result['Summary'] = self.summary.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RealTimeRes') is not None:
            temp_model = main_models.QueryResourceStaticsResponseBodyDataRealTimeRes()
            self.real_time_res = temp_model.from_map(m.get('RealTimeRes'))

        if m.get('Summary') is not None:
            temp_model = main_models.QueryResourceStaticsResponseBodyDataSummary()
            self.summary = temp_model.from_map(m.get('Summary'))

        return self

class QueryResourceStaticsResponseBodyDataSummary(DaraModel):
    def __init__(
        self,
        active_cpu: float = None,
        cpu: float = None,
        cu: float = None,
        ephemeral_storage: float = None,
        gpu_a10: float = None,
        gpu_ppu_810e: float = None,
        idle_cpu: float = None,
        memory: float = None,
    ):
        # The usage of active vCPU. Unit: Core*min.
        self.active_cpu = active_cpu
        # The CPU usage. Unit: core per minute.
        self.cpu = cpu
        # The CU usage.
        self.cu = cu
        # The storage size of the temporary storage space. Unit: GiB.
        self.ephemeral_storage = ephemeral_storage
        self.gpu_a10 = gpu_a10
        self.gpu_ppu_810e = gpu_ppu_810e
        # The usage of idle CPU. Unit: Core*min.
        self.idle_cpu = idle_cpu
        # The memory usage. Unit: GiB per minute.
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_cpu is not None:
            result['ActiveCpu'] = self.active_cpu

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.cu is not None:
            result['Cu'] = self.cu

        if self.ephemeral_storage is not None:
            result['EphemeralStorage'] = self.ephemeral_storage

        if self.gpu_a10 is not None:
            result['GpuA10'] = self.gpu_a10

        if self.gpu_ppu_810e is not None:
            result['GpuPpu810e'] = self.gpu_ppu_810e

        if self.idle_cpu is not None:
            result['IdleCpu'] = self.idle_cpu

        if self.memory is not None:
            result['Memory'] = self.memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveCpu') is not None:
            self.active_cpu = m.get('ActiveCpu')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('EphemeralStorage') is not None:
            self.ephemeral_storage = m.get('EphemeralStorage')

        if m.get('GpuA10') is not None:
            self.gpu_a10 = m.get('GpuA10')

        if m.get('GpuPpu810e') is not None:
            self.gpu_ppu_810e = m.get('GpuPpu810e')

        if m.get('IdleCpu') is not None:
            self.idle_cpu = m.get('IdleCpu')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        return self

class QueryResourceStaticsResponseBodyDataRealTimeRes(DaraModel):
    def __init__(
        self,
        cpu: float = None,
        ephemeral_storage: float = None,
        memory: float = None,
    ):
        # The CPU usage. Unit: core per minute.
        self.cpu = cpu
        # The storage size of the temporary storage space. Unit: GiB.
        self.ephemeral_storage = ephemeral_storage
        # The memory usage. Unit: GiB per minute.
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.ephemeral_storage is not None:
            result['EphemeralStorage'] = self.ephemeral_storage

        if self.memory is not None:
            result['Memory'] = self.memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('EphemeralStorage') is not None:
            self.ephemeral_storage = m.get('EphemeralStorage')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        return self

