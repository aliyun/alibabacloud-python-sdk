# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDisasterRecoveryItemsRequest(DaraModel):
    def __init__(
        self,
        filter: str = None,
        page_number: int = None,
        page_size: int = None,
        topic_name: str = None,
    ):
        # The filter condition. Topics are filtered by topic name.
        self.filter = filter
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The topic name.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['filter'] = self.filter

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.topic_name is not None:
            result['topicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')

        return self

