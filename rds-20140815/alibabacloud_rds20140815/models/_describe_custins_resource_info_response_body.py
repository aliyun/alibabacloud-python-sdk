# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeCustinsResourceInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeCustinsResourceInfoResponseBodyData] = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeCustinsResourceInfoResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCustinsResourceInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        cpu_adjust_deadline: str = None,
        cpu_adjustable_max_ratio: str = None,
        cpu_adjustable_max_value: str = None,
        cpu_increase_ratio: str = None,
        cpu_increase_ratio_value: str = None,
        dbinstance_id: str = None,
        iops_adjustable_max_value: str = None,
        max_conn_adjust_deadline: str = None,
        max_conn_adjustable_max_value: str = None,
        max_conn_increase_ratio: str = None,
        max_conn_increase_ratio_value: str = None,
        max_iops_adjust_deadline: str = None,
        max_iops_increase_ratio: str = None,
        max_iops_increase_ratio_value: str = None,
        mem_adjustable_max_ratio: str = None,
        mem_adjustable_max_value: str = None,
        memory_adjust_deadline: str = None,
        memory_increase_ratio: str = None,
        memory_increase_ratio_value: str = None,
        origin_cpu: str = None,
        origin_max_conn: str = None,
        origin_max_iops: str = None,
        origin_memory: str = None,
    ):
        # The deadline for the CPU adjustment.
        self.cpu_adjust_deadline = cpu_adjust_deadline
        # The maximum percentage of the system CPU resources that the instance can use.
        self.cpu_adjustable_max_ratio = cpu_adjustable_max_ratio
        # The maximum CPU utilization.
        self.cpu_adjustable_max_value = cpu_adjustable_max_value
        # The CPU utilization.
        self.cpu_increase_ratio = cpu_increase_ratio
        # The CPU utilization. Unit: percentage.
        self.cpu_increase_ratio_value = cpu_increase_ratio_value
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The maximum IOPS.
        self.iops_adjustable_max_value = iops_adjustable_max_value
        # The deadline for the adjustment of the maximum number of connections.
        self.max_conn_adjust_deadline = max_conn_adjust_deadline
        # The maximum number of concurrent connections.
        self.max_conn_adjustable_max_value = max_conn_adjustable_max_value
        # The maximum number of concurrent connections.
        self.max_conn_increase_ratio = max_conn_increase_ratio
        # The maximum number of concurrent connections.
        self.max_conn_increase_ratio_value = max_conn_increase_ratio_value
        # The deadline for the adjustment of the maximum IOPS.
        self.max_iops_adjust_deadline = max_iops_adjust_deadline
        # The maximum IOPS.
        self.max_iops_increase_ratio = max_iops_increase_ratio
        # The maximum IOPS that can be supported by the instance.
        self.max_iops_increase_ratio_value = max_iops_increase_ratio_value
        # The maximum percentage of the system memory that the instance can use.
        self.mem_adjustable_max_ratio = mem_adjustable_max_ratio
        # The maximum value of the resources to be evaluated.
        self.mem_adjustable_max_value = mem_adjustable_max_value
        # The deadline for the memory adjustment.
        self.memory_adjust_deadline = memory_adjust_deadline
        # The memory increase percentage.
        self.memory_increase_ratio = memory_increase_ratio
        # The memory usage. Unit: MB.
        self.memory_increase_ratio_value = memory_increase_ratio_value
        # The number of CPUs of the instance.
        self.origin_cpu = origin_cpu
        # The maximum number of concurrent connections.
        self.origin_max_conn = origin_max_conn
        # The maximum IOPS.
        self.origin_max_iops = origin_max_iops
        # The actual memory used. Unit: MB.
        self.origin_memory = origin_memory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_adjust_deadline is not None:
            result['CpuAdjustDeadline'] = self.cpu_adjust_deadline

        if self.cpu_adjustable_max_ratio is not None:
            result['CpuAdjustableMaxRatio'] = self.cpu_adjustable_max_ratio

        if self.cpu_adjustable_max_value is not None:
            result['CpuAdjustableMaxValue'] = self.cpu_adjustable_max_value

        if self.cpu_increase_ratio is not None:
            result['CpuIncreaseRatio'] = self.cpu_increase_ratio

        if self.cpu_increase_ratio_value is not None:
            result['CpuIncreaseRatioValue'] = self.cpu_increase_ratio_value

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.iops_adjustable_max_value is not None:
            result['IopsAdjustableMaxValue'] = self.iops_adjustable_max_value

        if self.max_conn_adjust_deadline is not None:
            result['MaxConnAdjustDeadline'] = self.max_conn_adjust_deadline

        if self.max_conn_adjustable_max_value is not None:
            result['MaxConnAdjustableMaxValue'] = self.max_conn_adjustable_max_value

        if self.max_conn_increase_ratio is not None:
            result['MaxConnIncreaseRatio'] = self.max_conn_increase_ratio

        if self.max_conn_increase_ratio_value is not None:
            result['MaxConnIncreaseRatioValue'] = self.max_conn_increase_ratio_value

        if self.max_iops_adjust_deadline is not None:
            result['MaxIopsAdjustDeadline'] = self.max_iops_adjust_deadline

        if self.max_iops_increase_ratio is not None:
            result['MaxIopsIncreaseRatio'] = self.max_iops_increase_ratio

        if self.max_iops_increase_ratio_value is not None:
            result['MaxIopsIncreaseRatioValue'] = self.max_iops_increase_ratio_value

        if self.mem_adjustable_max_ratio is not None:
            result['MemAdjustableMaxRatio'] = self.mem_adjustable_max_ratio

        if self.mem_adjustable_max_value is not None:
            result['MemAdjustableMaxValue'] = self.mem_adjustable_max_value

        if self.memory_adjust_deadline is not None:
            result['MemoryAdjustDeadline'] = self.memory_adjust_deadline

        if self.memory_increase_ratio is not None:
            result['MemoryIncreaseRatio'] = self.memory_increase_ratio

        if self.memory_increase_ratio_value is not None:
            result['MemoryIncreaseRatioValue'] = self.memory_increase_ratio_value

        if self.origin_cpu is not None:
            result['OriginCpu'] = self.origin_cpu

        if self.origin_max_conn is not None:
            result['OriginMaxConn'] = self.origin_max_conn

        if self.origin_max_iops is not None:
            result['OriginMaxIops'] = self.origin_max_iops

        if self.origin_memory is not None:
            result['OriginMemory'] = self.origin_memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuAdjustDeadline') is not None:
            self.cpu_adjust_deadline = m.get('CpuAdjustDeadline')

        if m.get('CpuAdjustableMaxRatio') is not None:
            self.cpu_adjustable_max_ratio = m.get('CpuAdjustableMaxRatio')

        if m.get('CpuAdjustableMaxValue') is not None:
            self.cpu_adjustable_max_value = m.get('CpuAdjustableMaxValue')

        if m.get('CpuIncreaseRatio') is not None:
            self.cpu_increase_ratio = m.get('CpuIncreaseRatio')

        if m.get('CpuIncreaseRatioValue') is not None:
            self.cpu_increase_ratio_value = m.get('CpuIncreaseRatioValue')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('IopsAdjustableMaxValue') is not None:
            self.iops_adjustable_max_value = m.get('IopsAdjustableMaxValue')

        if m.get('MaxConnAdjustDeadline') is not None:
            self.max_conn_adjust_deadline = m.get('MaxConnAdjustDeadline')

        if m.get('MaxConnAdjustableMaxValue') is not None:
            self.max_conn_adjustable_max_value = m.get('MaxConnAdjustableMaxValue')

        if m.get('MaxConnIncreaseRatio') is not None:
            self.max_conn_increase_ratio = m.get('MaxConnIncreaseRatio')

        if m.get('MaxConnIncreaseRatioValue') is not None:
            self.max_conn_increase_ratio_value = m.get('MaxConnIncreaseRatioValue')

        if m.get('MaxIopsAdjustDeadline') is not None:
            self.max_iops_adjust_deadline = m.get('MaxIopsAdjustDeadline')

        if m.get('MaxIopsIncreaseRatio') is not None:
            self.max_iops_increase_ratio = m.get('MaxIopsIncreaseRatio')

        if m.get('MaxIopsIncreaseRatioValue') is not None:
            self.max_iops_increase_ratio_value = m.get('MaxIopsIncreaseRatioValue')

        if m.get('MemAdjustableMaxRatio') is not None:
            self.mem_adjustable_max_ratio = m.get('MemAdjustableMaxRatio')

        if m.get('MemAdjustableMaxValue') is not None:
            self.mem_adjustable_max_value = m.get('MemAdjustableMaxValue')

        if m.get('MemoryAdjustDeadline') is not None:
            self.memory_adjust_deadline = m.get('MemoryAdjustDeadline')

        if m.get('MemoryIncreaseRatio') is not None:
            self.memory_increase_ratio = m.get('MemoryIncreaseRatio')

        if m.get('MemoryIncreaseRatioValue') is not None:
            self.memory_increase_ratio_value = m.get('MemoryIncreaseRatioValue')

        if m.get('OriginCpu') is not None:
            self.origin_cpu = m.get('OriginCpu')

        if m.get('OriginMaxConn') is not None:
            self.origin_max_conn = m.get('OriginMaxConn')

        if m.get('OriginMaxIops') is not None:
            self.origin_max_iops = m.get('OriginMaxIops')

        if m.get('OriginMemory') is not None:
            self.origin_memory = m.get('OriginMemory')

        return self

