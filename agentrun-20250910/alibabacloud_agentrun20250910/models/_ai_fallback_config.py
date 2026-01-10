# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class AiFallbackConfig(DaraModel):
    def __init__(
        self,
        service_configs: List[main_models.AiFallbackServiceConfig] = None,
    ):
        self.service_configs = service_configs

    def validate(self):
        if self.service_configs:
            for v1 in self.service_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['serviceConfigs'] = []
        if self.service_configs is not None:
            for k1 in self.service_configs:
                result['serviceConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.service_configs = []
        if m.get('serviceConfigs') is not None:
            for k1 in m.get('serviceConfigs'):
                temp_model = main_models.AiFallbackServiceConfig()
                self.service_configs.append(temp_model.from_map(k1))

        return self

