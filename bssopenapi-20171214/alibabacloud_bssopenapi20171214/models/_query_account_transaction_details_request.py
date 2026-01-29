# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryAccountTransactionDetailsRequest(DaraModel):
    def __init__(
        self,
        create_time_end: str = None,
        create_time_start: str = None,
        max_results: int = None,
        next_token: str = None,
        record_id: str = None,
        transaction_channel: str = None,
        transaction_channel_sn: str = None,
        transaction_number: str = None,
        transaction_type: str = None,
    ):
        # The end of the creation time range to query.
        self.create_time_end = create_time_end
        # The beginning of the creation time range to query.
        self.create_time_start = create_time_start
        # This parameter is invalid.
        self.max_results = max_results
        # The token that is used for paging.
        self.next_token = next_token
        # The ID of the order or bill.
        self.record_id = record_id
        # The transaction channel.
        self.transaction_channel = transaction_channel
        # The serial number of the transaction channel.
        self.transaction_channel_sn = transaction_channel_sn
        # The number of the transaction.
        self.transaction_number = transaction_number
        # The type of the transaction.
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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.record_id is not None:
            result['RecordID'] = self.record_id

        if self.transaction_channel is not None:
            result['TransactionChannel'] = self.transaction_channel

        if self.transaction_channel_sn is not None:
            result['TransactionChannelSN'] = self.transaction_channel_sn

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

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RecordID') is not None:
            self.record_id = m.get('RecordID')

        if m.get('TransactionChannel') is not None:
            self.transaction_channel = m.get('TransactionChannel')

        if m.get('TransactionChannelSN') is not None:
            self.transaction_channel_sn = m.get('TransactionChannelSN')

        if m.get('TransactionNumber') is not None:
            self.transaction_number = m.get('TransactionNumber')

        if m.get('TransactionType') is not None:
            self.transaction_type = m.get('TransactionType')

        return self

