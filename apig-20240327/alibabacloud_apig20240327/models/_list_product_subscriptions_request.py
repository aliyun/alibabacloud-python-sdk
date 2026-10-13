# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProductSubscriptionsRequest(DaraModel):
    def __init__(
        self,
        consumer_name: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
    ):
        # The keyword of the consumer name used to search the subscription records of the API product by consumer name.
        self.consumer_name = consumer_name
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
        if self.consumer_name is not None:
            result['consumerName'] = self.consumer_name

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerName') is not None:
            self.consumer_name = m.get('consumerName')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

