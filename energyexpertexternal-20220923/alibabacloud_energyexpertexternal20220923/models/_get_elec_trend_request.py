# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetElecTrendRequest(DaraModel):
    def __init__(
        self,
        code: str = None,
        year_list: List[int] = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # List of years.
        # 
        # This parameter is required.
        self.year_list = year_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.year_list is not None:
            result['yearList'] = self.year_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('yearList') is not None:
            self.year_list = m.get('yearList')

        return self

