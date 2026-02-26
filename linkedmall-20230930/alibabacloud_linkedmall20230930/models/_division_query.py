# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DivisionQuery(DaraModel):
    def __init__(
        self,
        division_code: str = None,
    ):
        # divisionCode
        # 
        # This parameter is required.
        self.division_code = division_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.division_code is not None:
            result['divisionCode'] = self.division_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('divisionCode') is not None:
            self.division_code = m.get('divisionCode')

        return self

