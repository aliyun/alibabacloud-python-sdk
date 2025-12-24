# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePriceForRenewDesktopOversoldGroupRequest(DaraModel):
    def __init__(
        self,
        oversold_group_id: str = None,
        period: int = None,
        period_unit: str = None,
    ):
        self.oversold_group_id = oversold_group_id
        self.period = period
        self.period_unit = period_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oversold_group_id is not None:
            result['OversoldGroupId'] = self.oversold_group_id

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OversoldGroupId') is not None:
            self.oversold_group_id = m.get('OversoldGroupId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        return self

