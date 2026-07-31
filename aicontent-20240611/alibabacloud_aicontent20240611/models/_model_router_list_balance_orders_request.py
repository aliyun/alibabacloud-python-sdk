# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterListBalanceOrdersRequest(DaraModel):
    def __init__(
        self,
        balance_type: str = None,
        direction: str = None,
        max_results: int = None,
        next_token: str = None,
        order_type: str = None,
        page: int = None,
        page_size: int = None,
    ):
        # The balance type filter. Valid values: permanent, monthly. If this parameter is left empty, all types are queried.
        self.balance_type = balance_type
        # The direction filter. Valid values: in (income), out (expenditure). If this parameter is left empty, all directions are queried.
        self.direction = direction
        # The maximum number of results.
        self.max_results = max_results
        # The pagination token for the next page.
        self.next_token = next_token
        # The change type filter. Valid values: recharge, periodic_recharge, manual_deduct, transfer_out, transfer_in, return_out, return_in, write_off, monthly_expire, and deficit_writeoff. If this parameter is left empty, all types are queried.
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

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

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

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('orderType') is not None:
            self.order_type = m.get('orderType')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

