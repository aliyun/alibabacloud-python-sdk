# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PAL7ConfigRewriteOp(DaraModel):
    def __init__(
        self,
        key: str = None,
        old_value: str = None,
        op: str = None,
        value: str = None,
        value_variable: str = None,
    ):
        self.key = key
        self.old_value = old_value
        self.op = op
        self.value = value
        self.value_variable = value_variable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.old_value is not None:
            result['OldValue'] = self.old_value

        if self.op is not None:
            result['Op'] = self.op

        if self.value is not None:
            result['Value'] = self.value

        if self.value_variable is not None:
            result['ValueVariable'] = self.value_variable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('OldValue') is not None:
            self.old_value = m.get('OldValue')

        if m.get('Op') is not None:
            self.op = m.get('Op')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('ValueVariable') is not None:
            self.value_variable = m.get('ValueVariable')

        return self

