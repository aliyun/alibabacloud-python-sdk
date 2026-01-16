# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WildcardRule(DaraModel):
    def __init__(
        self,
        match: str = None,
        replacement: str = None,
    ):
        # This parameter is required.
        self.match = match
        # This parameter is required.
        self.replacement = replacement

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.match is not None:
            result['match'] = self.match

        if self.replacement is not None:
            result['replacement'] = self.replacement

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('match') is not None:
            self.match = m.get('match')

        if m.get('replacement') is not None:
            self.replacement = m.get('replacement')

        return self

