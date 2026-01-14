# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEmissionSourceConstituteRequest(DaraModel):
    def __init__(
        self,
        code: str = None,
        module_code: str = None,
        module_type: int = None,
        year: int = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # Module code.
        self.module_code = module_code
        # Module type.
        # 
        # This parameter is required.
        self.module_type = module_type
        # Year of inventory.
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

        if self.module_code is not None:
            result['moduleCode'] = self.module_code

        if self.module_type is not None:
            result['moduleType'] = self.module_type

        if self.year is not None:
            result['year'] = self.year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('moduleCode') is not None:
            self.module_code = m.get('moduleCode')

        if m.get('moduleType') is not None:
            self.module_type = m.get('moduleType')

        if m.get('year') is not None:
            self.year = m.get('year')

        return self

