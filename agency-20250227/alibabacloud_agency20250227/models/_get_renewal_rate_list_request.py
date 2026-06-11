# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRenewalRateListRequest(DaraModel):
    def __init__(
        self,
        fiscal_year_and_quarter: str = None,
    ):
        # Fiscal year and quarter
        # 
        # This parameter is required.
        self.fiscal_year_and_quarter = fiscal_year_and_quarter

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fiscal_year_and_quarter is not None:
            result['FiscalYearAndQuarter'] = self.fiscal_year_and_quarter

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FiscalYearAndQuarter') is not None:
            self.fiscal_year_and_quarter = m.get('FiscalYearAndQuarter')

        return self

