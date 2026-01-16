# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Key(DaraModel):
    def __init__(
        self,
        prefix: str = None,
        suffix: str = None,
    ):
        self.prefix = prefix
        self.suffix = suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prefix is not None:
            result['prefix'] = self.prefix

        if self.suffix is not None:
            result['suffix'] = self.suffix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')

        if m.get('suffix') is not None:
            self.suffix = m.get('suffix')

        return self

