# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListHiMarketConsumersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListHiMarketConsumersResponseBodyData = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The response status code.
        self.code = code
        # The response data.
        self.data = data
        # The maximum number of entries on the current page.
        self.max_results = max_results
        # The response message.
        self.message = message
        # The pagination token for the next page. An empty value indicates that the last page has been reached.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.message is not None:
            result['message'] = self.message

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListHiMarketConsumersResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListHiMarketConsumersResponseBodyData(DaraModel):
    def __init__(
        self,
        content: List[main_models.ListHiMarketConsumersResponseBodyDataContent] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of consumers. Each element represents a HiMarket consumer.
        self.content = content
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['content'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('content') is not None:
            for k1 in m.get('content'):
                temp_model = main_models.ListHiMarketConsumersResponseBodyDataContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListHiMarketConsumersResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        consumer_id: str = None,
        description: str = None,
        is_primary: bool = None,
        name: str = None,
    ):
        # The consumer ID. You can use this ID to locate the consumer in operations such as GetHiMarketConsumer, DeleteHiMarketConsumer, GetHiMarketConsumerCredential, and ListHiMarketConsumerSubscriptions.
        self.consumer_id = consumer_id
        # The description of the consumer.
        self.description = description
        # Indicates whether the consumer is a primary consumer.
        self.is_primary = is_primary
        # The name of the consumer.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_id is not None:
            result['consumerId'] = self.consumer_id

        if self.description is not None:
            result['description'] = self.description

        if self.is_primary is not None:
            result['isPrimary'] = self.is_primary

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerId') is not None:
            self.consumer_id = m.get('consumerId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('isPrimary') is not None:
            self.is_primary = m.get('isPrimary')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

