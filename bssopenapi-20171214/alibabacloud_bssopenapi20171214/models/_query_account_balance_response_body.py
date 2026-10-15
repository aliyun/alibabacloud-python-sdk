# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QueryAccountBalanceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryAccountBalanceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryAccountBalanceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryAccountBalanceResponseBodyData(DaraModel):
    def __init__(
        self,
        available_amount: str = None,
        available_cash_amount: str = None,
        credit_amount: str = None,
        currency: str = None,
        mybank_credit_amount: str = None,
        quota_limit: str = None,
    ):
        # The available credit.
        self.available_amount = available_amount
        # The available cash balance.
        self.available_cash_amount = available_cash_amount
        # The credit limit.
        self.credit_amount = credit_amount
        # The currency. Valid values:
        # 
        # - CNY: Chinese Yuan
        # 
        # - USD: US Dollar
        # 
        # - JPY: Japanese Yen
        self.currency = currency
        # The credit limit granted by MYbank.
        self.mybank_credit_amount = mybank_credit_amount
        # The quota limit for ecosystem customers.
        self.quota_limit = quota_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_amount is not None:
            result['AvailableAmount'] = self.available_amount

        if self.available_cash_amount is not None:
            result['AvailableCashAmount'] = self.available_cash_amount

        if self.credit_amount is not None:
            result['CreditAmount'] = self.credit_amount

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.mybank_credit_amount is not None:
            result['MybankCreditAmount'] = self.mybank_credit_amount

        if self.quota_limit is not None:
            result['QuotaLimit'] = self.quota_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableAmount') is not None:
            self.available_amount = m.get('AvailableAmount')

        if m.get('AvailableCashAmount') is not None:
            self.available_cash_amount = m.get('AvailableCashAmount')

        if m.get('CreditAmount') is not None:
            self.credit_amount = m.get('CreditAmount')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('MybankCreditAmount') is not None:
            self.mybank_credit_amount = m.get('MybankCreditAmount')

        if m.get('QuotaLimit') is not None:
            self.quota_limit = m.get('QuotaLimit')

        return self

