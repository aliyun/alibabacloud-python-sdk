# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class GetFundAccountAvailableAmountResponseBody(DaraModel):
    def __init__(
        self,
        available_amount: str = None,
        available_credit_amount: str = None,
        bank_acceptance_amount: str = None,
        cash_amount: str = None,
        credit_amount: str = None,
        credit_refund_amount: str = None,
        credit_user: bool = None,
        currency: str = None,
        current_month_uncleared_amount: str = None,
        extend_ledger_list: List[main_models.GetFundAccountAvailableAmountResponseBodyExtendLedgerList] = None,
        fund_account_id: str = None,
        fund_account_owner_account_id: str = None,
        fund_account_status: str = None,
        fund_account_type: str = None,
        history_month_uncleared_amount: str = None,
        metadata: Any = None,
        negative_bill_amount: str = None,
        original_cash_amount_list: List[main_models.GetFundAccountAvailableAmountResponseBodyOriginalCashAmountList] = None,
        quota_amount: str = None,
        quota_consumed_amount: str = None,
        request_id: str = None,
        uncleared_amount: str = None,
    ):
        self.available_amount = available_amount
        self.available_credit_amount = available_credit_amount
        self.bank_acceptance_amount = bank_acceptance_amount
        self.cash_amount = cash_amount
        self.credit_amount = credit_amount
        self.credit_refund_amount = credit_refund_amount
        self.credit_user = credit_user
        self.currency = currency
        self.current_month_uncleared_amount = current_month_uncleared_amount
        self.extend_ledger_list = extend_ledger_list
        self.fund_account_id = fund_account_id
        self.fund_account_owner_account_id = fund_account_owner_account_id
        self.fund_account_status = fund_account_status
        self.fund_account_type = fund_account_type
        self.history_month_uncleared_amount = history_month_uncleared_amount
        self.metadata = metadata
        self.negative_bill_amount = negative_bill_amount
        self.original_cash_amount_list = original_cash_amount_list
        self.quota_amount = quota_amount
        self.quota_consumed_amount = quota_consumed_amount
        self.request_id = request_id
        self.uncleared_amount = uncleared_amount

    def validate(self):
        if self.extend_ledger_list:
            for v1 in self.extend_ledger_list:
                 if v1:
                    v1.validate()
        if self.original_cash_amount_list:
            for v1 in self.original_cash_amount_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_amount is not None:
            result['AvailableAmount'] = self.available_amount

        if self.available_credit_amount is not None:
            result['AvailableCreditAmount'] = self.available_credit_amount

        if self.bank_acceptance_amount is not None:
            result['BankAcceptanceAmount'] = self.bank_acceptance_amount

        if self.cash_amount is not None:
            result['CashAmount'] = self.cash_amount

        if self.credit_amount is not None:
            result['CreditAmount'] = self.credit_amount

        if self.credit_refund_amount is not None:
            result['CreditRefundAmount'] = self.credit_refund_amount

        if self.credit_user is not None:
            result['CreditUser'] = self.credit_user

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.current_month_uncleared_amount is not None:
            result['CurrentMonthUnclearedAmount'] = self.current_month_uncleared_amount

        result['ExtendLedgerList'] = []
        if self.extend_ledger_list is not None:
            for k1 in self.extend_ledger_list:
                result['ExtendLedgerList'].append(k1.to_map() if k1 else None)

        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id

        if self.fund_account_owner_account_id is not None:
            result['FundAccountOwnerAccountId'] = self.fund_account_owner_account_id

        if self.fund_account_status is not None:
            result['FundAccountStatus'] = self.fund_account_status

        if self.fund_account_type is not None:
            result['FundAccountType'] = self.fund_account_type

        if self.history_month_uncleared_amount is not None:
            result['HistoryMonthUnclearedAmount'] = self.history_month_uncleared_amount

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.negative_bill_amount is not None:
            result['NegativeBillAmount'] = self.negative_bill_amount

        result['OriginalCashAmountList'] = []
        if self.original_cash_amount_list is not None:
            for k1 in self.original_cash_amount_list:
                result['OriginalCashAmountList'].append(k1.to_map() if k1 else None)

        if self.quota_amount is not None:
            result['QuotaAmount'] = self.quota_amount

        if self.quota_consumed_amount is not None:
            result['QuotaConsumedAmount'] = self.quota_consumed_amount

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.uncleared_amount is not None:
            result['UnclearedAmount'] = self.uncleared_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableAmount') is not None:
            self.available_amount = m.get('AvailableAmount')

        if m.get('AvailableCreditAmount') is not None:
            self.available_credit_amount = m.get('AvailableCreditAmount')

        if m.get('BankAcceptanceAmount') is not None:
            self.bank_acceptance_amount = m.get('BankAcceptanceAmount')

        if m.get('CashAmount') is not None:
            self.cash_amount = m.get('CashAmount')

        if m.get('CreditAmount') is not None:
            self.credit_amount = m.get('CreditAmount')

        if m.get('CreditRefundAmount') is not None:
            self.credit_refund_amount = m.get('CreditRefundAmount')

        if m.get('CreditUser') is not None:
            self.credit_user = m.get('CreditUser')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('CurrentMonthUnclearedAmount') is not None:
            self.current_month_uncleared_amount = m.get('CurrentMonthUnclearedAmount')

        self.extend_ledger_list = []
        if m.get('ExtendLedgerList') is not None:
            for k1 in m.get('ExtendLedgerList'):
                temp_model = main_models.GetFundAccountAvailableAmountResponseBodyExtendLedgerList()
                self.extend_ledger_list.append(temp_model.from_map(k1))

        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')

        if m.get('FundAccountOwnerAccountId') is not None:
            self.fund_account_owner_account_id = m.get('FundAccountOwnerAccountId')

        if m.get('FundAccountStatus') is not None:
            self.fund_account_status = m.get('FundAccountStatus')

        if m.get('FundAccountType') is not None:
            self.fund_account_type = m.get('FundAccountType')

        if m.get('HistoryMonthUnclearedAmount') is not None:
            self.history_month_uncleared_amount = m.get('HistoryMonthUnclearedAmount')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('NegativeBillAmount') is not None:
            self.negative_bill_amount = m.get('NegativeBillAmount')

        self.original_cash_amount_list = []
        if m.get('OriginalCashAmountList') is not None:
            for k1 in m.get('OriginalCashAmountList'):
                temp_model = main_models.GetFundAccountAvailableAmountResponseBodyOriginalCashAmountList()
                self.original_cash_amount_list.append(temp_model.from_map(k1))

        if m.get('QuotaAmount') is not None:
            self.quota_amount = m.get('QuotaAmount')

        if m.get('QuotaConsumedAmount') is not None:
            self.quota_consumed_amount = m.get('QuotaConsumedAmount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UnclearedAmount') is not None:
            self.uncleared_amount = m.get('UnclearedAmount')

        return self

class GetFundAccountAvailableAmountResponseBodyOriginalCashAmountList(DaraModel):
    def __init__(
        self,
        amount: str = None,
        currency: str = None,
    ):
        self.amount = amount
        self.currency = currency

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        return self

class GetFundAccountAvailableAmountResponseBodyExtendLedgerList(DaraModel):
    def __init__(
        self,
        currency: str = None,
        ledger_name: str = None,
        original_amount: str = None,
    ):
        self.currency = currency
        self.ledger_name = ledger_name
        self.original_amount = original_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['Currency'] = self.currency

        if self.ledger_name is not None:
            result['LedgerName'] = self.ledger_name

        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('LedgerName') is not None:
            self.ledger_name = m.get('LedgerName')

        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')

        return self

