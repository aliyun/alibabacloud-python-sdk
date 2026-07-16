# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TagCondition(DaraModel):
    def __init__(
        self,
        key: str = None,
        op: str = None,
        value: str = None,
    ):
        self.key = key
        self.op = op
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

        if self.op is not None:
            result['op'] = self.op

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('op') is not None:
            self.op = m.get('op')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

