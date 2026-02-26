# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SkuSpec(DaraModel):
    def __init__(
        self,
        key: str = None,
        key_id: int = None,
        value: str = None,
        value_alias: str = None,
        value_id: int = None,
    ):
        self.key = key
        self.key_id = key_id
        self.value = value
        self.value_alias = value_alias
        self.value_id = value_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.key_id is not None:
            result['keyId'] = self.key_id

        if self.value is not None:
            result['value'] = self.value

        if self.value_alias is not None:
            result['valueAlias'] = self.value_alias

        if self.value_id is not None:
            result['valueId'] = self.value_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('keyId') is not None:
            self.key_id = m.get('keyId')

        if m.get('value') is not None:
            self.value = m.get('value')

        if m.get('valueAlias') is not None:
            self.value_alias = m.get('valueAlias')

        if m.get('valueId') is not None:
            self.value_id = m.get('valueId')

        return self

