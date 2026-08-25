# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListServerIdeEcsSpecsResponseBody(DaraModel):
    def __init__(
        self,
        ecs_specs: List[main_models.ListServerIdeEcsSpecsResponseBodyEcsSpecs] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The list of available ECS instance types for personal development environments.
        self.ecs_specs = ecs_specs
        # The maximum number of records returned in this response.
        self.max_results = max_results
        # The pagination token for the next page. An empty value indicates that no more results are available.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.ecs_specs:
            for v1 in self.ecs_specs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EcsSpecs'] = []
        if self.ecs_specs is not None:
            for k1 in self.ecs_specs:
                result['EcsSpecs'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ecs_specs = []
        if m.get('EcsSpecs') is not None:
            for k1 in m.get('EcsSpecs'):
                temp_model = main_models.ListServerIdeEcsSpecsResponseBodyEcsSpecs()
                self.ecs_specs.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListServerIdeEcsSpecsResponseBodyEcsSpecs(DaraModel):
    def __init__(
        self,
        accelerator_type: str = None,
        cpu: int = None,
        cu: float = None,
        gpu: int = None,
        gpu_memory_size: float = None,
        gpu_type: str = None,
        instance_type: str = None,
        is_available: bool = None,
        memory: float = None,
    ):
        # The accelerator type. Valid values:
        # - CPU: uses only CPU.
        # - GPU: uses GPU acceleration.
        self.accelerator_type = accelerator_type
        # The number of CPU cores.
        self.cpu = cpu
        # The number of compute units (CUs) consumed by this instance type.
        self.cu = cu
        # The number of GPU cards.
        self.gpu = gpu
        # The GPU memory size.
        self.gpu_memory_size = gpu_memory_size
        # The GPU model.
        self.gpu_type = gpu_type
        # The ECS instance type.
        self.instance_type = instance_type
        # Indicates whether the instance type is available.
        self.is_available = is_available
        # The memory size, in GB.
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.cu is not None:
            result['Cu'] = self.cu

        if self.gpu is not None:
            result['Gpu'] = self.gpu

        if self.gpu_memory_size is not None:
            result['GpuMemorySize'] = self.gpu_memory_size

        if self.gpu_type is not None:
            result['GpuType'] = self.gpu_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.is_available is not None:
            result['IsAvailable'] = self.is_available

        if self.memory is not None:
            result['Memory'] = self.memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')

        if m.get('GpuMemorySize') is not None:
            self.gpu_memory_size = m.get('GpuMemorySize')

        if m.get('GpuType') is not None:
            self.gpu_type = m.get('GpuType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IsAvailable') is not None:
            self.is_available = m.get('IsAvailable')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        return self

