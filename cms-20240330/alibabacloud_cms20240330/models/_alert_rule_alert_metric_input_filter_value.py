# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AlertRuleAlertMetricInputFilterValue(DaraModel):
    def __init__(
        self,
        dim: str = None,
        opt: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.dim = dim
        # This parameter is required.
        self.opt = opt
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dim is not None:
            result['dim'] = self.dim

        if self.opt is not None:
            result['opt'] = self.opt

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dim') is not None:
            self.dim = m.get('dim')

        if m.get('opt') is not None:
            self.opt = m.get('opt')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

