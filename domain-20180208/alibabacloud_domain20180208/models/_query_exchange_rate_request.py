# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryExchangeRateRequest(DaraModel):
    def __init__(
        self,
        from_currency: str = None,
        to_currency: str = None,
    ):
        # This parameter is required.
        self.from_currency = from_currency
        # This parameter is required.
        self.to_currency = to_currency

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_currency is not None:
            result['FromCurrency'] = self.from_currency

        if self.to_currency is not None:
            result['ToCurrency'] = self.to_currency

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromCurrency') is not None:
            self.from_currency = m.get('FromCurrency')

        if m.get('ToCurrency') is not None:
            self.to_currency = m.get('ToCurrency')

        return self

