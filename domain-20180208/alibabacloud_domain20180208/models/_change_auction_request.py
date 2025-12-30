# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180208 import models as main_models
from darabonba.model import DaraModel

class ChangeAuctionRequest(DaraModel):
    def __init__(
        self,
        auction_list: List[main_models.ChangeAuctionRequestAuctionList] = None,
    ):
        self.auction_list = auction_list

    def validate(self):
        if self.auction_list:
            for v1 in self.auction_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AuctionList'] = []
        if self.auction_list is not None:
            for k1 in self.auction_list:
                result['AuctionList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auction_list = []
        if m.get('AuctionList') is not None:
            for k1 in m.get('AuctionList'):
                temp_model = main_models.ChangeAuctionRequestAuctionList()
                self.auction_list.append(temp_model.from_map(k1))

        return self

class ChangeAuctionRequestAuctionList(DaraModel):
    def __init__(
        self,
        bid_records: List[main_models.ChangeAuctionRequestAuctionListBidRecords] = None,
        domain_name: str = None,
        end_time: str = None,
        is_reserve: int = None,
        reserve_price: float = None,
        reserve_range: str = None,
        status: str = None,
        time_left: int = None,
        winner: str = None,
        winner_price: float = None,
    ):
        self.bid_records = bid_records
        # This parameter is required.
        self.domain_name = domain_name
        # This parameter is required.
        self.end_time = end_time
        self.is_reserve = is_reserve
        self.reserve_price = reserve_price
        self.reserve_range = reserve_range
        self.status = status
        self.time_left = time_left
        # This parameter is required.
        self.winner = winner
        # This parameter is required.
        self.winner_price = winner_price

    def validate(self):
        if self.bid_records:
            for v1 in self.bid_records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BidRecords'] = []
        if self.bid_records is not None:
            for k1 in self.bid_records:
                result['BidRecords'].append(k1.to_map() if k1 else None)

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.is_reserve is not None:
            result['IsReserve'] = self.is_reserve

        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price

        if self.reserve_range is not None:
            result['ReserveRange'] = self.reserve_range

        if self.status is not None:
            result['Status'] = self.status

        if self.time_left is not None:
            result['TimeLeft'] = self.time_left

        if self.winner is not None:
            result['Winner'] = self.winner

        if self.winner_price is not None:
            result['WinnerPrice'] = self.winner_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bid_records = []
        if m.get('BidRecords') is not None:
            for k1 in m.get('BidRecords'):
                temp_model = main_models.ChangeAuctionRequestAuctionListBidRecords()
                self.bid_records.append(temp_model.from_map(k1))

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IsReserve') is not None:
            self.is_reserve = m.get('IsReserve')

        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')

        if m.get('ReserveRange') is not None:
            self.reserve_range = m.get('ReserveRange')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeLeft') is not None:
            self.time_left = m.get('TimeLeft')

        if m.get('Winner') is not None:
            self.winner = m.get('Winner')

        if m.get('WinnerPrice') is not None:
            self.winner_price = m.get('WinnerPrice')

        return self

class ChangeAuctionRequestAuctionListBidRecords(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        price: float = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.create_time = create_time
        # This parameter is required.
        self.price = price
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.price is not None:
            result['Price'] = self.price

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

