# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UmodelEntityFilter(DaraModel):
    def __init__(
        self,
        field: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The field name to filter on.
        self.field = field
        # The comparison operator to use. Supported operators include `=`, `>`, `<`, `!=`, `IN`, and `NOT IN`.
        self.operator = operator
        # The value to compare the field against.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field is not None:
            result['field'] = self.field

        if self.operator is not None:
            result['operator'] = self.operator

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('field') is not None:
            self.field = m.get('field')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

