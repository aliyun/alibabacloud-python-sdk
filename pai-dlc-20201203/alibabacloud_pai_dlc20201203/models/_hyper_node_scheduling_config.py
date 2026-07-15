# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HyperNodeSchedulingConfig(DaraModel):
    def __init__(
        self,
        min_available: int = None,
        quality_policy: str = None,
    ):
        self.min_available = min_available
        self.quality_policy = quality_policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.min_available is not None:
            result['MinAvailable'] = self.min_available

        if self.quality_policy is not None:
            result['QualityPolicy'] = self.quality_policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MinAvailable') is not None:
            self.min_available = m.get('MinAvailable')

        if m.get('QualityPolicy') is not None:
            self.quality_policy = m.get('QualityPolicy')

        return self

