# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StatusFilter(DaraModel):
    def __init__(
        self,
        eq: str = None,
    ):
        self.eq = eq

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eq is not None:
            result['eq'] = self.eq

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eq') is not None:
            self.eq = m.get('eq')

        return self

