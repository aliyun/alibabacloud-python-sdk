# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryAccountTransactionsRequest(DaraModel):
    def __init__(
        self,
        create_time_end: str = None,
        create_time_start: str = None,
        page_num: int = None,
        page_size: int = None,
        record_id: str = None,
        transaction_channel: str = None,
        transaction_channel_sn: str = None,
        transaction_flow: str = None,
        transaction_number: str = None,
        transaction_type: str = None,
    ):
        # The end time of the creation time range. If not specified, the default value is the current time. Example: 2018-01-01T00:00:00Z.
        self.create_time_end = create_time_end
        # The start time of the creation time range. If not specified, the default value is one month before the current time. Example: 2018-01-01T00:00:00Z.
        self.create_time_start = create_time_start
        # The page number. Default value: 1.
        self.page_num = page_num
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The order or bill number.
        self.record_id = record_id
        # The transaction channel. If you specify a transaction channel, the query returns results of the corresponding type. If no results exist, an empty result is returned. If you do not specify this parameter, all types are returned by default. Valid values:
        # - AccountBalance: Account balance.
        # - BankTransfer: Bank transfer.
        # - Alipay: Alipay.
        # - AntCreditPay: Ant Credit Pay.
        # - OfflineRemittance: Offline remittance.
        # - RegularBankCreditRefund: Credit-based payment refund.
        # - CreditCard: Credit card.
        # - MyBankCredit: MYbank Credit.
        # - HuaxiaBankCInstallment: Huaxia Bank installment.
        # - ApplePay: Apple Pay.
        self.transaction_channel = transaction_channel
        # The payment reference No.
        self.transaction_channel_sn = transaction_channel_sn
        # The income and expense type. If you specify an income and expense type, the query returns results of the corresponding type. If no results exist, an empty result is returned. If you do not specify this parameter, all types are returned by default. Valid values:
        # - Income: Income.
        # - Expense: Expense.
        self.transaction_flow = transaction_flow
        # The transaction number.
        self.transaction_number = transaction_number
        # The transaction type. If you specify a transaction type, the query returns results of the corresponding type. If no results exist, an empty result is returned. If you do not specify this parameter, all types are returned by default. Valid values:
        # - Payment: Top-up.
        # - Withdraw: Withdrawal.
        # - Refund: Refund.
        # - Consumption: Consumption.
        # - Transfer: Transfer.
        # - Adjust: Adjustment.
        self.transaction_type = transaction_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end

        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.record_id is not None:
            result['RecordID'] = self.record_id

        if self.transaction_channel is not None:
            result['TransactionChannel'] = self.transaction_channel

        if self.transaction_channel_sn is not None:
            result['TransactionChannelSN'] = self.transaction_channel_sn

        if self.transaction_flow is not None:
            result['TransactionFlow'] = self.transaction_flow

        if self.transaction_number is not None:
            result['TransactionNumber'] = self.transaction_number

        if self.transaction_type is not None:
            result['TransactionType'] = self.transaction_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')

        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RecordID') is not None:
            self.record_id = m.get('RecordID')

        if m.get('TransactionChannel') is not None:
            self.transaction_channel = m.get('TransactionChannel')

        if m.get('TransactionChannelSN') is not None:
            self.transaction_channel_sn = m.get('TransactionChannelSN')

        if m.get('TransactionFlow') is not None:
            self.transaction_flow = m.get('TransactionFlow')

        if m.get('TransactionNumber') is not None:
            self.transaction_number = m.get('TransactionNumber')

        if m.get('TransactionType') is not None:
            self.transaction_type = m.get('TransactionType')

        return self

