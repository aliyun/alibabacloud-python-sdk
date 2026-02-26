# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ProductPrice(DaraModel):
    def __init__(
        self,
        fund_amount_money: str = None,
    ):
        self.fund_amount_money = fund_amount_money

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fund_amount_money is not None:
            result['fundAmountMoney'] = self.fund_amount_money

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fundAmountMoney') is not None:
            self.fund_amount_money = m.get('fundAmountMoney')

        return self

