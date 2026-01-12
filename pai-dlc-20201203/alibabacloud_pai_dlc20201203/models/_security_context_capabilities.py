# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SecurityContextCapabilities(DaraModel):
    def __init__(
        self,
        add: List[str] = None,
        drop: List[str] = None,
    ):
        self.add = add
        self.drop = drop

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add is not None:
            result['Add'] = self.add

        if self.drop is not None:
            result['Drop'] = self.drop

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Add') is not None:
            self.add = m.get('Add')

        if m.get('Drop') is not None:
            self.drop = m.get('Drop')

        return self

