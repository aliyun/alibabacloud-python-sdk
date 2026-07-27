# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PrometheusNamedQueryEntry(DaraModel):
    def __init__(
        self,
        expr: str = None,
        name: str = None,
    ):
        self.expr = expr
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expr is not None:
            result['expr'] = self.expr

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expr') is not None:
            self.expr = m.get('expr')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

