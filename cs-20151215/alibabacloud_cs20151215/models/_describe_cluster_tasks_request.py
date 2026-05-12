# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClusterTasksRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['max_results'] = self.max_results

        if self.next_token is not None:
            result['next_token'] = self.next_token

        if self.page_number is not None:
            result['page_number'] = self.page_number

        if self.page_size is not None:
            result['page_size'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('max_results') is not None:
            self.max_results = m.get('max_results')

        if m.get('next_token') is not None:
            self.next_token = m.get('next_token')

        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        return self

