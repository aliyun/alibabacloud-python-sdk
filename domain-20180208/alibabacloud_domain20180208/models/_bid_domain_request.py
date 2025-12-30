# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BidDomainRequest(DaraModel):
    def __init__(
        self,
        auction_id: str = None,
        currency: str = None,
        max_bid: float = None,
    ):
        # This parameter is required.
        self.auction_id = auction_id
        # This parameter is required.
        self.currency = currency
        # This parameter is required.
        self.max_bid = max_bid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.max_bid is not None:
            result['MaxBid'] = self.max_bid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('MaxBid') is not None:
            self.max_bid = m.get('MaxBid')

        return self

