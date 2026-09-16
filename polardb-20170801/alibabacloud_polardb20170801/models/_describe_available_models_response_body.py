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
        model_type: str = None,
        request_id: str = None,
        tune_arch: str = None,
    ):
        # The database engine.
        self.engine = engine
        # The database engine version.
        self.engine_version = engine_version
        # The list of models.
        self.items = items
        # The model type corresponding to the request.
        self.model_type = model_type
        # Id of the request
        self.request_id = request_id
        # The model fine-tuning architecture.
        self.tune_arch = tune_arch

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

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tune_arch is not None:
            result['TuneArch'] = self.tune_arch

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

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TuneArch') is not None:
            self.tune_arch = m.get('TuneArch')

        return self

class DescribeAvailableModelsResponseBodyItems(DaraModel):
    def __init__(
        self,
        custom_model_name: str = None,
        display_model_name: str = None,
        gmt_modified: str = None,
        gpu_required: List[main_models.DescribeAvailableModelsResponseBodyItemsGpuRequired] = None,
        minimum_cpu: int = None,
        minimum_memory: int = None,
        model_name: str = None,
        model_series: str = None,
        model_type: str = None,
        oss_path: str = None,
        supported_gpu_models: List[str] = None,
        tune_arch: str = None,
    ):
        # The custom model registration key.
        self.custom_model_name = custom_model_name
        # The display name of the model.
        self.display_model_name = display_model_name
        # The last modified time of the registration.
        self.gmt_modified = gmt_modified
        # The supported GPU types.
        self.gpu_required = gpu_required
        # The minimum number of CPUs.
        self.minimum_cpu = minimum_cpu
        # The minimum memory size.
        self.minimum_memory = minimum_memory
        # The model name.
        self.model_name = model_name
        # The model series.
        self.model_series = model_series
        # The model type.
        self.model_type = model_type
        # The OSS path of the custom model.
        self.oss_path = oss_path
        # The supported GPU models.
        self.supported_gpu_models = supported_gpu_models
        self.tune_arch = tune_arch

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
        if self.custom_model_name is not None:
            result['CustomModelName'] = self.custom_model_name

        if self.display_model_name is not None:
            result['DisplayModelName'] = self.display_model_name

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

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

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.oss_path is not None:
            result['OssPath'] = self.oss_path

        if self.supported_gpu_models is not None:
            result['SupportedGpuModels'] = self.supported_gpu_models

        if self.tune_arch is not None:
            result['TuneArch'] = self.tune_arch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomModelName') is not None:
            self.custom_model_name = m.get('CustomModelName')

        if m.get('DisplayModelName') is not None:
            self.display_model_name = m.get('DisplayModelName')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

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

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')

        if m.get('SupportedGpuModels') is not None:
            self.supported_gpu_models = m.get('SupportedGpuModels')

        if m.get('TuneArch') is not None:
            self.tune_arch = m.get('TuneArch')

        return self

class DescribeAvailableModelsResponseBodyItemsGpuRequired(DaraModel):
    def __init__(
        self,
        gpu_min_count: str = None,
        gpu_model: str = None,
    ):
        # The minimum number of GPUs.
        self.gpu_min_count = gpu_min_count
        # The GPU model.
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

