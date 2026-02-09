# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class GetFundAccountTransactionDetailsResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[main_models.GetFundAccountTransactionDetailsResponseBodyData] = None,
        metadata: Any = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.data = data
        self.metadata = metadata
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetFundAccountTransactionDetailsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetFundAccountTransactionDetailsResponseBodyData(DaraModel):
    def __init__(
        self,
        balance: str = None,
        bill_number: str = None,
        channel_transaction_number: str = None,
        currency: str = None,
        fund_account_ecid: str = None,
        fund_account_id: int = None,
        fund_account_name: str = None,
        fund_account_owner_account_id: int = None,
        fund_type: str = None,
        nbid: str = None,
        remark: str = None,
        site: str = None,
        transaction_account: str = None,
        transaction_amount: str = None,
        transaction_channel: str = None,
        transaction_direction: str = None,
        transaction_number: int = None,
        transaction_time: str = None,
        transaction_type: str = None,
    ):
        self.balance = balance
        self.bill_number = bill_number
        self.channel_transaction_number = channel_transaction_number
        self.currency = currency
        self.fund_account_ecid = fund_account_ecid
        self.fund_account_id = fund_account_id
        self.fund_account_name = fund_account_name
        self.fund_account_owner_account_id = fund_account_owner_account_id
        self.fund_type = fund_type
        self.nbid = nbid
        self.remark = remark
        self.site = site
        self.transaction_account = transaction_account
        self.transaction_amount = transaction_amount
        self.transaction_channel = transaction_channel
        self.transaction_direction = transaction_direction
        self.transaction_number = transaction_number
        self.transaction_time = transaction_time
        self.transaction_type = transaction_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.balance is not None:
            result['Balance'] = self.balance

        if self.bill_number is not None:
            result['BillNumber'] = self.bill_number

        if self.channel_transaction_number is not None:
            result['ChannelTransactionNumber'] = self.channel_transaction_number

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.fund_account_ecid is not None:
            result['FundAccountEcid'] = self.fund_account_ecid

        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id

        if self.fund_account_name is not None:
            result['FundAccountName'] = self.fund_account_name

        if self.fund_account_owner_account_id is not None:
            result['FundAccountOwnerAccountId'] = self.fund_account_owner_account_id

        if self.fund_type is not None:
            result['FundType'] = self.fund_type

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.site is not None:
            result['Site'] = self.site

        if self.transaction_account is not None:
            result['TransactionAccount'] = self.transaction_account

        if self.transaction_amount is not None:
            result['TransactionAmount'] = self.transaction_amount

        if self.transaction_channel is not None:
            result['TransactionChannel'] = self.transaction_channel

        if self.transaction_direction is not None:
            result['TransactionDirection'] = self.transaction_direction

        if self.transaction_number is not None:
            result['TransactionNumber'] = self.transaction_number

        if self.transaction_time is not None:
            result['TransactionTime'] = self.transaction_time

        if self.transaction_type is not None:
            result['TransactionType'] = self.transaction_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Balance') is not None:
            self.balance = m.get('Balance')

        if m.get('BillNumber') is not None:
            self.bill_number = m.get('BillNumber')

        if m.get('ChannelTransactionNumber') is not None:
            self.channel_transaction_number = m.get('ChannelTransactionNumber')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('FundAccountEcid') is not None:
            self.fund_account_ecid = m.get('FundAccountEcid')

        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')

        if m.get('FundAccountName') is not None:
            self.fund_account_name = m.get('FundAccountName')

        if m.get('FundAccountOwnerAccountId') is not None:
            self.fund_account_owner_account_id = m.get('FundAccountOwnerAccountId')

        if m.get('FundType') is not None:
            self.fund_type = m.get('FundType')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Site') is not None:
            self.site = m.get('Site')

        if m.get('TransactionAccount') is not None:
            self.transaction_account = m.get('TransactionAccount')

        if m.get('TransactionAmount') is not None:
            self.transaction_amount = m.get('TransactionAmount')

        if m.get('TransactionChannel') is not None:
            self.transaction_channel = m.get('TransactionChannel')

        if m.get('TransactionDirection') is not None:
            self.transaction_direction = m.get('TransactionDirection')

        if m.get('TransactionNumber') is not None:
            self.transaction_number = m.get('TransactionNumber')

        if m.get('TransactionTime') is not None:
            self.transaction_time = m.get('TransactionTime')

        if m.get('TransactionType') is not None:
            self.transaction_type = m.get('TransactionType')

        return self

