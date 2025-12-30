# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePartnerReservePriceRequest(DaraModel):
    def __init__(
        self,
        bidding_id: int = None,
        domain_name: str = None,
        partner_type: str = None,
        reserve_price: float = None,
    ):
        # This parameter is required.
        self.bidding_id = bidding_id
        # This parameter is required.
        self.domain_name = domain_name
        # This parameter is required.
        self.partner_type = partner_type
        # This parameter is required.
        self.reserve_price = reserve_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bidding_id is not None:
            result['BiddingId'] = self.bidding_id

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.partner_type is not None:
            result['PartnerType'] = self.partner_type

        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BiddingId') is not None:
            self.bidding_id = m.get('BiddingId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('PartnerType') is not None:
            self.partner_type = m.get('PartnerType')

        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')

        return self

