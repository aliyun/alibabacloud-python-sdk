# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryExportAuctionDetailResponseBody(DaraModel):
    def __init__(
        self,
        auction_end_time: str = None,
        auction_id: str = None,
        auction_status: str = None,
        book_end_time: str = None,
        buyer_status: str = None,
        current_price: float = None,
        increase_price: float = None,
        my_price: float = None,
        my_proxy_price: float = None,
        others_max_proxy_price: float = None,
        proxy_price: float = None,
        request_id: str = None,
    ):
        self.auction_end_time = auction_end_time
        self.auction_id = auction_id
        self.auction_status = auction_status
        self.book_end_time = book_end_time
        self.buyer_status = buyer_status
        self.current_price = current_price
        self.increase_price = increase_price
        self.my_price = my_price
        self.my_proxy_price = my_proxy_price
        self.others_max_proxy_price = others_max_proxy_price
        self.proxy_price = proxy_price
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auction_end_time is not None:
            result['AuctionEndTime'] = self.auction_end_time

        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id

        if self.auction_status is not None:
            result['AuctionStatus'] = self.auction_status

        if self.book_end_time is not None:
            result['BookEndTime'] = self.book_end_time

        if self.buyer_status is not None:
            result['BuyerStatus'] = self.buyer_status

        if self.current_price is not None:
            result['CurrentPrice'] = self.current_price

        if self.increase_price is not None:
            result['IncreasePrice'] = self.increase_price

        if self.my_price is not None:
            result['MyPrice'] = self.my_price

        if self.my_proxy_price is not None:
            result['MyProxyPrice'] = self.my_proxy_price

        if self.others_max_proxy_price is not None:
            result['OthersMaxProxyPrice'] = self.others_max_proxy_price

        if self.proxy_price is not None:
            result['ProxyPrice'] = self.proxy_price

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuctionEndTime') is not None:
            self.auction_end_time = m.get('AuctionEndTime')

        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')

        if m.get('AuctionStatus') is not None:
            self.auction_status = m.get('AuctionStatus')

        if m.get('BookEndTime') is not None:
            self.book_end_time = m.get('BookEndTime')

        if m.get('BuyerStatus') is not None:
            self.buyer_status = m.get('BuyerStatus')

        if m.get('CurrentPrice') is not None:
            self.current_price = m.get('CurrentPrice')

        if m.get('IncreasePrice') is not None:
            self.increase_price = m.get('IncreasePrice')

        if m.get('MyPrice') is not None:
            self.my_price = m.get('MyPrice')

        if m.get('MyProxyPrice') is not None:
            self.my_proxy_price = m.get('MyProxyPrice')

        if m.get('OthersMaxProxyPrice') is not None:
            self.others_max_proxy_price = m.get('OthersMaxProxyPrice')

        if m.get('ProxyPrice') is not None:
            self.proxy_price = m.get('ProxyPrice')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

