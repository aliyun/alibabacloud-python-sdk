# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListConsumerGroupsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListConsumerGroupsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response status code. Ok is returned if the request is successful.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # Id of the request
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

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListConsumerGroupsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListConsumerGroupsResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListConsumerGroupsResponseBodyDataItems] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # The list of consumer groups.
        self.items = items
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of consumer groups that match the conditions.
        self.total_size = total_size

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
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_size is not None:
            result['totalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListConsumerGroupsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')

        return self

class ListConsumerGroupsResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        consumer_count: int = None,
        consumer_group_id: str = None,
        create_timestamp: int = None,
        description: str = None,
        gateway_type: str = None,
        name: str = None,
    ):
        # The number of consumers in the consumer group.
        self.consumer_count = consumer_count
        # The consumer group ID.
        self.consumer_group_id = consumer_group_id
        # The creation time of the consumer group, in Unix millisecond timestamp.
        self.create_timestamp = create_timestamp
        # The consumer group description.
        self.description = description
        # The gateway type. Valid values: API or AI.
        self.gateway_type = gateway_type
        # The consumer group name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_count is not None:
            result['consumerCount'] = self.consumer_count

        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id

        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp

        if self.description is not None:
            result['description'] = self.description

        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerCount') is not None:
            self.consumer_count = m.get('consumerCount')

        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')

        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

