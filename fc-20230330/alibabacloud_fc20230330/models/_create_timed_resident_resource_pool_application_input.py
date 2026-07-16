# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class CreateTimedResidentResourcePoolApplicationInput(DaraModel):
    def __init__(
        self,
        associated_pool_id: str = None,
        disk_size_in_gb: int = None,
        gpu_type: str = None,
        memory_size_in_gb: int = None,
        operation_type: str = None,
        pool_name: str = None,
        reason: str = None,
        timed_config: main_models.TimedPoolConfig = None,
        timed_pool_id: str = None,
        total_gpucards: int = None,
        v_cpu_cores: int = None,
    ):
        self.associated_pool_id = associated_pool_id
        self.disk_size_in_gb = disk_size_in_gb
        self.gpu_type = gpu_type
        self.memory_size_in_gb = memory_size_in_gb
        self.operation_type = operation_type
        self.pool_name = pool_name
        self.reason = reason
        self.timed_config = timed_config
        self.timed_pool_id = timed_pool_id
        self.total_gpucards = total_gpucards
        self.v_cpu_cores = v_cpu_cores

    def validate(self):
        if self.timed_config:
            self.timed_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_pool_id is not None:
            result['associatedPoolId'] = self.associated_pool_id

        if self.disk_size_in_gb is not None:
            result['diskSizeInGB'] = self.disk_size_in_gb

        if self.gpu_type is not None:
            result['gpuType'] = self.gpu_type

        if self.memory_size_in_gb is not None:
            result['memorySizeInGB'] = self.memory_size_in_gb

        if self.operation_type is not None:
            result['operationType'] = self.operation_type

        if self.pool_name is not None:
            result['poolName'] = self.pool_name

        if self.reason is not None:
            result['reason'] = self.reason

        if self.timed_config is not None:
            result['timedConfig'] = self.timed_config.to_map()

        if self.timed_pool_id is not None:
            result['timedPoolId'] = self.timed_pool_id

        if self.total_gpucards is not None:
            result['totalGPUCards'] = self.total_gpucards

        if self.v_cpu_cores is not None:
            result['vCpuCores'] = self.v_cpu_cores

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('associatedPoolId') is not None:
            self.associated_pool_id = m.get('associatedPoolId')

        if m.get('diskSizeInGB') is not None:
            self.disk_size_in_gb = m.get('diskSizeInGB')

        if m.get('gpuType') is not None:
            self.gpu_type = m.get('gpuType')

        if m.get('memorySizeInGB') is not None:
            self.memory_size_in_gb = m.get('memorySizeInGB')

        if m.get('operationType') is not None:
            self.operation_type = m.get('operationType')

        if m.get('poolName') is not None:
            self.pool_name = m.get('poolName')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('timedConfig') is not None:
            temp_model = main_models.TimedPoolConfig()
            self.timed_config = temp_model.from_map(m.get('timedConfig'))

        if m.get('timedPoolId') is not None:
            self.timed_pool_id = m.get('timedPoolId')

        if m.get('totalGPUCards') is not None:
            self.total_gpucards = m.get('totalGPUCards')

        if m.get('vCpuCores') is not None:
            self.v_cpu_cores = m.get('vCpuCores')

        return self

