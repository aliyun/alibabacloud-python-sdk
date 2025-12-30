# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryAuctionDetailResponseBody(DaraModel):
    def __init__(
        self,
        auction_end_time: int = None,
        auction_id: str = None,
        book_end_time: int = None,
        booked_partner: str = None,
        currency: str = None,
        delivery_time: int = None,
        domain_name: str = None,
        domain_type: str = None,
        fail_code: str = None,
        high_bid: float = None,
        high_bidder: str = None,
        next_valid_bid: float = None,
        partner_type: str = None,
        pay_end_time: int = None,
        pay_price: float = None,
        pay_status: str = None,
        produce_status: str = None,
        request_id: str = None,
        reserve_met: bool = None,
        reserve_price: float = None,
        status: str = None,
        transfer_in_price: float = None,
        your_current_bid: float = None,
        your_max_bid: float = None,
    ):
        self.auction_end_time = auction_end_time
        self.auction_id = auction_id
        self.book_end_time = book_end_time
        self.booked_partner = booked_partner
        self.currency = currency
        self.delivery_time = delivery_time
        self.domain_name = domain_name
        self.domain_type = domain_type
        self.fail_code = fail_code
        self.high_bid = high_bid
        self.high_bidder = high_bidder
        self.next_valid_bid = next_valid_bid
        self.partner_type = partner_type
        self.pay_end_time = pay_end_time
        self.pay_price = pay_price
        self.pay_status = pay_status
        self.produce_status = produce_status
        self.request_id = request_id
        self.reserve_met = reserve_met
        self.reserve_price = reserve_price
        self.status = status
        self.transfer_in_price = transfer_in_price
        self.your_current_bid = your_current_bid
        self.your_max_bid = your_max_bid

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

        if self.book_end_time is not None:
            result['BookEndTime'] = self.book_end_time

        if self.booked_partner is not None:
            result['BookedPartner'] = self.booked_partner

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.delivery_time is not None:
            result['DeliveryTime'] = self.delivery_time

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_type is not None:
            result['DomainType'] = self.domain_type

        if self.fail_code is not None:
            result['FailCode'] = self.fail_code

        if self.high_bid is not None:
            result['HighBid'] = self.high_bid

        if self.high_bidder is not None:
            result['HighBidder'] = self.high_bidder

        if self.next_valid_bid is not None:
            result['NextValidBid'] = self.next_valid_bid

        if self.partner_type is not None:
            result['PartnerType'] = self.partner_type

        if self.pay_end_time is not None:
            result['PayEndTime'] = self.pay_end_time

        if self.pay_price is not None:
            result['PayPrice'] = self.pay_price

        if self.pay_status is not None:
            result['PayStatus'] = self.pay_status

        if self.produce_status is not None:
            result['ProduceStatus'] = self.produce_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.reserve_met is not None:
            result['ReserveMet'] = self.reserve_met

        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price

        if self.status is not None:
            result['Status'] = self.status

        if self.transfer_in_price is not None:
            result['TransferInPrice'] = self.transfer_in_price

        if self.your_current_bid is not None:
            result['YourCurrentBid'] = self.your_current_bid

        if self.your_max_bid is not None:
            result['YourMaxBid'] = self.your_max_bid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuctionEndTime') is not None:
            self.auction_end_time = m.get('AuctionEndTime')

        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')

        if m.get('BookEndTime') is not None:
            self.book_end_time = m.get('BookEndTime')

        if m.get('BookedPartner') is not None:
            self.booked_partner = m.get('BookedPartner')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DeliveryTime') is not None:
            self.delivery_time = m.get('DeliveryTime')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')

        if m.get('FailCode') is not None:
            self.fail_code = m.get('FailCode')

        if m.get('HighBid') is not None:
            self.high_bid = m.get('HighBid')

        if m.get('HighBidder') is not None:
            self.high_bidder = m.get('HighBidder')

        if m.get('NextValidBid') is not None:
            self.next_valid_bid = m.get('NextValidBid')

        if m.get('PartnerType') is not None:
            self.partner_type = m.get('PartnerType')

        if m.get('PayEndTime') is not None:
            self.pay_end_time = m.get('PayEndTime')

        if m.get('PayPrice') is not None:
            self.pay_price = m.get('PayPrice')

        if m.get('PayStatus') is not None:
            self.pay_status = m.get('PayStatus')

        if m.get('ProduceStatus') is not None:
            self.produce_status = m.get('ProduceStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ReserveMet') is not None:
            self.reserve_met = m.get('ReserveMet')

        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TransferInPrice') is not None:
            self.transfer_in_price = m.get('TransferInPrice')

        if m.get('YourCurrentBid') is not None:
            self.your_current_bid = m.get('YourCurrentBid')

        if m.get('YourMaxBid') is not None:
            self.your_max_bid = m.get('YourMaxBid')

        return self

