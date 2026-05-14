# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateModelServiceRequest(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        cpu: int = None,
        gpu: int = None,
        gpu_memory: int = None,
        memory: int = None,
        model_params: str = None,
        model_service_name: str = None,
        model_type: str = None,
        provider: str = None,
        service_count: int = None,
        task_type: str = None,
    ):
        self.api_key = api_key
        self.cpu = cpu
        self.gpu = gpu
        self.gpu_memory = gpu_memory
        self.memory = memory
        self.model_params = model_params
        # This parameter is required.
        self.model_service_name = model_service_name
        # This parameter is required.
        self.model_type = model_type
        self.provider = provider
        self.service_count = service_count
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.gpu is not None:
            result['gpu'] = self.gpu

        if self.gpu_memory is not None:
            result['gpuMemory'] = self.gpu_memory

        if self.memory is not None:
            result['memory'] = self.memory

        if self.model_params is not None:
            result['modelParams'] = self.model_params

        if self.model_service_name is not None:
            result['modelServiceName'] = self.model_service_name

        if self.model_type is not None:
            result['modelType'] = self.model_type

        if self.provider is not None:
            result['provider'] = self.provider

        if self.service_count is not None:
            result['serviceCount'] = self.service_count

        if self.task_type is not None:
            result['taskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('gpu') is not None:
            self.gpu = m.get('gpu')

        if m.get('gpuMemory') is not None:
            self.gpu_memory = m.get('gpuMemory')

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('modelParams') is not None:
            self.model_params = m.get('modelParams')

        if m.get('modelServiceName') is not None:
            self.model_service_name = m.get('modelServiceName')

        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('serviceCount') is not None:
            self.service_count = m.get('serviceCount')

        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')

        return self

