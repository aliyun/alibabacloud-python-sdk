# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class SLSCollectConfigs(DaraModel):
    def __init__(
        self,
        collect_configs: List[main_models.SLSCollectConfig] = None,
    ):
        self.collect_configs = collect_configs

    def validate(self):
        if self.collect_configs:
            for v1 in self.collect_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CollectConfigs'] = []
        if self.collect_configs is not None:
            for k1 in self.collect_configs:
                result['CollectConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.collect_configs = []
        if m.get('CollectConfigs') is not None:
            for k1 in m.get('CollectConfigs'):
                temp_model = main_models.SLSCollectConfig()
                self.collect_configs.append(temp_model.from_map(k1))

        return self

