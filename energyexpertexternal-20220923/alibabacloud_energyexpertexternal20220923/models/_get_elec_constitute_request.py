# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetElecConstituteRequest(DaraModel):
    def __init__(
        self,
        code: str = None,
        year: int = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # Year.
        # 
        # This parameter is required.
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.year is not None:
            result['year'] = self.year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('year') is not None:
            self.year = m.get('year')

        return self

