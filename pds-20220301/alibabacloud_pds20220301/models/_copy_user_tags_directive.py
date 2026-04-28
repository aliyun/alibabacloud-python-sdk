# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CopyUserTagsDirective(DaraModel):
    def __init__(
        self,
        directive: str = None,
        keys: List[str] = None,
    ):
        self.directive = directive
        self.keys = keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directive is not None:
            result['directive'] = self.directive

        if self.keys is not None:
            result['keys'] = self.keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('directive') is not None:
            self.directive = m.get('directive')

        if m.get('keys') is not None:
            self.keys = m.get('keys')

        return self

