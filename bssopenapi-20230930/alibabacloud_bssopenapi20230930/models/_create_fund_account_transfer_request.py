# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFundAccountTransferRequest(DaraModel):
    def __init__(
        self,
        amount: str = None,
        currency: str = None,
        finance_type: str = None,
        from_fund_account_id: int = None,
        remark: str = None,
        to_fund_account_id: int = None,
        transfer_type: str = None,
    ):
        # This parameter is required.
        self.amount = amount
        # This parameter is required.
        self.currency = currency
        # This parameter is required.
        self.finance_type = finance_type
        # This parameter is required.
        self.from_fund_account_id = from_fund_account_id
        # This parameter is required.
        self.remark = remark
        # This parameter is required.
        self.to_fund_account_id = to_fund_account_id
        # This parameter is required.
        self.transfer_type = transfer_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.finance_type is not None:
            result['FinanceType'] = self.finance_type

        if self.from_fund_account_id is not None:
            result['FromFundAccountId'] = self.from_fund_account_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.to_fund_account_id is not None:
            result['ToFundAccountId'] = self.to_fund_account_id

        if self.transfer_type is not None:
            result['TransferType'] = self.transfer_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('FinanceType') is not None:
            self.finance_type = m.get('FinanceType')

        if m.get('FromFundAccountId') is not None:
            self.from_fund_account_id = m.get('FromFundAccountId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ToFundAccountId') is not None:
            self.to_fund_account_id = m.get('ToFundAccountId')

        if m.get('TransferType') is not None:
            self.transfer_type = m.get('TransferType')

        return self

