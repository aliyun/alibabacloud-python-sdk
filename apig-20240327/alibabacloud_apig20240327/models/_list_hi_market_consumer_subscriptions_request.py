# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHiMarketConsumerSubscriptionsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
    ):
        # The maximum number of entries per page. The default value and valid values are not specified in the API definition.
        self.max_results = max_results
        # The pagination cursor. Pass the nextToken returned in the previous response to retrieve the next page. Do not pass this parameter for the first query.
        self.next_token = next_token
        # The page number. Pages start from 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The subscription status used to filter subscriptions. Valid values: PENDING and APPROVED.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

