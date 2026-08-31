# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterListMemberBalanceOrdersRequest(DaraModel):
    def __init__(
        self,
        balance_type: str = None,
        direction: str = None,
        order_type: str = None,
        page: int = None,
        page_size: int = None,
    ):
        # The balance type filter. Valid values: permanent and monthly.
        self.balance_type = balance_type
        # The change direction filter. Valid values: in and out.
        self.direction = direction
        # The change type filter.
        self.order_type = order_type
        # The page number.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.balance_type is not None:
            result['balanceType'] = self.balance_type

        if self.direction is not None:
            result['direction'] = self.direction

        if self.order_type is not None:
            result['orderType'] = self.order_type

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('balanceType') is not None:
            self.balance_type = m.get('balanceType')

        if m.get('direction') is not None:
            self.direction = m.get('direction')

        if m.get('orderType') is not None:
            self.order_type = m.get('orderType')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

