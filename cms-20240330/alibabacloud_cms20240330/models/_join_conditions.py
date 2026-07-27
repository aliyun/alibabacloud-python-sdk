# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class JoinConditions(DaraModel):
    def __init__(
        self,
        lhs_field: str = None,
        operator: str = None,
        rhs_field: str = None,
    ):
        self.lhs_field = lhs_field
        self.operator = operator
        self.rhs_field = rhs_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lhs_field is not None:
            result['lhsField'] = self.lhs_field

        if self.operator is not None:
            result['operator'] = self.operator

        if self.rhs_field is not None:
            result['rhsField'] = self.rhs_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lhsField') is not None:
            self.lhs_field = m.get('lhsField')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('rhsField') is not None:
            self.rhs_field = m.get('rhsField')

        return self

