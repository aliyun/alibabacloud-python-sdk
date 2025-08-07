# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 


class MoMValues(DaraModel):
    def __init__(
        self,
        current_value: int = None,
        last_day_value: int = None,
        last_month_value: int = None,
    ):
        # total
        self.current_value = current_value
        # daily addition
        self.last_day_value = last_day_value
        # monthly addition
        self.last_month_value = last_month_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_value is not None:
            result['currentValue'] = self.current_value

        if self.last_day_value is not None:
            result['lastDayValue'] = self.last_day_value

        if self.last_month_value is not None:
            result['lastMonthValue'] = self.last_month_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentValue') is not None:
            self.current_value = m.get('currentValue')

        if m.get('lastDayValue') is not None:
            self.last_day_value = m.get('lastDayValue')

        if m.get('lastMonthValue') is not None:
            self.last_month_value = m.get('lastMonthValue')

        return self

