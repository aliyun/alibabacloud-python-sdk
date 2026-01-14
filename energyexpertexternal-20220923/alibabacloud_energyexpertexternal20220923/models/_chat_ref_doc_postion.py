# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChatRefDocPostion(DaraModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x is not None:
            result['x'] = self.x

        if self.y is not None:
            result['y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('x') is not None:
            self.x = m.get('x')

        if m.get('y') is not None:
            self.y = m.get('y')

        return self

