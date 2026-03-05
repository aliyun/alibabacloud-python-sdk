# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_modelservice20220614 import models as main_models
from darabonba.model import DaraModel

class ListDayAmountResponseBody(DaraModel):
    def __init__(
        self,
        day_amounts: List[main_models.ListDayAmountResponseBodyDayAmounts] = None,
        request_id: str = None,
    ):
        self.day_amounts = day_amounts
        self.request_id = request_id

    def validate(self):
        if self.day_amounts:
            for v1 in self.day_amounts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DayAmounts'] = []
        if self.day_amounts is not None:
            for k1 in self.day_amounts:
                result['DayAmounts'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.day_amounts = []
        if m.get('DayAmounts') is not None:
            for k1 in m.get('DayAmounts'):
                temp_model = main_models.ListDayAmountResponseBodyDayAmounts()
                self.day_amounts.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self



class ListDayAmountResponseBodyDayAmounts(DaraModel):
    def __init__(
        self,
        amount: int = None,
        date: str = None,
    ):
        self.amount = amount
        self.date = date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.date is not None:
            result['Date'] = self.date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Date') is not None:
            self.date = m.get('Date')

        return self

