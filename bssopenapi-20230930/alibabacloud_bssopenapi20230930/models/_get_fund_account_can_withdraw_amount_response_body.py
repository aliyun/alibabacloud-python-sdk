# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class GetFundAccountCanWithdrawAmountResponseBody(DaraModel):
    def __init__(
        self,
        can_original_withdraw_amount: str = None,
        can_withdraw_amount: str = None,
        cannot_original_withdraw_amount: str = None,
        cash_amount: str = None,
        credit_memo_amount: str = None,
        current_month_uncleared_amount: str = None,
        history_month_uncleared_amount: str = None,
        metadata: Any = None,
        pay_as_you_go_reversed_amount: str = None,
        request_id: str = None,
        transfer_amount: str = None,
    ):
        self.can_original_withdraw_amount = can_original_withdraw_amount
        self.can_withdraw_amount = can_withdraw_amount
        self.cannot_original_withdraw_amount = cannot_original_withdraw_amount
        self.cash_amount = cash_amount
        self.credit_memo_amount = credit_memo_amount
        self.current_month_uncleared_amount = current_month_uncleared_amount
        self.history_month_uncleared_amount = history_month_uncleared_amount
        self.metadata = metadata
        self.pay_as_you_go_reversed_amount = pay_as_you_go_reversed_amount
        self.request_id = request_id
        self.transfer_amount = transfer_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_original_withdraw_amount is not None:
            result['CanOriginalWithdrawAmount'] = self.can_original_withdraw_amount

        if self.can_withdraw_amount is not None:
            result['CanWithdrawAmount'] = self.can_withdraw_amount

        if self.cannot_original_withdraw_amount is not None:
            result['CannotOriginalWithdrawAmount'] = self.cannot_original_withdraw_amount

        if self.cash_amount is not None:
            result['CashAmount'] = self.cash_amount

        if self.credit_memo_amount is not None:
            result['CreditMemoAmount'] = self.credit_memo_amount

        if self.current_month_uncleared_amount is not None:
            result['CurrentMonthUnclearedAmount'] = self.current_month_uncleared_amount

        if self.history_month_uncleared_amount is not None:
            result['HistoryMonthUnclearedAmount'] = self.history_month_uncleared_amount

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.pay_as_you_go_reversed_amount is not None:
            result['PayAsYouGoReversedAmount'] = self.pay_as_you_go_reversed_amount

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.transfer_amount is not None:
            result['TransferAmount'] = self.transfer_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanOriginalWithdrawAmount') is not None:
            self.can_original_withdraw_amount = m.get('CanOriginalWithdrawAmount')

        if m.get('CanWithdrawAmount') is not None:
            self.can_withdraw_amount = m.get('CanWithdrawAmount')

        if m.get('CannotOriginalWithdrawAmount') is not None:
            self.cannot_original_withdraw_amount = m.get('CannotOriginalWithdrawAmount')

        if m.get('CashAmount') is not None:
            self.cash_amount = m.get('CashAmount')

        if m.get('CreditMemoAmount') is not None:
            self.credit_memo_amount = m.get('CreditMemoAmount')

        if m.get('CurrentMonthUnclearedAmount') is not None:
            self.current_month_uncleared_amount = m.get('CurrentMonthUnclearedAmount')

        if m.get('HistoryMonthUnclearedAmount') is not None:
            self.history_month_uncleared_amount = m.get('HistoryMonthUnclearedAmount')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('PayAsYouGoReversedAmount') is not None:
            self.pay_as_you_go_reversed_amount = m.get('PayAsYouGoReversedAmount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TransferAmount') is not None:
            self.transfer_amount = m.get('TransferAmount')

        return self

