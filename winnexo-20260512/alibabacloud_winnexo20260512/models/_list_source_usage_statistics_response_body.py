# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListSourceUsageStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        has_more: bool = None,
        items: List[main_models.ListSourceUsageStatisticsResponseBodyItems] = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The status code.
        self.code = code
        # Indicates whether there is a next page.
        self.has_more = has_more
        # The user information.
        self.items = items
        # The description of the status code.
        self.message = message
        # The current page number.
        self.page = page
        # The page size. Maximum value: 100.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of data entries.
        self.total = total

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.has_more is not None:
            result['hasMore'] = self.has_more

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListSourceUsageStatisticsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListSourceUsageStatisticsResponseBodyItems(DaraModel):
    def __init__(
        self,
        last_event_time: str = None,
        retrieval_count: int = None,
        source_id: str = None,
        source_name: str = None,
        source_type: str = None,
        usage_count: int = None,
    ):
        # The time of the most recent reporting and ingestion within the filtered range.
        self.last_event_time = last_event_time
        # The number of deduplicated sources.
        self.retrieval_count = retrieval_count
        # The ID of the data source, which is unique within the tenant.
        self.source_id = source_id
        # The name of the data source.
        self.source_name = source_name
        # The skill source type.
        self.source_type = source_type
        # The number of used sources.
        self.usage_count = usage_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_event_time is not None:
            result['lastEventTime'] = self.last_event_time

        if self.retrieval_count is not None:
            result['retrievalCount'] = self.retrieval_count

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.source_name is not None:
            result['sourceName'] = self.source_name

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.usage_count is not None:
            result['usageCount'] = self.usage_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lastEventTime') is not None:
            self.last_event_time = m.get('lastEventTime')

        if m.get('retrievalCount') is not None:
            self.retrieval_count = m.get('retrievalCount')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('sourceName') is not None:
            self.source_name = m.get('sourceName')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('usageCount') is not None:
            self.usage_count = m.get('usageCount')

        return self

