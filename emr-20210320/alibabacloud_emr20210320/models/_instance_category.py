# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class InstanceCategory(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        keys: List[str] = None,
        values: List[str] = None,
    ):
        # 默认值。
        self.default_value = default_value
        self.keys = keys
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.keys is not None:
            result['Keys'] = self.keys

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Keys') is not None:
            self.keys = m.get('Keys')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

