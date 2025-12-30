# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryBookingDomainInfoResponseBody(DaraModel):
    def __init__(
        self,
        auction_id: int = None,
        book_end_time: int = None,
        currency: str = None,
        max_bid: float = None,
        partner_type: str = None,
        request_id: str = None,
        snatch_no: str = None,
        transfer_in_price: float = None,
    ):
        self.auction_id = auction_id
        self.book_end_time = book_end_time
        self.currency = currency
        self.max_bid = max_bid
        self.partner_type = partner_type
        self.request_id = request_id
        self.snatch_no = snatch_no
        self.transfer_in_price = transfer_in_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id

        if self.book_end_time is not None:
            result['BookEndTime'] = self.book_end_time

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.max_bid is not None:
            result['MaxBid'] = self.max_bid

        if self.partner_type is not None:
            result['PartnerType'] = self.partner_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.snatch_no is not None:
            result['SnatchNo'] = self.snatch_no

        if self.transfer_in_price is not None:
            result['TransferInPrice'] = self.transfer_in_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')

        if m.get('BookEndTime') is not None:
            self.book_end_time = m.get('BookEndTime')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('MaxBid') is not None:
            self.max_bid = m.get('MaxBid')

        if m.get('PartnerType') is not None:
            self.partner_type = m.get('PartnerType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SnatchNo') is not None:
            self.snatch_no = m.get('SnatchNo')

        if m.get('TransferInPrice') is not None:
            self.transfer_in_price = m.get('TransferInPrice')

        return self

