# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QueryAccountTransactionDetailsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryAccountTransactionDetailsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned.
        self.code = code
        # The data returned.
        self.data = data
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
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
            temp_model = main_models.QueryAccountTransactionDetailsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryAccountTransactionDetailsResponseBodyData(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_transactions_list: main_models.QueryAccountTransactionDetailsResponseBodyDataAccountTransactionsList = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # The name of the account.
        self.account_name = account_name
        # The details of the transactions within the account.
        self.account_transactions_list = account_transactions_list
        # This parameter is invalid.
        self.max_results = max_results
        # The token that is used for paging.
        self.next_token = next_token
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.account_transactions_list:
            self.account_transactions_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_transactions_list is not None:
            result['AccountTransactionsList'] = self.account_transactions_list.to_map()

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountTransactionsList') is not None:
            temp_model = main_models.QueryAccountTransactionDetailsResponseBodyDataAccountTransactionsList()
            self.account_transactions_list = temp_model.from_map(m.get('AccountTransactionsList'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryAccountTransactionDetailsResponseBodyDataAccountTransactionsList(DaraModel):
    def __init__(
        self,
        account_transactions_list: List[main_models.QueryAccountTransactionDetailsResponseBodyDataAccountTransactionsListAccountTransactionsList] = None,
    ):
        self.account_transactions_list = account_transactions_list

    def validate(self):
        if self.account_transactions_list:
            for v1 in self.account_transactions_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccountTransactionsList'] = []
        if self.account_transactions_list is not None:
            for k1 in self.account_transactions_list:
                result['AccountTransactionsList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account_transactions_list = []
        if m.get('AccountTransactionsList') is not None:
            for k1 in m.get('AccountTransactionsList'):
                temp_model = main_models.QueryAccountTransactionDetailsResponseBodyDataAccountTransactionsListAccountTransactionsList()
                self.account_transactions_list.append(temp_model.from_map(k1))

        return self

class QueryAccountTransactionDetailsResponseBodyDataAccountTransactionsListAccountTransactionsList(DaraModel):
    def __init__(
        self,
        amount: str = None,
        balance: str = None,
        billing_cycle: str = None,
        fund_type: str = None,
        record_id: str = None,
        remarks: str = None,
        transaction_account: str = None,
        transaction_channel: str = None,
        transaction_channel_sn: str = None,
        transaction_flow: str = None,
        transaction_number: str = None,
        transaction_time: str = None,
        transaction_type: str = None,
    ):
        # The amount of the transaction.
        self.amount = amount
        # The balance of the account.
        self.balance = balance
        # The billing cycle.
        self.billing_cycle = billing_cycle
        # The type of transaction payment. Valid values:
        # 
        # Cash: pay for the transaction in cash. Deposit: pay for the transaction with deposit. RegularBankCreditRefund: pay for the transaction with credit refund controlled by a bank. DirectPay: directly pay for the transaction.
        self.fund_type = fund_type
        # The ID of the order or bill.
        self.record_id = record_id
        # The remarks.
        self.remarks = remarks
        # The transaction account.
        self.transaction_account = transaction_account
        # The transaction channel.
        self.transaction_channel = transaction_channel
        # The serial number of the transaction channel.
        self.transaction_channel_sn = transaction_channel_sn
        # Indicates whether the transaction is of the income type or the expenditure type. If one of the following types is specified, results for the specific type are returned. If the type that you specified for the parameter does not belong to the following types, no result is returned. If the parameter is left empty, results for transactions of the income and expenditure types are all returned. Valid values:
        # 
        # Income and Expense.
        self.transaction_flow = transaction_flow
        # The number of the transaction.
        self.transaction_number = transaction_number
        # The time when the transaction was made.
        self.transaction_time = transaction_time
        # The type of the transaction. If one of the following transaction types is specified, results for the specified transaction type are returned. If the transaction type that you specified does not belong to the following transaction types, no result is returned. If the parameter is left empty, results for all transaction types are returned. Valid values:
        # 
        # Payment, Withdraw, Refund, Consumption, Transfer, and Adjust.
        self.transaction_type = transaction_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.balance is not None:
            result['Balance'] = self.balance

        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle

        if self.fund_type is not None:
            result['FundType'] = self.fund_type

        if self.record_id is not None:
            result['RecordID'] = self.record_id

        if self.remarks is not None:
            result['Remarks'] = self.remarks

        if self.transaction_account is not None:
            result['TransactionAccount'] = self.transaction_account

        if self.transaction_channel is not None:
            result['TransactionChannel'] = self.transaction_channel

        if self.transaction_channel_sn is not None:
            result['TransactionChannelSN'] = self.transaction_channel_sn

        if self.transaction_flow is not None:
            result['TransactionFlow'] = self.transaction_flow

        if self.transaction_number is not None:
            result['TransactionNumber'] = self.transaction_number

        if self.transaction_time is not None:
            result['TransactionTime'] = self.transaction_time

        if self.transaction_type is not None:
            result['TransactionType'] = self.transaction_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Balance') is not None:
            self.balance = m.get('Balance')

        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')

        if m.get('FundType') is not None:
            self.fund_type = m.get('FundType')

        if m.get('RecordID') is not None:
            self.record_id = m.get('RecordID')

        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')

        if m.get('TransactionAccount') is not None:
            self.transaction_account = m.get('TransactionAccount')

        if m.get('TransactionChannel') is not None:
            self.transaction_channel = m.get('TransactionChannel')

        if m.get('TransactionChannelSN') is not None:
            self.transaction_channel_sn = m.get('TransactionChannelSN')

        if m.get('TransactionFlow') is not None:
            self.transaction_flow = m.get('TransactionFlow')

        if m.get('TransactionNumber') is not None:
            self.transaction_number = m.get('TransactionNumber')

        if m.get('TransactionTime') is not None:
            self.transaction_time = m.get('TransactionTime')

        if m.get('TransactionType') is not None:
            self.transaction_type = m.get('TransactionType')

        return self

