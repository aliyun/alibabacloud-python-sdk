# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListTopicsRequest(DaraModel):
    def __init__(
        self,
        filter: str = None,
        message_types: List[str] = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The filter condition for the query. If not provided, all topics under the instance will be queried.
        self.filter = filter
        # The message type of the topic.
        self.message_types = message_types
        # Page number, indicating which page of results to return.
        self.page_number = page_number
        # Page size, the maximum number of results to display per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['filter'] = self.filter

        if self.message_types is not None:
            result['messageTypes'] = self.message_types

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')

        if m.get('messageTypes') is not None:
            self.message_types = m.get('messageTypes')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

