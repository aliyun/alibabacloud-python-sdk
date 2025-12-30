# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryAuctionsRequest(DaraModel):
    def __init__(
        self,
        auction_end_time_order: str = None,
        current_page: int = None,
        page_size: int = None,
        status: str = None,
        statuses: str = None,
    ):
        self.auction_end_time_order = auction_end_time_order
        self.current_page = current_page
        self.page_size = page_size
        self.status = status
        self.statuses = statuses

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auction_end_time_order is not None:
            result['AuctionEndTimeOrder'] = self.auction_end_time_order

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        if self.statuses is not None:
            result['Statuses'] = self.statuses

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuctionEndTimeOrder') is not None:
            self.auction_end_time_order = m.get('AuctionEndTimeOrder')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')

        return self

