# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetCarbonEmissionTrendRequest(DaraModel):
    def __init__(
        self,
        code: str = None,
        module_code: str = None,
        module_type: int = None,
        trend_type: int = None,
        year_list: List[int] = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # Module code.
        self.module_code = module_code
        # Module type.
        self.module_type = module_type
        # Trend Type.
        # 
        # This parameter is required.
        self.trend_type = trend_type
        # The list of inventory year.
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

        if self.module_code is not None:
            result['moduleCode'] = self.module_code

        if self.module_type is not None:
            result['moduleType'] = self.module_type

        if self.trend_type is not None:
            result['trendType'] = self.trend_type

        if self.year_list is not None:
            result['yearList'] = self.year_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('moduleCode') is not None:
            self.module_code = m.get('moduleCode')

        if m.get('moduleType') is not None:
            self.module_type = m.get('moduleType')

        if m.get('trendType') is not None:
            self.trend_type = m.get('trendType')

        if m.get('yearList') is not None:
            self.year_list = m.get('yearList')

        return self

