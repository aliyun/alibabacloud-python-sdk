# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterListSubscriptionsRequest(DaraModel):
    def __init__(
        self,
        balance_type: str = None,
        max_results: int = None,
        next_token: str = None,
        status: str = None,
    ):
        # Filters by balance type (permanent/monthly).
        self.balance_type = balance_type
        # The maximum number of results to return per page.
        self.max_results = max_results
        # The pagination token. Do not specify this parameter for the first query. For subsequent queries, specify the value returned from the previous query. Set to "" when no more data is available. Set to "5" when there is a next page.
        self.next_token = next_token
        # Filters by status (active/stopped).
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.balance_type is not None:
            result['balanceType'] = self.balance_type

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('balanceType') is not None:
            self.balance_type = m.get('balanceType')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

