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
        # The end of the creation time range to query. By default, the transactions in the last month are queried. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2018-01-01T00:00:00Z.
        self.create_time_end = create_time_end
        # The beginning of the creation time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2018-01-01T00:00:00Z.
        self.create_time_start = create_time_start
        # The number of the page to return. Default value is 1.
        self.page_num = page_num
        # The number of entries to return on each page. Default value is 20.
        self.page_size = page_size
        # The ID of the order or bill.
        self.record_id = record_id
        # The transaction channel. If you specify one of the following transaction channels for this parameter, the results for the specified transaction channel are returned. If the transaction channel that you specify does not belong to the following transaction channels, no result is returned. If you leave this parameter empty, the results for all the following transaction channels are returned by default. Valid values:
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
        # The type of the transaction flow. If you specify one of the following types for this parameter, the results for the specified type are returned. If the type that you specify does not belong to the following types, no result is returned. If you leave this parameter empty, the results for the following two types are returned by default. Valid values:
        # 
        # *   Income
        # *   Expense
        self.transaction_flow = transaction_flow
        # The number of the transaction.
        self.transaction_number = transaction_number
        # The type of the transaction. If you specify one of the following transaction types for this parameter, the results for the specified transaction type are returned. If the transaction type that you specify does not belong to the following types, no result is returned. If you leave this parameter empty, the results for all the following transaction types are returned by default. Valid values:
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

