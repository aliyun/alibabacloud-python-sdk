# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class QuotaDetail(DaraModel):
    def __init__(
        self,
        cpu: str = None,
        gpu: str = None,
        gpudetails: List[main_models.GPUDetail] = None,
        gputype: str = None,
        gputype_full_name: str = None,
        memory: str = None,
    ):
        self.cpu = cpu
        self.gpu = gpu
        self.gpudetails = gpudetails
        self.gputype = gputype
        self.gputype_full_name = gputype_full_name
        self.memory = memory

    def validate(self):
        if self.gpudetails:
            for v1 in self.gpudetails:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['CPU'] = self.cpu

        if self.gpu is not None:
            result['GPU'] = self.gpu

        result['GPUDetails'] = []
        if self.gpudetails is not None:
            for k1 in self.gpudetails:
                result['GPUDetails'].append(k1.to_map() if k1 else None)

        if self.gputype is not None:
            result['GPUType'] = self.gputype

        if self.gputype_full_name is not None:
            result['GPUTypeFullName'] = self.gputype_full_name

        if self.memory is not None:
            result['Memory'] = self.memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')

        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')

        self.gpudetails = []
        if m.get('GPUDetails') is not None:
            for k1 in m.get('GPUDetails'):
                temp_model = main_models.GPUDetail()
                self.gpudetails.append(temp_model.from_map(k1))

        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')

        if m.get('GPUTypeFullName') is not None:
            self.gputype_full_name = m.get('GPUTypeFullName')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        return self

