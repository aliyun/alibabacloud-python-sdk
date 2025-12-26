# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListNodeInstanceTypeResponseBody(DaraModel):
    def __init__(
        self,
        node_instance_type_models: List[main_models.ListNodeInstanceTypeResponseBodyNodeInstanceTypeModels] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The resource types.
        self.node_instance_type_models = node_instance_type_models
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries on each page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.node_instance_type_models:
            for v1 in self.node_instance_type_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NodeInstanceTypeModels'] = []
        if self.node_instance_type_models is not None:
            for k1 in self.node_instance_type_models:
                result['NodeInstanceTypeModels'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_instance_type_models = []
        if m.get('NodeInstanceTypeModels') is not None:
            for k1 in m.get('NodeInstanceTypeModels'):
                temp_model = main_models.ListNodeInstanceTypeResponseBodyNodeInstanceTypeModels()
                self.node_instance_type_models.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListNodeInstanceTypeResponseBodyNodeInstanceTypeModels(DaraModel):
    def __init__(
        self,
        cpu: str = None,
        gpu: str = None,
        gpu_memory: int = None,
        max_capacity: int = None,
        memory: int = None,
        node_instance_type: str = None,
        node_instance_type_family: str = None,
        node_type_name: str = None,
    ):
        # The number of vCPUs.
        self.cpu = cpu
        # The number of GPUs.
        self.gpu = gpu
        # The GPU size. Unit: MB.
        self.gpu_memory = gpu_memory
        # The maximum number of sessions to which a resource can connect at the same time. If a resource connects to a large number of sessions at the same time, user experience can be compromised. The value range varies based on the resource type. The following items describe the value ranges of different resource types:
        # 
        # *   appstreaming.general.4c8g: 1 to 2
        # *   appstreaming.general.8c16g: 1 to 4
        # *   appstreaming.vgpu.8c16g.4g: 1 to 4
        # *   appstreaming.vgpu.8c31g.16g: 1 to 4
        # *   appstreaming.vgpu.14c93g.12g: 1 to 6
        self.max_capacity = max_capacity
        # The memory size. Unit: MB.
        self.memory = memory
        # The ID of the resource type.
        self.node_instance_type = node_instance_type
        # The resource type family.
        # 
        # Valid values:
        # 
        # *   appstreaming.general: WUYING - General
        # *   appstreaming.vgpu: WUYING - Graphics
        self.node_instance_type_family = node_instance_type_family
        # The name of the resource type.
        self.node_type_name = node_type_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.gpu is not None:
            result['Gpu'] = self.gpu

        if self.gpu_memory is not None:
            result['GpuMemory'] = self.gpu_memory

        if self.max_capacity is not None:
            result['MaxCapacity'] = self.max_capacity

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type

        if self.node_instance_type_family is not None:
            result['NodeInstanceTypeFamily'] = self.node_instance_type_family

        if self.node_type_name is not None:
            result['NodeTypeName'] = self.node_type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')

        if m.get('GpuMemory') is not None:
            self.gpu_memory = m.get('GpuMemory')

        if m.get('MaxCapacity') is not None:
            self.max_capacity = m.get('MaxCapacity')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')

        if m.get('NodeInstanceTypeFamily') is not None:
            self.node_instance_type_family = m.get('NodeInstanceTypeFamily')

        if m.get('NodeTypeName') is not None:
            self.node_type_name = m.get('NodeTypeName')

        return self

