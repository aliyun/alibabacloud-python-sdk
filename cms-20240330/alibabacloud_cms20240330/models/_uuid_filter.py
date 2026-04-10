# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UuidFilter(DaraModel):
    def __init__(
        self,
        eq: str = None,
        in_: List[str] = None,
    ):
        self.eq = eq
        self.in_ = in_

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eq is not None:
            result['eq'] = self.eq

        if self.in_ is not None:
            result['in'] = self.in_

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eq') is not None:
            self.eq = m.get('eq')

        if m.get('in') is not None:
            self.in_ = m.get('in')

        return self

