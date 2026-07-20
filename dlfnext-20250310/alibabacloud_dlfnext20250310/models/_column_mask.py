# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ColumnMask(DaraModel):
    def __init__(
        self,
        expression: str = None,
        transform: str = None,
    ):
        self.expression = expression
        self.transform = transform

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression is not None:
            result['expression'] = self.expression

        if self.transform is not None:
            result['transform'] = self.transform

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expression') is not None:
            self.expression = m.get('expression')

        if m.get('transform') is not None:
            self.transform = m.get('transform')

        return self

