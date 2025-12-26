# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GPUMetric(DaraModel):
    def __init__(
        self,
        index: int = None,
        model: str = None,
        status: int = None,
        usage_rate: float = None,
    ):
        self.index = index
        self.model = model
        self.status = status
        self.usage_rate = usage_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['Index'] = self.index

        if self.model is not None:
            result['Model'] = self.model

        if self.status is not None:
            result['Status'] = self.status

        if self.usage_rate is not None:
            result['UsageRate'] = self.usage_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UsageRate') is not None:
            self.usage_rate = m.get('UsageRate')

        return self

