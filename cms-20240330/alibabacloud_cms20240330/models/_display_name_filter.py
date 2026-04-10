# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisplayNameFilter(DaraModel):
    def __init__(
        self,
        contains: str = None,
        not_contains: str = None,
    ):
        self.contains = contains
        self.not_contains = not_contains

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contains is not None:
            result['contains'] = self.contains

        if self.not_contains is not None:
            result['notContains'] = self.not_contains

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contains') is not None:
            self.contains = m.get('contains')

        if m.get('notContains') is not None:
            self.not_contains = m.get('notContains')

        return self

