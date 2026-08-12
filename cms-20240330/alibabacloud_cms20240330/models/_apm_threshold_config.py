# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApmThresholdConfig(DaraModel):
    def __init__(
        self,
        max: float = None,
        min: float = None,
        severity: str = None,
        threshold: float = None,
    ):
        # The upper bound of the range.
        self.max = max
        # The lower bound of the range.
        self.min = min
        # The alert level.
        # 
        # This parameter is required.
        self.severity = severity
        # The threshold. This parameter is required for APM_SIMPLE_CONDITION.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max is not None:
            result['max'] = self.max

        if self.min is not None:
            result['min'] = self.min

        if self.severity is not None:
            result['severity'] = self.severity

        if self.threshold is not None:
            result['threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('max') is not None:
            self.max = m.get('max')

        if m.get('min') is not None:
            self.min = m.get('min')

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        return self

