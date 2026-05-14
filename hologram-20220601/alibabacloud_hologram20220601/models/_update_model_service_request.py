# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateModelServiceRequest(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        gpu: int = None,
        memory: int = None,
        model_service_name: str = None,
        model_type: str = None,
        service_count: int = None,
    ):
        self.cpu = cpu
        self.gpu = gpu
        self.memory = memory
        # This parameter is required.
        self.model_service_name = model_service_name
        self.model_type = model_type
        self.service_count = service_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.gpu is not None:
            result['gpu'] = self.gpu

        if self.memory is not None:
            result['memory'] = self.memory

        if self.model_service_name is not None:
            result['modelServiceName'] = self.model_service_name

        if self.model_type is not None:
            result['modelType'] = self.model_type

        if self.service_count is not None:
            result['serviceCount'] = self.service_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('gpu') is not None:
            self.gpu = m.get('gpu')

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('modelServiceName') is not None:
            self.model_service_name = m.get('modelServiceName')

        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        if m.get('serviceCount') is not None:
            self.service_count = m.get('serviceCount')

        return self

