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
        # - **2xx**: The request was successful.
        # 
        # - **3xx**: The request was redirected.
        # 
        # - **4xx**: A client error occurred.
        # 
        # - **5xx**: A server error occurred.
        self.code = code
        # The resource usage information.
        self.data = data
        # The error code.
        # 
        # - This parameter is not returned if the request is successful.
        # 
        # - This parameter is returned if the request fails. For more information, see the **Error codes** section in this topic.
        self.error_code = error_code
        # The response message.
        # 
        # - If the request is successful, **success** is returned.
        # 
        # - If the request fails, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # 
        # - **false**: The request failed.
        self.success = success
        # The trace ID used to query the details of a request.
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
        # The resource usage in the current month.
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
        # The active vCPU usage, in Core·min.
        self.active_cpu = active_cpu
        # The CPU usage, in Core·min.
        self.cpu = cpu
        # The number of CUs used.
        self.cu = cu
        # The ephemeral storage usage, in GiB·min.
        self.ephemeral_storage = ephemeral_storage
        # The GpuA10 usage.
        self.gpu_a10 = gpu_a10
        # The GpuPpu810e usage.
        self.gpu_ppu_810e = gpu_ppu_810e
        # The idle vCPU usage, in Core·min.
        self.idle_cpu = idle_cpu
        # The memory usage, in GiB·min.
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
        # The CPU usage, in Core·min.
        self.cpu = cpu
        # The ephemeral storage usage, in GiB·min.
        self.ephemeral_storage = ephemeral_storage
        # The memory usage, in GiB·min.
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

