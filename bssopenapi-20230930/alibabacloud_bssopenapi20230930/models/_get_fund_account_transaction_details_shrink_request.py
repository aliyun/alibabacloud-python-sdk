# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetFundAccountTransactionDetailsShrinkRequest(DaraModel):
    def __init__(
        self,
        bill_number: str = None,
        channel_transaction_number: str = None,
        current_page: int = None,
        end_time: int = None,
        fund_account_id: int = None,
        page_size: int = None,
        start_time: int = None,
        transaction_channel_list_shrink: str = None,
        transaction_direction: str = None,
        transaction_number: int = None,
        transaction_type: str = None,
        transaction_type_list_shrink: str = None,
    ):
        self.bill_number = bill_number
        self.channel_transaction_number = channel_transaction_number
        self.current_page = current_page
        self.end_time = end_time
        self.fund_account_id = fund_account_id
        self.page_size = page_size
        self.start_time = start_time
        self.transaction_channel_list_shrink = transaction_channel_list_shrink
        self.transaction_direction = transaction_direction
        self.transaction_number = transaction_number
        self.transaction_type = transaction_type
        self.transaction_type_list_shrink = transaction_type_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_number is not None:
            result['BillNumber'] = self.bill_number

        if self.channel_transaction_number is not None:
            result['ChannelTransactionNumber'] = self.channel_transaction_number

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.transaction_channel_list_shrink is not None:
            result['TransactionChannelList'] = self.transaction_channel_list_shrink

        if self.transaction_direction is not None:
            result['TransactionDirection'] = self.transaction_direction

        if self.transaction_number is not None:
            result['TransactionNumber'] = self.transaction_number

        if self.transaction_type is not None:
            result['TransactionType'] = self.transaction_type

        if self.transaction_type_list_shrink is not None:
            result['TransactionTypeList'] = self.transaction_type_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillNumber') is not None:
            self.bill_number = m.get('BillNumber')

        if m.get('ChannelTransactionNumber') is not None:
            self.channel_transaction_number = m.get('ChannelTransactionNumber')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TransactionChannelList') is not None:
            self.transaction_channel_list_shrink = m.get('TransactionChannelList')

        if m.get('TransactionDirection') is not None:
            self.transaction_direction = m.get('TransactionDirection')

        if m.get('TransactionNumber') is not None:
            self.transaction_number = m.get('TransactionNumber')

        if m.get('TransactionType') is not None:
            self.transaction_type = m.get('TransactionType')

        if m.get('TransactionTypeList') is not None:
            self.transaction_type_list_shrink = m.get('TransactionTypeList')

        return self

