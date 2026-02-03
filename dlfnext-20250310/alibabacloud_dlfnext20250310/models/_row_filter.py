# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RowFilter(DaraModel):
    def __init__(
        self,
        expression: str = None,
        predicate: str = None,
    ):
        self.expression = expression
        self.predicate = predicate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression is not None:
            result['expression'] = self.expression

        if self.predicate is not None:
            result['predicate'] = self.predicate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expression') is not None:
            self.expression = m.get('expression')

        if m.get('predicate') is not None:
            self.predicate = m.get('predicate')

        return self

