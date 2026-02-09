# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetFundAccountCreditAmountRequest(DaraModel):
    def __init__(
        self,
        credit_amount: str = None,
        currency: str = None,
        fund_account_id: int = None,
    ):
        # This parameter is required.
        self.credit_amount = credit_amount
        # This parameter is required.
        self.currency = currency
        self.fund_account_id = fund_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credit_amount is not None:
            result['CreditAmount'] = self.credit_amount

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreditAmount') is not None:
            self.credit_amount = m.get('CreditAmount')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')

        return self

