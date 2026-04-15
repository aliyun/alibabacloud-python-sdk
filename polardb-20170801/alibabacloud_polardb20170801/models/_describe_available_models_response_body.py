# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeAvailableModelsResponseBody(DaraModel):
    def __init__(
        self,
        engine: str = None,
        engine_version: str = None,
        items: List[main_models.DescribeAvailableModelsResponseBodyItems] = None,
        request_id: str = None,
    ):
        self.engine = engine
        self.engine_version = engine_version
        self.items = items
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeAvailableModelsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAvailableModelsResponseBodyItems(DaraModel):
    def __init__(
        self,
        gpu_required: List[main_models.DescribeAvailableModelsResponseBodyItemsGpuRequired] = None,
        minimum_cpu: int = None,
        minimum_memory: int = None,
        model_name: str = None,
        model_series: str = None,
        supported_gpu_models: List[str] = None,
    ):
        self.gpu_required = gpu_required
        self.minimum_cpu = minimum_cpu
        self.minimum_memory = minimum_memory
        self.model_name = model_name
        self.model_series = model_series
        self.supported_gpu_models = supported_gpu_models

    def validate(self):
        if self.gpu_required:
            for v1 in self.gpu_required:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GpuRequired'] = []
        if self.gpu_required is not None:
            for k1 in self.gpu_required:
                result['GpuRequired'].append(k1.to_map() if k1 else None)

        if self.minimum_cpu is not None:
            result['MinimumCpu'] = self.minimum_cpu

        if self.minimum_memory is not None:
            result['MinimumMemory'] = self.minimum_memory

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_series is not None:
            result['ModelSeries'] = self.model_series

        if self.supported_gpu_models is not None:
            result['SupportedGpuModels'] = self.supported_gpu_models

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gpu_required = []
        if m.get('GpuRequired') is not None:
            for k1 in m.get('GpuRequired'):
                temp_model = main_models.DescribeAvailableModelsResponseBodyItemsGpuRequired()
                self.gpu_required.append(temp_model.from_map(k1))

        if m.get('MinimumCpu') is not None:
            self.minimum_cpu = m.get('MinimumCpu')

        if m.get('MinimumMemory') is not None:
            self.minimum_memory = m.get('MinimumMemory')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelSeries') is not None:
            self.model_series = m.get('ModelSeries')

        if m.get('SupportedGpuModels') is not None:
            self.supported_gpu_models = m.get('SupportedGpuModels')

        return self

class DescribeAvailableModelsResponseBodyItemsGpuRequired(DaraModel):
    def __init__(
        self,
        gpu_min_count: str = None,
        gpu_model: str = None,
    ):
        self.gpu_min_count = gpu_min_count
        self.gpu_model = gpu_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gpu_min_count is not None:
            result['GpuMinCount'] = self.gpu_min_count

        if self.gpu_model is not None:
            result['GpuModel'] = self.gpu_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GpuMinCount') is not None:
            self.gpu_min_count = m.get('GpuMinCount')

        if m.get('GpuModel') is not None:
            self.gpu_model = m.get('GpuModel')

        return self

