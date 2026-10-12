# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HttpApiBackendMatchCondition(DaraModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        type: str = None,
        value: str = None,
    ):
        # The match key.
        self.key = key
        # The operator. Three matching methods are supported: exact match, prefix match, and regular expression.
        self.operator = operator
        # The match type. Supports matching by query parameter or header parameter.
        self.type = type
        # The match value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.operator is not None:
            result['operator'] = self.operator

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

