# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class RoutingConfiguration(DaraModel):
    def __init__(
        self,
        version_weights: List[main_models.VersionWeight] = None,
    ):
        # 不同版本的流量权重配置
        self.version_weights = version_weights

    def validate(self):
        if self.version_weights:
            for v1 in self.version_weights:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['versionWeights'] = []
        if self.version_weights is not None:
            for k1 in self.version_weights:
                result['versionWeights'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.version_weights = []
        if m.get('versionWeights') is not None:
            for k1 in m.get('versionWeights'):
                temp_model = main_models.VersionWeight()
                self.version_weights.append(temp_model.from_map(k1))

        return self

