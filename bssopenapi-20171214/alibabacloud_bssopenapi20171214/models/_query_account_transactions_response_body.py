# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QueryAccountTransactionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryAccountTransactionsResponseBodyData = None,
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
            temp_model = main_models.QueryAccountTransactionsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryAccountTransactionsResponseBodyData(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_transactions_list: main_models.QueryAccountTransactionsResponseBodyDataAccountTransactionsList = None,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The name of your Alibaba Cloud account.
        self.account_name = account_name
        # The information about transactions.
        self.account_transactions_list = account_transactions_list
        # The page number of the returned page.
        self.page_num = page_num
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of returned entries.
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

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountTransactionsList') is not None:
            temp_model = main_models.QueryAccountTransactionsResponseBodyDataAccountTransactionsList()
            self.account_transactions_list = temp_model.from_map(m.get('AccountTransactionsList'))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryAccountTransactionsResponseBodyDataAccountTransactionsList(DaraModel):
    def __init__(
        self,
        account_transactions_list: List[main_models.QueryAccountTransactionsResponseBodyDataAccountTransactionsListAccountTransactionsList] = None,
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
                temp_model = main_models.QueryAccountTransactionsResponseBodyDataAccountTransactionsListAccountTransactionsList()
                self.account_transactions_list.append(temp_model.from_map(k1))

        return self

class QueryAccountTransactionsResponseBodyDataAccountTransactionsListAccountTransactionsList(DaraModel):
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
        # The amount.
        self.amount = amount
        # The balance of the account.
        self.balance = balance
        # The billing cycle. Format: YYYY-MM.
        self.billing_cycle = billing_cycle
        # The type of transaction payment. Valid values:
        # 
        # *   Cash: pay for the transaction in cash.
        # *   Deposit: pay for the transaction with deposit.
        # *   RegularBankCreditRefund: pay for the transaction with credit refund controlled by a bank.
        # *   DirectPay: directly pay for the transaction.
        self.fund_type = fund_type
        # The number of the order or bill.
        self.record_id = record_id
        # The remarks on the transaction.
        self.remarks = remarks
        # The transaction account. For example, the account is a recharge account in Alipay or a transfer account.
        self.transaction_account = transaction_account
        # The transaction channel.
        # 
        # *   AccountBalance
        # *   BankTransfer
        # *   Alipay
        # *   AntCreditPay
        # *   OfflineRemittance
        # *   RegularBankCreditRefund
        # *   CreditCard
        # *   MyBankCredit
        # *   HuaxiaBankCInstallment
        # *   ApplePay
        self.transaction_channel = transaction_channel
        # The serial number of the transaction channel.
        self.transaction_channel_sn = transaction_channel_sn
        # The type of the transaction flow.
        # 
        # *   Income
        # *   Expense
        self.transaction_flow = transaction_flow
        # The number of the transaction.
        self.transaction_number = transaction_number
        # The time when the transaction was made.
        self.transaction_time = transaction_time
        # The type of the transaction.
        # 
        # *   Payment
        # *   Withdraw
        # *   Refund
        # *   Consumption
        # *   Transfer
        # *   Adjust
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

