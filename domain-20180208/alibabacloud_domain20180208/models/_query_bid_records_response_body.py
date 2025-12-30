# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180208 import models as main_models
from darabonba.model import DaraModel

class QueryBidRecordsResponseBody(DaraModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[main_models.QueryBidRecordsResponseBodyData] = None,
        page_size: int = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.page_size = page_size
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

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
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num

        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryBidRecordsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')

        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')

        return self

class QueryBidRecordsResponseBodyData(DaraModel):
    def __init__(
        self,
        bid: float = None,
        bid_time: int = None,
        bidder: str = None,
        currency: str = None,
        domain_name: str = None,
    ):
        self.bid = bid
        self.bid_time = bid_time
        self.bidder = bidder
        self.currency = currency
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bid is not None:
            result['Bid'] = self.bid

        if self.bid_time is not None:
            result['BidTime'] = self.bid_time

        if self.bidder is not None:
            result['Bidder'] = self.bidder

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')

        if m.get('BidTime') is not None:
            self.bid_time = m.get('BidTime')

        if m.get('Bidder') is not None:
            self.bidder = m.get('Bidder')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        return self

