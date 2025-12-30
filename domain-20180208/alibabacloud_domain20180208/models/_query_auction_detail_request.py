# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryAuctionDetailRequest(DaraModel):
    def __init__(
        self,
        auction_id: str = None,
    ):
        # This parameter is required.
        self.auction_id = auction_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')

        return self

