# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ProductSpecValue(DaraModel):
    def __init__(
        self,
        value: str = None,
        value_alias: str = None,
        value_id: int = None,
    ):
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
        if self.value is not None:
            result['value'] = self.value

        if self.value_alias is not None:
            result['valueAlias'] = self.value_alias

        if self.value_id is not None:
            result['valueId'] = self.value_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('value') is not None:
            self.value = m.get('value')

        if m.get('valueAlias') is not None:
            self.value_alias = m.get('valueAlias')

        if m.get('valueId') is not None:
            self.value_id = m.get('valueId')

        return self

