# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrayTrafficWeight(DaraModel):
    def __init__(
        self,
        version: str = None,
        weight: float = None,
    ):
        # 灰度版本号
        self.version = version
        # 流量权重比例（0.0-1.0）
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.version is not None:
            result['version'] = self.version

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

