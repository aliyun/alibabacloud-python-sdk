# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class Money(DaraModel):
    def __init__(
        self,
        amount: int = None,
        amount_as_string: str = None,
        amount_string: str = None,
        cent: int = None,
        currency: main_models.MoneyCurrency = None,
        currency_code: str = None,
        positive: bool = None,
    ):
        # amount
        self.amount = amount
        # amountAsString
        self.amount_as_string = amount_as_string
        # amountString
        self.amount_string = amount_string
        # cent
        self.cent = cent
        # currency
        self.currency = currency
        # currencyCode
        self.currency_code = currency_code
        # positive
        self.positive = positive

    def validate(self):
        if self.currency:
            self.currency.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.amount_as_string is not None:
            result['amountAsString'] = self.amount_as_string

        if self.amount_string is not None:
            result['amountString'] = self.amount_string

        if self.cent is not None:
            result['cent'] = self.cent

        if self.currency is not None:
            result['currency'] = self.currency.to_map()

        if self.currency_code is not None:
            result['currencyCode'] = self.currency_code

        if self.positive is not None:
            result['positive'] = self.positive

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('amountAsString') is not None:
            self.amount_as_string = m.get('amountAsString')

        if m.get('amountString') is not None:
            self.amount_string = m.get('amountString')

        if m.get('cent') is not None:
            self.cent = m.get('cent')

        if m.get('currency') is not None:
            temp_model = main_models.MoneyCurrency()
            self.currency = temp_model.from_map(m.get('currency'))

        if m.get('currencyCode') is not None:
            self.currency_code = m.get('currencyCode')

        if m.get('positive') is not None:
            self.positive = m.get('positive')

        return self



class MoneyCurrency(DaraModel):
    def __init__(
        self,
        currency_code: str = None,
        default_fraction_digits: int = None,
        display_name: str = None,
        numeric_code: int = None,
        symbol: str = None,
    ):
        # currencyCode
        self.currency_code = currency_code
        # defaultFractionDigits
        self.default_fraction_digits = default_fraction_digits
        # displayName
        self.display_name = display_name
        # numericCode
        self.numeric_code = numeric_code
        # symbol
        self.symbol = symbol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency_code is not None:
            result['currencyCode'] = self.currency_code

        if self.default_fraction_digits is not None:
            result['defaultFractionDigits'] = self.default_fraction_digits

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.numeric_code is not None:
            result['numericCode'] = self.numeric_code

        if self.symbol is not None:
            result['symbol'] = self.symbol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currencyCode') is not None:
            self.currency_code = m.get('currencyCode')

        if m.get('defaultFractionDigits') is not None:
            self.default_fraction_digits = m.get('defaultFractionDigits')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('numericCode') is not None:
            self.numeric_code = m.get('numericCode')

        if m.get('symbol') is not None:
            self.symbol = m.get('symbol')

        return self

