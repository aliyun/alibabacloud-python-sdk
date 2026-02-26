# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PointInt64(DaraModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        # The distance from the X-coordinate of the vertex to the left edge. Unit: pixel.
        self.x = x
        # The distance from the Y-coordinate of the vertex to the top. Unit: pixel.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

