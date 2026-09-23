# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetFundAccountCreditAmountRequest(DaraModel):
    def __init__(
        self,
        cancel_credit: str = None,
        credit_amount: str = None,
        currency: str = None,
        fund_account_id: int = None,
    ):
        # Specifies whether to cancel credit control. Valid values:
        # - true: Cancel credit control.
        # - false or empty: Set credit control.
        # 
        # When canceling credit control, CreditAmount must be set to 0.
        self.cancel_credit = cancel_credit
        # The credit limit.
        # 
        # This parameter is required.
        self.credit_amount = credit_amount
        # The currency of the credit limit. Currently, only CNY is supported for Chinese mainland accounts, and only USD is supported for international accounts.
        # 
        # This parameter is required.
        self.currency = currency
        # The fund account ID. If this parameter is not specified, the account owned by the current account is used by default.
        self.fund_account_id = fund_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cancel_credit is not None:
            result['CancelCredit'] = self.cancel_credit

        if self.credit_amount is not None:
            result['CreditAmount'] = self.credit_amount

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CancelCredit') is not None:
            self.cancel_credit = m.get('CancelCredit')

        if m.get('CreditAmount') is not None:
            self.credit_amount = m.get('CreditAmount')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')

        return self

