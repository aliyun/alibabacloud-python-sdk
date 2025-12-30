# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PurchaseIntlDomainRequest(DaraModel):
    def __init__(
        self,
        auction_id: str = None,
        currency: str = None,
        price: float = None,
    ):
        # This parameter is required.
        self.auction_id = auction_id
        # This parameter is required.
        self.currency = currency
        # This parameter is required.
        self.price = price

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

        if self.price is not None:
            result['Price'] = self.price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        return self

